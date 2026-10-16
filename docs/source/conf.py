"""Sphinx configuration for the PortaPyC documentation."""

import os
import sys

import sphinx_rtd_theme
from portapyc.version import version_string


sys.path.insert(0, os.path.abspath("../.."))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PortaPyC'
copyright = '2005-2013, Tomer Filiba, 2026, THALES LAS France'
author = 'Tomer Filiba, Maxime Djomby'
release = version_string

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx_rtd_theme']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/banner.png'
html_favicon = '_static/favicon.ico'
html_theme_options = {
    'style_nav_header_background': '#499159',
    'logo_only': True,
}
