registrations = {
    "Arun": ["Python", "Java", "SQL", "Python"],
    "Bala": ["Python", "C", "SQL"],
    "Charan": ["Java", "Python", "SQL"],
    "Divya": ["Python", "Java"],
    "Ezhil": ["C", "Java", "Java"]
}

target = "Arun"
target_courses = set(registrations[target])
common_students = {}

for student, courses in registrations.items():
    if student == target:
        continue

    common = target_courses & set(courses)
    if len(common) >= 2:
        common_students[student] = sorted(common)

print("Common courses:", common_students)
