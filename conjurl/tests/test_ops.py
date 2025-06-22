def test_using_ops():
    from conjurl import github

    httpx = github.com / "encode" / "ops"
    assert httpx
