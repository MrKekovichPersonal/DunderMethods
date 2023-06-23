"""
dunder = double underscore
python version: 3.10 99 in total
few examples:
__init__ ; __add__ ; __str__
"""


class Point:  # let's imagine we need to calculate points in 2d dimension.
    def __init__(self, x, y):  # point has x and y
        print('Calling __init__')
        self.x = x
        self.y = y

    def __add__(self, other):  # when we add two points
        print('Calling __add__')
        # we have to calculate new point by adding x and y of both points
        return Point(self.x + other.x, self.y + other.y)  # and return new point

    # but oh! What do we print? X? Y?
    def __str__(self):  # here comes the magic __str__ method
        print('Calling __str__')
        return f"({self.x}, {self.y})"  # we simply return two coordinates of a point


point_1 = Point(1, 2)  # calls __init__
point_2 = Point(3, 4)  # calls __init__

print(point_1)

print(point_1 + point_2)  # calls __add__  | returns new Point(4, 6) and calls __str__ for this object

str(point_2)  # calls __str__
