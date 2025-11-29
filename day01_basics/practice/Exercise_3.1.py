# Exercise 3.1 – AI Dataset Eligibility
# Ask for dataset size. If ≥ 1000 → Sufficient for training else Insufficient data.


num = int(input("Enter size of the dataset: "))     # type cast for type safety while checking the condition

if (num >= 1000):
    print("Sufficient for training :)")
else:
    print("Insufficient data for training :(")