import json
from datetime import datetime


def get_employee_data():
    file = open('files/employee_list.json')
    return json.load(file)


def list_all_employees(data: list):
    print("All emplooyes are:")
    for elm in data:
        print(elm['name'])
    print()


def list_all_position(data):
    all_positions = set([a['position'] for a in data])
    print("All positions are:")
    for position in all_positions:
        print(position)
    print()


def get_total_salary(data):
    salary = sum(a['salary'] for a in data)
    print(f'We have to pay {salary}')
    return salary


def get_total_tax_to_pay(data):
    to_pay = get_total_salary(data)
    tax_percent = float(input('Input tax percent (ex: 20): '))
    print(f'We have to pay {to_pay * tax_percent / 100:.3f} tax per month')


def get_top_most_payed(data):
    sorted_list_of_employees = sorted(data, key=lambda a: a['salary'], reverse=True)
    for employee in sorted_list_of_employees[:10]:
        print(f'{employee["name"]}|{employee["position"]}|{employee["salary"]}|{employee["employee_from"]}')


def get_employee_date_sorting_key(employee):
    return datetime.strptime(employee['employee_from'], '%m/%d/%Y')


def get_top_most_experience(data):
    print()
    print('Most experience employees')
    sorted_list_of_employees = sorted(data, key=get_employee_date_sorting_key)
    for employee in sorted_list_of_employees[:10]:
        print(f'{employee["name"]}|{employee["position"]}|{employee["salary"]}|{employee["employee_from"]}')


if __name__ == '__main__':
    data = get_employee_data()
    list_all_employees(data)
    list_all_position(data)
    get_total_salary(data)
    get_total_tax_to_pay(data)
    get_top_most_payed(data)
    get_top_most_experience(data)
