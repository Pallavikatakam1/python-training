import greetings
import importlib

print("Initial greeting:")
greetings.greet()

input("\nNow modify 'greetings' to change the greet() message, then press Enter...")

print("\nReloading module...")
importlib.reload(greetings)

print("Greeting after reload:")
greetings.greet()
