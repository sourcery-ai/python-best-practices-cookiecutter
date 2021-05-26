import sys
from subprocess import check_call


def set_python_version():
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"

    file_names = [
        "Dockerfile",
        "Pipfile",
        ".github/workflows/test.yml",
    ]
    for file_name in file_names:
        with open(file_name) as f:
            contents = f.read().replace(r"{python_version}", python_version)
        with open(file_name, "w") as f:
            f.write(contents)


def git_init():
    check_call("git init", shell=True)


def install_dev():
    check_call("pipenv install --dev", shell=True)
    print("Initialized dev packages")


def git_hooks():
    check_call(
        """\
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
""",
        shell=True,
    )
    print("Setup git hooks")


SUCCESS = "\x1b[1;32m"
TERMINATOR = "\x1b[0m"


def main():
    set_python_version()
    git_init()
    install_dev()
    git_hooks()

    print(f"{SUCCESS} Project successfully initialized + {TERMINATOR}")


if __name__ == "__main__":
    main()
