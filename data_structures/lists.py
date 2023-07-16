"""
Working with Lists

- Duplicates are allowed
- Order is guaranteed
"""
print("===================")
print("Intro to Lists")
print("===================")
numbers = [1, 2, 3, 4, 5, 8, -1]
numbersToBeCleared = [1, 2, 3, 4, 5, 8, -1]

print(numbers)
# print(numbers[0])
# print(numbers[6])

# Common List methods
print("===================")
print("Common List Methods")
print("===================")

# Sort numbers
print("--- Sort numbers")
numbers.sort()
print(numbers)

# Reverse numbers
print("--- Reverse numbers")
numbers.reverse()
print(numbers)

# Append numbers
print("--- Append numbers")
numbers.append(55)
print(numbers)

# Get length
print("--- Get length")
print(len(numbers))

# Clear list
print("--- Clear list")
print(f"Before clear(): {numbersToBeCleared}")
print(numbersToBeCleared.clear())
print(f"After clear(): {numbersToBeCleared}")

# Find if a number is in the list
print("--- Find if a number is in the list")
print(f"5 in numbers: {5 in numbers}")
print(f"300 in numbers: {300 in numbers}")

print("")

# Remove an element from the List (Choose the actual element to be removed) -- APPROACH 1
print("--- Remove an element from the List (Choose the actual element to be removed) -- APPROACH 1")
print(f"Before removal {numbers}")
numbers.remove(8)
print(f"After removal {numbers}")

# Remove an element from the List -- APPROACH 2
print("--- Remove an element from the List -- APPROACH 2")
print(f"Before removal {numbers}")
del numbers[1]
print(f"Before removal {numbers} -- 4 was removed from index 1")

# Remove elements within a range (From index 0 to 3 | Exclusive)-- APPROACH 3
print("--- Remove elements within a range (From index 0 to 3 | Exclusive)-- APPROACH 3")
print(f"Before removal {numbers}")
del numbers[0:3]
print(f"After removal {numbers} -- values 5, 3, and 2 were removed from index 0 to 2")

# Remove the last element of the List (from the top of the "Stack")
print("--- Remove the last element of the List (from the top of the 'Stack')")
print(f"Before removal {numbers}")
numbers.pop()
print(f"After removal {numbers} -- 55 was removed")
