"""
Scrieți un program_exemplu pentru a citi temperatura de la utilizator și pentru a afișa un mesaj adecvat în funcție de starea temperaturii de mai jos.
Temp -40-(-10) atunci 'Vremea extrem de rece'
Temp -10-0 atunci 'Vremea foarte rece'
Temp 0-10 atunci 'Vreme rece'
Temp 10-20 atunci 'Vreme normala'
Temp 20-30 atunci 'Vreme calda'
Temp 30-40 atunci 'Este foarte cald'
Temp >=40 atunci 'Este extrem de cald'
"""
temperatura = float(input("Introduceți temperatura: "))

if temperatura >= 40:
    print("Este extrem de cald")
elif temperatura >= 30:
    print("Este foarte cald")
elif temperatura >= 20:
    print("Vreme caldă")
elif temperatura >= 10:
    print("Vreme normală")
elif temperatura >= 0:
    print("Vreme rece")
elif temperatura >= -10:
    print("Vreme foarte rece")
else:
    print("Vreme extrem de rece")

# Alta varianta
# if temperatura >= -40 and temperatura <= -10:
#     print("Vreme extrem de rece")
# elif temperatura < 0 and temperatura > -10:
#     print("Vreme foarte rece")

# Inca una
# if -40 <= temperatura <= -10:
#     print("Vreme extrem de rece")
