"""
Create Instance Variables

Ways to Access Instance Variable

Instance Variables Naming Conventions

Dynamically Adding Instance Variable to Object

Dynamically Delete Instance Variable

Twitter @i_amgoke: https://twitter.com/i_amgoke

Github: https://www.github.com/Gokegold

Date Created: April 28, 2023

last modification:: [May 8, 2023],[May 9, 2023],[May 10, 2023],[May 11, 2023],[May 12, 2023]

"""
# Instance variables are declared inside a method using the self keyword.
# We use a constructor to define and initialize the instance variables.
# Let’s see the example to declare an instance variable in Python.

# EXAMPLE ONE

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create first object
s1 = Student("Jessa", 20)

# access instance variable
print('Object 1')
# Output = <__main__.Student object at .......>
print('Name:', s1.name)
# output = Name: Jesse
print('Age:', s1.age)
# Output = Age: 20

# create second object
s2= Student("Kelly", 10)

# access instance variable
print('Object 2')
print('Name:', s2.name)
# Output = Name: Kelly
print('Age:', s2.age)
# Output = Age: 10

# WAYS TO ACCESS INSTANCE VARIABLE

"""
There are two ways to access the instance variable of class:

Within the class in instance method by USING THE OBJECT REFERENCE (self)
Using getattr() method
"""


# USING THE OBJECT REFERENCE
# EXAMPLE ONE
class Student:
    # The 'def' function as a constructor
    # nom, sex, percentage are the Parameters to construct
    def __init__(self, nom, sex, percentage):
        # INSTANCE VARIABLE
        self.nom = nom
        self.sex = sex
        self.percentage = percentage

    # Here is the INSTANCE METHOD
    # the behavior of the class Student and how the format of how th object will act
    # Instance method access instance variable
    def show(self):
        print("Students Name is,", self.nom, "and Student is a,", self.sex, "With a percentage of", self.percentage)


# Create object
# The object to the class Student
stud = Student
# The instances of the object stud
jesse = Student('Jesse', 'Female', '15%')
# Call instance method
stud.show(jesse)


# EXAMPLE TWO
# USING getattr(object, Parameters in the constructor
"""
ACCESS INSTANCE VARIABLE USING getattr()
To gain access into ACCESS VARIABLE
"""

# EXAMPLE TWO
"""
ACCESS INSTANCE VARIABLE USING getattr()
To gain access into ACCESS VARIABLE
    Pass the object reference and instance variable name to the getattr() method...
    ...to get the value of an instance variable.
    
    getattr(Object, 'instance_variable')
"""


class Pupils:
    # constructor
    def __init__(self, noms, ages):
        # Instance variable
        self.noms = noms
        self.ages = ages


# create object
pupil = Pupils("Jesse", 20)

# Use getattr() to access the values of the instance variable
print('Name: ', getattr(pupil, 'noms'))
print("AGE: ", getattr(pupil, 'ages'))


# INSTANCE VARIABLES NAMING CONVENTIONS
"""
    Instance variable names should be all lower case. For example, 'id'
    Words in an instance variable name should be separated by an underscore.
    # FOR EXAMPLE, store_name
    Non-public instance variables should begin wth a single Underscore
    if an instance needs to bee mangled, two underscores may begin its name
"""
# DYNAMICALLY ADD INSTANCE VARIABLE TO A OBJECT
"""
    We can add instance variables from the outside of class to a particular object.
    Use the following syntax to add the new instance variable to the object
    object_referance.variable_name = value
"""


# EXAMPLE:
class Apprentice:
    # Instance variable
    def __init__(self, names, ages):
        self.names = names
        self.ages = ages


# create object
app = Apprentice('JONES', 21)

print('Before')
print('Name:', app.names, 'AGES:', app.ages)

# add new instance variable 'scores' to app
app.scores = 75
print('After')
print('Name:', app.names, 'AGES:', app.ages), 'SCORES:', app.scores)

"""
NOTE:
    We cannot add an instance variable to a class from outside...
    ...because INSTANCE VARIABLE BELONGS TO OBJECTS.
    
    Adding an instance variable to one object will not be reflected the remaining objects...
    ...because every object has a separate copy of the instance variable.
    (i.e) app = Apprentice('JONES', 21), instance variable remains ('JONES', 21)
"""


# DYNAMICALLY DELETE INSTANCE VARIABLE
"""
NOTE:
    In Python, we use the del statement and delattr() function to delete the attribute of an object.
    Both of them do the same thing.
    
DEL STATEMENT
    del statement: The del keyword is used to delete objects.
    In Python, everything is an object,...
    ...so the del keyword can also be used to delete variables,...
    ...lists, or parts of a list, etc.
    
DELATTR() FUNCTION
    delattr() function: Used to delete an instance variable dynamically.

NOTE:
    When the deleted attribute is tried to be accessed, Attribute error, is raised.
"""


# EXAMPLE 1.
class Student:
    def __init__(self, roll_no, name):
        # Instance variable
        self.roll_no = roll_no
        self.name = name


# create object
s1 = Student(10, 'Jessa')
print(s1.roll_no, s1.name)

# del name
del s1.name
# Try to access name variable
print(s1.name)


class Freshman:
    def __init__(self, roll_no, tag):
        # Instance variable
        self.roll_no = roll_no
        self.tag = tag


f1 = Freshman(10, 'JENNY')
print(s1.roll_no, s1.name)

del f1.roll_no
print(f1.tag)


# DYNAMICALLY DELETE INSTANCE VARIABLE
"""
NOTE:
    In Python, we use the del statement and delattr() function to delete the attribute of an object.
    Both of them do the same thing.
    
DEL STATEMENT
    del statement: The del keyword is used to delete objects.
    In Python, everything is an object,...
    ...so the del keyword can also be used to delete variables,...
    ...lists, or parts of a list, etc.
    
DELATTR() FUNCTION
    delattr() function: Used to delete an instance variable dynamically.

NOTE:
    When the deleted attribute is tried to be accessed, Attribute error, is raised.
"""


# USING THE del FUNCTION
# EXAMPLE 1.
class Student:
    def __init__(self, roll_no, name):
        # Instance variable
        self.roll_no = roll_no
        self.name = name


# create object
s1 = Student(10, 'Jessa')
print(s1.roll_no, s1.name)

# del name
del s1.name
# Try to access name variable
print(s1.name)


class Freshman:
    def __init__(self, roll_no, tag):
        # Instance variable
        self.roll_no = roll_no
        self.tag = tag


f1 = Freshman(10, 'JENNY')
print(s1.roll_no, s1.name)

del f1.roll_no
print(f1.tag)

# USING THE delattr() FUNCTION

"""
    delattr() function
        The delattr() function is used to delete the named attribute from the object...
        ...with the prior permission of the object. Use the following syntax.
    USING:
        delattr(object, 'name')
            object:
                the object whose attribute we want to delete
            name:
                the name of the instance variable we wish to delete from the chosen object
"""


# EXAMPLE_1
class Undergraduate:
    def __init__(self, naam, span, gender):
        self.naam = naam
        self.span = span
        self.gender = gender

    def reveal(self):
        print(self.span, self.gender)


U_1 = Undergraduate("PRINCE", "Male", 72)
U_1.reveal()
delattr(U_1, 'gender')
U_1.reveal()

"""
    NOTE: 
        For the del function the syntax is
            del object.name
                Object:
                    the object we wish to delete from 
                name:
                    the instance variable we want to delete from the selected object
        
        FOR THE delattr() function:
            the delattr function stands for delete attribute the syntax is
                delattr(object, name)
                    Object:
                    the object we wish to delete from 
                name:
                    the instance variable we want to delete from the selected object
"""

# ACCESS INSTANCE VARIABLE FROM ANOTHER CLASS

"""
    USING OBJECT REFERENCE
        Using this One class instance variable can be accessed by another 
    
    It is useful when we implement the concept of inheritance in Python, and we want to access the parent class instance variable from a child class.

    let’s understand this with the help of an example.
    
    In this example, the engine is an instance variable of the Vehicle class.
    We inherited a Vehicle class to access its instance variables in Car class
"""


class Conveyance:
    def __init__(self):
        self.engine = '1500cc'


# Inheriting the instance variable from th class conveyance
class Carrier(Conveyance):
    def __init__(self, top_speed):
        # Call parent class constructor
        super().__init__()
        self.top_speed = top_speed

    def display(self):
        # Accessing parent class instance variable 'engine'
        # print("Engine:", self.engine)
        # print("TOP SPEED:", self.top_speed)
        return f'The car {"ENGINE".swapcase()} number:{self.engine} and TOP SPEED of the car is:{self.top_speed}'


carrier_1 = Carrier(280)
carrier_1.display()
print(carrier_1.display())

# LIST ALL INSTANCE VARIABLES OF A OBJECT LIKE A DICTIONARY
"""
    We can get the list of all the instance variables the object has.
    Use the __dict__ function of an object to get all instance variables along with their value.
    
    The __dict__ function returns a dictionary that contains variable name as a key...
    ...and variable value as a value
"""


class SchoolChild:
    def __init__(self, roll_call, label):
        self.roll_call = roll_call
        self.label = label


sc_1 = SchoolChild(10, 'JERRY')
sc_2 = SchoolChild(20, 'JAMES')
print("INSTANCE VARIABLE OBJECT HAS")
print(sc_1.__dict__)
print(sc_2.__dict__)
# Output of print(sc_1.__dict__) IS {'roll_call': 10, 'label': 'JERRY'}


# Get each instance variable
# like ever for loop it prints the item in the items
for key_value in sc_1.__dict__.items():
    # This says use the instance variable from the object created...
    # ...to create a list in a dictionary.
    print(key_value[0], '=', key_value[1])
    # Output for key_value[0] is roll_call = 10
    # Output for key_value[1] is label = JERRY
    """
        the object sc_1 created has it instance variable passed in it
        OR initialized variable in it
        and
        the variables are number or counted from zero to the max number if variable in the object
        as for sc_1:
            sc_1 = SchoolChild(10, 'JERRY')
                the instance variable '10' which in a variable initialized as 'roll_call' is counted as 0
            sc_1 = SchoolChild(10, 'JERRY')
                the instance variable 'JERRY' which in a variable initialized as 'label' is counted as 1
        HENCE:
            The result of for key_value[0], '=', key_value=[1] will be,
                roll_call = 10
                label = JERRY

    """

for value in sc_2.__dict__.values():
    print(value[0], '=', value[2])



"""
    ALL OUTPUT
        Name:  Jesse
        AGE:  20
        
        Before
        Name: JONES AGES: 21
        
        After
        Name: JONES AGES: 21 SCORES: 75
"""

