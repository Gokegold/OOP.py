"""
Python OOP crash course

Twitter @i_amgoke: https://twitter.com/i_amgoke

Github: https://www.github.com/Gokegold

Date Created: April 28, 2023

last modification:: [May 8, 2023],[May 9, 2023],[May 10, 2023],[May 11, 2023],[May 14, 2023]
[May 15, 2023],[May 16, 2023],[May 17, 2023]

"""


class Vehicle:"""
Python crash course

Twitter @i_amgoke: https://twitter.com/i_amgoke

Github: https://www.github.com/Gokegold

Date Created: April 28, 2023

last modification:: [May 8, 2023],[May 9, 2023],[May 10, 2023],[May 11, 2023]

"""

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())



"""
        write the controller class for the following Blood Pressure Calculator,...
        ...if you know the normal pressure is 120/80 
        should any number go higher meaning pressure increased
        and vice versa
"""
'''

normal_systolic = 120
normal_diastolic = 80
normal_pressure = f'{normal_systolic}/{normal_diastolic}'


current_systolic = int(input("Current Systolic:"))
current_diastolic = int(input("Current Diastolic:"))

weight_pressure = f'{current_systolic}/{current_diastolic}'

if current_diastolic and current_systolic == normal_pressure:
    print("Pressure Regulated")
elif current_diastolic and current_systolic >= normal_pressure:
    print("Smiles")
    
    normal pressure = (180 and 80)
    normal p = (self.normal_diastolic, self.normal_systolic)
'''


class NormalPressure:

    def __init__(self, normal_diastolic=80, normal_systolic=120):
        self.normal_diastolic = normal_diastolic
        self.normal_systolic = normal_systolic

    def normal(self):
        return f'Blood Pressure is {self}'
    
    
    
    #  BLOOD PRESSURE MOST RECENT
    
    class NormalPressure:
    def __init__(self, f_nom, l_nom):
        self.f_nom = f_nom
        self.l_nom = l_nom

    def n_diastolic(self, normal_diastolic):
        return f"Diastolic Pressure is {self.f_nom, self.l_nom} is {normal_diastolic}"

    def n_systolic(self, normal_systolic):
        return f"Diastolic Pressure is {self.f_nom, self.l_nom} is {normal_systolic}"


class CurrentPressure(NormalPressure):
    def recent_systolic(self, normal_systolic=120):
        return super().n_systolic(normal_systolic)

    def recent_diastolic(self, normal_diastolic=80):
        return super().n_diastolic(normal_diastolic)


class CurrentPressure:
    def __init__(self, current_diastolic, current_systolic):
        self.current_diastolic = input("Enter a number: ")
        self.current_systolic = input("Enter a number: ")
        
        

class BloodPressure:
    nom_systolic = 120
    nom_diastolic = 70
    def __init__(self, user_systolic, user_diastolic):
        user_systolic = input(int("Systolic Pressure: "))
        user_diastolic = input(int("Diastolic Pressure"))
    
    def healthy(self):
        if user_systolic == nom_systolic and user_diatolic == nom_diatolic
        return f"User blood pressure is healthy"
    def unhealthy(self):
        if user_systolic <= nom_systolic or user_diatolic >= nom_diatolic
        return f"User blood pressure is unhealthy"

User = BloodPressure(
    
class BloodPressure:
    def __init__(self, norm_systolic=120, norm_diastolic=70):
        self.norm_systolic = norm_systolic
        self.norm_diastolic = norm_diastolic

    def noms(self):
        print("Healthy blood pressure")
        return f"{self.norm_systolic}/{self.norm_diastolic}"

class User:
    def user(_systolic, _diastolic):
        _systolic = None
        _diastolic = None

        if _systolic is None:
            _systolic._get_input()
        else:
            if isinstance(_systolic, str):
                _systolic = int(_systolic)

                return f"{_systolic}"
        
        if _diastolic is None:
            _diastolic._get_input()
        else:
            if isinstance(_diastolic, str):
                _diastolic = int(_diastolic)

                return f"{_diastolic}"

User.user(180, 90)
