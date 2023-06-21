math_grades = {"John": 85, "Emily": 92, "Michael": 78, "Jessica": 95}
science_grades = {"John": 90, "Emily": 88, "Michael": 92, "Jessica": 87}

average_grades = {}

for student in math_grades:
    average_grades[student] = (math_grades[student] + science_grades[student]) / 2

print(average_grades)
