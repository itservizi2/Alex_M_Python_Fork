math_grades = {"John": 85, "Emily": 92, "Michael": 78, "Jessica": 95, "Ion": 100}
science_grades = {"John": 90, "Emily": 88, "Michael": 92, "Jessica": 87, "Marius": 100}
bio_grades = {"John": 95, "Emily": 70, "Michael": 20, "Jessica": 74, "Victor": 100}

average_grades = dict()

common_students = set(math_grades).intersection(set(science_grades)).intersection(set(bio_grades))
print(common_students)

for student in set(math_grades).union(set(science_grades)).union(bio_grades):
    if student not in common_students:
        print(f'Student {student} doens\'t have enough grades')

toate_materiile = [math_grades, science_grades, bio_grades]

for student_name in common_students:
    total = 0
    grades_count = 0
    for notele_la_materia in toate_materiile:
        if student_name in notele_la_materia:
            total += notele_la_materia[student_name]
            grades_count += 1
    average_grades[student_name] = total / grades_count
print(average_grades)
