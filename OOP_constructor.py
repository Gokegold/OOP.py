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
# PARAMETERIZED CONSTRUCTION = def __init__(self):
# Non-PARAMETERIZED CONSTRUCTION = def __init__(self, v1, v2..., vn):

# DEFAULT CONSTRUCTOR
"""
    python will provide a default constructor if no constructor is defined.
    Python adds a default constructor when we  do not include the  constructor in the class
    or when w forget to declare created constructor(s)
    no task are preformed object are only initialized.
    BECAUSE: The construct is without a body hence it's empty and can not preform. 
    It does not perform any task but initializes the objects.
    It is an empty constructor without a body.
    
    Note:
        The default constructor is not present in the source py file.
        It is inserted into the code during compilation if not exists. See the below image.
        If you implement your constructor, then the default constructor will not be added.
"""


class Employees:

    def display(self):
        print('Inside Display')


emp = Employees()
emp.display()


# NON-PARAMETERIZED CONSTRUCTION
"""
    A constructor without any arguments is called a non-parameterized constructor.
    This type of constructor is used to initialize each object with default values.

    This constructor does not accept the arguments during object creation.
    Instead, it initializes every object with the same set of values.
"""


# NON ARGUMENT CONSTRUCTOR
class Company:

    # no-argument constructor
    def __init__(self):
        self.name = "NATIVE"
        self.address = "ABC Street"

    # a method for printing data members
    def show(self):
        print('Name:', self.name, 'Address:', self.address)


# creating object of the class
cmp = Company()

# calling the instance method using the object
cmp.show()


# PARAMETERIZED CONSTRUCTION
"""
    Parameterized Constructor
        A constructor with defined parameters or arguments is called a parameterized constructor.
        We can pass different values to each object at the time of creation using a parameterized constructor.
        
        The first parameter to constructor is self that is a reference to the being constructed,
        and the rest of the arguments are provided by the programmer.
        A parameterized constructor can have any number of arguments.
        
        For example, consider a company that contains thousands of employees.
        In this case, while creating each employee object,
        we need to pass a different name, age, and salary. In such cases,
        use the parameterized constructor.
"""


class Employees:
    # parameterized constructor
    def __init__(self, name, age, salary):
        # name is a parameter pass or the argument
        # age is a parameter passed
        self.name = name
        self.age = age
        self.salary = salary

    # display object
    def shows(self):
        print(self.name, self.age, self.salary)


# creating object of the Employee class
emma = Employees('Emma', 23, 7500)
emma.shows()

kelly = Employees('Kelly', 25, 8500)
kelly.shows()
