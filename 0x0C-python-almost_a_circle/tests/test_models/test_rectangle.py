#!/usr/bin/python3
"""
'test_rectangle' is a class testing module.
"""
import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """Tests the implementations of the Rectangle class.

    Parent class:
        unittest.TestCase: Provides resources for proper testing.
    """

    def setUp(self):
        """Initializes values to be create before each test."""
        self.rect = Rectangle(17, 29)

    def test_instanciation(self):
        """Right instanciation of Rectangle objects"""
        self.assertIsInstance(self.rect, Rectangle)

    def test_init(self):
        """Proper initialization of Rectangle objects"""
        self.assertEqual(self.rect.width , 17)
        self.assertEqual(self.rect.height , 29)
        self.assertEqual(self.rect.id , 4)
        self.assertEqual(self.rect.x , 0)
        self.assertEqual(self.rect.y , 0)

        self.rect = Rectangle(11, 23, 37, 41)

        self.assertEqual(self.rect.width , 11)
        self.assertEqual(self.rect.height , 23)
        self.assertEqual(self.rect.id , 5)
        self.assertEqual(self.rect.x , 37)
        self.assertEqual(self.rect.y , 41)

        self.rect = Rectangle(91, 83, 79, 67, 51)

        self.assertEqual(self.rect.width , 91)
        self.assertEqual(self.rect.height , 83)
        self.assertEqual(self.rect.id , 51)
        self.assertEqual(self.rect.x , 79)
        self.assertEqual(self.rect.y , 67)



if __name__ == "__main__":
    unittest.main()
