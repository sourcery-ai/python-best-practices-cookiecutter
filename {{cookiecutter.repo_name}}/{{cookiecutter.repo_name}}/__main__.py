import sys

from {{cookiecutter.repo_name}}.{{cookiecutter.repo_name}} import fib

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(fib(n))
