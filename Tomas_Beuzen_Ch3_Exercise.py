# 1.
# The function area() accepts the argument radius and calculates the area of a circle.
#
# Write three tests using assert statements for the following conditions:
#
# Assert that area(1) returns a float;
#
# Assert that area(0) returns a value of 0;
#
# Assert that area(5) is approximately equal to 78.5 (hint: math.isclose(..., abs_tol=0.1))

# 2.
# In the spirit of the EAFP (easier to ask for forgiveness than permission) philosophy.
#
# Modify the code of the function area() and add a try/except statement to
#
# catch the type error raised by passing a string to area() as shown below:
#
# area('10')

#3.
#In the spirit of the LBYL (look before you leap) philosophy.
#
# Modify the code of the function area()
#
# and add a conditional if/else statement to make sure that a user has passed a number (int or float)
#
# to the area() function.
#
# If they pass something else, raise a TypeError.
#
#5.
# For this exercise I want you to create a class called Circle. It should have the following characteristics:
#
# It should be initiated with the argument radius and store this as an instance attribute.
#
# Have a method area() which calculates the area of the circle.
#
# Have a method circumference() which calculates the circumference of the circle.
#
# Have the method __str__() which is a special method in Python and
#
# controls what is output to the screen when you print() an instance of your class (learn more here).
#
# The print() statement should print the string f"A Circle with radius {self.radius}".
#
# I’ve provided some tests for you to check your class.
import math


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def __str__(self):
        return f"A Circle with radius {self.radius}"

    def area(self):

        """Calculate the area of a circle based on the given radius."""
        # try:
        #     return math.pi * radius ** 2
        # except TypeError:
        #     print(f"radius should be a number but you entered a {type(radius)}")
        # except:
        #     print("Some other error occurred!")

        if type(self.radius) is (int or float):
            return math.pi * self.radius * self.radius
        else:
            raise TypeError("Radius should be an int or float. You have entered a", type(self.radius))

        # try:
        #     #return 10*3.14*'10'*'10'
        #     return 3.14*radius*radius
        # except TypeError:
        #     print("Radius should be a number. You have entered a", type(radius))

    def circumference(self):
        return 2*math.pi*self.radius


class Sphere(Circle):
    # def __init__(self):
    #     super().__init__()

    def __str__(self):
        return f"A Sphere with volume {round(self.volume(), 2)}"

    def volume(self):
        return (4/3)*math.pi*self.radius*self.radius*self.radius

    @classmethod
    def from_circ(cls, circ: float):
        rad = circ/(2*math.pi)
        return cls(rad)


if __name__ == '__main__':
    # circle1 = Circle(10)
    # print(str(circle1))
    # print(Sphere(1))
    print(Sphere.from_circ(6).__str__())
    # test_area = area('10')
    # print("Test area: ", test_area)



