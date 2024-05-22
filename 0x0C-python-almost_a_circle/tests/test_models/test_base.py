#!/usr/bin/python3

# Project structure
# 0x0C-python-almost_a_circle/
# ├── models/
# │   └── base.py
# └── tests/
#     └── test_models/
#         └── test_base.py


"""
'0-main' is the unit test for '/models/base.py'.
"""
import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """Class of test methods for the Base class and its instances.

    Parent Class:
        TestCase: Sub class of the built-in unittest module.
    """

    def test_id_value(self):
        """Correct creation of Base instance"""
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

        obj2 = Base()
        self.assertEqual(obj2.id, 2)

        obj3 = Base(25)
        self.assertEqual(obj3.id, 25)

        obj4 = Base()
        self.assertEqual(obj4.id, 3)


if __name__ == "__main__":
    unittest.main()
