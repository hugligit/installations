# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Debian Installation'
copyright = '2025, Marcel'
author = 'Marcel'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        'sphinx.ext.todo',
        'sphinx.ext.graphviz',
        'sphinx_rtd_theme',
        'sphinx_toolbox.collapse',
        # 'sphinx_rtd_dark_mode',
        ]

templates_path = ['_templates']
exclude_patterns = []


html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 6,
    "sticky_navigation": True,
    "includehidden": True,
}



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [ 'custom.css', ]
todo_include_todos = True
default_dark_mode = False
