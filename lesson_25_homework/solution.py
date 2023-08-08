import random

import pandas as pd
from openpyxl import load_workbook, Workbook

from lesson_18_live.decorator_example import print_exec_time


@print_exec_time
def load_data(file_path):
    return pd.read_excel(file_path)


@print_exec_time
def show_missing_scores(data):
    missing_scores = data[data['score'].isna()]
    print(missing_scores)


@print_exec_time
def show_scores_between(data, a, b):
    selected_scores = data[(data['score'] >= a) & (data['score'] <= b)]
    print(selected_scores)


def show_sorted_by_score(data):
    sorted_by_score = data.sort_values(by='score')
    print(sorted_by_score)


def show_sorted_by_name(data):
    sorted_by_name = data.sort_values(by='name')
    print(sorted_by_name)


def add_new_element(data):
    name = input("Enter name: ")
    score = float(input("Enter score: "))
    new_element = pd.DataFrame(
        [
            {'name': name, 'score': score, 'attempts': int(input('Attempts')),
             'qualify': input('Qualify ? Yes/No')}
        ]
    )
    data = pd.concat([data, new_element], ignore_index=True)
    return data


def remove_result_by_index(data):
    index = int(input("Enter index to remove: "))
    data = data.drop(index, axis=0)
    return data


def save_qualified_students(data):
    qualified_students = data[['name', 'score']].dropna()

    qualified_students_file = 'qualified_students.xlsx'
    qualified_students.to_excel(qualified_students_file, index=False)
    print(f"Qualified students saved to {qualified_students_file}")


def main():
    file_path = input("Insert file path")
    data = load_data(file_path)

    while True:
        print("1. Show rows with missing scores")
        print("2. Show rows with scores between a and b")
        print("3. Show rows sorted by score")
        print("4. Show rows sorted by name")
        print("5. Add a new element")
        print("6. Remove a result by index")
        print("7. Save qualified students to Excel")
        print("8. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            show_missing_scores(data)
        elif choice == 2:
            a = float(input("Enter lower limit a: "))
            b = float(input("Enter upper limit b: "))
            show_scores_between(data, a, b)
        elif choice == 3:
            show_sorted_by_score(data)
        elif choice == 4:
            show_sorted_by_name(data)
        elif choice == 5:
            data = add_new_element(data)
        elif choice == 6:
            data = remove_result_by_index(data)
        elif choice == 7:
            save_qualified_students(data)
        elif choice == 8:
            break
        else:
            print("Invalid choice. Please choose a valid option.")

    print("Program ended.")


@print_exec_time
def seed_xlsx():
    dataframe = pd.read_excel('homework.xlsx')
    new_element = pd.DataFrame(
        [
            {'name': 'example', 'score': random.randrange(1, 20), 'attempts': random.randrange(1, 20),
             'qualify': bool([random.randrange(0, 1)])}
            for el in range(0, 5000)
        ]
    )
    dataframe = pd.concat([dataframe, new_element], ignore_index=True)
    dataframe.to_excel('homework.xlsx')


if __name__ == "__main__":
    # seed_xlsx()
    main()


def respond_to_request(request):
    try:
        return 200
    except FileNotFoundError:
        return 404
    except ValueError:
        return 400
    except Exception:
        return 500
