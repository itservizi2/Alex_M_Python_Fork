nr = 25

prime = True

for a in range(2, nr // 2 + 1):
    print("checking", a)
    if nr % a == 0:
        prime = False

print(prime)
