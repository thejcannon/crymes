import pytest


@pytest.fixture(autouse=True)
def _purge_sys_modules():
    import sys

    for key in list(sys.modules.keys()):
        if key.startswith("conjurl.github.com."):
            del sys.modules[key]


@pytest.fixture(autouse=True)
def _purge_github_com_attrs():
    import conjurl.github.com

    for key in dir(conjurl.github.com):
        if not key.startswith("__"):
            delattr(conjurl.github.com, key)
