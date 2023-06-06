"""
Nota trecătoare la un test.
Presupunem că pentru a avea o notă trecătoare la un test,
elevii trebuie să obţină minim 15 puncte.
Scrieţi un program care citeşte de la tastatură punctajul obţinut de un elev şi
afişează dacă elevul are o notă trecătoare sau va trebui să mai susţină încă o dată testul.
"""
punctaj_minim = 15
punctaj_obtinut = int(input("introduceti punctaj obtinut : "))
este_trecator = bool(punctaj_obtinut >= punctaj_minim)
if este_trecator:
    print("Elevul a trecut testul ")
else:
    print("Elevul va trebui să mai susţină încă o dată testul ")

