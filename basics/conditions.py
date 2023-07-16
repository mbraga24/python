"""
Working with conditions
"""
print("=========================")
print("If Statements")
print("=========================")

number = 5

if number > 0:
    print(f"{number} is greater than 0")
elif number < 0:
    print(f"{number} is less than 0")
else:
    print(f"{number}")

if number == 5:
    print(f"yayy, it's {number}!")

print(f"Print after condition")


# Ternary Operator
print("=========================")
print("Ternary Operator")
print("=========================")

print(f"It is {number}, indeed!" if number == 5 else "Nope!")