# Homework

# EN

# Ex 1.1

Using your classes **Shape**, **Circle**, **Rectangle** and **Square**.

Implement the necessary methods to:

* Get the area of the shape (Circle, Rectangle, Square), as a property. Except for Shape (shape can't have an area)
* Be able to compare shapes (only shapes of the same type can be compared)
    * Only shapes of the same type can be compared:
        * I should be able to compare a Circle with another circle
        * I should not be able to compare a Circle with a Square
    * I should be able to compare a Square and a Rectangle, because they have the same properties.
    * When comparing Rectangles, compare the area of the rectangle (not the width and length)
* Be able to perform addition, subtraction and multiplication of shapes (for example _rectangle1 + rectangle2_)
    * When performing such operations, perform the operations on the common properties of the 2 objects (
      width/length/radius)
    * When performing subtraction, the value of properties of a shape should not be less than 0.
    * Only shapes with the same properties can have the operations performed (ex: Circle and Square can not be added,
      Square and Rectangles can). You can use the isinstance and issubclass checks to perform the checks.
    * When performing multiplication, also allow to multiply the object with a number.
        * Example: Rectangle(2,4) * 2 = Rectangle(4,8)

# Ex 1.2

Create a Shape service.

The methods inside shape service should all be staticmethods.

The Shape service should have the following properties as class properties:

DEFAULT_INNER_COLOR, DEFAULT_OUTER_COLOR - You can choose any string default values

The Shape service should have the following methods:

* create_default_circle(radius) - creates and returns a Circle object, with properties for colors form the defaults.
* create_default_rectangle(width, length) - creates and returns a Rectangle object, with properties for colors form the
  defaults.
* create_default_square(side_length) - creates and returns a Square object, with properties for colors from defaults.
* color_shapes(list_of_shapes, inner_color, border_color) - set's the colors of all the shapes in the list to the colors
  from the arguments.

# Ex 2.

If you take a look at the file [conversion_rates.json](conversion_rates.json) You will see a very long list of all
currencies and their conversion rate from and to MDL.

## Task

Create a program that is going to load this list into the program.

On program start-up, show the list of all possible conversions, with rates from lowest to highest.

Let the user input the name of the currency to convert to. Example: EUR or MDL

* If the input currency is MDL, then use the ask the user to input again what currency to convert to MDL. Example USD
    * Let the user input the value of MDL to convert to that currency.
    * Print the converted value with only 2 decimal points (example 92.43)
* If the input currency is not MDL, then:
    * Let the user input the value of MDL to convert to that currency.

## Conditions

* The entire program should be object-oriented (only use classes), except for the main.py which will run the program
* You should create CurrencyConversion object, that will store all information about each conversion.
    * Example. CurrencyConversion(from="MDL", to="EUR", rate=0.049175765442905, inverse_rate=20.335219818002, name="
      EUR")
* In order to have the ability to sort CurrencyConversion objects, implement `__lt__, __eq__`
  functions. These functions should compare the rates of the CurrencyConversion objects.
* Have a CurrencyConversionService that will manage all the currency conversion information, and should have at least
  this method below.
    * convert(from_currency, to_currency, amount)

## Considerations

The json contains a dict of dicts. It's not a list, so pay attention, and analyze the data you are working with before
you start.

# RO:

# Temă pentru acasă

# Ex 1.1

Folosind clasele **Shape**, **Circle**, **Rectangle** și **Square**.

Implementați metodele necesare pentru:

* Obțineți aria formei (Circle, Rectangle, Square), ca proprietate. Cu excepția formei de bază (Shape, care nu poate
  avea o arie).
* Să puteți compara forme (doar forme de același tip pot fi comparate)
    * Numai forme de același tip pot fi comparate:
        * Trebuie să pot compara un cerc cu un alt cerc.
        * Nu trebuie să pot compara un cerc cu un pătrat.
    * Trebuie să pot compara un pătrat și un dreptunghi, deoarece au aceleași proprietăți.
    * La compararea dreptunghiurilor, comparați aria dreptunghiului (nu lățimea și lungimea).
* Să puteți efectua operații de adunare, scădere și înmulțire a formelor (de exemplu, _rectangle1 + rectangle2_).
    * Când efectuați astfel de operații, efectuați operațiile pe proprietățile comune ale celor 2 obiecte (
      lățime/lungime/radius).
    * La efectuarea scăderii, valoarea proprietăților unei forme nu trebuie să fie mai mică decât 0.
    * Numai formele cu aceleași proprietăți pot avea operațiile efectuate (ex: Cerc și Pătrat nu pot fi adăugate,
      Pătrat și Dreptunghi pot fi adăugate). Puteți folosi verificări cu `isinstance` și `issubclass` pentru a efectua
      aceste verificări.
    * La efectuarea înmulțirii, permiteți și înmulțirea obiectului cu un număr.
        * Exemplu: Rectangle(2,4) * 2 = Rectangle(4,8)

# Ex 1.2

Creați un serviciu pentru forme (Shape service).

Metodele din serviciul pentru forme (Shape service) ar trebui să fie toate `staticmethods`.

Serviciul pentru forme (Shape service) ar trebui să aibă următoarele proprietăți ca proprietăți ale clasei:

DEFAULT_INNER_COLOR, DEFAULT_OUTER_COLOR - Puteți alege orice valori implicite de tip șir (string).

Serviciul pentru forme (Shape service) ar trebui să aibă următoarele metode:

* create_default_circle(radius) - creează și returnează un obiect de tip Cerc (Circle) cu proprietăți pentru culori
  preluate din valorile implicite.
* create_default_rectangle(width, length) - creează și returnează un obiect de tip Dreptunghi (Rectangle) cu proprietăți
  pentru culori preluate din valorile implicite.
* create_default_square(side_length) - creează și returnează un obiect de tip Pătrat (Square) cu proprietăți pentru
  culori preluate din valorile implicite.
* color_shapes(list_of_shapes, inner_color, border_color) - setează culorile tuturor formelor din lista de forme la
  culorile specificate ca argumente.

# Ex 2.

Dacă aruncați o privire în fișierul [conversion_rates.json](conversion_rates.json), veți vedea o listă foarte lungă cu
toate monedele și rata de conversie a acestora din și în MDL.

## Sarcină

Creați un program care va încărca această listă în program.

La pornirea programului, afișați lista tuturor conversiilor posibile, cu ratele de la cea mai mică la cea mai mare.

Permiteți utilizatorului să introducă numele monedei către care să se facă conversia. Exemplu: EUR sau MDL.

* Dacă moneda introdusă este MDL, atunci cereți utilizatorului să introducă din nou moneda către care să se facă
  conversia din MDL. Exemplu: USD
    * Permiteți utilizatorului să introducă valoarea MDL pentru a o converti în moneda respectivă.
    * Afișați valoarea convertită cu doar 2 zecimale (de exemplu, 92.43)
* Dacă moneda introdusă nu este MDL, atunci:
    * Permiteți utilizatorului să introducă valoarea MDL pentru a o converti în moneda respectivă.

## Condiții

* Întregul program ar trebui să fie orientat pe obiecte (să utilizeze doar clase), cu excepția fișierului main.py care
  va rula programul.
* Ar trebui să creați un obiect `CurrencyConversion`, care va stoca toate informațiile despre fiecare conversie.
    * Exemplu. CurrencyConversion(from="MDL", to="EUR", rate=0.049175765442905, inverse_rate=20.335219818002, name="
      EUR")
* Pentru a avea posibilitatea de a sorta obiectele `CurrencyConversion`, implementați funcțiile `__lt__, __eq__`.
  Aceste funcții ar trebui să compare ratele obiectelor `CurrencyConversion`.
* Aveți un serviciu `CurrencyConversionService` care va gestiona toate informațiile despre conversiile de valută și ar
  trebui să aibă cel puțin următoarea metodă.
    * `convert(from_currency, to_currency, amount)`

## Considerații

Json-ul conține un dicționar de dicționare. Nu este o listă, așa că acordați atenție și analizați datele cu care lucrați
înainte de a începe.