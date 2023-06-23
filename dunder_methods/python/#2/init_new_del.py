"""
__new__ is called when object is being created.
"""


class MyClass:
    prop1 = "'I'm property'"  # class property
    prop2 = 'hey!'  # class property
    countdown = 5

    def __init__(self, prop3, prop4):
        self.prop1 = prop3  # instance property
        self.prop2 = prop4  # instance property
        self.countdown = 0  # won't affect class property, but will rewrite instance property

    @classmethod
    def class_method1(cls):  # notice the cls. It is used to access class attributes such as prop1 and prop2
        return [cls.prop1, cls.prop2]

    @classmethod
    def class_method2(cls):  # also cls is used to access class methods
        return ['I am class method', cls.class_method1()]


