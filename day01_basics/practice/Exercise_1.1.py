# Exercise 1.1 – User Profile Card
# Create a program that asks name, country, profession and prints a formatted profile card.

# Sample - Output:
# ---- PROFILE ----
# Name: ___
# Country: ___
# Profession: ___

name = input("Enter your name")
country = input("Enter your country")
profession = input("Enter your profession")

print("---- Profile ----")
print(f"Name: {name}")
print(f"Country: {country}")
print(f"Profession: {profession}")