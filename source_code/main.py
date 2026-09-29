from student_data import add_student, add_course, set_att, do_student
from grading import do_grading
from attendance import do_attendance
from report import do_report

def main():
    add_student("22BCE1001", "Aarav Sharma", "CSE", 3)
    add_course("22BCE1001", "Python Basics", 85, 4)
    add_course("22BCE1001", "Maths", 78, 3)
    set_att("22BCE1001", 32, 40)

    add_student("22BCE1002", "Priya Nair", "ECE", 3)
    add_course("22BCE1002", "Python Basics", 92, 4)
    add_course("22BCE1002", "Circuits", 88, 3)
    set_att("22BCE1002", 26, 40)

    while True:
        print("\n==========================================")
        print("    Student Grade & Attendance System     ")
        print("==========================================")
        print("1. Student Management")
        print("2. Course Grading")
        print("3. Attendance Tracking")
        print("4. Academic Reports")
        print("5. Exit")
        print("------------------------------------------")

        ch = input("Enter choice (1-5): ").strip()

        if ch == "1":
            do_student()
        elif ch == "2":
            do_grading()
        elif ch == "3":
            do_attendance()
        elif ch == "4":
            do_report()
        elif ch == "5":
            print("\nExiting program.")
            break
        else:
            print("\nInvalid choice. Please choose from 1 to 5.")

if __name__ == "__main__":
    main()
