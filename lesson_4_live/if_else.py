# a = int(input('a'))
# b = int(input('b'))
# if a > b:
#     print(f"A: {a} e mai mare")
# if a < b:
#     print(f"b: {b} e mai mare")
# if a == b:
#     print(f"c: sunt egale")


# print('Scrie salut')
#
# a = input('?:')
# if a == 'salut':
#     print('Salut')
# else:
#     print('Am spus sa scrii salut')


# Forma de inregistrare

valid_email = 'mt@mt.com'
is_registered = True

check_email = input("Enter your email")
if check_email == valid_email and is_registered:
    print('Introdu Parola')
    print('Sau tasteaza forgot password')
elif check_email == valid_email and not is_registered:
    print('inregistreazate')
else:
    print("email gresit")


if check_email == valid_email:
    if is_registered:
        print('Introdu Parola')
        print('Sau tasteaza forgot password')
    else:
        print('inregistreazate')
else:
    print("email gresit")

