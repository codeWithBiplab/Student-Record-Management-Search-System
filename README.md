# Student-Record-Management-Search-System



## A. Title

Student Record Management and Search System using

## B. Objective

The main objective of this project is to create a simple Student Record Management and Search System using Python.

In this project, student information is stored using different file formats like TXT, CSV and JSON. The project also uses Object-Oriented Programming concepts to create and manage student records.

The system can add, display, update and remove student records. It can also search students using Student ID, Name, Department and average marks.

This project helped me to understand Python classes, objects, methods, file handling and basic searching using loops and conditions.

## C. Features

The main features of the project are:

* Create and store student records
* Add a new student
* Display student information
* Calculate total marks
* Calculate average marks
* Check pass or fail status
* Update student marks
* Remove a student
* Search student by Student ID
* Search students by Name
* Search students by Department
* Search students whose average marks are above a given value
* Read student records from TXT file
* Read and write student records using CSV file
* Read and write student records using JSON file
* Use command-line arguments with argparse
* Manage multiple Student objects using StudentManager

The three subjects used in this project are:

* DBMS
* OS
* Computer Network

The `Subject1`, `Subject2` and `Subject3` given in the problem statement are represented using these actual subject names.

## D. Project Structure

The project has the following structure:

```text
student-record-system/
│
├── main.py
├── student.py
├── manager.py
├── file_handler.py
│
├── data/
│   ├── students.txt
│   ├── students.csv
│   └── students.json
│
└── README.md
```

### main.py

This is the main file of the project. It handles command-line arguments using the `argparse` module and controls the different operations of the program.

### student.py

This file contains the `Student` class. It stores the information of one student and contains methods for calculating total marks, average marks, result and updating marks.

### manager.py

This file contains the `StudentManager` class. It manages multiple Student objects and performs operations like adding, removing, displaying and searching students.

### file_handler.py

This file is used for file handling. It contains methods for reading and writing student records in TXT, CSV and JSON formats.

### data folder

The data folder contains the sample student records in TXT, CSV and JSON format.

### README.md

This file contains the project documentation, features, commands and explanation of the project.

## E. Requirements

The following are required to run this project:

* Python 3
* Any Python IDE or code editor
* Command Prompt or Terminal

The project uses only Python built-in modules.

Modules used:

```text
argparse
csv
json
```

No external Python packages are required.

Pandas and NumPy are not used in this project.

## F. How to Run

First open the terminal and go to the project folder:

```bash
cd student-record-system
```

The program is executed using `main.py`.

### Display all students from CSV

```bash
python main.py --file data/students.csv --format csv --mode display
```

### Search student by ID

```bash
python main.py --file data/students.csv --format csv --mode search-id --id 102
```

### Search student by name

```bash
python main.py --file data/students.csv --format csv --mode search-name --name Rahul
```

### Search students by department

```bash
python main.py --file data/students.csv --format csv --mode search-department --department "Computer Science"
```

### Search students by average marks

The following command searches students having average marks greater than 75.

```bash
python main.py --file data/students.csv --format csv --mode search-average --average 75
```

### Add a new student

```bash
python main.py --file data/students.csv --format csv --mode add --id 106 --name Riya --department "Computer Science" --semester 2 --dbms 85 --os 90 --computer-network 88
```

### Update marks

```bash
python main.py --file data/students.csv --format csv --mode update --id 101 --dbms 85 --os 88 --computer-network 90
```

### Remove a student

```bash
python main.py --file data/students.csv --format csv --mode remove --id 105
```

### Working with JSON

Display students from JSON:

```bash
python main.py --file data/students.json --format json --mode display
```

Search a student by name in JSON:

```bash
python main.py --file data/students.json --format json --mode search-name --name Priya
```

Search a student by ID in JSON:

```bash
python main.py --file data/students.json --format json --mode search-id --id 102
```

### Working with TXT

Display students from TXT:

```bash
python main.py --file data/students.txt --format txt --mode display
```

Search student by ID in TXT:

```bash
python main.py --file data/students.txt --format txt --mode search-id --id 103
```

Search students by department in TXT:

```bash
python main.py --file data/students.txt --format txt --mode search-department --department Mathematics
```

Search students by average in TXT:

```bash
python main.py --file data/students.txt --format txt --mode search-average --average 75
```

## G. Input and Output

### Input

The program takes the following student information:

* Student ID
* Name
* Department
* Semester
* DBMS marks
* OS marks
* Computer Network marks

The input file and file format are given using command-line arguments.

For example:

```bash
python main.py --file data/students.csv --format csv --mode display
```

### Input Files

The project contains three sample input files:

```text
data/students.txt
data/students.csv
data/students.json
```

Each file contains five student records.

### Output

The program displays the student information in the terminal.

For every student, it displays:

* Student ID
* Name
* Department
* Semester
* DBMS marks
* OS marks
* Computer Network marks
* Total marks
* Average marks
* Pass/Fail result

When a student is added, updated or removed, the selected file is also updated.

### Example Output

For example, when displaying a student:

```text
Student ID: 101
Name: Rahul
Department: Computer Science
Semester: 1
DBMS: 78.0
OS: 82.0
Computer Network: 69.0
Total Marks: 229.0
Average Marks: 76.33
Result: Pass
```

For a search where no student is found:

```text
Student not found.
```

For an average search where there are no matching records:

```text
No matching students found.
```

## H. OOP Concepts Used

Object-Oriented Programming is used in this project mainly through two classes.

### Student Class

The `Student` class represents one student.

The constructor is:

```python
__init__()
```

It is used to initialize student information.

The class contains attributes such as:

```text
student_id
name
department
semester
dbms
os
computer_network
```

The class also contains the following methods:

```text
calculate_total()
calculate_average()
get_result()
update_marks()
display_student()
```

### StudentManager Class

The `StudentManager` class is used to manage multiple Student objects.

It contains a list called `students` where Student objects are stored.

The methods include:

```text
add_student()
remove_student()
search_student()
search_by_name()
search_by_department()
search_by_average()
display_all_students()
load_from_file()
save_to_file()
```

This shows the difference between a class which represents one student and another class which manages many student objects.

## I. File Handling Concepts Used

The project works with three different file formats.

### TXT File

The TXT file contains student information in comma-separated form.

Example:

```text
101, Rahul, Computer Science, 1, 78, 82, 69
```

The program uses Python file handling functions such as:

```text
open()
readlines()
write()
```

Different file modes like `r` and `w` are used.

### CSV File

The CSV file contains a header and student records.

Example header:

```text
Student_ID,Name,Department,Semester,DBMS,OS,Computer_Network
```

The Python `csv` module is used.

Functions used include:

```text
csv.reader()
csv.writer()
```

The first row of the CSV file is treated as the header.

### JSON File

The JSON file stores the student information using dictionaries and lists.

The Python `json` module is used.

Functions used include:

```text
json.load()
json.dump()
```

The JSON data is read from the file and converted into Student objects.

## J. Searching Concepts Used

The searching operations are implemented using basic Python logic.

No Pandas, NumPy or other search libraries are used.

### Search by Student ID

The program checks each Student object using a loop.

The student ID is compared with the given ID.

```text
for student in students:
    if student.student_id == student_id:
```

### Search by Name

The program checks the name of each student and compares it with the entered name.

The search is case-insensitive.

### Search by Department

The department of each student is checked using a loop and condition.

### Search by Average Marks

The program calculates the average marks of every student and checks whether it is greater than the given value.

For example:

```text
if student.calculate_average() > average:
```

This is done using simple loops, conditions and comparisons as required in the assignment.

## K.  Conclusion

Through this assignment, I learned how to create classes and objects in Python and how to divide a program into different Python files.

I also learned how to read and write data using TXT, CSV and JSON files. I understood how CSV and JSON modules work and how file data can be converted into Python objects.

Another important part I learned was implementing searching using loops and conditions instead of using advanced searching functions or libraries.

I also learned how to use command-line arguments with `argparse`.

The main difficulty I faced was managing the same student data in three different file formats and making sure that the data can be converted correctly into Student objects.

Overall, this assignment helped me understand Python OOP, file handling, basic searching and modular programming in a practical way.


