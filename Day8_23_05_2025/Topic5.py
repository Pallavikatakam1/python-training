# Class +  object + inheritance

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display(self):
        print(f"Make: {self.make}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def display(self):
        super().display()
        print(f"Number of doors: {self.num_doors}")

print("Enter details for a general vehicle:")
v_make = input("Enter make: ")
v_model = input("Enter model: ")
v = Vehicle(v_make, v_model)

print("\nEnter details for a car:")
c_make = input("Enter make: ")
c_model = input("Enter model: ")
c_num_doors = int(input("Enter number of doors: "))
c = Car(c_make, c_model, c_num_doors)

print("\nVehicle details:")
v.display()

print("\nCar details:")
c.display()