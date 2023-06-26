"""
Exercise 1: Grading System
Write a program_exemplu that takes a student's score as input and prints their corresponding grade based on the following conditions:
- Score >= 90: Grade A
- Score >= 80: Grade B
- Score >= 70: Grade C
- Score >= 60: Grade D
- Score < 60: Grade F
"""

puncte_la_test = int(input('Score:'))

if puncte_la_test >= 90:
    print('Grade A')
elif puncte_la_test >= 80:
    print('Grade B')
elif puncte_la_test >= 70:
    print('Grade C')
elif puncte_la_test >= 60:
    print('Grade D')
else:
    print("Grade F")
