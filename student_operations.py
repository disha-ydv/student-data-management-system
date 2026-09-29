from student_data import roster


def add_entry():
    num = int(input("Enter roll number: "))

    for entry in roster:
        if entry["_id"] == num:
            print("Roll number already exists!")
            return

    usr = input("Enter student name: ")
    age = int(input("Enter age: "))
    prog = input("Enter course: ")
    scores = float(input("Enter marks: "))

    roster.append({
        "_id": num,
        "name": usr,
        "age": age,
        "course": prog,
        "marks": scores
    })

    print("Student added successfully!")


def show_all():
    if not roster:
        print("No student records found.")
        return

    print("\n========== STUDENT RECORDS ==========")

    for entry in roster:
        print("Roll Number:", entry["_id"])
        print("Name:", entry["name"])
        print("Age:", entry["age"])
        print("Course:", entry["course"])
        print("Marks:", entry["marks"])
        print("-------------------------------------")


def search():
    if not roster:
        print("No student records found.")
        return

    num = int(input("Enter roll number to search: "))
    is_found = False

    for entry in roster:
        if entry["_id"] == num:
            print("\n--- Student Found ---")
            print("Roll Number:", entry["_id"])
            print("Name:", entry["name"])
            print("Age:", entry["age"])
            print("Course:", entry["course"])
            print("Marks:", entry["marks"])

            is_found = True
            break

    if not is_found:
        print("Student not found.")


def update():
    if not roster:
        print("No student records found.")
        return

    num = int(input("Enter roll number to update: "))
    is_found = False

    for entry in roster:
        if entry["_id"] == num:
            print("\nStudent found.")

            entry["name"] = input("Enter new name: ")
            entry["age"] = int(input("Enter new age: "))
            entry["course"] = input("Enter new course: ")
            entry["marks"] = float(input("Enter new marks: "))

            print("Student updated successfully!")

            is_found = True
            break

    if not is_found:
        print("Student not found.")


def delete():
    if not roster:
        print("No student records found.")
        return

    num = int(input("Enter roll number to delete: "))
    is_found = False

    for entry in roster:
        if entry["_id"] == num:
            roster.remove(entry)

            print("Student deleted successfully!")

            is_found = True
            break

    if not is_found:
        print("Student not found.")
