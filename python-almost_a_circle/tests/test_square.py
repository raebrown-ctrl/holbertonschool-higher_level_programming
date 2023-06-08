#!/usr/bin/env python3
"""Module for TestSquare class"""

import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import os
import io
import json


class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        s1 = Square(5)
        self.assertEqual(s1.id, 1)

        s2 = Square(5, 1, 2)
        self.assertEqual(s2.id, 2)

        s3 = Square(5, id=12)
        self.assertEqual(s3.id, 12)

    def test_attributes(self):
        s1 = Square(4, 2, 3, 12)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 12)

    def test_inheritance(self):
        s1 = Square(5)
        self.assertTrue(issubclass(type(s1), Rectangle))
        self.assertTrue(issubclass(type(s1), Base))

    def test_raise(self):
        with self.assertRaises(TypeError):
            s2 = Square()

        with self.assertRaises(ValueError):
            s3 = Square(-3, -3, -3, 12)

        with self.assertRaises(TypeError):
            s4 = Square("hi", [], {}, 12)

    def test_square_1(self):
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_2(self):
        s = Square(1, 2)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

    def test_square_3(self):
        s = Square(1, 2, 3)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_invalid_size_type(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_square_invalid_x_type(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_square_invalid_y_type(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_invalid_id(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_negative_size_square(self):
        with self.assertRaises(ValueError):
            s = Square(-1)

    def test_negative_x_square(self):
        with self.assertRaises(ValueError):
            s = Square(1, -2)

    def test_negative_y_square(self):
        with self.assertRaises(ValueError):
            s = Square(1, 2, -3)

    def test_zero_size_square(self):
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_str_square(self):
        s = Square(5, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 5")

    def test_to_dictionary(self):
        s = Square(1, 1, 1, 1)
        self.assertEqual(s.to_dictionary(), {'id': 1, 'size': 1, 'x': 1, 'y': 1})

    def test_update(self):
        s = Square(5, 2, 3, 4)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_args(self):
        s = Square(5, 2, 3, 4)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_args_with_size(self):
        s = Square(5, 2, 3, 4)
        s.update(89, 2)
        self.assertEqual(s.size, 2)

    def test_update_args_with_x(self):
        s = Square(5, 2, 3, 4)
        s.update(89, 2, 3)
        self.assertEqual(s.x, 3)

    def test_update_args_with_y(self):
        s = Square(5, 2, 3, 4)
        s.update(89, 2, 3, 4)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        s = Square(5, 2, 3, 4)
        s.update(id=101)
        self.assertEqual(s.id, 101)

    def test_update_kwargs_with_size(self):
        s = Square(5, 2, 3, 4)
        s.update(id=101, size=1)
        self.assertEqual(s.size, 1)

    def test_update_kwargs_with_x(self):
        s = Square(5, 2, 3, 4)
        s.update(id=101, size=1, x=2)
        self.assertEqual(s.x, 2)

    def test_update_kwargs_with_y(self):
        s = Square(5, 2, 3, 4)
        s.update(id=101, size=1, x=2, y=3)
        self.assertEqual(s.y, 3)

    def test_create_square(self):
        s = Square.create(id=89, size=1, x=2, y=3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_list_squares(self):
        s1 = Square(1, 1, 1, 1)
        s2 = Square(2, 2, 2, 2)
        
        # Confirm the Square instances are initialized as expected
        self.assertEqual(s1.to_dictionary(), {"id": 1, "size": 1, "x": 1, "y": 1})
        self.assertEqual(s2.to_dictionary(), {"id": 2, "size": 2, "x": 2, "y": 2})
        
        Square.save_to_file([s1, s2])
        
        with open("Square.json", "r") as f:
            contents = f.read()
            
            # Confirm that the file contains the expected text
            self.assertIn('{"id": 1, "size": 1, "x": 1, "y": 1}', contents)
            self.assertIn('{"id": 2, "size": 2, "x": 2, "y": 2}', contents)


    def test_load_from_file_not_exists(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        s1 = Square(1, 1, 1, 1)
        s2 = Square(2, 2, 2, 2)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertEqual(squares[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(squares[1].to_dictionary(), s2.to_dictionary())

if __name__ == "__main__":
    unittest.main()
