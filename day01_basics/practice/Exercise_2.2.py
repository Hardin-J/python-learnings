# Exercise 2.2 – Type Conversion Test
# Ask a number as string, convert it into int and float, print both and their types.

num = str(input("Enter a number: "))

# type conversion
_int = int(num)
_float = float(num)

print(f"{type(num)} - {num}")
print(f"{type(_int)} - {_int}")
print(f"{type(_float)} - {_float}")