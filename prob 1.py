
def evaluate(m1, m2, m3, attendance):


    average = (m1 + m2 + m3) / 3

    all_subjects_pass = m1 >= 40 and m2 >= 40 and m3 >= 40
    good_average = average >= 75
    good_attendance = attendance >= 75

    if all_subjects_pass and good_average and good_attendance:
        return average, "Eligible"

    return average, "Not Eligible"


def main():
    data = input("Enter marks and attendance: ").split()

    if len(data) != 4:
        print("Error: enter exactly 4 values (m1 m2 m3 attendance).")
        return

    try:
        m1, m2, m3, attendance = map(float, data)
    except ValueError:
        print("Error: all values must be numbers.")
        return

    for value in (m1, m2, m3, attendance):
        if not 0 <= value <= 100:
            print("Error: values must be between 0 and 100.")
            return

    average, status = evaluate(m1, m2, m3, attendance)

    print("Average:", round(average, 2))
    print("Status:", status)


main()
