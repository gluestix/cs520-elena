# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath("../../src/backend/controller"))
sys.path.insert(0, os.path.abspath("../../src/backend/view"))
sys.path.insert(0, os.path.abspath("../../src/backend/model"))


project = 'The Semicolon Coders: EleNA'
copyright = '2022, Logan Mimaroglu, Jiachang Situ, Saiyyam Kochar, Rishab Maheshwari'
author = 'Logan Mimaroglu, Jiachang Situ, Saiyyam Kochar, Rishab Maheshwari'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.todo", "sphinx.ext.viewcode", "sphinx.ext.autodoc", "sphinx.ext.napoleon"]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
