# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
import sys

# -- Project information -----------------------------------------------------

project = 'Modulo2'
copyright = 'CC-BY-NC'
author = 'Groupe de travail DGEP, EPFL, HEP, UNIL'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
sys.path.append(os.path.abspath("../exts"))
extensions = [
    'codeplay',
    'glossary',
    'myst_parser',
    'questions',
    'sphinx_panels',
    'videos',
    'logic',
    'blanks',
    'timeline',
    'exercise',
]

glossary_doc = 'glossaire'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['../templates']
html_extra_path = ['../assets']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'fr'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages. See the documentation for
# a list of builtin themes.
#

html_theme = 'furo'
html_show_copyright = False
html_show_sphinx = False
html_show_copyright = False
html_favicon = '../static/modulo-icon.ico'
html_title = 'Apprendre'
html_theme_options = {
    "light_logo": "modulo-logo-light.svg",
    "dark_logo": "modulo-logo-dark.svg",
    "navigation_with_keys": True,
    "light_css_variables": {

        # Fonts
        'font-stack': "Montserrat, system-ui, -apple-system, BlinkMacSystemFont,\"Segoe UI\", Roboto, \"Helvetica Neue\", Arial, \"Noto Sans\", sans-serif,\"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\", \"Noto Color Emoji\"",

        # Base colors
        "color-foreground-primary": "black",
        "color-foreground-secondary": "#5a5c63", # for secondary text,
        "color-foreground-muted": "#646776", # for muted text
        "color-foreground-border": "#878787", # for content borders

        "color-background-primary": "white", # for content
        "color-background-secondary": "#f8f9fb", # for navigation + ToC
        "color-background-hover": "#efeff4ff", # for navigation-item hover
        "color-background-over--transparent": "#efeff400", 
        "color-background-border": "#eeebee", # for UI borders

        # Announcement colors
        "color-announcement-background": "#000000dd",
        "color-announcement-text": "#eeebee",

        # Brand colors
        "color-brand-primary": "#8044FF", # violet
        "color-brand-content": "#8044FF", # violet
        
        # Admonition font size
        "admonition-font-size": "0.9rem",
        "admonition-title-font-size": "0.9rem",
    },
    "dark_css_variables": {

        # Fonts
        'font-stack': "Montserrat, system-ui, -apple-system, BlinkMacSystemFont,\"Segoe UI\", Roboto, \"Helvetica Neue\", Arial, \"Noto Sans\", sans-serif,\"Apple Color Emoji\", \"Segoe UI Emoji\", \"Segoe UI Symbol\", \"Noto Color Emoji\"",

        # Base colors
        "color-foreground-primary": "#ffffffcc",
        "color-foreground-secondary": "#9ca0a5", # for secondary text,
        "color-foreground-muted": "#81868d", # for muted text
        "color-foreground-border": "#666666", # for content borders

        "color-background-primary": "#131416", # for content
        "color-background-secondary": "#131416", # for navigation + ToC
        "color-background-hover": "#1e2124ff", # for navigation-item hover
        "color-background-over--transparent": "#1e212400", 
        "color-background-border": "#303335", # for UI borders

        # Announcement colors
        "color-announcement-background": "#000000dd",
        "color-announcement-text": "#eeebee",

        # Brand colors
        "color-brand-primary": "#7C3EFF", # violet clair
        "color-brand-content": "#7C3EFF", # violet clair
        
        # Admonition font size
        "admonition-font-size": "0.9rem",
        "admonition-title-font-size": "0.9rem",
    },
}

html_css_files = ['styles/global.css', 'styles/reactions.css', 'styles/progress.css', 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['./static']
html_js_files = ['https://unpkg.com/@popperjs/core@2', 'scripts/reactions.js', 'scripts/progress.js', 'scripts/dark.js', 'scripts/frames.js']

pygments_sytle = "sphinx"
pygments_dark_style = "monokai"

myst_enable_extensions = ['amsmath', 'colon_fence', 'deflist', 'dollarmath', 'html_admonition', 'html_image', 'replacements', 'smartquotes', 'substitution']
myst_url_schemes = ['mailto', 'http', 'https']