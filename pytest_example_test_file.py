import pytest
# Our code to be tested
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height


@pytest.fixture
def rectangle():
    return Rectangle(0, 0)


def test_negative_case(rectangle):
    print(rectangle.width)
    rectangle.set_width(-1)
    rectangle.set_height(2)
    assert rectangle.get_area() == -2, "incorrect negative output"

# The test function to be executed by PyTest
# def test_normal_case():
#     rectangle = Rectangle(2, 3)
#     assert rectangle.get_area() == 6, "incorrect area"
#
# class TestGetAreaRectangle:
#     def test_normal_case(self):
#         rectangle = Rectangle(2, 3)
#         assert rectangle.get_area() == 6, "incorrect area"
#     def test_negative_case(self):
#         """expect -1 as output to denote error when looking at negative area"""
#         rectangle = Rectangle(-1, 2)
#         assert rectangle.get_area() == -2, "incorrect negative output"

