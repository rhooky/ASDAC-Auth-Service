import os
import unittest
import pytest
from model import *

class MyTestCase(unittest.TestCase):

#    def setUp(self):
#        model.app.testing = True
#        self.app = model.app.test_client()

#    def tearDown(self):
#        pass

    def test_createUser(self):
        user = createUser("admin", "password", "email", "1234", "admin")
        self.assertIn("password", user['password'])

    def test_updateUser(self):
        user = updateUser("admin_admin", "phone", "5555")
        self.assertIn('5555', user['phone'])

    def test_zdeleteUser(self):
        user = deleteUser("admin_admin")
        self.assertIs(user, 1)

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
