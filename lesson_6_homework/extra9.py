## Exercițiul 9:

# Scrieți un program care afișează numerele de la 1 la 100. Pentru multiplii de 3, se va afișa "Fizz" în locul numărului.
# Pentru multiplii de 5, se va afișa "Buzz". Pentru numerele care sunt multipli atât de 3, cât și de 5, se va afișa "
# FizzBuzz".

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

