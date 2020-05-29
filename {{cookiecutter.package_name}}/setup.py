#!/usr/bin/env python
"""Setup, configuration, and metadata file for the {{ cookiecutter.package_name}} package."""
from setuptools import find_packages
from setuptools import setup


install_requires = []
doc_requires = ["sphinx", "sphinx_rtd_theme", "sphinxcontrib.napoleon"]
test_requires = ["pytest"]
dev_requires = ["flake8", "mypy"] + doc_requires + test_requires

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.version }}",
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    description="{{ cookiecutter.package_short_description }}",
    url="{{ cookiecutter.url }}",
    author="{{ cookiecutter.first_name.strip() + ' ' + cookiecutter.last_name.strip() }}",
    author_email="{{ cookiecutter.email }}",
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    python_requires='>=3.6',
    install_requires=install_requires,
    extras_require={"docs": doc_requires, "tests": test_requires, "dev": dev_requires},
    test_suite="tests",
    include_package_data=True,
    project_urls={
        'Source': "{{ cookiecutter.url }}",
        'Bug Reports': "{{ cookiecutter.url }}/issues",
    },
)
