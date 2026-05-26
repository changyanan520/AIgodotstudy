# Configuration file for the Sphinx documentation builder.
project = 'AI+Godot 开发教学文档'
copyright = '2026, cynloves'
author = 'cynloves'

release = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_extra_path = ['../downloads']

html_context = {
    'download_url': '/zh-cn/latest/_downloads/docs_source.zip',
}

language = 'zh_CN'

templates_path = ['_templates', '_templates']