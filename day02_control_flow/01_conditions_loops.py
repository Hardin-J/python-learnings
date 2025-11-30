"""
Day 2 - Conditions and Loops Practice

Goal:
- Understand if/elif/else
- Use for and while loops
- Use break and continue
"""

# ----- IF / ELIF / ELSE EXAMPLE -----

score = int(input("Enter your model accuracy (0-100): "))

# Basic conditional branching based on score value
if score >= 90:
    print("Excellent model ✅")
elif score >= 75:
    print("Good model 👍")
elif score >= 50:
    print("Average model ⚠️")
else:
    print("Poor model ❌")


# ----- FOR LOOP EXAMPLE -----

# A list of dummy audio file names (in real life, we will read these from a folder)
audio_files = ["audio_01.wav", "audio_02.wav", "noise_01.wav"]

print("\nIterating through audio files:")
for file_name in audio_files:
    # Each iteration, file_name holds one element from audio_files
    print("Processing:", file_name)


# ----- WHILE LOOP + BREAK / CONTINUE -----

print("\nSimple menu (type 0 to exit):")

while True:  # Infinite loop, we will break manually
    print("\n1. Train model")
    print("2. Evaluate model")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == "0":
        print("Exiting menu...")
        break  # Exit the loop

    # Skip empty input
    if choice.strip() == "":
        print("Empty input, please enter something.")
        continue  # Go back to the start of the loop

    if choice == "1":
        print("Training model... (dummy action)")
    elif choice == "2":
        print("Evaluating model... (dummy action)")
    else:
        print("Invalid option. Try again.")
