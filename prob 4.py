marks = [35, 60, 45, 80, 35, 55, 60, 95, 40, 80]

passed = [mark for mark in marks if mark >= 40]
unique_marks = sorted(set(passed))
qualified = [mark for mark in unique_marks if mark >= 60]
top_three = qualified[-3:][::-1]

print("Processed marks:", unique_marks)
print("Qualified marks:", qualified)
print("Top three:", top_three)
