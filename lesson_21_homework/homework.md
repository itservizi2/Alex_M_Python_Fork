# Homework - EN

## Testing the exercises.

To test your classes, create test functions that will execute all the methods that you have added to your classes.

Each of your classes should be defined in separate files, that have the same name as the name of the Class.

Example class Human should be in Human.py file.

## Ex 1

Create a class that describes a human.

Human object should have the following properties:

* First Name - string
* Last Name - string
* Date of Birth - datetime.date

All the properties above should be initialized in the constructor function, by arguments to the constructor.

And the following methods:

* A method to get the full name of the human
* A method to get the age of the human

When printing the human object the console should output something like example below:

`Marius Tricolici, age 24`

## Ex 2

Create a class that describes a pet.

A pet should have the following properties:

* A name - string
* A type (cat/dog/bird) - string
* A favourite food - string

All the properties above should be initialized in the constructor function, by arguments to the constructor.

When a pet object is printed it should output something like this:

`Cat called Garfield that loves lasagna`
or
`Dog called Kuzea that loves bones`

Also create a new class HumanWithPet:

The HumanWithPet should have the same properties as the Human in [Ex 1](#ex-1).

Additionally, the HumanWithPet class should have a list of pets as a property.

Add two methods to the HumanWithPet class:

* Adopt new pet - Adds a new pet object to the list of pets
* Give away pet - Removes a pet from the humans list of pets

When printing a HumanWithPet object, the console should output the according to the following examples:

`Marius Tricolici, age 24 with a pet: Cat called Garfield that loves lasagna` - If the human has 1 pets.

`Marius Tricolici, age 24 with 2 pets: Cat called Garfield that loves lasagna, Dog called Kuzea that loves bones` - If
the human has 2 or more pets.

### Want more ? Let me know :)

# RO

# Tema

## Testarea exercițiilor.

Pentru a testa clasele, creați funcții de testare care vor executa toate metodele pe care le-ați adăugat la clase.

Fiecare dintre clasele voastre ar trebui să fie definite în fișiere separate, care au același nume cu numele clasei.

De exemplu, clasa Human ar trebui să fie în fișierul Human.py.

## Ex 1

Creați o clasă care descrie un om.

Obiectul Human ar trebui să aibă următoarele proprietăți:

* Nume - șir
* Prenume - șir
* Data nașterii - datetime.date

Toate proprietățile de mai sus ar trebui să fie inițializate în funcția constructor, prin argumente pentru constructor.

Și următoarele metode:

* O metodă pentru a obține numele complet al omului
* O metodă pentru a obține vârsta omului

La tipărirea obiectului Human, consola ar trebui să afișeze ceva similar cu exemplul de mai jos:

`Marius Tricolici, vârsta 24`

## Ex 2

Creați o clasă care descrie un animal de companie.

Un animal de companie ar trebui să aibă următoarele proprietăți:

* Nume - șir
* Tip (pisică/câine/păsăre) - șir
* Mâncarea preferată - șir

Toate proprietățile de mai sus ar trebui să fie inițializate în funcția constructor, prin argumente pentru constructor.

Când un obiect pet este tipărit, ar trebui să afișeze ceva similar cu acesta:

`Pisică numită Garfield, care iubește lasagna`
sau
`Câine numit Kuzea, care iubește oasele`

Creați, de asemenea, o nouă clasă HumanWithPet:

Clasa HumanWithPet ar trebui să aibă aceleași proprietăți ca și clasa Human din [Ex 1](#ex-1).

În plus, clasa HumanWithPet ar trebui să aibă o listă de animale de companie ca proprietate.

Adăugați două metode la clasa HumanWithPet:

* Adoptă un nou animal de companie - Adaugă un nou obiect animal de companie la lista de animale de companie
* Dă un animal de companie - Elimină un animal de companie din lista de animale a omului

La tipărirea unui obiect HumanWithPet, consola ar trebui să afișeze conform exemplului de mai jos:

`Marius Tricolici, vârsta 24, cu un animal de companie: Pisică numită Garfield, care iubește lasagna` - Dacă omul are 1
animal de companie.

`Marius Tricolici, vârsta 24, cu 2 animale de companie: Pisică numită Garfield, care iubește lasagna, Câine numit Kuzea, care iubește oasele` -
Dacă omul are 2 sau mai multe animale de companie.

### Vrei mai multe? Spune-mi :)