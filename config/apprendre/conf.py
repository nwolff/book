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
copyright = '2021, Groupe de travail DGEP, EPFL, HEP, UNIL'
author = 'Groupe de travail DGEP, EPFL, HEP, UNIL'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
sys.path.append(os.path.abspath("../extensions/codeplay"))
sys.path.append(os.path.abspath("../extensions/glossary"))
sys.path.append(os.path.abspath("../extensions/questions"))
sys.path.append(os.path.abspath("../extensions/videos"))
extensions = [
    'codeplay',
    'glossary',
    'myst_parser',
    'questions',
    'sphinx_panels',
    'videos'
]

glossary_doc = 'glossaire'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['../source/_templates']
html_extra_path = ['../source/assets']

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
html_favicon = '../source/_static/modulo-icon.ico'
html_title = 'Apprendre'

html_theme_options = {
    "light_logo": "modulo-logo-light.svg",
    "dark_logo": "modulo-logo-dark.svg",
    "announcement": (
        "version : 2021-12-03b"
    )
}

html_css_files = ['styles/global.css']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../source/_static']
html_js_files = ['https://unpkg.com/@popperjs/core@2', 'scripts/frames.js']