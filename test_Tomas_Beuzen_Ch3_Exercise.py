from Tomas_Beuzen_Ch3_Exercise import Circle, Sphere
import math

import unittest
from io import StringIO
import sys
import math


class TestCircle(unittest.TestCase):

    # def test_radius_of_one_returns_float(self):
    #     test_area = area(1)
    #     assert type(test_area) is float
    #
    #
    # def test_radius_of_zero_returns_zero(self):
    #     test_area = area(0)
    #     assert test_area == 0
    #
    # def test_radius_of_five_returns_approx_value(self):
    #     test_area = area(5)
    #     print("Test area of radius 5: ", test_area)
    #     assert test_area == 78.5
    #     # compare = math.isclose(test_area,178.5, abs_tol=0.1)
    #     # print("Compare: ", compare)
    #     # assert compare == True
    #
    # def test_radius_of_str_ten_throws_exception(self):
    #     # with self.assertRaises(TypeError) as context:
    #     #     test_area = area('10')
    #     #     # print("Test area of radius 5: ", test_area)
    #     #     # print(str(context.exception))
    #     # self.assertTrue("Radius should be a number." in str(context.exception))
    #     # # print(str(context.exception))
    #
    #     captured_output = StringIO()
    #     sys.stdout = captured_output
    #
    #     area('10')
    #     self.assertIn("Radius should be a number. You have entered a", captured_output.getvalue())
    #
    # def test_radius_throws_TypeError_for_non_int_or_float(self):
    #     with self.assertRaises(TypeError) as context:
    #         test_area = area('10')
    #         print("Test area of radius 5: ", test_area)
    #         print(str(context.exception))
    #     self.assertTrue("Radius should be an int or float. You have entered a" in str(context.exception))
    #     #
    #     # captured_output = StringIO()
    #     # sys.stdout = captured_output
    #     #
    #     # area('10')
    #     # self.assertIn("Radius should be an int or float. You have entered a", captured_output.getvalue())

    def test_for_class_circle(self):
        print("Radius of circle: ", Circle(3).radius)
        assert Circle(3).radius == 3 #"Test 1 failed."
        assert math.isclose(Circle(3).area(), 28.3, abs_tol=0.1) # "Test 2 failed."
        assert math.isclose(Circle(3).circumference(), 18.8, abs_tol=0.1) # "Test 3 failed."
        assert Circle(3).__str__() == "A Circle with radius 3" # "Test 4 failed."

    def test_for_class_sphere(self):
        assert Sphere(3).radius == 3, "Test 1 failed."
        assert math.isclose(Sphere(3).area(), 28.3, abs_tol=0.1), "Test 2 failed."
        assert math.isclose(Sphere(3).circumference(), 18.8, abs_tol=0.1), "Test 3 failed."
        assert math.isclose(Sphere(3).volume(), 113.1, abs_tol=0.1), "Test 3 failed."
        assert Sphere(1).__str__() == "A Sphere with volume 4.19", "Test 4 failed."

    def test_from_circ_method(self):
        assert Sphere.from_circ(0).radius == 0, "Test 1 failed."
        assert Sphere.from_circ(3 * math.pi).radius == 1.5, "Test 2 failed."
        assert math.isclose(Sphere.from_circ(6).radius, 0.95, abs_tol=0.1), "Test 3 failed."
        assert math.isclose(Sphere.from_circ(6).volume(), 3.65, abs_tol=0.1), "Test 4 failed."
        assert Sphere.from_circ(6).__str__() == "A Sphere with volume 3.65", "Test 5 failed."



