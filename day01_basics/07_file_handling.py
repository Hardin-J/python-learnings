# Writing to a file
with open("day01_basics/sample.txt", "w") as file:
    file.write("This is AI Learning Log\n")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()

print(content)
