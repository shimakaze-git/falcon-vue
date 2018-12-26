import os
import sys
import inspect

from .core import FalconVueAdapter
from .util import is_path_abs, abs_dirname


def register_vue_app(
    app,
    api_url="/dist",
    src_path=""
):
    """""
    register_vue_app

    Parameters
    ----------
    app : object
        falcon.API object
    api_url : str
        api url
    src_path : str
        api src path

    Returns
    -------
    app : object
        falcon.API object
    """""

    if is_path_abs(src_path):
        src_full_path = src_path
    else:
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0]) 
        filename = module.__file__

        dirname = abs_dirname(filename)
        src_full_path = os.path.abspath(
            dirname + "/" + src_path
        )

    if os.path.exists(src_full_path):
        falcon_vue = FalconVueAdapter(src_full_path, api_url)
        app.add_sink(falcon_vue, api_url)

        return app
    else:
        sys.exit("Error : %s directory does not exist." % (src_path))
