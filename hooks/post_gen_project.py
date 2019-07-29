import sys

python_version = str(sys.version_info.major) + '.' + str(sys.version_info.minor)


with open('Pipfile') as f:
    pipfile = f.read()
    pipfile = pipfile.replace(r'{python_version}', python_version)


with open('Pipfile', 'w') as f:
    f.write(pipfile)
