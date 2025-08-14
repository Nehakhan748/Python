#------------Employee Payroll System------------#
class Employee:
    def __init__(self, name, base_salary):
        self.name = name 
        self.base_salary = base_salary

    def calculate_salary(self):
        print(f"Name: {self.name}   Base Salary: {self.base_salary}")

class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
       print(f"Name: {self.name}   Salary: {self.base_salary + self.bonus}")
    
class Developer(Employee):
    def __init__(self, name, base_salary, overtime_hours, hourly_rate):
        super().__init__(name, base_salary)
        self.overtime_hours = overtime_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        overtime_pay = self.overtime_hours * self.hourly_rate
        print(f"Name: {self.name}   Salary: {self.base_salary + overtime_pay}")

class Intern(Employee):
    def __init__(self, name, stipend):
        super().__init__(name, base_salary = 0)
        self.stipend = stipend

    def calculate_salary(self):
       print(f"Name: {self.name}   Salary: {self.stipend}")
    
members = [
    Manager("Ali", 67894, 3000),
    Developer("Sara", 69934, 3, 2000),
    Intern("Asad", 20000),
    Manager("Irtaza", 47000, 2200),
    Developer("Saneha", 100000, 5, 2000),
    Intern("Ayyat", 20000)
]

for m in members:
    m.calculate_salary()

#--------------Vehicle Management System:--------------#
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}  Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
    
    def display_info(self):
        print(f"Brand: {self.brand}  Model: {self.model}  FuelType: {self.fuel_type}")

class Bike(Vehicle):
    def __init__(self, brand, model, engine_capacity):
        super().__init__(brand, model)
        self.engine_capacity = engine_capacity

    def display_info(self):
        print(f"Brand: {self.brand}  Model: {self.model}  EngineCapacity: {self.engine_capacity}")

class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity

    def display_info(self):
        print(f"Brand: {self.brand}  Model: {self.model} LoadCapacity: {self.load_capacity}")
        
items =[
    Car("Toyota", "Corolla","Petrol"),
    Bike("Honda", "CB125F", "124 cc"),
    Truck("Volvo" ,"FH16", "44 tons"),
    Car("Tesla", "Model 3", "Electric"),
    Bike("Yamaha", "YZF-R3", "321 cc"),
    Truck("Scania" ,"R500", "40 tons")
]
for i in items:
    i.display_info()