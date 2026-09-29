# Project Statement: Student Grade and Attendance System

## 1. Problem Statement
In schools and colleges, teachers usually calculate grades, GPAs, and attendance percentages manually on paper or in simple spreadsheets. When calculating weighted GPA with different credit courses, it is very easy to make calculation mistakes with grade points. Also, students often do not realize that their attendance has dropped below 75% until the final exam hall ticket is denied. So I built a simple command line python program that separates student management, course grading, attendance tracking, and report cards into clean modules, automatically converts marks into letter grades and grade points, calculates credit-weighted GPA, and warns if attendance is below the 75% cutoff rule.

## 2. Scope of the Project
This project covers the core tasks of managing academic records for students:
- Storing student personal details like Student ID, Name, Department, and Semester.
- Recording marks and course credit hours for multiple subjects in a dedicated grading module.
- Converting numeric marks (0-100) into letter grades (S, A, B, C, D, E, F) and grade points (0 to 10).
- Calculating the overall semester GPA weighted by course credits.
- Tracking attendance in a dedicated attendance module and calculating percentage.
- Determining exam eligibility based on the 75% attendance rule and calculating how many more classes are needed if short.
- Generating a formatted report card in the terminal and viewing class performance tables.

## 3. Target Users
- College professors, school teachers, and academic staff who want a fast, simple terminal tool to record marks and attendance.
- Students who want to check their grades, GPA, standing, and check if they are eligible to sit for exams.

## 4. High-Level Features
- Student Management: Adds new students with duplicate ID checking, deletes students, and lists enrolled students.
- Course Grading: Records course marks and credits, converts to grades/GP, and displays individual grade reports with GPA.
- Attendance Tracking: Records classes attended, computes percentage, verifies 75% eligibility, and displays attendance warnings.
- Academic Reports: Displays a consolidated report card showing both academic marks and attendance status, plus class summaries.
