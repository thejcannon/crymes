test:
    uv run pytest

build project:
    uv build --project {{project}}

publish project: (build project)
    uv publish --project {{project}}

publish-test project: (build project)
    uv publish --project {{project}} --index test-pypi
