"""
Working with Dictionaries

- Key / Value pair data structure
- Duplicates are not allowed
- Will have the same common methods introduced in Lists and more
"""

person = {
    "name": "Marlon",
    "age": 22,
    "address": "Somewhere Over the Rainbow 222"
}

print(person["name"])
print(person["age"])
print(person["address"])
print(f"person.keys(): {person.keys()}")
print(f"person.values(): {person.values()}")
person["age"] = 25
print(person)