
import unittest
from io import StringIO
import sys


# Assume the area function is defined in a module named 'circle'
# from circle import area

def area(radius: float):
    """Calculate the area of a circle based on the given radius."""
    try:
        return 3.14 * radius * radius
    except TypeError:
        print("Radius should be a number. You have entered a", type(radius))


class TestAreaFunction(unittest.TestCase):

    def test_area_valid_input(self):
        self.assertAlmostEqual(area(5), 78.5)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(2.5), 19.625)

    def test_area_invalid_input(self):
        # Redirect stderr to capture print statements
        captured_output = StringIO()
        sys.stdout = captured_output

        area("ten")
        self.assertIn("Radius should be a number. You have entered a", captured_output.getvalue())

        area([10])
        self.assertIn("Radius should be a number. You have entered a", captured_output.getvalue())

        # Reset redirect.
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()