from student_data import roster


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
