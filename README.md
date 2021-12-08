# Python Best Practices Cookiecutter
[![License](https://img.shields.io/github/license/jevandezande/python-best-practices-cookiecutter)](https://github.com/jevandezande/python-best-practices-cookiecutter/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/jevandezande/python-best-practices-cookiecutter/Test)](https://github.com/jevandezande/python-best-practices-cookiecutter/actions/)
[![Codecov](https://img.shields.io/codecov/c/github/{{cookiecutter.user_name}}/{{cookiecutter.repo_name}})](https://app.codecov.io/gh/jevandezande/python-best-practices-cookiecutter/)

Best practices [cookiecutter](https://github.com/audreyr/cookiecutter) template as described in this [blogpost](https://sourcery.ai/blog/python-best-practices/).

## Features
- Testing with [pytest](https://docs.pytest.org/en/latest/)
- Formatting with [black](https://github.com/psf/black)
- Import sorting with [isort](https://github.com/timothycrosley/isort)
- Static typing with [mypy](http://mypy-lang.org/)
- Linting with [flake8](http://flake8.pycqa.org/en/latest/)
- Git hooks that run all the above with [pre-commit](https://pre-commit.com/)
- Continuous Integration with [GitHub Actions](https://github.com/features/actions)
- Code coverage with [Codecov](https://codecov.io)


## Setup
Most of the setup steps are automated, but one can also follow a flow similar to the below.

```sh
# Install pipx if pipenv and cookiecutter are not installed
python3 -m pip install pipx
python3 -m pipx ensurepath

# Install pipenv using pipx
pipx install pipenv

# Use cookiecutter to create project from this template
pipx run cookiecutter gh:sourcery-ai/python-best-practices-cookiecutter

# Enter project directory
cd <repo_name>

# Initialise git repo
git init

# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```
