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
        self.assertEqual(self.rect.x , 0)
        self.assertEqual(self.rect.y , 0)

        self.rect = Rectangle(11, 23, 37, 41)

        self.assertEqual(self.rect.width , 11)
        self.assertEqual(self.rect.height , 23)
        self.assertEqual(self.rect.x , 37)
        self.assertEqual(self.rect.y , 41)

        self.rect = Rectangle(91, 83, 79, 67, 51)

        self.assertEqual(self.rect.width , 91)
        self.assertEqual(self.rect.height , 83)
        self.assertEqual(self.rect.x , 79)
        self.assertEqual(self.rect.y , 67)

    def test_types(self):
        """Type Exceptions raised"""
        with self.assertRaises(TypeError) as error1:
            self.rect.width = 91.7
        self.assertEqual(str(error1.exception), "width must be an integer")

        with self.assertRaises(TypeError) as error2:
            self.rect.height = "83"
        self.assertEqual(str(error2.exception), "height must be an integer")

        with self.assertRaises(TypeError) as error4:
            self.rect.x = {79, 97}
        self.assertEqual(str(error4.exception), "x must be an integer")

        with self.assertRaises(TypeError) as error5:
            self.rect.y = 'a'
        self.assertEqual(str(error5.exception), "y must be an integer")

    def test_values(self):
        """Value Exceptions raised"""
        with self.assertRaises(ValueError) as error1:
            self.rect.width = -91
        self.assertEqual(str(error1.exception), "width must be > 0")

        with self.assertRaises(ValueError) as error2:
            self.rect.height = -10
        self.assertEqual(str(error2.exception), "height must be > 0")

        with self.assertRaises(ValueError) as error4:
            self.rect.x = -79
        self.assertEqual(str(error4.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as error5:
            self.rect.y = -1001
        self.assertEqual(str(error5.exception), "y must be >= 0")

    def test_area(self):
        """Correct area value"""
        self.assertEqual(self.rect.area(), self.rect.width * self.rect.height)


if __name__ == "__main__":
    unittest.main()
