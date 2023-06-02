# Exercițiul 6: Minute în ore și minute
# Scrie un program care preia numărul de minute ca intrare și îl convertește în ore și minute. Afișează orele și minutele convertite.
minute = int(input("Introdu numărul de minute: "))

ore = minute // 60  #
minute_ramase = minute % 60  #

print(f"{minute} minute sunt echivalente cu {ore} ore și {minute_ramase} minute.")

ore = int(minute / 60)
minute_ramase = minute - ore * 60
print(ore, minute_ramase)
