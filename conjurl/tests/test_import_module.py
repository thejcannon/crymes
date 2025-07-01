import importlib

def test_using_ops():
    httpx = importlib.import_module("https://github.com/encode/httpx")
    assert httpx
    print(httpx.get("https://google.com"))
