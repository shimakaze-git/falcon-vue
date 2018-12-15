from falcon_vue import register_vue_app
import os
import falcon
from wsgiref import simple_server


app = falcon.API()

app = register_vue_app(
    app,
    api_url="/test/hoge",
    # api_url="/",
    src_path="./test_project/dist"
)

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
