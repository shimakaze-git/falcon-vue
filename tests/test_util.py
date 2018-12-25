#!/usr/bin/python
'''
Created on 2018/12/25
@author: shimakaze-git
'''
import unittest
import sys
import os
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from falcon_vue.util import is_path_abs, abs_dirname


class TestUtil(unittest.TestCase):
    """ Test Util Class """

    def setUp(self):
        """ setUp """
        self.test = "gegrege"
        self.root_dir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

    def test_is_path_abs(self):

        """ file_path """
        file_path = os.path.abspath(__file__)
        self.assertTrue(is_path_abs(file_path))

        """ setup_file_path """
        setup_file_path = self.root_dir
        setup_file_path += "/setup.py"
        self.assertTrue(is_path_abs(setup_file_path))

    def test_abs_dirname(self):
        file_path = os.path.abspath(__file__)

        tests_dir = self.root_dir + "/tests"
        self.assertTrue(abs_dirname(file_path))
        self.assertEqual(tests_dir, abs_dirname(file_path))


if __name__ == '__main__':
    unittest.main()
