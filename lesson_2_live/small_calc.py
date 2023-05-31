# Nu putem face asa
# a = input(int())

a = int(input())
b = int(input())
result = a + b
print(str(a) + '+' + str(b) + '=' + str(result))
# Positional (DUpa pozitia argumentelor si placeholderului)
print("{}+{}={}".format(b, a, result))

# Dupa cuvant cheie
print("{b}+{a}={result}".format(b=b, a=a, result=result))

# F-string
print(f"{a}+{b}={result}")

s1 = "Hi"
s2 = "Bye"
print("{}{}{}".format(s1, s2, s1))

