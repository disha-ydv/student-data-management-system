# Student Data Management System

A Python-based **Student Data Management System** developed as a beginner-friendly programming project.

The system allows users to add, view, search, update, and delete student records. It also provides features for calculating marks statistics, checking pass/fail results, searching by course, and sorting students according to their marks.

## Features

* Add new student records
* Display all student records
* Search for a student using roll number
* Update student information
* Delete student records
* Calculate average marks
* Find highest and lowest marks
* Display pass/fail results
* Search students by course
* Sort students by marks
* Display student statistics
* Demonstrate the use of tuples
* Use NumPy arrays for marks calculations

## Technologies Used

* Python
* NumPy
* GitHub

## Python Concepts Used

This project demonstrates the following concepts:

* Functions
* Lists
* Tuples
* Dictionaries
* `for` loops
* `while` loops
* `if`, `elif`, and `else` statements
* Conditional statements
* Arrays
* NumPy
* Basic data manipulation

## NumPy Usage

NumPy is used in the project to store student marks in an array and perform calculations such as:

* Average marks
* Highest marks
* Lowest marks
* Total marks

Example:

```python
marks_array = np.array(marks_list)

average = np.mean(marks_array)
highest = np.max(marks_array)
lowest = np.min(marks_array)
total = np.sum(marks_array)
```

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Install NumPy

Open Command Prompt or Terminal and run:

```bash
pip install numpy
```

### 3. Run the program

Open the Python file:

```text
Student Data Management System.py
```

Run it using Python IDLE or another Python editor.

## Main Menu

The program provides the following options:

```text
1. Add Student
2. Display Students
3. Search Student
4. Update Student
5. Delete Student
6. Calculate Average Marks
7. Highest and Lowest Marks
8. Pass/Fail Result
9. Search by Course
10. Sort Students by Marks
11. Display Statistics
12. Display Student Tuple
13. Exit
```

## Project Structure

```text
student-data-management-system/
│
├── README.md
└── Student Data Management System.py
```

## Future Improvements

Possible future improvements include:

* Saving student records permanently using files
* Adding a graphical user interface
* Adding student grades
* Adding login functionality
* Connecting the project to a database

## Author

**Disha Yadav**



