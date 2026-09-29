from student_data import get_student, set_att

def calc_pct(att, tot):
    if tot == 0:
        return 0.0
    return round((att / tot) * 100, 2)

def check_eligibility(pct):
    if pct >= 75.0:
        return True
    else:
        return False

def get_warning(att, tot):
    pct = calc_pct(att, tot)
    if pct >= 75.0:
        return "Attendance is good"
    elif tot == 0:
        return "No classes recorded"
    else:
        w = (0.75 * tot - att) / 0.25
        return "Warning: need " + str(int(w) + 1) + " more classes for 75%"

def do_set_attendance():
    sid = input("Enter Student ID: ").strip()
    st = get_student(sid)
    if st is None:
        print("Error: Student ID not found.")
        return
    a_str = input("Enter Classes Attended: ").strip()
    t_str = input("Enter Total Classes: ").strip()
    if not a_str.isdigit() or not t_str.isdigit():
        print("Error: Class counts must be integers.")
        return
    a = int(a_str)
    t = int(t_str)
    if a < 0 or t < 0:
        print("Error: Classes cannot be negative.")
    elif a > t:
        print("Error: Attended classes cannot be more than total.")
    else:
        set_att(sid, a, t)
        print("Attendance updated.")

def do_view_attendance():
    sid = input("Enter Student ID: ").strip()
    st = get_student(sid)
    if st is None:
        print("Error: Student ID not found.")
        return
    att = st["att"][0]
    tot = st["att"][1]
    pct = calc_pct(att, tot)
    ok = check_eligibility(pct)
    print("\nAttendance for " + st["n"] + " (" + st["sid"] + "):")
    print("--------------------------------------------------")
    print("Attended   : " + str(att) + " / " + str(tot) + " classes")
    print("Percentage : " + str(pct) + "%")
    if ok:
        print("Status     : ELIGIBLE FOR EXAMS")
    else:
        print("Status     : DEBARRED (Attendance < 75%)")
        print("Advice     : " + get_warning(att, tot))

def do_attendance():
    print("\n--- Attendance Tracking ---")
    print("1. Enter Attendance")
    print("2. View Attendance & Eligibility")
    ch = input("Enter choice (1-2): ").strip()
    if ch == "1":
        do_set_attendance()
    elif ch == "2":
        do_view_attendance()
    else:
        print("Invalid choice.")
