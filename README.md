Falcon Vue
====

Falcon Vue is a plugin for the [Falcon Web Framework](https://github.com/falconry/falcon).

falcon-vue is a plug-in for distributing static files built by vue.js (vue-cli) on falcon.

## Description

falcon-vue is a plug-in for distributing static files built by vue.js (vue-cli) on falcon.
To use this plugin, you need to install vue-cli and build it to generate a static file.

## Install

```bash
pip3 install falcon-vue
```

## Usage

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

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)
