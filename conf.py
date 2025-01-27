# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PO Numerical Simulations guide'
copyright = '2024, M. Alho & the PO NSWG'
author = 'M. Alho & the PO NSWG'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

if html_theme == "sphinx_rtd_theme":
    # RTD theme option
    html_theme_options = {
        # 'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
        # 'analytics_anonymize_ip': False,
        # 'logo_only': False,
        # 'prev_next_buttons_location': 'bottom',
        # 'style_external_links': False,
        # 'vcs_pageview_mode': '',
        # 'style_nav_header_background': 'white',
        # 'flyout_display': 'hidden',
        # 'version_selector': True,
        # 'language_selector': True,
        # Toc options
        'collapse_navigation': False,
        'sticky_navigation': True,
        'navigation_depth': 4,
        'includehidden': True,
        'titles_only': False,
    }
elif html_theme == "sphinx_book_theme":
    html_theme_options = {
        "show_navbar_depth": 2,
        'navigation_depth': 4,
        # 'titles_only': False,
        # 'includehidden': True,
        'collapse_navigation': False,
        # 'sticky_navigation': True,
    }
