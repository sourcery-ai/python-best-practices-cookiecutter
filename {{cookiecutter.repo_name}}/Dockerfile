FROM python:{python_version}-slim

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1

# Install pipenv and deps
RUN pip install pipenv
RUN apt-get update && apt-get install -y gcc > /dev/null

# Install application into container
RUN mkdir /app
WORKDIR /app
COPY . .

# Install dependencies
RUN pipenv install --deploy --system

# Run the executable
ENTRYPOINT ["python", "-m", "{{cookiecutter.repo_name}}"]
CMD ["10"]
