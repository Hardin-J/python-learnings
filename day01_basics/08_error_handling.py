# try-except prevents program crash

try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ValueError:
    print("Invalid input. Enter only numbers.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
