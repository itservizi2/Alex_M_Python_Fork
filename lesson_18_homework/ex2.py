def calculate_sum():
    def validate_input(value):
        try:
            return float(value)
        except ValueError:
            raise ValueError("Result is not numeric")

    num1 = validate_input(input("Enter the first number: "))
    num2 = validate_input(input("Enter the second number: "))
    num3 = validate_input(input("Enter the third number: "))
    return num1 + num2 + num3

try:
    result = calculate_sum()
    print("Sum:", result)
except ValueError as e:
    print("Error:", str(e))

