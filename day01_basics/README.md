# 📚 Day 1 - Python Basics

Welcome to Day 1 of Python Programming! This folder contains comprehensive exercises and lessons covering fundamental Python concepts essential for beginners and AI/ML development.

## 📋 Folder Structure

```
day01_basics/
├── 01_input_output.py          # Input/Output fundamentals
├── 02_datatypes.py             # Python data types
├── 03_conditions.py            # Conditional statements (if/else)
├── 04_loops.py                 # Looping structures (for/while)
├── 05_collections.py           # Lists, tuples, dictionaries
├── 06_functions.py             # Function definitions and usage
├── 07_file_handling.py         # Reading and writing files
├── 08_error_handling.py        # Exception handling (try/except)
├── 09_mini_calculator.py       # Mini calculator project
├── 10_logger.py                # Logging system
├── practice/                   # Practice exercises
│   ├── Exercise_1.1.py to 1.2.py    # Input/Output exercises
│   ├── Exercise_2.1.py to 2.2.py    # Data Types exercises
│   ├── Exercise_3.1.py to 3.2.py    # Conditions exercises
│   ├── Exercise_4.1.py to 4.2.py    # Loops exercises
│   ├── Exercise_5.1.py to 5.2.py    # Collections exercises
│   ├── Exercise_6.1.py to 6.2.py    # Functions exercises
│   ├── Exercise_7.1.py to 7.2.py    # File Handling exercises
│   ├── Exercise_8.1.py to 8.2.py    # Error Handling exercises
│   └── data files (.txt files)
├── README.md                   # Quick overview
└── day1_python_exercises.txt   # Detailed exercise descriptions
```

## 🎯 Topics Covered

### 1. **Input/Output** (`01_input_output.py`)
Learn how to receive user input and display formatted output using Python.

**Key Concepts:**
- `input()` function for receiving user data
- `print()` function for displaying output
- String formatting with f-strings
- Type conversion basics

**Practice Exercises:**
- **Exercise 1.1**: User Profile Card - Create formatted profile output
- **Exercise 1.2**: Voice Project Setup Info - Display project information

---

### 2. **Data Types** (`02_datatypes.py`)
Understand Python's fundamental data types and type conversion.

**Key Concepts:**
- Integers, floats, strings, booleans
- `type()` function to check data types
- Type conversion: `int()`, `float()`, `str()`
- Dynamic typing in Python

**Practice Exercises:**
- **Exercise 2.1**: Type Inspector - Explore different data types
- **Exercise 2.2**: Type Conversion Test - Convert between types

---

### 3. **Conditions** (`03_conditions.py`)
Control program flow using conditional statements.

**Key Concepts:**
- `if`, `elif`, `else` statements
- Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Logical operators (`and`, `or`, `not`)
- Nested conditions

**Practice Exercises:**
- **Exercise 3.1**: AI Dataset Eligibility - Validate dataset size
- **Exercise 3.2**: Login System - Simple authentication

---

### 4. **Loops** (`04_loops.py`)
Automate repetitive tasks using loops.

**Key Concepts:**
- `for` loops for iteration
- `while` loops for condition-based repetition
- Loop control: `break`, `continue`
- `range()` function
- Nested loops

**Practice Exercises:**
- **Exercise 4.1**: Sum of N Numbers - Calculate sum using loops
- **Exercise 4.2**: Dataset Iterator - Iterate through lists

---

### 5. **Collections** (`05_collections.py`)
Work with Python's collection data structures.

**Key Concepts:**
- **Lists**: Ordered, mutable sequences
  - Methods: `append()`, `remove()`, `pop()`, `sort()`
- **Tuples**: Ordered, immutable sequences
- **Dictionaries**: Key-value pairs
  - Methods: `keys()`, `values()`, `items()`
- List comprehensions
- Indexing and slicing

**Practice Exercises:**
- **Exercise 5.1**: Student Marks - Work with lists (sum, average)
- **Exercise 5.2**: Voice Metadata Dictionary - Dictionary operations

---

### 6. **Functions** (`06_functions.py`)
Create reusable code blocks with functions.

**Key Concepts:**
- Function definition with `def`
- Parameters and arguments
- Return values
- Default parameters
- Docstrings
- Scope and local variables

**Practice Exercises:**
- **Exercise 6.1**: Area Calculator - Function for geometric calculations
- **Exercise 6.2**: AI Accuracy Checker - Validation functions

---

### 7. **File Handling** (`07_file_handling.py`)
Read from and write to files.

**Key Concepts:**
- Opening files with `open()`
- Reading: `read()`, `readline()`, `readlines()`
- Writing: `write()`, `writelines()`
- File modes: `'r'`, `'w'`, `'a'`, `'r+'`
- Context managers: `with` statement
- File closing and cleanup

**Practice Exercises:**
- **Exercise 7.1**: Notes Saver - Save and read notes from file
- **Exercise 7.2**: Dataset List Writer - Write data to file

---

### 8. **Error Handling** (`08_error_handling.py`)
Handle exceptions gracefully.

**Key Concepts:**
- `try`, `except`, `else`, `finally` blocks
- Common exceptions: `ValueError`, `FileNotFoundError`, `ZeroDivisionError`
- Raising exceptions
- Custom error messages

**Practice Exercises:**
- **Exercise 8.1**: Safe Division - Handle division by zero
- **Exercise 8.2**: Safe File Reader - Handle missing files

---

### 9. **Mini Calculator** (`09_mini_calculator.py`)
**Project**: Build a functional calculator combining multiple concepts.

**Features:**
- Menu-based interface
- Support for basic operations: +, -, *, /
- Error handling for invalid inputs
- Can use functions for each operation

---

### 10. **Logger System** (`10_logger.py`)
**Project**: Create a logging system for tracking activities.

**Features:**
- Log user actions with timestamps
- Write logs to files
- Read and display logged activities
- Useful for tracking login attempts and commands

---

## 🚀 How to Use This Folder

### **For Learning:**
1. Start with the concept files (`01_input_output.py` through `10_logger.py`)
2. Read and run each file to understand the concept
3. Modify the code and experiment with changes

### **For Practice:**
1. Navigate to the `practice/` folder
2. Attempt each exercise before checking the solution
3. Start with Exercise 1.1 and progress sequentially
4. Use `day1_python_exercises.txt` as a reference

### **Running the Programs:**
```bash
# Run a specific file
python 01_input_output.py

# Run practice exercises
python practice/Exercise_1.1.py
```

---

## 💡 Learning Goals

By completing this day's exercises, you will understand:
- ✅ How to interact with users through input/output
- ✅ Python's data types and type system
- ✅ Control flow using conditions and loops
- ✅ Working with data collections (lists, dicts)
- ✅ Writing reusable code with functions
- ✅ File I/O operations
- ✅ Error handling and exception management
- ✅ Building simple projects combining multiple concepts

---

## 📝 Reference Resources

- **Official Python Docs**: https://docs.python.org/3/
- **Built-in Functions**: https://docs.python.org/3/library/functions.html
- **Collections**: https://docs.python.org/3/tutorial/datastructures.html

---

## 🎓 Next Steps

After mastering Day 1 concepts:
- Move to **Day 2**: Control Flow & Advanced Techniques
- Practice writing your own programs combining these concepts
- Try building small projects like TO-DO lists, expense trackers, etc.

---

## 📌 Tips for Success

1. **Type Along**: Don't just read code; type it yourself
2. **Experiment**: Modify the code and see what breaks
3. **Debug**: Use `print()` statements to understand program flow
4. **Document**: Add comments to explain your code
5. **Practice Consistently**: Do at least 2-3 exercises daily

---

Happy Coding! 🐍✨
