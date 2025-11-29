# Logs user activity to a file with timestamp

from datetime import datetime

log_file = "activity_log.txt"

name = input("Enter your name: ")
activity = input("Enter your activity: ")

# Open file in append mode so old data is preserved
with open(log_file, "a") as file:
    file.write(f"{datetime.now()} | {name} | {activity}\n")

print("Log saved successfully.")
