from student_data import get_student, add_course

def get_gp(m):
    if m >= 90:
        return 10.0
    elif m >= 80:
        return 9.0
    elif m >= 70:
        return 8.0
    elif m >= 60:
        return 7.0
    elif m >= 50:
        return 6.0
    elif m >= 40:
        return 5.0
    else:
        return 0.0

def get_gr(m):
    if m >= 90:
        return "S"
    elif m >= 80:
        return "A"
    elif m >= 70:
        return "B"
    elif m >= 60:
        return "C"
    elif m >= 50:
        return "D"
    elif m >= 40:
        return "E"
    else:
        return "F"

def get_standing(gpa):
    if gpa >= 9.0:
        return "First Class with Distinction"
    elif gpa >= 8.0:
        return "First Class"
    elif gpa >= 6.5:
        return "Second Class"
    elif gpa >= 5.0:
        return "Pass Class"
    elif gpa > 0.0:
        return "Academic Warning"
    else:
        return "No Grades"

def calc_gpa(crs):
    if len(crs) == 0:
        return 0.0
    tot_crd = 0
    w_pts = 0.0
    for c in crs:
        gp = get_gp(c["m"])
        tot_crd = tot_crd + c["crd"]
        w_pts = w_pts + (gp * c["crd"])
    if tot_crd == 0:
        return 0.0
    return round(w_pts / tot_crd, 2)

def calc_avg(crs):
    if len(crs) == 0:
        return 0.0
    tot_m = 0.0
    for c in crs:
        tot_m = tot_m + c["m"]
    return round(tot_m / len(crs), 2)

def do_add_marks():
    sid = input("Enter Student ID: ").strip()
    st = get_student(sid)
    if st is None:
        print("Error: Student ID not found.")
        return
    c_n = input("Enter Course Name: ").strip()
    m_str = input("Enter Marks (0-100): ").strip()
    crd_str = input("Enter Credits (1-6): ").strip()
    try:
        m = float(m_str)
        crd = int(crd_str)
        if m < 0 or m > 100:
            print("Error: Marks must be between 0 and 100.")
        elif crd < 1 or crd > 6:
            print("Error: Credits must be between 1 and 6.")
        else:
            add_course(sid, c_n, m, crd)
            print("Course marks added.")
    except ValueError:
        print("Error: Please enter valid numbers.")

def do_view_grades():
    sid = input("Enter Student ID: ").strip()
    st = get_student(sid)
    if st is None:
        print("Error: Student ID not found.")
        return
    print("\nGrades for " + st["n"] + " (" + st["sid"] + "):")
    print("Course Name         Credits  Marks   Grade   GP")
    print("--------------------------------------------------")
    if len(st["courses"]) == 0:
        print("No courses entered yet.")
    else:
        for c in st["courses"]:
            gp = get_gp(c["m"])
            gr = get_gr(c["m"])
            print(c["c_n"].ljust(20) + str(c["crd"]).ljust(9) + str(c["m"]).ljust(8) + gr.ljust(8) + str(gp))
    gpa = calc_gpa(st["courses"])
    avg_m = calc_avg(st["courses"])
    print("--------------------------------------------------")
    print("GPA : " + str(gpa) + " / 10.0   Standing : " + get_standing(gpa))
    print("Average Marks : " + str(avg_m))

def do_grading():
    print("\n--- Course Grading ---")
    print("1. Enter Course Marks")
    print("2. View Grades and GPA")
    ch = input("Enter choice (1-2): ").strip()
    if ch == "1":
        do_add_marks()
    elif ch == "2":
        do_view_grades()
    else:
        print("Invalid choice.")
