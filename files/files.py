import os.path

# NOTE
# "w" creates the file while "r+" allows to open the file to read and
# write to the file, but it won't create the file.

# w - writing
# a appending
# r reading
# r+ reading and writing

write_to_file = open("./data.csv", "w")

# WRITE TO THE FILE
write_to_file.write("id, name, age, email\n")
write_to_file.write("1, John, 23, john@email.com\n")
write_to_file.write("2, Sara, 25, sara@email.com\n")
write_to_file.write("3, Bianca, 28, bianca@email.com\n")
write_to_file.close()

# APPEND TO THE FILE
append_to_file = open("./data.csv", "a")
append_to_file.write("4, samuel, 24, samuel@email.com")
append_to_file.close()

# READ FROM FILE
read_from_file = open("./data.csv", "r")

# reads all content
# print(read_from_file.read())
# print()

# prints out each content of the document
# for line in read_from_file:
#     print(line)
# print()

# creates a list and saves each line in the list
# print(read_from_file.readlines())

read_from_file.close()

# ==============================
# Proper way to work with files
# ==============================

# use the os.path import to check if a file exists
# import os.path

# checks if file exists
proper_file_name = "./data.csv"
wrong_file_name = "./ddaattaa.csv"

if os.path.isfile(proper_file_name):
    # this approach opens and closes the file automatically
    with open(proper_file_name, "r") as file:
        print(file.read())
else:
    print(f"File {proper_file_name} does not exist")

print("=============================================")

if os.path.isfile(wrong_file_name):
    # this approach opens and closes the file automatically
    with open(wrong_file_name, "r") as file:
        print(file.read())
else:
    print(f"File {wrong_file_name} does not exist")
