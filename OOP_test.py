"""
OOP_test.py

Twitter @i_amgoke: https://twitter.com/i_amgoke

Github: https://www.github.com/Gokegold

Date Created: April 28, 2023

last modification:: [May 8, 2023],[May 9, 2023],[May 10, 2023],[May 12, 2023], [May 18, 2023], [May 27, 2023], [May 28, 2023]

"""


# QUESTION 1
# OOP Exercise 1: Create a Class with instance attributes
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    # constructor
    def __init__(self, mileage, max_speed):
        self.mileage = mileage
        self.max_speed = max_speed

    def camry(self):
        return 'engine' ' ' 'chase'.format(self.mileage, self.max_speed)


# Variable declared outside __init__() belong to the class. They’re shared by all instances.
# create the object(modelx)
# values are passed to the instance variables using a constructor.
modelx = Vehicle(240, 18)
ev = Vehicle(400, 80)

modelx.mileage = 700
modelx.max_speed = 1000

# modify instance variable
ev.mileage = 1000
ev.max_speed = 1000

print('modelx: ', modelx)
print('ev-Max_speed: ', ev.max_speed, ' Ev-Mileage: ', ev.mileage)
print('modelx.max_speed: ', modelx.max_speed, ' Modelx.mileage: ', modelx.mileage)
print(modelx.__dict__)
print('Camry-modelx: ', modelx.camry())

print(' ')
print(Vehicle.camry(modelx))
print(ev.mileage)

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
print('Name:', s1.name)
print('Age:', s1.age)

# create second object
s2 = Student("Kelly", 10)

# access instance variable
print('Object 2')
print('Name:', s2.name)
print('Age:', s2.age)


# QUESTION 2
# OOP Exercise 2: Create a Vehicle class without any variables and methods

class Vehicle:
    pass

# QUESTION 3
# OOP Exercise 3: Create a child class Bus that will inherit all of
# the variables and methods of the Vehicle class


class Automobile:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Automobile):

    def __init__(self, name, max_speed, mileage, color):
        # Super().__init__ means copy the __init__ of the class to inherit from
        super().__init__(name, max_speed, mileage)
        self.color = color


#child = Bus('Oval', 840, 789, 'Blue')
#print('Vehicle Name', name, 'Speed',max_speed, 'mileage' 'child.color)

# INHERITANCE
# TYPES OF INHERITANCE

# Single inheritance:
# Single, inheritance a child class inherits from a single-parent class.
# Here there is on e child and parent class.

# EXAMPLE:

class Mobile:
    def mobile_info(self):
        print('Inside Mobile class')


class Car(Mobile):
    def car_info(self):
        print('Inside car class')


car = Car()

car.mobile_info()
car.car_info()

# Multiple Inheritance
# In multiple inheritance, one child can inherit from multiple parent classes.

# Example:


# Parent class 1
class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name: ', name, 'Age: ', age)


# Parent class 2
class Company:

    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name: ', company_name, 'location: ', location)


class Employee(Person, Company):
    def employee_info(self, salary, skill):
        print('Inside Employee class')
        print('salary: ',  salary, ' Skill: ',  skill)


# create  object of employee
employ = Employee()

# access date
employ.person_info('Jesse', 28)
employ.company_info('Google', 'Atlanta')
employ.company_info(12000, 'Machine Learning')


# MULTILEVEL INHERITANCE

# Multilevel Inheritance: a class inherits from a child class or derived class.
# Suppose three classes A,B,c.
# Where A is the superclass,
# B is the child class of A
# C is the child class of B
# In other words we can say, multilevel inheritance could be called a chain of classes

# EXAMPLE

# Base class
class Motor:
    def motor_info(self):
        print('Inside Motor class')


# Child class
class Machine(Motor):
    def machine_info(self):
        print('Inside Machine class')


# Child class
class SportCar(Machine):
    def sport_car_info(self):
        print('Inside Sport Car class')


# create object of Sport-Car
s_car = SportCar()

print(s_car.motor_info())
print(s_car.sport_car_info())
print(s_car.machine_info())
"""
In the above example, we can see there are three classes named Vehicle, Car, SportsCar. 
Vehicle is the superclass, 
Car is a child of Vehicle,
SportsCar is a child of Car. 
So we can see the chaining of classes.
"""

# HIERARCHICAL INHERITANCE

# Hierarchical Inheritance:
# In Hierarchical inheritance, more than one child class is derived from a single parent class.
# In other words, we can say,
# Hierarchical Inheritance is one parent class and multiple child classes.

# EXAMPLE


# Parent class
class Wheels:
    def info(self):
        print('Inside Wheels class')


# Child class
class Jalopy(Wheels):
    def jalopy_info(self, name):
        print('car name is:', name)


# Child class
class Limo(Wheels):
    def limo_info(self, name):
        print('Inside Limo class: ',name)


# create object for Jalopy
obj1 = Jalopy()
obj1.info()
obj1.jalopy_info('BWN')

obj2 = Limo()
obj2.info()
obj2.limo_info('GAC')


# Hybrid Inheritance

# HYBRID INHERITANCE:

# When inheritance consists of multiple types or a combination of different
# inheritance is called hybrid inheritance.

# EXAMPLE:

# Parent class
class Company:
    def company_name(self):
        return 'Google'

class Employee(Company):
    def info(self):
        # Calling the superclass method using super()function
        c_name = super().company_name()
        print("Jessa works at", c_name)

# Creating object of child class
emp = Employee()
emp.info()


class Carriage:
    def carriage_info(self):
        print('Inside Carriage class')

# Parent class
class MotorCar(Carriage):
    def __init__(self, name, color, doors, engine):
        self.name = name
        self.color = color
        self.doors = doors
        self.engine = engine

    def motor_info(self):
        return 'Name: ' ' ' 'Color: '.format(self.name, self.color)


class Truck(MotorCar):
    def truck_info(self):
        return 'Doors: ' ' Engine: '.format(self.doors, self.color)

    def truck_info(self):
        print("Inside Truck class")

class RaceCars(MotorCar, Carriage):
    def race_car_info(self):
        return 'Doors ' ' Engine'.format(MotorCar, Carriage)




prod_1 = MotorCar('TOYOTA', 'BLACK')
prod_2 = Truck(4, 4.5)


class Saloon:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def saloon_info(self):
        return f'car-brand:{self.name} \nCars-color:{self.color}'


class Car(Saloon):
    doors = 4
    engine = 'Two Horse Power'

    def car_info(self):
        return f'car-brand:{self.doors} \nCars-color:{self.engine}'


class Truck(Saloon):

    def truck_info(self):
        print("Inside Truck class")


# Sports Car can, inherits properties of Vehicle and Car
class SportsCar(Car, Saloon):
    def sports_car_info(self):
        print("Inside SportsCar class")


# create object
driver_1 = Saloon('Fear', 'Blue')
driver_2 = Saloon('Modelx', 'Red')
four_doors = Car(4, 'Two Horse Power')
two_doors = Car(2, 'Two Horse Power')

print(Saloon.saloon_info(driver_1))
print(' ')
print(Saloon.saloon_info(driver_2))
print(Car.car_info(two_doors))

# QUESTION $

"""
        write the controller class for the following Blood Pressure Calculator,...
        ...if you know the normal pressure is 120/80 
        should any number go higher meaning pressure increased
        and vice versa
"""

class BloodPressure:
    def pressure(self, systolic_p, diastolic_p):
        return f"{systolic_p}/{diastolic_p}"


normal = BloodPressure()
normal.systolic = 180
normal.diastolic = 80
print(f"Healthy Pressure is: {normal.systolic}/{normal.diastolic}")

print("Enter Details")
user = BloodPressure()
user.systolic = input("Systolic: ")
user.diastolic = input("Diastolic: ")
print(f"Your Pressure is: {user.systolic}/{user.diastolic}")


class CheckUp:
    healthy_systolic = 120
    healthy_diastolic = 80

    def __init__(self, name: str, systolic: float, diastolic: float):

        assert diastolic >= 70
        print(f"An instance created: {name}")
        self.name = name
        self.systolic = systolic
        self.diastolic = diastolic
        # Above a dynamic attribute name has been assigned using self.name

    def patient_pressure(self):
        return f"{self.systolic}/{self.diastolic}"


patient_1 = CheckUp("John", 180, 70)
patient_2 = CheckUp("TOl", 182, 72)

print(patient_2.patient_pressure())

# QUESTION @

"""
Create a Car class with two instance attributes:

.color, which stores the name of the car’s color as a string
.mileage, which stores the number of miles on the car as an integer
Then instantiate two Car objects—a blue car with 20,000 miles and a red car with 30,000 miles—and print out their colors and mileage. Your output should look like this:

The blue car has 20,000 miles.
The red car has 30,000 miles.
"""


class Car:
    def __init__(self, name, colour, mileage: int):
        self.name = name
        self.mileage = mileage
        self.colour = colour

    def car_description(self):
        return f"{self.name}, is {self.colour}, and can travel {self.mileage} miles"


car_1 = Car("ModelX","Blue", 20000)
car_2 = Car("ModelY", "Red", 30000)

print(Car.car_description(car_1))
print(Car.car_description(car_2))

# OR

class Cars:
    def __init__(self, color, mileages):
        self.color = color
        self.mileage = mileages


blue_car = Cars(color="Blue", mileages=20_000)
red_car = Cars(color="Red", mileages=30_000)

for car in (blue_car, red_car):
    print(f"The {car.color} car can cover, {car.mileage:,} miles")
    
    
 # QUESTION
"""
Create a GoldenRetriever class that inherits from the Dog class.
Give the sound argument of GoldenRetriever.speak() a default value of "Bark".
Use the following code for your parent Dog class:
"""
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age: float):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog):
    species = input("ENTER: ")

    def __init__(self, name, age, sounds="Bark"):
        super().__init__(name, age)
        self.sounds = sounds
        # Then super() is used to call the parent class attributes
        # with the same argument passed
        # Then a new attribute (sounds) is added

    def sound(self):
        return f"{self.species}, {self.name}, {self.age}, {self.sounds}"


D1 = Dog("Chi", 5)
D2 = GoldenRetriever("top", 4, "bark")

print(GoldenRetriever.sound(D2))

# OR

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age: float):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)
