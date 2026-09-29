from grading import calc_gpa, calc_avg, get_standing, get_gp, get_gr
from attendance import calc_pct, check_eligibility, get_warning
from student_data import get_student, all_students

def build_report(st):
    gpa = calc_gpa(st["courses"])
    avg_m = calc_avg(st["courses"])
    std = get_standing(gpa)
    att = st["att"][0]
    tot = st["att"][1]
    pct = calc_pct(att, tot)
    ok = check_eligibility(pct)

    l = []
    l.append("==================================================")
    l.append("              ACADEMIC REPORT CARD                ")
    l.append("==================================================")
    l.append("ID   : " + st["sid"] + "   Name : " + st["n"])
    l.append("Dept : " + st["dept"] + "   Sem  : " + str(st["sem"]))
    l.append("--------------------------------------------------")
    l.append("Course Name         Credits  Marks   Grade   GP")
    l.append("--------------------------------------------------")
    if len(st["courses"]) == 0:
        l.append("No courses entered yet.")
    else:
        for c in st["courses"]:
            gp = get_gp(c["m"])
            gr = get_gr(c["m"])
            l.append(c["c_n"].ljust(20) + str(c["crd"]).ljust(9) + str(c["m"]).ljust(8) + gr.ljust(8) + str(gp))
    l.append("--------------------------------------------------")
    l.append("GPA : " + str(gpa) + " / 10.0   Standing : " + std)
    l.append("Average Marks : " + str(avg_m))
    l.append("Attendance : " + str(att) + "/" + str(tot) + " (" + str(pct) + "%)")
    if ok:
        l.append("Exam Status : ELIGIBLE")
    else:
        l.append("Exam Status : DEBARRED (Attendance < 75%)")
        l.append("Note        : " + get_warning(att, tot))
    l.append("==================================================")
    return "\n".join(l)

def do_view_report():
    sid = input("Enter Student ID: ").strip()
    st = get_student(sid)
    if st is None:
        print("Error: Student ID not found.")
    else:
        card = build_report(st)
        print("\n" + card)

def do_class_summary():
    stus = all_students()
    if len(stus) == 0:
        print("\nNo students found.")
        return
    print("\nID          Name            Dept    Sem   GPA    Att%   Status")
    print("------------------------------------------------------------------")
    for s in stus:
        gpa = calc_gpa(s["courses"])
        pct = calc_pct(s["att"][0], s["att"][1])
        if check_eligibility(pct):
            status = "Eligible"
        else:
            status = "Debarred"
        print(s["sid"].ljust(12) + s["n"].ljust(16) + s["dept"].ljust(8) + str(s["sem"]).ljust(6) + str(gpa).ljust(7) + str(pct).ljust(7) + status)

def do_report():
    print("\n--- Academic Reports ---")
    print("1. Student Report Card")
    print("2. Class Performance Summary")
    ch = input("Enter choice (1-2): ").strip()
    if ch == "1":
        do_view_report()
    elif ch == "2":
        do_class_summary()
    else:
        print("Invalid choice.")
