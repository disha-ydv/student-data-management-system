# Student Data Management System

## About the Project

The Student Data Management System is a simple Python console-based project made to manage student records and perform basic analysis on their marks.

The program provides a menu through which a user can add, view, search, update, and delete student records. It also includes some basic operations such as finding average marks, highest and lowest marks, pass/fail results, searching by course, and sorting students according to their marks.

I made the project using separate Python files so that different parts of the program are easier to understand and manage.

## Features

The main features of the project are:

* Add a new student
* Display all student records
* Search for a student using roll number
* Update student information
* Delete a student record
* Calculate average marks
* Find highest and lowest marks
* Display pass/fail results
* Search students by course
* Sort students by marks
* Display basic statistics
* Display selected student information as a tuple

## Technologies Used

* Python
* NumPy
* Git and GitHub

## Python Concepts Used

This project uses some basic Python concepts that I learned during the course, including:

* Lists
* Dictionaries
* Tuples
* Functions
* Loops
* Conditional statements
* Modules and imports
* Searching
* Sorting

NumPy is used for some of the marks calculations.

## How NumPy is Used

The `marks_analysis.py` file uses NumPy to work with the marks of students.

It is used for:

* Finding the average marks
* Finding the highest marks
* Finding the lowest marks
* Finding the total marks
* Creating an array of student marks

## Project Files

```text
Student Data Management System/
│
├── main.py
├── student_data.py
├── student_operations.py
├── marks_analysis.py
├── search_sort.py
├── student_utils.py
├── requirements.txt
├── README.md
├── statement.md
├── .gitignore
│
├── class_diagram.png
├── component_diagram.png
├── sequence_diagram.png
├── student_data_architecture.png
├── student_data_flowchart.png
└── student_data_use_case.png
```

### What each Python file does

| File                    | Purpose                                                                |
| ----------------------- | ---------------------------------------------------------------------- |
| `main.py`               | Displays the main menu and controls the program                        |
| `student_data.py`       | Stores the student records in the `roster` list                        |
| `student_operations.py` | Handles adding, displaying, searching, updating, and deleting students |
| `marks_analysis.py`     | Performs marks calculations and displays statistics                    |
| `search_sort.py`        | Searches students by course and sorts students by marks                |
| `student_utils.py`      | Displays selected student information as a tuple                       |

## How to Run the Project

First, make sure Python is installed.

Install the required library:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python main.py
```

The main menu will appear and the user can choose the required operation.

## Data Storage

At the moment, the project stores student information in a Python list called `roster`.

The data is available while the program is running. Since the project does not use a database or permanent file storage, the data is lost when the program is closed.

## Basic Error Handling

The program handles some common situations, such as:

* Trying to add a duplicate roll number
* Trying to use an operation when there are no records
* Searching for a student who does not exist
* Selecting an invalid menu option

## Documentation

The project also includes documentation diagrams covering:

* System workflow
* System architecture
* Use case diagram
* Module/class structure
* Component diagram
* Sequence diagram

The project statement and other documentation are also included in the repository.

## Future Improvements

Some things that could be added in the future are:

* Saving student data permanently
* Connecting the project to a database
* Better input validation
* Attendance management
* Grade calculation
* A graphical user interface
* Generating student reports

## Project Status

This is a working student project developed using Python. It currently focuses on basic student record management and marks analysis through a console-based menu.

## Author

**Disha Yadav**
