class Vehicle:
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


class CurrentPressure:
    def __init__(self, current_diastolic, current_systolic):
        self.current_diastolic = input("Enter a number: ")
        self.current_systolic = input("Enter a number: ")
