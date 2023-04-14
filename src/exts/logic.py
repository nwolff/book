import asyncio
import base64
import hashlib
import os
import sys
from dataclasses import dataclass
from functools import cached_property
from typing import Any, Callable, List, Optional, Tuple, TypeVar, Union

from docutils import nodes  # type: ignore
from docutils.nodes import Node, system_message  # type: ignore
from docutils.parsers.rst import directives  # type: ignore
from myst_parser.main import MdParserConfig, to_html
from sphinx.application import Sphinx
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective, SphinxRole, SphinxTranslator

# import urllib
# import zlib
# import lzstring

## REF: https://www.sphinx-doc.org/en/master/extdev/index.html

MAIN_LOGIC_URL = "https://logic.modulo-info.ch"

logger = logging.getLogger(__name__)

StringOrList = Union[str, List[str]]

# reassigned when importing from playwright
Page = Any 
sync_playwright: Callable[[], Any] = None # type: ignore

def md5(string: str) -> str:
    md5_builder = hashlib.md5()
    md5_builder.update(string.encode("utf-8"))
    return md5_builder.hexdigest()


T = TypeVar("T")


@dataclass
class LogicDiagramData:
    data_json: str
    mode: str
    height: Optional[int]

    @cached_property
    def content_based_filename(self) -> str:
        height_str = "-1" if self.height is None else str(self.height)
        spec = "/".join([self.data_json, self.mode, height_str])
        spec_md5 = md5(spec)  # should be 32 chars hex
        return f"{spec_md5}.png"

class PlaywrightWrapper:
    def __init__(self) -> None:
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.webkit.launch(headless=True)
        self.context = self.browser.new_context()

    def close(self) -> None:
        self.context.close()
        self.browser.close()
        self.playwright.stop()

    def new_page(self) -> Page:
        return self.context.new_page()

    result: str
    error: Optional[str]


def browser_launch() -> PlaywrightWrapper:
    return PlaywrightWrapper()


def browser_close(browser: Union[PlaywrightWrapper, None]) -> None:
    if browser is not None:
        browser.close()


def to_png(data: LogicDiagramData, output_file: str, browser: PlaywrightWrapper) -> bool:
    page = browser.new_page()
    page.goto(MAIN_LOGIC_URL)

    conversion_function = "toPNG"
    # conversion_function = "toSVG"

    result = page.evaluate(
        f"""async () => {{
        try {{
            const editor = window.Logic.singleton
            if (typeof editor === 'undefined') {{
                return "error: no editor"
            }}

            const dataJson = JSON.stringify({data.data_json})
            editor.loadCircuit(dataJson)
            editor.setModeFromString("{data.mode}")
            const withMetadata = false
            const heightHint = {"undefined" if data.height is None else data.height}
            const blob = await editor.{conversion_function}(withMetadata, heightHint)
            const asBase64 = await editor.toBase64(blob)
            return asBase64
        }} catch (e) {{
            return "error: " + e
        }}
    }}"""
    )
    page.close()

    if result is None:
        logger.error("error: no result from PNG conversion")
        return False

    if result.startswith("error:"):
        logger.error(result)
        return False

    with open(output_file, "wb") as f:
        f.write(base64.b64decode(result))
    return True


class logic_diagram(nodes.Element, nodes.General):
    pass


def begin_logic_diagram_html(self: SphinxTranslator, node: Node) -> None:
    content = node["content"].strip()
    ref = node["ref"]
    height = node["height"]
    mode = node["mode"]
    showonly = node["showonly"]

    tag = self.starttag(
        node,
        "div",
        CLASS="logic-container",
        style="height: " + str(height) + "px;",
    )
    self.body.append(tag.strip())

    attrs_str = ""
    if ref:
        attrs_str += ' id="logic_' + ref + '"'
    if mode:
        attrs_str += ' mode="' + mode + '"'
    if showonly:
        attrs_str += ' showonly="' + showonly + '"'

    self.body.append(
        "<logic-editor" + attrs_str + ">" + "\n" + '<script type="application/json">' + "\n" + content + "\n"
    )


def end_logic_diagram_html(self: SphinxTranslator, node: Node) -> None:
    self.body.append("</script>")
    self.body.append("</logic-editor>")
    self.body.append("</div>")


def begin_logic_diagram_latex(self: SphinxTranslator, node: Node) -> None:

    content = node["content"].strip()
    height = node["height"]
    mode = node["mode"]

    png_folder = os.path.join(self.builder.outdir, "logic_png")
    if not os.path.exists(png_folder):
        os.makedirs(png_folder)

    data = LogicDiagramData(content, mode, height)
    target_file = os.path.join(png_folder, data.content_based_filename)

    include_image = False
    if os.path.exists(target_file):
        include_image = True
    else:
        if browser is None:
            logger.error("browser page is not initialized to generate PNGs for logic diagrams")
        else:
            include_image = to_png(data, target_file, browser)
            if include_image:
                logger.info("Generated logic diagram: %s", target_file)
            else:
                logger.error("Failed to generate logic diagram: %s", target_file)

    if include_image:
        self.body.append(
            f"\n\\begin{{center}}\n  \\includegraphics[scale=0.33]{{{target_file}}}\n\\end{{center}}\n"
        )
    else:
        self.body.append("\n \\fbox{logic diagram} \\\ ")


def end_logic_diagram_latex(self: SphinxTranslator, node: Node) -> None:
    self.body.append("\n")


def directive_mode(argument: str) -> Any:
    return directives.choice(argument, ("static", "tryout", "connect", "design", "full"))


class LogicDiagram(SphinxDirective):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "ref": directives.unchanged,
        "height": directives.positive_int,
        "mode": directive_mode,
        "showonly": directives.unchanged,
    }
    has_content = True

    def run(self) -> List[Node]:
        self.assert_has_content()

        ref = self.options.get("ref", "")
        height = self.options.get("height", 500)
        mode = self.options.get("mode", "")
        showonly = self.options.get("showonly", "")

        node = logic_diagram(
            "",
            content="\n".join(self.content),
            ref=ref,
            height=height,
            mode=mode,
            showonly=showonly,
        )

        self.set_source_info(node)

        return [node]


class logic_highlight(nodes.Inline, nodes.TextElement):
    pass


def _parse_highlight_content(string: str) -> Tuple[StringOrList, StringOrList, str]:
    def _parse_ids(string: str) -> List[str]:
        if string.startswith("{") and string.endswith("}"):
            return string[1:-1].split(",")
        return [string]

    if "|" in string:
        [refs, display] = string.split("|", 2)
        if "." in refs:
            [diagramrefs, componentrefs] = refs.split(".", 2)
            return _parse_ids(diagramrefs), _parse_ids(componentrefs), display

    return "", "", string


class LogicHighlightRefRole(SphinxRole):
    def run(self) -> Tuple[List[Node], List[system_message]]:
        diagramrefs, componentrefs, display = _parse_highlight_content(self.text)
        myst_config = self.env.myst_config  # type: ignore
        node = logic_highlight(
            "",
            "",
            diagramrefs=diagramrefs,
            componentrefs=componentrefs,
            display=display,
            config=myst_config,
        )
        return [node], []


def _render_inline(source: str, config: MdParserConfig) -> str:
    # WARNING: this should not be called when creating the nodes
    # as it screws up the global parser state
    html = str(to_html(source, config=config)).strip()
    if html.startswith("<p>") and html.endswith("</p>"):
        html = html[3:-4]
    return html


def begin_logic_highlight_html(self: SphinxTranslator, node: Node) -> None:
    def _to_js_string(refs: List[str]) -> str:
        if len(refs) == 1:
            return '"' + refs[0] + '"'
        return "[" + ", ".join(['"' + r + '"' for r in refs]) + "]"

    js_on_click = (
        "Logic.highlight("
        + _to_js_string(node["diagramrefs"])
        + ", "
        + _to_js_string(node["componentrefs"])
        + ")"
    )
    tag = self.starttag(
        node,
        "span",
        CLASS="logic-highlight",
        onclick=js_on_click,
    )
    self.body.append(tag.strip())
    content = _render_inline(node["display"], node["config"])
    self.body.append(content)


def end_logic_highlight_html(self: SphinxTranslator, node: Node) -> None:
    self.body.append("</span>")


def _render_latex(source: str) -> str:
    # ugly hack, should used child nodes instead (micha)
    source.strip()
    source = source.replace("_", "")
    return source


def begin_logic_highlight_latex(self: SphinxTranslator, node: Node) -> None:
    content = _render_latex(node["display"])
    self.body.append(content)


def end_logic_highlight_latex(self: SphinxTranslator, node: Node) -> None:
    pass


class logic_gate(nodes.Inline, nodes.TextElement):
    pass


class LogicGateRole(SphinxRole):
    def run(self) -> Tuple[List[Node], List[system_message]]:
        node = logic_gate(
            "",
            "",
            display=self.text,
        )
        return [node], []


def begin_logic_gate_html(self: SphinxTranslator, node: Node) -> None:
    tag = self.starttag(
        node,
        "span",
        CLASS="logic-gate",
    )
    self.body.append(tag.strip())
    self.body.append(node["display"])


def end_logic_gate_html(self: SphinxTranslator, node: Node) -> None:
    self.body.append("</span>")


def begin_logic_gate_latex(self: SphinxTranslator, node: Node) -> None:
    self.body.append("\\textbf{")
    self.body.append(node["display"])


def end_logic_gate_latex(self: SphinxTranslator, node: Node) -> None:
    self.body.append("}")


browser: Union[PlaywrightWrapper, None] = None


def build_starting(app: Sphinx) -> None:
    global browser, Page, sync_playwright
    if app.builder is not None and app.builder.name == "latex":
        from playwright.sync_api import Page, sync_playwright
        logger.info("starting headless browser")
        browser = browser_launch()


def build_finished(app: Sphinx, exception: Any) -> None:
    global browser
    if app.builder is not None and app.builder.name == "latex":
        logger.info("shutting down headless browser")
        browser_close(browser)
        browser = None


def setup(app: Sphinx) -> None:
    app.add_directive("logic", LogicDiagram)
    app.add_node(
        logic_diagram,
        html=(begin_logic_diagram_html, end_logic_diagram_html),
        latex=(begin_logic_diagram_latex, end_logic_diagram_latex),
    )
    app.add_js_file(MAIN_LOGIC_URL + "/simulator/lib/bundle.js")

    app.add_role("logicref", LogicHighlightRefRole())
    app.add_node(
        logic_highlight,
        html=(begin_logic_highlight_html, end_logic_highlight_html),
        latex=(begin_logic_highlight_latex, end_logic_highlight_latex),
    )

    app.add_role("lg", LogicGateRole())
    app.add_node(
        logic_gate,
        html=(begin_logic_gate_html, end_logic_gate_html),
        latex=(begin_logic_gate_latex, end_logic_gate_latex),
    )

    app.add_css_file("logic.css")

    app.connect("builder-inited", build_starting)
    app.connect("build-finished", build_finished)
