set dotenv-load

test:
    uv run pytest

build project:
    uv build --project {{project}}

# Publishes a project to PyPI
publish project: (build project)
    uv publish --project {{project}}

# Publishes a project to Test PyPI
publish-test project: (build project)
   @uv publish --project {{project}} --index test-pypi
