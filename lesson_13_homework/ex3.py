while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print(f"The division of {num1} by {num2} is {result}")
        break
    except ZeroDivisionError:
        print("Error: division by zero. Please enter a non-zero value for the second number.")
