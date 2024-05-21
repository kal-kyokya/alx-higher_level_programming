#!/usr/bin/python3

# Project structure
# 0x0C-python-almost_a_circle/
# ├── models/
# │   └── base.py
# └── tests/
#     └── test_base.py


"""
'0-main' is the unit test for '/models/base.py'.
"""
import unittest
from base import Base


class BaseTestClass(unittest.TestCase):
    """Class of test methods for the Base class and its instances.

    Parent Class:
        TestCase: Sub class of the built-in unittest module.
    """

    def testBaseClass1(self):
        """First test of creation of a Base class instance."""
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

    def testBaseClass2(self):
        """Second test of creation of a Base class instance."""
        obj2 = Base()
        self.assertEqual(obj2.id, 2)

    def testBaseClass3(self):
        """Third test of creation of a Base class instance."""
        obj3 = Base(25)
        self.assertEqual(obj3.id, 25)

    def testBaseClass4(self):
        """Fourth test of creation of a Base class instance."""
        obj4 = Base()
        self.assertEqual(obj4.id, 3)


if __name__ == "__main__":
    unittest.main()
