from __future__ import annotations

import os
import shutil
import sys
from subprocess import check_call
from typing import Optional

licenses = {
    "apache-2",
    "bsd-3-clause",
    "lgpl-3.0",
    "mit",
    None,
}


def set_python_version():
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"

    file_names = [
        "Pipfile",
        ".github/workflows/test.yml",
    ]

    for file_name in file_names:
        with open(file_name) as f:
            contents = f.read().replace(r"{python_version}", python_version)
        with open(file_name, "w") as f:
            f.write(contents)


def set_license(license: Optional[str] = "MIT"):
    if not license:
        return

    if (license := license.lower()) not in licenses:
        raise ValueError(f"{license=} is not available yet. Please select from:\n    {"    \n".join(licenses)}")

    license_path = os.path.expanduser(f"~/.cookiecutters/python-best-practices/licenses/{license}")
    print(f"Set {license=}")
    shutil.copy(license_path, "{{cookiecutter.repo_name}}/LICENSE")


def git_init():
    check_call("git init".split())


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
    set_license()
    git_init()
    install_dev()
    git_hooks()

    print(f"{SUCCESS} Project successfully initialized + {TERMINATOR}")


if __name__ == "__main__":
    main()
