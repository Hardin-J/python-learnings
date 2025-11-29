# Exercise 4.1 – Sum of N Numbers
# Ask for N. Use a loop to calculate sum of 1 to N.

n = int(input("Enter the N to calculate sum of 1 to N= "))
sum = 0
for i in range(1,n+1):
    sum+= i
    print(f"{i}. Sum is {sum}")
 