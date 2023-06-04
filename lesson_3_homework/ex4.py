"""Scrieţi un program care citeşte de la tastatură de 3 ori timpul în care un sportiv aleargă proba de 100 metri (numărul de secunde).
Apoi afişaţi la ecran timpul mediu (media aritmetică a celor 3 încercări) în secunde."""

timp1 = float(input("introduceti nr de secunde : "))
timp2 = float(input("introduceti nr de secunde : "))
timp3 = float(input("introduceti nr de secunde : "))
timpul_mediu = (timp1 + timp2 + timp3) / 3
print(f"Timpul mediu = {timpul_mediu}")
