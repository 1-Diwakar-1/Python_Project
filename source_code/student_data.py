stus = {}

def add_student(sid, n, dept, sem):
    sid = str(sid).strip().upper()
    n = str(n).strip()
    dept = str(dept).strip().upper()
    sem = int(sem)
    if sid in stus:
        return False
    stus[sid] = {
        "sid": sid,
        "n": n,
        "dept": dept,
        "sem": sem,
        "courses": [],
        "att": (0, 0)
    }
    return True

def get_student(sid):
    sid = str(sid).strip().upper()
    if sid in stus:
        return stus[sid]
    return None

def add_course(sid, c_n, m, crd):
    st = get_student(sid)
    if st is None:
        return False
    c_n = str(c_n).strip()
    m = float(m)
    crd = int(crd)
    found = False
    for c in st["courses"]:
        if c["c_n"].lower() == c_n.lower():
            c["m"] = m
            c["crd"] = crd
            found = True
            break
    if not found:
        st["courses"].append({"c_n": c_n, "m": m, "crd": crd})
    return True

def set_att(sid, att, tot):
    st = get_student(sid)
    if st is None:
        return False
    st["att"] = (int(att), int(tot))
    return True

def del_student(sid):
    sid = str(sid).strip().upper()
    if sid in stus:
        del stus[sid]
        return True
    return False

def all_students():
    return list(stus.values())

def do_add_student():
    sid = input("Enter Student ID: ").strip()
    if len(sid) == 0:
        print("Error: Student ID cannot be empty.")
        return
    n = input("Enter Name: ").strip()
    if len(n) == 0:
        print("Error: Name cannot be empty.")
        return
    dept = input("Enter Department: ").strip()
    sem_str = input("Enter Semester (1-12): ").strip()
    if not sem_str.isdigit():
        print("Error: Semester must be a number.")
        return
    sem = int(sem_str)
    if sem < 1 or sem > 12:
        print("Error: Semester must be between 1 and 12.")
        return
    succ = add_student(sid, n, dept, sem)
    if succ:
        print("Student added successfully.")
    else:
        print("Error: Student ID already exists.")

def do_delete_student():
    sid = input("Enter Student ID to delete: ").strip()
    succ = del_student(sid)
    if succ:
        print("Student deleted.")
    else:
        print("Error: Student not found.")

def do_list_students():
    all_s = all_students()
    if len(all_s) == 0:
        print("\nNo students found.")
        return
    print("\nID          Name            Dept    Sem")
    print("------------------------------------------")
    for s in all_s:
        print(s["sid"].ljust(12) + s["n"].ljust(16) + s["dept"].ljust(8) + str(s["sem"]))

def do_student():
    print("\n--- Student Management ---")
    print("1. Add New Student")
    print("2. Delete Student")
    print("3. List All Students")
    ch = input("Enter choice (1-3): ").strip()
    if ch == "1":
        do_add_student()
    elif ch == "2":
        do_delete_student()
    elif ch == "3":
        do_list_students()
    else:
        print("Invalid choice.")
