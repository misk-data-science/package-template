#!/usr/bin/env python
"""Pre-project generation checks."""
import re
import sys


MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

module_name = "{{ cookiecutter.package_name }}"
language = "{{ cookiecutter.package_language }}".strip().lower()

if not re.match(MODULE_REGEX, module_name):
    raise ValueError(
        f"""The package name {module_name} is not a valid name.
        Please do not use a - and use _ instead."""
    )

    # Exit to cancel project
    sys.exit(1)

if language not in ['r', 'python']:
    raise ValueError("The package language must be either 'r' or 'python'.")

    # Exit to cancel project
    sys.exit(1)
