import os
import unittest
import pytest
import api
from model import *

class MyTestCase(unittest.TestCase):

    def setUp(self):
        api.app.testing = True
        self.app = api.app.test_client()

    def tearDown(self):
        pass

    def test_login(self):
        response = self.app.get('/api/v1/authenticate?username=admin&password=password', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'true', response.data)

    
    def test_login_fail(self):
        response = self.app.get('/api/v1/authenticate?username=admin&password=notthepassword', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'true', response.data)

    def test_notification(self):
        createUser("admin", "password", "email", "1234", "admin", "email")
        response = self.app.get('/api/v1/getNotificationMethod?username=admin', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(u'email', response.data)
        deleteUser("admin")


if __name__ == '__main__':
    unittest.main()


# Method	Equivalent to
# .assertEqual(a, b)	a == b
# .assertTrue(x)	bool(x) is True
# .assertFalse(x)	bool(x) is False
# .assertIs(a, b)	a is b
# .assertIsNone(x)	x is None
# .assertIn(a, b)	a in b
# .assertIsInstance(a, b)	isinstance(a, b)
# .assertIs(), .assertIsNone(), .assertIn(), and .assertIsInstance() all have opposite methods, named .assertIsNot(), and so forth.
