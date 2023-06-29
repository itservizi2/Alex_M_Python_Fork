def sum_of_integers(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input should be a list of integers")

    try:
        return sum(numbers)
    except TypeError:
        raise ValueError("List should only contain integers")


while True:
    try:
        input_list = input("Enter a list of integers (space-separated): ")
        input_list = [int(x) for x in input_list.split()]
        result = sum_of_integers(input_list)
        print("Sum of the list:", result)
        break
    except ValueError:
        print("Invalid input. Please enter a list of integers.")
    except TypeError as err:
        print(err)






