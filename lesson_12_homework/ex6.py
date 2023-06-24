def is_palindrome(text):
    text = text.lower().replace(" ", "").replace(",", "").replace(".", "")
    return text == text[::-1]


text = input("Enter a text: ")
result = is_palindrome(text)

print("Palindrome:", result)
