"""Scrieţi un program_exemplu care citeşte de la tastatură de 3 ori timpul în care un sportiv aleargă proba de 100 metri (numărul de secunde).
Apoi afişaţi la ecran timpul mediu (media aritmetică a celor 3 încercări) în secunde."""

# Solution
timpul_1 = float(input('Timp 1'))
timpul_2 = float(input('Timp 2'))
timpul_3 = float(input('Timp 3'))
average_time = (timpul_1 + timpul_2 + timpul_3) / 3
print(f'Timpul mediu este: {average_time:.3f} secunde')
