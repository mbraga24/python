"""
Working with Strings
"""
# =============================
# The basics of String
# =============================
brand = "Louis Vuitton"
print(brand.upper())
print(brand.replace("s", "X"))
print(len(brand))
print(brand == "Louis Vuitton")
print(brand == "Louix Vuitton")

# booleans
print("Lou" in brand)
print("Louix" not in brand)

# =============================
# Multiline and Formatting Strings
# =============================

comment_on_different_lines = "Just some simple text " \
                             "to test how long Strings " \
                             "work in Python. See other " \
                             "examples below."

print(comment_on_different_lines)

comment_on_different_lines_python = """
Just some simple text
to test how long Strings 
work in Python. See other
examples below.
"""

print(comment_on_different_lines_python)

# Passing variables

name = "Marlon"

question_one_str_var = """
How are you today, {}?
"""

print(question_one_str_var.format(name))

name1 = "Claire"
name2 = "Michael"
name3 = "Ashley"

question_two_or_more_str_var = """
These are my friends {}, {}, and {}. And my name is {}.
"""

print(question_two_or_more_str_var.format(name1, name2, name3, name))

sister = "Nathalie"
niece = "Lyla"

question_cleaner_format = f"""
My sister's name is {sister}. And My niece's name is {niece}.
"""

print(question_cleaner_format)
