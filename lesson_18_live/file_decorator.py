import json
import os.path


def json_file_open(file_name):
    def inner(function):
        try:
            with open(file_name) as file:
                json_data = json.load(file)
        except Exception as ex:
            print(f'file doesn\'t work: {str(ex)}')
            json_data = None

        def wrapper(*args, **kwargs):
            processed_data = function(json_data, *args, **kwargs)
            with open(file_name, 'w') as file:
                json.dump(processed_data or json_data, file)
            return processed_data

        return wrapper

    return inner


@json_file_open('example2.json')
def do_this_with_file(json_data):
    print(json_data)
    if isinstance(json_data, list):
        json_data.append(input())
    return json_data


@json_file_open('hello.json')
def sum_of_arr(json_data):
    print(sum(json_data))
    return [a for a in range(sum(json_data))]


sum_of_arr()
do_this_with_file()


def example(file_name, function_to_call):
    try:
        with open(file_name) as file:
            json_data = json.load(file)
    except Exception as ex:
        print(f'file doesn\'t work: {str(ex)}')
        json_data = None
    processed_data = function_to_call(json_data)
    with open(file_name, 'w') as file:
        json.dump(processed_data or json_data, file)