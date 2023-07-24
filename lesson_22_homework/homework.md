# Homework

# Ex 1

Create the classes listed below. Use Inheritance.

For all the properties, use underscores inside the class to hide the properties (example self._inner_color), and declare
get and set methods (example set_inner_color).

Create a Class that describes a **Shape**

The shape class should have the following properties:

* inner color
* border color

Create another class **Circle** which extends **Shape**.

The circle class should have the following additional properties.

* radius

Create another class **Rectangle** which also extends **Shape**

The rectangle class should have the following additional properties.

* width
* length

Create another class **Square** that extends **Rectangle**

The Square class should make sure that the width and length are equal when one of them is set. For example if I set
square.set_length(4), square.get_width() should also be 4.

# Ex 2

Make a new class **NumbersList** that extends the `list` class.

The **NumbersList** class should only allow for numeric values (int and float) to be added to the list.

This means you have to overwrite the `__init__, append, extend` functions.

Add additional methods as described below:

* get_sum() - returns the sum of all the values
* get_average() - returns the average value of all numbers in the list




# Tema

# Exercițiul 1

Creați clasele enumerate mai jos. Utilizați moștenirea.

Pentru toate proprietățile, utilizați sublinieri în interiorul clasei pentru a ascunde proprietățile (exemplu self._inner_color) și declarați metode get și set (exemplu set_inner_color).

Creați o clasă care descrie o **Formă (Shape)**

Clasa Formă ar trebui să aibă următoarele proprietăți:

* culoarea interioară (inner color)
* culoarea marginii (border color)

Creați o altă clasă **Cerc (Circle)** care extinde clasa **Formă (Shape)**.

Clasa cerc ar trebui să aibă următoarele proprietăți suplimentare:

* rază (radius)

Creați o altă clasă **Dreptunghi (Rectangle)** care, de asemenea, extinde clasa **Formă (Shape)**

Clasa dreptunghi ar trebui să aibă următoarele proprietăți suplimentare:

* lățime (width)
* lungime (length)

Creați o altă clasă **Pătrat (Square)** care extinde clasa **Dreptunghi (Rectangle)**

Clasa Pătrat ar trebui să se asigure că lățimea și lungimea sunt egale atunci când una dintre ele este setată. De exemplu, dacă setez square.set_length(4), square.get_width() ar trebui să fie și el 4.

# Exercițiul 2

Creați o nouă clasă **ListăNumere (NumbersList)** care extinde clasa `list`.

Clasa **ListăNumere (NumbersList)** ar trebui să permită doar valori numerice (int și float) să fie adăugate în listă.

Acest lucru înseamnă că va trebui să suprascrieți funcțiile `__init__, append, extend`.

Adăugați metode suplimentare după cum este descris mai jos:

* get_sum() - returnează suma tuturor valorilor
* get_average() - returnează valoarea medie a tuturor numerelor din listă