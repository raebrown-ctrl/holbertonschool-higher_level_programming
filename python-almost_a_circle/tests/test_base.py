#!/usr/bin/env python3
"""Test cases for the Base class"""
import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    """Defines a class to evaluate diferent test cases of Base"""

    def test_id_assigned(self):
        """Tests id assignment"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_id_given(self):
        """Tests id assignment when id is given"""
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base(3)
        self.assertEqual(b5.id, 3)

        b6 = Base()
        self.assertEqual(b6.id, 4)  # as previous instantiation was with id=3


if __name__ == '__main__':
    unittest.main()
