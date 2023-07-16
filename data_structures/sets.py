"""
Working with Sets

- Duplicates are not allowed
- Order is not guaranteed
- Will have the same common methods introduced in Lists
"""
print("===================")
print("Intro to Sets")
print("===================")

numbersSet = {1, 2, 2}
lettersSet = {"A", "B", "C", "D", "D"}

print(f"numbersSet: {numbersSet}")
print(f"numbersSet: {numbersSet} -- no duplicates")
print(f"lettersSet: {lettersSet} -- notice that order can change")

print("=========================================")
print("Set - Union |, Intersection, & and Difference -")
print("=========================================")

lettersA = {"A", "B", "C", "D"}
lettersB = {"E", "F"}
lettersC = {"A", "B", "G", "H"}

union = lettersA | lettersB
intersection = lettersA & lettersC
differenceForA = lettersA - lettersC
differenceForC = lettersC - lettersA

print(f"lettersA: {lettersA}")
print(f"lettersB: {lettersB}")
print(f"lettersC: {lettersC}")
print()
print(f"Union: {union}")
print(f"Intersection: {intersection}")
print(f"Difference For A: {differenceForA}")
print(f"Difference For C: {differenceForC}")
