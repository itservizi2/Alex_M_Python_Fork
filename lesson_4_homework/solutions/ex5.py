"""
Nota trecătoare la un test.
Presupunem că pentru a avea o notă trecătoare la un test,
elevii trebuie să obţină minim 15 puncte.
Scrieţi un program_exemplu care citeşte de la tastatură punctajul obţinut de un elev şi
afişează dacă elevul are o notă trecătoare sau va trebui să mai susţină încă o dată testul.
"""

nota_testului = int(input("Introduceți punctajul obținut: "))
nota_maxima = int(input('Puncte max'))
nota_min = int(input('Puncte min'))

if nota_testului >= nota_min:
    print("Felicitări! Aveți o notă trecătoare.")
elif nota_testului > nota_maxima:
    print('Eroare: Nu poate fi mai mult de 100p.')
else:
    print("Nu ați obținut nota trecătoare. Va trebui să susțineți testul din nou.")
