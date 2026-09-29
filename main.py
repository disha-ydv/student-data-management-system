from student_operations import add_entry, show_all, search, update, delete
from marks_analysis import avg_score, extremes, pass_fail, stats
from search_sort import search_course, sort_by_marks
from student_utils import show_tuple


print("========================================")
print("     STUDENT DATA MANAGEMENT SYSTEM")
print("========================================")


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
