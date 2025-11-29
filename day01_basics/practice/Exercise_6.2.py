# Exercise 6.2 – AI Accuracy Checker
# Create function is_accurate(score).

# sample output
# If score ≥ 0.8 → return "Good Model"
# Else → "Needs Improvement"

def check_accuracy(score):
    if score >= 0.8:
        return "Good Model"
    else:
        return "Need Improvement"
    
score = float(input("Enter your model score (1 to 100) :"))
score/=100
print(check_accuracy(score))