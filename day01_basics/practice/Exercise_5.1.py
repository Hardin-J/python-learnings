# Exercise 5.1 – Student Marks
# Create list of marks, add one mark, print total and average.

student_mark = []

# appends students mark
def appendMark(mark):
    return student_mark.append(mark)

def listMarks():
    for idx in range(len(student_mark)):
        print(f"{idx+1}. {student_mark[idx]}")

# returns sum of list and average
def sumAndAvg():
    sum = 0
    for mark in student_mark:
        sum += mark
    avg = sum/ len(student_mark)
    return sum, avg

while(True):
    print("---- Student Mark System ----")
    print("1. Enter 1 to Enter Mark ")
    if( len(student_mark) > 0):
        print("2. Enter 2 to List all mark(s) ")
    if( len(student_mark) > 1):
        print("3. Enter 3 to Get Sum and Average of Mark(s) ")
        
    print("---------------------------")
    
    choice = int(input("Enter you choice: "))
    if choice == 1:
        mark = int(input("Enter the Mark: "))
        appendMark(mark)
    
    elif choice == 3:
        if len(student_mark) == 0:
            print("Invalid Choice :(")
            continue
        sum, avg = sumAndAvg()
        print(f"The Sum = {sum} and The Avg = {avg}")
    
    elif choice == 2:
        if len(student_mark) == 0:
            print("Invalid Choice :(")
            continue
        listMarks()
    else:
        print("Invalid Choice :(")


    command = input("Do you want to continue(y/n): ")
    if command.lower() == 'n':
        exit()
    
    

