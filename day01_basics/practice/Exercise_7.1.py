# Exercise 7.1 – Notes Saver
# Ask user for a note, save to notes.txt, read and display.

file = "day01_basics/practice/note.txt"

# writing the file
with open(file, 'a') as _file:
    note = input("Enter a notes: ")
    _file.write(note + "\n")
    print("Note saved Successfully!")

# reading the file
with open(file,'r') as _file:
    content = _file.read()
    print(content)
