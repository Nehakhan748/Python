# 01 ->  "School Member System"
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Name is {self.name} and i'm {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def introduce(self):
        print(f"Name \tAge\tGrade\n{self.name}\t{self.age}\t{self.grade}\n")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print(f"Name\tAge\tSubject\n{self.name}\t{self.age}\t{self.subject}\n")

class Staff(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

    def introduce(self):
        print(f"Name\tAge\tRole\n{self.name}\t{self.age}\t{self.role}\n")

information = [
    Student("Neha", 19, "A"),
    Teacher("Saima", 35, "Python"),
    Staff("Rasheed", 44, "Clark"),
    Student("Maryam", 19, "A"),
    Teacher("Saima", 35, "Python"),
    Staff("Arshad", 44, "Headmaster")
]
print("===School Member System===\n")
for info in information:
    info.introduce()


# 02 -> "Zoo Management System"
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Animal Sound!"

    def show_info(self):
        return f"Name: {self.name}, Species: {self.species}"

class Bird(Animal):
    def __init__(self, name, species, wing_span):
        super().__init__(name, species)
        self.wing_span = wing_span

    def make_sound(self):
        return "Chirp Chirp!"
    def show_info(self):
        return f"{super().show_info()}, Wing Span: {self.wing_span} meters"

class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color

    def make_sound(self):
        return "Roar!"
    def show_info(self):
        return f"{super().show_info()}, Color: {self.fur_color}"
    
class Reptile(Animal):
    def __init__(self, name, species, is_venomous):
        super().__init__(name, species)
        self.is_venomous = is_venomous

    def make_sound(self):
        return "Hiss!"
    def show_info(self):
        venom_status = "Venomous" if self.is_venomous else "Non-venomous"
        return f"{super().show_info()}, {venom_status}"
    
zoo_animals = [
    Bird("Parrot", "Bird", 0.5),
    Bird("Eagle", "Bird", 2.1),
    Mammal("Lion", "Mammal", "Golden"),
    Mammal("Panda", "Mammal", "Black & White"),
    Reptile("Cobra", "Reptile", True),
    Reptile("Turtle", "Reptile", False)
]
print("===Zoo Management System===\n")
for animal in zoo_animals:
    print(animal.show_info())
    print(f"Sound: {animal.make_sound()}\n")


# 03 -> "Transport Booking System"
class Transport:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def book_ticket(self):
        print(f"Booking ticket for transport: {self.name} with capacity {self.capacity}")

class Bus(Transport):
    def __init__(self, name, capacity, route_number):
        super().__init__(name, capacity)
        self.route_number = route_number

    def book_ticket(self):
        print(f"Bus '{self.name}' on Route {self.route_number} booked successfully. Capacity: {self.capacity}")

class Train(Transport):
    def __init__(self, name, capacity, coach_type):
        super().__init__(name, capacity)
        self.coach_type = coach_type

    def book_ticket(self):
        print(f"Train '{self.name}' ({self.coach_type} coach) ticket booked. Capacity: {self.capacity}")

class Flight(Transport):
    def __init__(self, name, capacity, airline):
        super().__init__(name, capacity)
        self.airline = airline
    
    def book_ticket(self):
        print(f"Flight '{self.name}' by {self.airline} booked successfully. Capacity: {self.capacity}")
    
transport_list = [
    Bus("City Express", 50, 101),
    Bus("Metro Shuttle", 40, 202),
    Train("Green Valley Express", 200, "Sleeper"),
    Train("Mountain Rider", 150, "AC Chair Car"),
    Flight("PK-305", 180, "PIA"),
    Flight("EK-615", 300, "Emirates")
]
print("=== Transport Booking System ===\n")
for transport in transport_list:
    transport.book_ticket()
