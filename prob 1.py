def evaluate(m1, m2, m3, attendance):
    average = (m1 + m2 + m3) / 3
    passed = m1 >= 40 and m2 >= 40 and m3 >= 40
    good_average = average >= 75
    good_attendance = attendance >= 75

    if passed and good_average and good_attendance:
        return average, "Eligible"
    return average, "Not Eligible"


m1, m2, m3, attendance = map(
    float, input("Enter marks and attendance: ").split()
)
average, status = evaluate(m1, m2, m3, attendance)
print("Average:", average)
print("Status:", status)
