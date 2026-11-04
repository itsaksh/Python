def find_common_courses(students, target, minimum=2):

    if target not in students:
        print(f"Error: '{target}' is not registered.")
        return {}
    target_courses = set(students[target])
    result = {}
    for student, courses in students.items():
        if student == target:
            continue
        common = target_courses.intersection(set(courses))
        if len(common) >= minimum:
            result[student] = sorted(common)
    return result
students = {
    "Arun": ["Java", "Python", "SQL", "Python"],
    "Bala": ["Python", "SQL"],
    "Charan": ["Java", "Python", "SQL"],
    "Divya": ["Java", "Python"],
    "Ezhil": ["Java", "Java", "C"],
    "Farah": ["Java", "Java", "C"]
}
answer = find_common_courses(students, "Arun")
print(answer)