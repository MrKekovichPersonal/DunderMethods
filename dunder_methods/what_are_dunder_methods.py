"""
dunder = double underscore
__init__ ; __add__ ; __str__
"""


class Example:
    def __init__(self, number: int):
        print("Calling init")
        self.number = number

    def __add__(self, other):
        print("Calling add")
        return self.number + other

    def __str__(self):
        print("Calling str")
        return str(self.number)
