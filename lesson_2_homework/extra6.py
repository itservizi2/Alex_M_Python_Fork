## Exercițiul 6: Minute în ore și minute
#Scrie un program care preia numărul de minute ca intrare și îl convertește în ore și minute. Afișează orele și minutele convertite.

minute_in_total = int(input("insert nr of minutes : "))
ore = minute_in_total // 60
minute = minute_in_total % 60

print(str(minute_in_total) + " minute = " + str(ore) + " ore " + str(minute) + " minute ")

print(f"{minute_in_total} minute sunt echivalente cu {ore} ore și {minute} minute.")
