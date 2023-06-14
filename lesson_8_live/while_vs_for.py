for a in range(0, 10):
    print(a)

end = 10
start = 0
while start < end:
    print(start)
    start += 1

# Bad practice example

my_list = [1, 2, 3]
for a in my_list:
    print(a)
    my_list.append(a + 1)
