# 01_input_output.py
# This program demonstrates how to take user input and display output

# input() always returns a string, so we store it in a variable
name = input("Enter your name: ")

# Convert string input into integer using int()
age = int(input("Enter your age: "))

# f-string is used for formatted output
print(f"Hello {name}, you are {age} years old.")
print(f"Next year you will be {age + 1} years old.")
