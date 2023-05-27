"""
OOP_test.py

Twitter @i_amgoke: https://twitter.com/i_amgoke

Github: https://www.github.com/Gokegold

Date Created: May 27, 2023

last modification:: [May 27, 2023]

"""
# The __str__ Method
"""
The str method is a built-in method that returns a string representation of an object.
When this method is called, it should return a human-readable string that describes the object.

EXAMPLE:
"""


class MyClass:
    def __str__(self):
        return "This is a MyClass object"


my_object = MyClass()
print(my_object)
# This is a MyClass object


# the __str__ method is called when we use the built-in str()
# function or the print() function on an object.

class TestClass:
    pass        # we didn't define __str__ here


testobject = TestClass()

print(testobject)      # <__main__.TestClass object at 0x10f580c90>

# conversely, if we don’t define the __str__ method,
# the default __str__ method will be called. And it prints some weird gibberish.

