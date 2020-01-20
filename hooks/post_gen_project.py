import os
import sys


def set_python_version():
    python_version = str(sys.version_info.major) + "." + str(sys.version_info.minor)

    file_names = ["Dockerfile", "Pipfile", ".github/workflows/test.yml"]
    for file_name in file_names:
        with open(file_name) as f:
            contents = f.read()
            contents = contents.replace(r"{python_version}", python_version)
        with open(file_name, "w") as f:
            f.write(contents)


def remove_docker():
    file_names = ["Dockerfile", ".dockerignore", ".github/workflows/publish_docker.yml"]
    for file_name in file_names:
        if os.path.exists(file_name):
            os.remove(file_name)


def remove_publish_docker():
    file_names = [".github/workflows/publish_docker.yml"]
    for file_name in file_names:
        if os.path.exists(file_name):
            os.remove(file_name)


SUCCESS = "\x1b[1;32m"
INFO = "\x1b[1;33m"
TERMINATOR = "\x1b[0m"


def main():
    set_python_version()

    docker = "{{ cookiecutter.docker }}".lower() == "y"
    dockerhub_username = "{{ cookiecutter.dockerhub_username }}"

    if not docker:
        remove_docker()

    if not dockerhub_username:
        remove_publish_docker()

    print(SUCCESS + "Project successfully initialized" + TERMINATOR)
    if docker and dockerhub_username:
        print(
            INFO
            + "Once you push to GitHub, add DOCKER_USERNAME and DOCKER_PASSWORD secrets to the repo\n"
            + 'or else the "Publish docker image" GitHub action will fail'
            + TERMINATOR
        )


if __name__ == "__main__":
    main()
