from __future__ import annotations

import os
import shutil
import sys
from datetime import datetime
from subprocess import check_call
from typing import Optional

LICENSES = (
    "apache-2",
    "bsd-3-clause",
    "lgpl-3.0",
    "mit",
)


def set_python_version():
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"

    file_names = [
        "Pipfile",
        ".github/workflows/test.yml",
    ]

    for file_name in file_names:
        with open(file_name) as f:
            contents = f.read().replace("{python_version}", python_version)
        with open(file_name, "w") as f:
            f.write(contents)


def set_license(license: Optional[str] = "MIT"):
    if not license:
        return

    if (license := license.lower()) not in LICENSES:
        raise ValueError(
            f"{license=} is not available yet. Please select from:"
            + "\n    "
            + "\n    ".join(LICENSES)
        )

    license_path = os.path.expanduser(f"~/.cookiecutters/python-best-practices/licenses/{license}")
    shutil.copy(license_path, "LICENSE")

    with open("LICENSE") as f:
        contents = f.read().replace("{year}", f"{datetime.now().year}")
        contents = contents.replace("{author_name}", "{{cookiecutter.author_name}}")
    with open("LICENSE", "w") as f:
        f.write(contents)


def git_init():
    check_call("git init".split())


def update_pipfile():
    with open("Pipfile") as f:
        # Extra space and .strip() prevents issues with quotes
        contents = f.read().replace("{pip_packages}", """{{cookiecutter.pip_packages}} """.strip())
        contents = contents.replace(
            "{pip_dev_packages}", """{{cookiecutter.pip_packages}} """.strip()
        )
    with open("Pipfile", "w") as f:
        f.write(contents)

    check_call("pipenv update".split())


def install_dev():
    check_call("pipenv install --dev".split())
    print("Initialized dev packages")


def git_hooks():
    check_call("pipenv run pre-commit install -t pre-commit".split())
    check_call("pipenv run pre-commit install -t pre-push".split())
    print("Setup git hooks")


SUCCESS = "\x1b[1;32m"
TERMINATOR = "\x1b[0m"


def main():
    set_python_version()
    set_license("{{cookiecutter.license}}")
    git_init()
    update_pipfile()
    install_dev()
    git_hooks()

    print(f"{SUCCESS} Project successfully initialized + {TERMINATOR}")


if __name__ == "__main__":
    main()
