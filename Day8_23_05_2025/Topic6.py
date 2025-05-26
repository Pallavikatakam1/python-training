# polymorphism + functions

class Dog:
    def sound(self):
        return "Woof"

class Cat:
    def sound(self):
        return "Meow"

def make_sound(animal):
    print(animal.sound())

# Take input from user
choice = input("Enter an animal (dog/cat): ").strip().lower()

if choice == "dog":
    make_sound(Dog())
elif choice == "cat":
    make_sound(Cat())
else:
    print("Unknown animal.")

