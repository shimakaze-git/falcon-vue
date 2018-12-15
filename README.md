# Falcon Vue

Falcon Vue is a plugin for the [Falcon Web Framework](https://github.com/falconry/falcon).

### Install

```bash
pip3 install falcon-vue
```

## Falcon Vue

```python
import os
import sys
import falcon
from wsgiref import simple_server
from falcon_vue import register_vue_app

app = falcon.API()

app = register_vue_app(
    app,
    api_url="/dist",
    src_path="./test_project/dist"
)

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
```

