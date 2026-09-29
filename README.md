# Student Grade and Attendance System

This is my python project for student grading and attendance tracking. In this project, a teacher or student can manage student records, enter course marks, track attendance, and automatically generate academic report cards with GPA and exam eligibility. I made this using basic python concepts like if else, while loop, functions, lists, and dictionaries.

## How to Set Up and Run

Here are the step by step instructions to run this project on your system.

### Environment Setup
You only need python 3 installed. You can check if python is working by opening terminal and typing:
```bash
python --version
```

If you want to use a virtual environment (optional):
```bash
python -m venv venv
```
And activate it:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

### Dependency Instalation
This project does not use any third party modules, only standard python is used. You can run this if needed:
```bash
pip install -r requirements.txt
```

### Configuration
No database or extra setup is required. Student records are stored inside a python dictionary so everything runs in memory when you start the code. Two demo students are preloaded automatically so you can test right away.

### Execution

step 1 : run the main.py
Open terminal inside the project folder and type:
```bash
python main/main.py
```
(or `python src/main.py` if you are in src folder)

step 2 : enter your choice
When the program starts, you will see 5 choices. Type a number and press Enter:
- Choice 1: Opens the student management menu to add a new student, delete a student, or view the student list.
- Choice 2: Opens the grading menu to enter course marks and view subject grades with GPA.
- Choice 3: Opens the attendance menu to record attended classes and check exam eligibility status.
- Choice 4: Opens the academic reports menu to view the full report card or class summary table.
- Choice 5: Exits the program.
