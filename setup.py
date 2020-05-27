# !/usr/bin/env python
"""Setup, configuration, and metadata file for the 84.51 Python package template."""
from setuptools import setup

doc_requires = ["alabaster==0.7.12"]
test_requires = ["pytest"]
dev_requires = (
    [
        "flake8",
        "cookiecutter>=1.4.0",
        "tox==3.14.1",
        "pytest-cookies>=0.4.0",
        "watchdog==0.9.0",
    ]
    + doc_requires
    + test_requires
)

setup(
    name="effo-pkg-template",
    packages=[],
    version="0.1.0",
    description="Cookiecutter template for an internal 84.51 Python package",
    author="Brad Boehmke",
    license="proprietary",
    author_email="bradley.boehmke@8451.com",
    url="https://dev.azure.com/8451/PoS/_git/effo-pkg-template",
    keywords=["cookiecutter", "template", "package"],
    python_requires=">=3.5",
    extras_require={"docs": doc_requires, "tests": test_requires, "dev": dev_requires},
    project_urls={
        "Documentation": "https://dev.azure.com/8451/PoS/_git/effo-pkg-template",
        "Source": "https://dev.azure.com/8451/PoS/_git/effo-pkg-template",
        "Bugs": "https://dev.azure.com/8451/PoS/_boards/board/t/APTS%20Team/Issues",
    },
)
