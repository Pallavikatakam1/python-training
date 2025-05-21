from helper import *

print("Calling public()...")
public()

print("Trying to call _helper() (should raise NameError)...")
try:
    _helper()
except NameError:
    print("_helper is not accessible with 'from helpers import *'")
