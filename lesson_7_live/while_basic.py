"""Write a program that uses a for loop to calculate the sum of all numbers from 1 to 100.
   Example output: 5050"""

nr_sum = 0
for a in range(101):
    nr_sum += a
print(nr_sum)

a = 0
nr_sum = 0
while a <= 100:
    nr_sum += a
    a += 1

print(nr_sum)
