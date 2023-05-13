"""
CONSTRUCTORS

Twitter @i_amgoke: https://twitter.com/i_amgoke

Github: https://www.github.com/Gokegold

Date Created: May 12, 2023

last modification: [May 12, 2023],[May 13, 2023]
"""



# WHAT IS A CONSTRUCTOR
"""
    What is Constructor in Python?
        In object-oriented programming,
        A constructor is a special method used to create and initialize an object of a class. 
        his method is defined in the class.
        
        The constructor is executed automatically at the time of object creation.
        The primary use of a constructor is to declare and initialize data member/ instance...
        ...variables of a class.
        The constructor contains a collection of statements (i.e., instructions)
        that executes at the time of object creation to initialize the attributes of an object.
        For example, when we execute obj = Sample(),
        Python gets to know that obj is an object of class Sample
        and calls the constructor of that class to create an object.
"""


class Student:

    # constructor
    # initialize instance variable
    def __init__(self, name):
        print('Inside Constructor')
        self.name = name
        print('All variables initialized')

    # instance Method
    def show(self):
        print('Hello, my name is', self.name)


# create object using constructor
s1 = Student('Emma')
s1.show()

"""
    In the above example, an object s1 is created using the constructor
    While creating a Student object name is passed as an argument
    to the __init__() method to initialize the object.
    Similarly, various objects of the Student class can be created
    by passing different names as arguments.

"""


# WHAT IS A CONSTRUCTOR IN PYTHON
"""
    In object-oriented programming, 
    A constructor is a special method used to create and initialize an object of a class.
    This method is defined in the class.
The constructor is executed automatically at the time of object creation.

    THE PRIMARY USE OF A CONSTRUCTOR:
        is to DECLARE and INITIALIZE Data Member/ Instance Variables of a class.
        The constructor CONTAINS a COLLECTION of STATEMENTS (i.e., INSTRUCTIONS)
        This INSTRUCTIONS get executes at the time of object creation to initialize...
        ...the attributes of an object.
    FOR EXAMPLE:
        when we execute obj = Sample(), Python gets to know that obj is an object of class...
        ...Sample and calls the constructor of that class to create an object.

NOTE:
    In Python, internally, the '__new__' is the method that creates the object, 
    and '__del__' method is called to destroy the object...
    ...when the reference count for that object becomes zero.

    In Python, Object creation is divided into two parts:
        'OBJECT CREATION' and OBJECT INITIALIZATION'


        INTERNALLY, the '__new__' is THE METHOD that CREATES THE OBJECT
        WHILE
        The __init__() METHOD we can implement constructor to initialize the object.
        Syntax of a constructor
"""


# THE CONSTRUCTOR
def __init__(self):
    # Body of the constructor
    pass


"""
    WHERE:
    
    def: The keyword is used to define function.
    __init__() Method: It is a reserved method. This method gets called as soon as an object of a class is instantiated.
    self: The first argument self refers to the current object. It binds the instance to the __init__() method. It’s usually named self to follow the naming convention.
    Note: The __init__() method arguments are optional. We can define a constructor with any number of arguments.
"""

# EXAMPLE:


class Shop:

    # constructor
    # initialize instance variable
    def __init__(self, name):
        print('Inside Constructor')
        # Variable name constructed
        self.name = name
        print('All variables initialized')

    # instance Method
    def see(self):
        print('Hello, my name is', self.name)


# create object using constructor
s1 = Student('Emma')
s1.show()

"""
    OUTPUT:
        Inside Constructor
        All variable initialized
        Hello, my name is Emma
"""

"""
    NOTE:
        For every object, the constructor will be executed only once. For example,
        if we create four objects, the constructor is called four times.
        
        In Python, every class has a constructor, 
        but it’s not required to define it explicitly. Defining constructors in class is optional.
        
        Python will provide a default constructor if no constructor is defined.
"""

# TYPES OF CONSTRUCTORS
# DEFAULT CONSTRUCTOR
# PARAMETERIZED CONSTRUCTION

