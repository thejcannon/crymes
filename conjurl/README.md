# `conjurl`

Conjurl is a Python crime which is meant to allow importing from various URLs (and URIs).

```py
from conjurl.github.com.encode import httpx
# or
import conjurl.github.com.encode.httpx as httpx
```

Alternatively...
```py
from conjurl import github

httpx = github.com / "encode" / "httpx"
```

or even...
```py
import importlib

httpx = importlib.import_module("https://github.com/encode/httpx")
```
