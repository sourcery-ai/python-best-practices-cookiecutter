from {{cookiecutter.repo_name}} import {{cookiecutter.repo_name}}


def test_fib() -> None:
    assert {{cookiecutter.repo_name}}.fib(0) == 0
    assert {{cookiecutter.repo_name}}.fib(1) == 1
    assert {{cookiecutter.repo_name}}.fib(2) == 1
    assert {{cookiecutter.repo_name}}.fib(3) == 2
    assert {{cookiecutter.repo_name}}.fib(4) == 3
    assert {{cookiecutter.repo_name}}.fib(5) == 5
    assert {{cookiecutter.repo_name}}.fib(10) == 55
