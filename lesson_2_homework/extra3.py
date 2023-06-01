## Exercițiul 3: Conversie de temperatură
# Scrie un program care preia o temperatură în grade Celsius ca intrare și o convertește în grade Fahrenheit.
# Formula de conversie este: Fahrenheit = Celsius * 9/5 + 32. Afișează temperatura convertită.

celsius_degree = float(input("Insert Celsius degrees: "))
fahrenheit_degree = celsius_degree * 9/5 + 32
print(str(celsius_degree) + " Celsius degrees = " + str(fahrenheit_degree) + " Fahrenheit degrees")

