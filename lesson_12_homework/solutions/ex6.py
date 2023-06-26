def is_palindrome(text):

    cleaned_text = text.replace(" ", "").lower()
    reversed_text = cleaned_text[::-1]

    return cleaned_text == reversed_text


text = input("Enter a text: ")

palindrome = is_palindrome(text)
print(f"Palindrome: {palindrome}")