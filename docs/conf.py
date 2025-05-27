# docs/conf.py

# -- Project information -----------------------------------------------------

project = 'ArttulOS Developer Documentation'
copyright = '2025, ArttulOS Contributors'
author = 'ArttulOS Team'

# The version info, e.g. '1.0' or '0.1'
release = '0.1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.autodoc',       # If you use autodoc for API docs
    'sphinx.ext.napoleon',      # Supports Google and NumPy style docstrings
    'sphinx.ext.viewcode',      # Add links to source code
]

# Paths that contain templates, relative to this directory.
templates_path = ['_templates']

# List of patterns to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'  # The ReadTheDocs theme

html_static_path = ['_static']

# Optionally, set the HTML title
html_title = 'ArttulOS Developer Documentation'
