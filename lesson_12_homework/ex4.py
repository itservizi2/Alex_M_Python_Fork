def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        else:
            return True

    else:
        return False

num = int(input("Enter a number: "))
if is_prime(num):
    print("Prime number: True")
else:
    print("Prime number: False")

