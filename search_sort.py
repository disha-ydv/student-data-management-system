from student_data import roster


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
