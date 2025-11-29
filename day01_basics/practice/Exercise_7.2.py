# Exercise 7.2 – Dataset List Writer
# Create list of 5 filenames and write into dataset.txt.

file = "day01_basics/practice/list_of_names.txt"
names = ["Jon", "Snow", "Denearys"]

# writing the file
with open(file, 'a') as _file:
    for name in names:
        _file.write(name + "\n")
    print("List of names saved Successfully!")

# reading the file
with open(file,'r') as _file:
    content = _file.read()
    print(content)
