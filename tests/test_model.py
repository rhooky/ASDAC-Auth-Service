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
        createUser("admin", "password", "email", "1234", "admin", "email")
        user = returnUser("admin")
        deleteUser("admin")
        print user
        self.assertIn("password", user['password'])

    def test_updateUser(self):
        createUser("admin", "password", "email", "1234", "admin", "email")
        user = updateUser("admin", "phone", "5555")
        self.assertIn('5555', user['phone'])

    #def test_zdeleteUser(self):
     #   createUser("computer", "password", "email", "1234", "admin", "email")
     #   deleteUser("computer")
     #   user = returnUser("computer")
     #   self.assertIsNot(str(user['username']), str("computer"))

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
