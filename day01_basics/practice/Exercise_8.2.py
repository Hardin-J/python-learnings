# Exercise 8.2 – Safe File Reader
# Try to open missing file and handle safely.

try:
    file_name = input("Enter the file name to read: ")
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("file not found")


