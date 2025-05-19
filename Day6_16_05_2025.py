# Inheritance
# 1. Employee Hierarchy
class Employee:
    def calculate_bonus(self):
        return 0

class Manager(Employee):
    def calculate_bonus(self):
        return 2000

class Developer(Employee):
    def calculate_bonus(self):
        return 1500

class Intern(Employee):
    def calculate_bonus(self):
        return 500

employees = [Manager(), Developer(), Intern()]
for emp in employees:
    print(emp.__class__.__name__, "Bonus:", emp.calculate_bonus())



# 2. Vehicle Fleet

print("\n")
class Vehicle:
    def get_max_speed(self):
        return 0

    def print_info(self):
        print(self.__class__.__name__,"speed:", self.get_max_speed(), "km/h")

class Car(Vehicle):
    def get_max_speed(self):
        return 180

class Truck(Vehicle):
    def get_max_speed(self):
        return 120

class Motorcycle(Vehicle):
    def get_max_speed(self):
        return 150

fleet = [Car(), Truck(), Motorcycle()]
for v in fleet:
    v.print_info()



# 3. Shape area calculator

print("\n")
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 7)]
for shape in shapes:
    print("{} area: {:.2f}".format(shape.__class__.__name__, shape.area()))



# 4. Notification system

print("\n")
class Notification:
    def send_notification(self):
        pass

class EmailNotification(Notification):
    def send_notification(self):
        print("Sending Email Notification")

class SMSNotification(Notification):
    def send_notification(self):
        print("Sending SMS Notification")

class PushNotification(Notification):
    def send_notification(self):
        print("Sending Push Notification")

def notify_all(notifications):
    for notif in notifications:
        notif.send_notification()

notifications = [EmailNotification(), SMSNotification(), PushNotification()]
notify_all(notifications)



# 5.Payment Gateway

print("\n")
class PaymentMethod:
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal")

class CryptoCurrency(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using CryptoCurrency")

def checkout(payment_method, amount):
    payment_method.pay(amount)

checkout(CreditCard(), 100)
checkout(PayPal(), 200)
checkout(CryptoCurrency(), 300)


# 6. Zoo animal sounds

print("\n")
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.make_sound()



# 7. Custom range Generator

print("\n")

class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

for num in MyRange(1, 5):
    print(num)



# 8. Fibonacci Sequence iterator

print("\n")
class Fibonacci:
    def __init__(self, limit):
        self.a, self.b = 0, 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        return val

for num in Fibonacci(50):
    print(num)



# 9. reverse string iterator

print("\n")
class ReverseString:
    def __init__(self, text):
        self.text = text
        self.index = len(text)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.text[self.index]

for ch in ReverseString("hello"):
    print(ch)


# 10. File  line grouper

print("\n")
class FileLineGrouper:
    def __init__(self, filename, group_size):
        self.file = open(filename)
        self.group_size = group_size

    def __iter__(self):
        return self

    def __next__(self):
        lines = []
        for _ in range(self.group_size):
            line = self.file.readline()
            if not line:
                break
            lines.append(line.strip())
        if not lines:
            self.file.close()
            raise StopIteration
        return lines

