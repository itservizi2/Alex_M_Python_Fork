# Scrie un program care preia numărul de secunde ca intrare și îl convertește în ore, minute și secunde.
# Afișează timpul convertit.

seconds = int(input(" Please input seconds value:"))

hours = seconds // 3600
minutes = seconds % 60
result = seconds % 60
print(f"Your time in hh:mm:ss is: {str(int(hours))}:{str(int(minutes))}:{result}")