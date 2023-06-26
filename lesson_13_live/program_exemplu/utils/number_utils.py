def input_n_numbers(n):
    time = 0
    all_values = []
    while time < n:
        value = input('Value')
        try:
            number_value = int(value)
        except ValueError as ex:
            print(f'Value {value} is not a whole number, trying to see if it\'s a float')
            try:
                number_value = float(value)
            except ValueError as ex:
                print(f'Value {value} is neither a float nor a integer, please try again')
                continue
        all_values.append(number_value)
        time += 1
    return all_values


print(input_n_numbers(5))


try:
    asd
except Exception:
    print('hehe')