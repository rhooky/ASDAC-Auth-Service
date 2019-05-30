import os
import unittest
import myapp
import pytest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        myapp.app.testing = True
        self.app = myapp.app.test_client()

    def tearDown(self):
		pass