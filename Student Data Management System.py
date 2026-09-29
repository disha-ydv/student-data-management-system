
import numpy as np

roster = []

print("========================================")
print("     STUDENT DATA MANAGEMENT SYSTEM")
print("========================================")


def add_entry():
    num = int(input("Enter roll number: "))

    # check for dupes
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


def avg_score():
    if not roster:
        print("No student records found.")
        return

    scores = []
    for entry in roster:
        scores.append(entry["marks"])

    score_arr = np.array(scores)

    print("\nMarks Array:", score_arr)
    print("Average Marks:", np.mean(score_arr))


def extremes():
    if not roster:
        print("No student records found.")
        return

    scores = []
    for entry in roster:
        scores.append(entry["marks"])

    score_arr = np.array(scores)

    highest = np.max(score_arr)
    lowest = np.min(score_arr)

    print("\nMarks Array:", score_arr)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)


def pass_fail():
    if not roster:
        print("No student records found.")
        return

    print("\n========== PASS / FAIL RESULT ==========")

    for entry in roster:
        print("\nRoll Number:", entry["_id"])
        print("Name:", entry["name"])
        print("Marks:", entry["marks"])

        if entry["marks"] >= 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")


def search_course():
    if not roster:
        print("No student records found.")
        return

    prog = input("Enter course to search: ")
    is_found = False

    print("\n--- Students in", prog, "---")

    for entry in roster:
        if entry["course"].lower() == prog.lower():
            print("Roll Number:", entry["_id"])
            print("Name:", entry["name"])
            print("Age:", entry["age"])
            print("Marks:", entry["marks"])
            print("-----------------------")

            is_found = True

    if not is_found:
        print("No students found in this course.")


def sort_by_marks():
    if not roster:
        print("No student records found.")
        return

    sorted_list = []
    for entry in roster:
        sorted_list.append((entry["name"], entry["marks"]))

    sorted_list.sort(key=lambda x: x[1], reverse=True)

    print("\n====== STUDENTS SORTED BY MARKS ======")

    for name, score in sorted_list:
        print("Name:", name)
        print("Marks:", score)
        print("-----------------------")


def stats():
    if not roster:
        print("No student records found.")
        return

    scores = []
    for entry in roster:
        scores.append(entry["marks"])

    score_arr = np.array(scores)

    print("\n========== STATISTICS ==========")
    print("Number of Students:", len(roster))
    print("Average Marks:", np.mean(score_arr))
    print("Highest Marks:", np.max(score_arr))
    print("Lowest Marks:", np.min(score_arr))
    print("Total Marks:", np.sum(score_arr))


def show_tuple():
    if not roster:
        print("No student records found.")
        return

    num = int(input("Enter roll number: "))

    for entry in roster:
        if entry["_id"] == num:
            student_info = (
                entry["_id"],
                entry["name"],
                entry["course"]
            )

            print("\nStudent Tuple:")
            print(student_info)

            print("Roll Number:", student_info[0])
            print("Name:", student_info[1])
            print("Course:", student_info[2])

            return

    print("Student not found.")


while True:
    print("\n========================================")
    print("              MAIN MENU")
    print("========================================")

    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Average Marks")
    print("7. Highest and Lowest Marks")
    print("8. Pass/Fail Result")
    print("9. Search by Course")
    print("10. Sort Students by Marks")
    print("11. Display Statistics")
    print("12. Display Student Tuple")
    print("13. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_entry()

    elif choice == "2":
        show_all()

    elif choice == "3":
        search()

    elif choice == "4":
        update()

    elif choice == "5":
        delete()

    elif choice == "6":
        avg_score()

    elif choice == "7":
        extremes()

    elif choice == "8":
        pass_fail()

    elif choice == "9":
        search_course()

    elif choice == "10":
        sort_by_marks()

    elif choice == "11":
        stats()

    elif choice == "12":
        show_tuple()

    elif choice == "13":
        print("\nThank you for using the system!")
        break

    else:
        print("Invalid choice. Please try again.")
