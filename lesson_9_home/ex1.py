"""
Creați două liste care vor reprezenta numele participanților la două evenimente.
 Transformați-le apoi în seturi.

Utilizați operațiile cu seturi și afișați rezultatele:

* câți participanți au fost prezenți la ambele evenimente
* câți participanți au fost prezenți doar la primul eveniment
* câți participanți au fost prezenți doar la al doilea eveniment
"""

participation_1 = ['Andrei', 'Ion', 'Marius', 'Cristna', 'Valeria', 'Lilia', 'Angela']
participation_2 = ['Cristian', 'Andrei', 'Valeria', 'Cezar', 'Mihai', 'Aureliu']

p_set_1 = set(participation_1)
p_set_2 = set(participation_2)

print(p_set_1.intersection(p_set_2))
print(p_set_1 - p_set_2)
print(p_set_2 - p_set_1)
