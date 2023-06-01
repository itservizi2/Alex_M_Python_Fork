## Exercițiul 7: Calculatorul de dobândă simplă
# Scrie un program care preia suma principală, rata dobânzii și timpul (în ani) ca intrare.
# Calculează și afișează dobânda simplă folosind formula: dobândă = (suma principală * rată dobândă * timp) / 100.

credit_acordat = float(input("insert suma credit acordat: "))
rata_dobinda = float(input("insert the rate of interest : "))
perioada = int(input("insert nr of years : "))
dobinda_spre_rambursare = (credit_acordat * rata_dobinda * perioada) / 100
print("dobinda spre rambursare este ", dobinda_spre_rambursare)
