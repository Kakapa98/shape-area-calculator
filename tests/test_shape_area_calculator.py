import unittest
from unittest.mock import patch
from io import StringIO
import math
from  shape_area_calculator import *

class TestMultiShapeAreaCalculator(unittest.TestCase):

    @patch("builtins.input", side_effect=["5"])
    def test_get_positive_number_valid(self, mock_input):
        self.assertEqual(get_positive_number("Enter a number: "), 5.0)

    @patch("builtins.input", side_effect=["-5", "5"])
    def test_get_positive_number_non_positive(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            get_positive_number("Enter a number: ")
            self.assertIn("Please enter a positive number.", fake_output.getvalue())

    @patch("builtins.input", side_effect=["abc", "5"])
    def test_get_positive_number_non_numeric(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            get_positive_number("Enter a number: ")
            self.assertIn("Please enter a valid number.", fake_output.getvalue())

    def test_calculate_triangle_area(self):
        self.assertEqual(calculate_triangle_area(5, 3), 7.5)
        self.assertEqual(calculate_triangle_area(0, 3), 0.0)
        self.assertEqual(calculate_triangle_area(1000, 2000), 1000000.0)

    def test_calculate_square_area(self):
        self.assertEqual(calculate_square_area(4), 16.0)
        self.assertEqual(calculate_square_area(0), 0.0)
        self.assertEqual(calculate_square_area(1000), 1000000.0)

    def test_calculate_rectangle_area(self):
        self.assertEqual(calculate_rectangle_area(5, 3), 15.0)
        self.assertEqual(calculate_rectangle_area(0, 3), 0.0)
        self.assertEqual(calculate_rectangle_area(1000, 2000), 2000000.0)

    def test_calculate_circle_area(self):
        self.assertAlmostEqual(calculate_circle_area(3), 28.274333882308138)
        self.assertEqual(calculate_circle_area(0), 0.0)
        self.assertAlmostEqual(calculate_circle_area(1000), 3141592.653589793)

    @patch("builtins.input", side_effect=["1", "5", "3", "no"])
    def test_main_triangle(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            main()
            self.assertIn("The area of the triangle is 7.5.", fake_output.getvalue())

    @patch("builtins.input", side_effect=["2", "4", "no"])
    def test_main_square(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            main()
            self.assertIn("The area of the square is 16.0.", fake_output.getvalue())

    @patch("builtins.input", side_effect=["3", "5", "3", "no"])
    def test_main_rectangle(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            main()
            self.assertIn("The area of the rectangle is 15.0.", fake_output.getvalue())

    @patch("builtins.input", side_effect=["4", "3", "no"])
    def test_main_circle(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            main()
            self.assertIn("The area of the circle is 28.274333882308138.", fake_output.getvalue())

    @patch("builtins.input", side_effect=["5", "1", "5", "3", "no"])
    def test_main_invalid_choice(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            main()
            self.assertIn("Invalid choice. Please try again.", fake_output.getvalue())

    @patch("builtins.input", side_effect=["1", "5", "3", "yes", "2", "4", "no"])
    def test_main_calculate_another_area(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            main()
            self.assertIn("The area of the triangle is 7.5.", fake_output.getvalue())
            self.assertIn("The area of the square is 16.0.", fake_output.getvalue())

if __name__ == "__main__":
    unittest.main()