import os
import unittest
import pytest
import api

class MyTestCase(unittest.TestCase):

    def setUp(self):
        api.app.testing = True
        self.app = api.app.test_client()

    def tearDown(self):
        pass

    def test_login(self):
        response = self.app.get('/api/v1/authenticate?username=admin&password=password', follow_redirects=True)
        self.assertEqual(response.status_code, 202)
        #self.assertIn(b'True', response.data)


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
