
# =============================
# Variables & Naming variables
#
# Python is dynamically typed language. The datatype of any variable
# or function is checked at runtime.
# =============================

# One line
firstName, age = "Marlon", 20

lastName = "Braga"
pi = 3.14

# Lists
number = [1, 2, 3, 5]

# Naming convention
full_name = "Steve K"
# constant names
CAPACITY = 100

print("Hello Marlon")
print(firstName)
print(lastName)
print(number)

# =============================
# Data Types
# =============================

city = "New York"
count = 1
halfCount = 0.5
guests = []
isTrue = False

print(type(city))
print(type(count))
print(type(halfCount))
print(type(guests))
print(type(isTrue))

"""
RETURN value from above print
 <class 'str'>
 <class 'int'>
 <class 'float'>
 <class 'list'>
 <class 'bool'>
"""

# =============================
# Explicitly Declaration
# =============================

# Variables
firstN: str = "Tom"
isTall: bool = True
tomAge: int = 22

# Functions
def helloTom() -> str:
    return "Hello, Tom!"

# The convention is to declare implicit variables and functions
def hisAge():
    return tomAge