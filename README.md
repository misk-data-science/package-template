<!-- badges: start -->
![](https://img.shields.io/badge/version-0.1.0-blue.svg)
[![lifecycle](https://img.shields.io/badge/lifecycle-maturing-brightgreen.svg)](https://www.tidyverse.org/lifecycle/#maturing)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
<!-- badges: end -->

# 84.51° Python Package Template

This is a proof of concept for providing a cookiecutter template to create an 84.51° internal Python package.

## Features

- Creates our preferred package structure.
- Provides you with a starting point for proper documentation.
- Uses pytest and creates proper test organization.
- Sets up linting and type checking configurations (flake8, mypy).
- Will set up [pre-commit](https://pre-commit.com/) configuration if desired.
- Will set up Azure pipelines for CI/CD if desired.

## Quickstart

Install the latest Cookiecutter:

```sh
pip install -U cookiecutter
```

Generate a Python package project:

```sh
cookiecutter https://8451@dev.azure.com/8451/PoS/_git/effo-pkg-template
```

Then...
