## Ex 1

## Ro:

1. De la consola se va introduce o bucata de text.
2. Calculati de cate ori fiecare cuvant a fost folosit.
3. Afisati informatia.

## Eng:

1. Ask the user to input a large text with many words. Ignoring punctuation.
2. Calculate how many times each word (regardless the case) was used.

Hints:
Use `str.split(' ')` to break down the text into a list

````
Example:
Input:
how much wood would a woodchuck chuck if a woodchuck could chuck wood
Output: 
Word "how" was used 1 times.
Word "much" was used 1 times.
Word "wood" was used 2 times.
Word "would" was used 1 times.
Word "a" was used 2 times.
Word "woodchuck" was used 2 times.
Word "chuck" was used 2 times.
Word "if" was used 1 times.
Word "could" was used 1 times.
````

## Ex 2

## RO:

Creaza un program care va inregistra o lista de oaspeti si comenzile lor la un restaurant.

Utilizatorul va introduce la consola cati oaspeti vor fi inregistrati.

Pentru fiecare oaspete, utilizatorul va introduce Numele Oaspetelui si 2 feluri de mancare.

La sfarsit, programul va trebui sa afiseze lista cu oaspeti, ce au comandat, si cat in total va trebui restaurantul sa
pregateasca.

**Folositi dict**

## ENG:

Create a program that will register a list of guests and food for a restaurant.

The user has to input how many guests will be coming

To register each guest, the user will input the name of the guest and two (2) dishes.

At the end, print out the list of the guests and what they ordered. And the total number of each dish the restaurant
will have to prepare.

**Use dict**

## Example:

```
Input:
3

Marius
Ravioli
Caesar Salad

Ana
Pepper steak
Caesar Salad

Gheorghe
Greek salad
Lentil Soup

Output:
The guests will be: [Marius, Ana, Gheorghe]

Marius ordered Ravioli and Caesar Salad 
Ana ordered Pepper steak and Caesar Salad 
Gheorghe ordered Greek salad and Lentil Soup
 
You will have to prepare:
Ravioli x 1
Caesar Salad x 2
Pepper steak x 1
Greek salad x 1
Lentil Soup x 1
```

## Ex 3

### EN

Given two dictionaries representing students' grades:

```python
math_grades = {"John": 85, "Emily": 92, "Michael": 78, "Jessica": 95}
science_grades = {"John": 90, "Emily": 88, "Michael": 92, "Jessica": 87}
```

Write a program that prints out a new dictionary
containing the average grades for each student.

### RO

Dat fiind două dicționare care reprezintă notele elevilor:

```python
math_grades = {"John": 85, "Emily": 92, "Michael": 78, "Jessica": 95}
science_grades = {"John": 90, "Emily": 88, "Michael": 92, "Jessica": 87}
```

Scrieți un program care care calculeaza media notelor la fiecare elev din ambele dictionare si le stocheaza intr-un
dictionar nou.