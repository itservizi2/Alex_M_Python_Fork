import string

text = input('Introdu un caracter').lower()
if len(text) > 1:
    print('Am cerut doar un caracter')
else:
    if text.isnumeric():
        print('Este numar')
    elif text.isspace():
        print('Este spatiu')
    elif text in string.punctuation:
        print('Este punctuatie')
    elif text in 'aeiou':
        print('Este vocala')
    else:
        print("Este consoana")

print('hello' in 'Hello, hello, hello')
# Echivalente
print('Hello, hello, hello'.count('hello') > 0)
