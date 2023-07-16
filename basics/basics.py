# =============================
# Variables & Naming variables
#
# Python is dynamically typed language. The datatype of any variable
# or function is checked at runtime.
# =============================

# One line
first_name, age = "Marlon", 20

last_name = "Braga"
pi = 3.14

# Lists
number = [1, 2, 3, 5]

# Naming convention
full_name = "Steve K"
# constant names
CAPACITY = 100

print("Hello Marlon")
print(first_name)
print(last_name)
print(number)

# =============================
# Data Types
# =============================

city = "New York"
count = 1
half_count = 0.5
guests = []
is_true = False

print(type(city))
print(type(count))
print(type(half_count))
print(type(guests))
print(type(is_true))

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
first_n: str = "Tom"
is_tall: bool = True
tom_age: int = 22


# Functions
def hello_tom() -> str:
    return "Hello, Tom!"


# The convention is to declare implicit variables and functions
def his_age():
    return tom_age
