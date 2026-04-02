# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import datetime as dt

project = 'O3-Shop'
copyright = '2023 - 2026, O3-Shop, based on 2021 - 2022 OXID eSales AG'.format(dt.date.today().year)
author = 'O3-Shop Community'

# The short X.Y version
version = '1.5'
# The full version, including alpha/beta/rc tags
release = '1.5.3'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  "myst_parser",
  "sphinxcontrib.jquery"
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
myst_enable_extensions = [
    "colon_fence",
    "substitution"
]

html_logo = 'assets/logo_light.png'
html_favicon = 'assets/favicon.ico'
html_css_files = [
    'css/o3.css',
]

html_context = {
    'current_version': '1.5',
    'versions':
        [
            ('1.5', 'https://docs.o3-shop.com/en/1.5/')
        ],
    'languages':
        [
            ('EN', 'https://docs.o3-shop.com/en/1.5/')
        ],

    'show_sphinx': False,

    "display_github": True,
    "github_user": "o3-shop",
    "github_repo": "o3-documentation",
    "github_version": "main",
    "conf_py_path": "/source/",
}

html_theme_options = {
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': 'blob',
    'style_nav_header_background': '#343131',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

myst_substitutions = {
    'baseurl': os.getenv("READTHEDOCS_CANONICAL_URL", "https://localhost/")
}
