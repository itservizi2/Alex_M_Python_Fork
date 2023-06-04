"""Utilizatorul va introduce un șir de caractere in consola.
* Calculați și afișați numarul total de litere în șirului de caractere
* Calculați și afișați numarul de vocale în șirul de caractere
* Calculați și afișați numarul de consoane în șirul de caractere

Note: Indiferent daca e majuscula sau minusucula litera

"""
sir = input("insert the string : ")
lungime = len(sir)
print(f"numarul total de caractere în sir este {lungime}")

#metoda 1 vocale
vocale = "aeiou"
enumar_vocale = {vocala_oarecare: sir.count(vocala_oarecare) for vocala_oarecare in vocale}
numar_total_vocale = sum(enumar_vocale.values())
print(f"numarul total de vocale în șirul de caractere este {numar_total_vocale}")

#metoda 2 vocale
vocale = "aeiou"
numar_vocale_total = sum(caracter.lower() in vocale for caracter in sir)
print(f"numarul total de vocale în șirul de caractere este {numar_vocale_total}")

vocale_distincte = set(caracter.lower() for caracter in sir if caracter.lower() in vocale)
numar_vocale_distincte = len(vocale_distincte)
print(f"Numărul de vocale distincte în șirul de caractere este: {numar_vocale_distincte}")

#metoda 1 consoane
consoane = "bcdfghjklmnpqrtvwxyz"
enumar_consoane = {consoana_oarecare: sir.count(consoana_oarecare) for consoana_oarecare in consoane}
numar_total_consoane = sum(enumar_consoane.values())
print(f"Numărul total de consoane  în șirul de caractere este {numar_total_consoane}")

#metoda 2 consoane
consoane = "bcdfghjklmnpqrtvwxyz"
numar_consoane_total = sum(caracter.lower() in consoane for caracter in sir)
print(f"numarul total de consoane în șirul de caractere este {numar_consoane_total}")

consoane_distincte = set(caracter.lower() for caracter in sir if caracter.lower() in consoane)
numar_consoane_distincte = len(consoane_distincte)
print(f"Numărul de consoane distincte în șirul de caractere este: {numar_consoane_distincte}")
