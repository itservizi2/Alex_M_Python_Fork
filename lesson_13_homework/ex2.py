def check_palindrome(input_str):
    if not input_str.strip():
        raise ValueError("Empty string provided")
    else:
        return input_str == input_str[::-1]


input_str = input("Enter a string to check if palindrome: ")
print(check_palindrome(input_str))
