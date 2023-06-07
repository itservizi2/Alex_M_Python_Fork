a = 'abc'
b = 'bc'

print(b in a)
# Asta noi nu folosim ca are __ (double underscore)
print(a.__contains__(b))
print(a.count(b) >= 1)

a = 'a'
b = 'a'

print(a in b)
