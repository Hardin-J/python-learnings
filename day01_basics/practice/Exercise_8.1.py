# Exercise 8.1 – Safe Division
# Ask two numbers and handle errors.

try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print( num1/ num2)
except ZeroDivisionError:
    print(" Zero is not divisible by any number")