#!/usr/bin/python3
"""Module for TestRectangle class"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
from contextlib import redirect_stdout
import io
import json
import os


class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(10, 2)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, id=12)
        self.assertEqual(r3.id, 12)

    def test_attributes(self):
        r1 = Rectangle(4, 2, 1, 1, 12)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, 12)

    def test_raise(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle()

        with self.assertRaises(ValueError):
            r5 = Rectangle(-3, -3, -1, -1, 12)

        with self.assertRaises(TypeError):
            r6 = Rectangle("hi", "hello", [], {}, 12)

    def test_rectangle_1(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_2(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)

    def test_rectangle_3(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_invalid_width_type(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rectangle_invalid_height_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rectangle_invalid_x_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rectangle_invalid_y_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rectangle_invalid_id(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_rectangle_negative_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

    def test_rectangle_negative_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)

    def test_rectangle_zero_width(self):
        with self.assertRaises(ValueError):
                r = Rectangle(0, 2)

    def test_rectangle_zero_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    def test_rectangle_negative_x(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)

    def test_rectangle_negative_y(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)

    def test_rectangle_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_rectangle_str(self):
        r = Rectangle(1, 2, 3, 4, 99)
        self.assertEqual(str(r), "[Rectangle] (99) 3/4 - 1/2")

    def test_display_no_xy(self):
        r = Rectangle(4, 6)
        expected_output = "####\n" * 6
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
        self.assertEqual(output, expected_output)

    def test_display_no_y(self):
        r = Rectangle(4, 6, 2)
        expected_output = "  ####\n" * 6
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
        self.assertEqual(output, expected_output)

    def test_display(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            r1 = Rectangle(3, 2, 1, 1)
            r1.display()
            output = buf.getvalue()
        expected_output = "\n ###\n ###\n"
        self.assertEqual(output, expected_output)

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(r1.to_dictionary(), {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)

    def test_update_id(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)

    def test_update_id_width(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 1)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

    def test_update_id_width_height(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 1, 2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_update_id_width_height_x(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 1, 2, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

    def test_update_id_width_height_x_y(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 1, 2, 3, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_update_kwargs_id(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(id=89)
        self.assertEqual(r1.id, 89)

    def test_update_kwargs_id_width(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(id=89, width=1)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

    def test_update_kwargs_id_width_height(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(id=89, width=1, height=2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_update_kwargs_id_width_height_x(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(id=89, width=1, height=2, x=3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

    def test_update_kwargs_id_width_height_x_y(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_create_id(self):
        r1 = Rectangle.create(id=89)
        self.assertEqual(r1.id, 89)

    def test_create_id_width(self):
        r1 = Rectangle.create(id=89, width=1)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

    def test_create_id_width_height(self):
        r1 = Rectangle.create(id=89, width=1, height=2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_save_to_file_None(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file_rectangle_list(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            contents = json.load(file)
            expected = [{"y": 0, "x": 0, "id": 1, "height": 2, "width": 1}]
            self.assertListEqual(contents, expected)

    def test_load_from_file_no_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        rectangles = Rectangle.load_from_file()
        self.assertEqual(rectangles, [])

    def test_load_from_file_with_file(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 1)
        self.assertEqual(rectangles[0].width, 1)
        self.assertEqual(rectangles[0].height, 2)

    def test_save_to_file_empty_list(self):
        """Test save_to_file with an empty list"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Rectangle.json")  # cleanup: remove the file after the test
        with self.assertRaises(FileNotFoundError):
            with open("Rectangle.json", "r") as file:
                pass  # just try to open the file, expecting it to not exist

if __name__ == "__main__":
    unittest.main()
