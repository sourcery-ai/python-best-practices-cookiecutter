import os
import sys

repo_name = '{{cookiecutter.repo_name }}'

def set_python_version():
    python_version = f"{str(sys.version_info.major)}.{str(sys.version_info.minor)}"

    file_names = ["Dockerfile", "Pipfile", ".github/workflows/test.yml"]
    for file_name in file_names:
        with open(file_name) as f:
            contents = f.read()
            contents = contents.replace(r"{python_version}", python_version)
        with open(file_name, "w") as f:
            f.write(contents)

def remove_main_if_lib():
    is_lib = '{{ cookiecutter.binary }}'
    if is_lib not in {"y", "Y"}:
        main_file_path = os.path.join(repo_name, '__main__.py')
        os.remove(main_file_path)

SUCCESS = "\x1b[1;32m"
INFO = "\x1b[1;33m"
TERMINATOR = "\x1b[0m"


def main():
    set_python_version()
    remove_main_if_lib()
    print(f"{SUCCESS}Project successfully initialized{TERMINATOR}")


if __name__ == "__main__":
    main()
