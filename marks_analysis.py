import numpy as np
from student_data import roster


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
