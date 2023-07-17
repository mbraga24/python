"""
Working with loops
"""

# Looping through Arrays and Sets
print("===================================")
print("Looping through Arrays and Sets")
print("===================================")
names = ["Michael", "Jeff", "Catherine", "Sarah"]

for name in names:
    print(name)

# Looping through Dictionaries
print("===================================")
print("Looping through Dictionaries")
print("===================================")

person = {
    "name": "Marlon",
    "age": 23,
    "address": "Somewhere over the rainbow 222"
}

for key in person:
    print(f"key: {key} -- value: {person[key]}")

print()

for key, value in person.items():
    print(f"key: {key} -- value: {value}")

print()

print(person.items())

print("===================================")
print("Loop to Exercise")
print("===================================")

numbers = [1, 3, 5, 9, 10, 20]

total = 0
for num in numbers:
    total += num

print(f"Total: {total}")

print("===================================")
print("While Loop")
print("===================================")

number = 0

while number < 10:
    print(f"Number: {number}")
    number += 1
else:
    number = 0
    print(f"number reset: {number} End of While Loop -- Normal")

print("===================================")
print("Break and Continue keyword")
print("===================================")

while number < 10:
    if number == 5:
        break
    print(f"Number: {number}")
    number += 1

number = 0
print(f"number reset {number} -- End of While Loop | Break")

while number < 10:
    number += 1
    if number < 5:
        print("Continue")
        continue
    print(f"Number: {number}")
else:
    number = 0
    print(f"number reset {number} -- End of While Loop | Continue")
