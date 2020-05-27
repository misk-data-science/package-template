#!/usr/bin/env python
"""Post-project generation checks."""
import os
import re
import shutil

import yaml


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
PACKAGE_NAME = "{{ cookiecutter.package_name }}"
PACKAGE_VERSION = "{{ cookiecutter.version }}"


def remove_file(filepath):
    """Remove un-requested files."""
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_directory(directory):
    """Remove un-requested directory."""
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, directory))


if __name__ == "__main__":

    if "{{ cookiecutter.package_language }}".lower().strip() == 'python':
        remove_directory("R")
        remove_directory(".Rproj.user")
        remove_file("DESCRIPTION")
        remove_file("{{ cookiecutter.package_name }}" + ".Rproj")
        remove_file(".Rbuildignore")
        remove_file("NEWS.md")

    if "{{ cookiecutter.package_language }}".lower().strip() == 'r':
        remove_directory("src")
        remove_file("setup.cfg")
        remove_file("setup.py")
        remove_file("tests/__init__.py")
        remove_file("CHANGELOG.md")
        remove_file(".editorconfig")
        remove_file("MANIFEST.in")
