"""
Working with functions
"""


def greet(name, age=-1):
    print(f"Hello {name}, how are you?")
    if not age < 0:
        print(f"You said you were {age}, is that right?")


greet("Marlon", 23)
greet("Dave")

print()


# Return Statements

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False


def convert_gender(gender="unknown"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == "F":
        return "Female"
    else:
        return "Other"


print(f"Is this person an adult? {is_adult(18)}")
print(convert_gender("M"))
print(convert_gender("F"))
print(convert_gender("None"))
