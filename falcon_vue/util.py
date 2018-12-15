import os
import inspect


def is_path_abs(path):
    """
    Decision it is a relative path or an absolute path
    """
    if os.path.isabs(path):
        return True
    return False


def abs_dirname(filename):
    """
    Get absolute path from file name
    """
    abs_path_file = os.path.abspath(filename)
    dirname = os.path.dirname(abs_path_file)
    return dirname
