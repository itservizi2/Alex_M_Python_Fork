"""
Scrieți un program pentru a citi temperatura de la utilizator și pentru a afișa un mesaj adecvat în funcție de starea temperaturii de mai jos.
Temp -40-(-10) atunci 'Vremea extrem de rece'
Temp -10-0 atunci 'Vremea foarte rece'
Temp 0-10 atunci 'Vreme rece'
Temp 10-20 atunci 'Vreme normala'
Temp 20-30 atunci 'Vreme calda'
Temp 30-40 atunci 'Este foarte cald'
Temp >=40 atunci 'Este extrem de cald'
"""

temperatura = int(input("introduceti temperatura : "))
if -40 <= temperatura < -10:
    print("'Vremea extrem de rece'")
elif -10 <= temperatura < 0:
    print('Vremea foarte rece')
elif 0 <= temperatura < 10:
    print('Vreme rece')
elif 10 <= temperatura < 20:
    print('Vreme normala')
elif 20 <= temperatura < 30:
    print('Vreme calda')
elif 30 <= temperatura < 40:
    print('Este foarte cald')
else:
    print('Este extrem de cald')

