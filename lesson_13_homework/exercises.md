# EN

1. Write a function that takes a list as input and returns the sum of its elements. Handle the TypeError if the input is
   not a list.

Task:

- Define a function that accepts one parameter.
- Check if the parameter is of type list using an if statement.
- If the parameter is a list, calculate the sum of its elements using the `sum()` function and return the result.
- If the parameter is not a list, raise a `TypeError` with an appropriate error message.

2. Create a function that takes a string as input and checks if it is a palindrome. Handle the ValueError if an empty
   string is provided.

Task:

- Define a function that accepts one parameter.
- Check if the input string is empty using an if statement.
- If the string is empty, raise a `ValueError` with an appropriate error message.
- If the string is not empty, compare it to its reverse and return `True` if they are equal (a palindrome) or `False` if
  they are not.

3. Write a program that prompts the user to enter two numbers and calculates their division. Handle the
   ZeroDivisionError if the second number is zero.

Task:

- Prompt the user to enter the first number and store it in a variable.
- Prompt the user to enter the second number and store it in another variable.
- Convert both inputs to floating-point numbers using the `float()` function.
- Divide the first number by the second number and store the result in a variable.
- Use a try-except block to handle the `ZeroDivisionError` and print an appropriate error message if the second number
  is zero.
- If the division is successful, print the result.

4. Create a function that calculates the factorial of a given positive integer. Handle the ValueError if a non-integer
   or negative number is provided.

Task:

- Define a function that accepts one parameter.
- Check if the parameter is an integer greater than or equal to zero using an if statement.
- If the parameter is not an integer or is negative, raise a `ValueError` with an appropriate error message.
- If the parameter is a valid positive integer, calculate its factorial using a loop.
- Return the factorial as the result.

5. Write a program that asks the user to enter their age and handles the AgeError if the age is less than 0 or greater
   than 150. Define a custom exception class called AgeError for this purpose.

Task:

- Define a custom exception class called `AgeError` that inherits from the base `Exception` class.
- Define a function that prompts the user to enter their age and returns the age as an integer.
- Use a try-except block to handle potential exceptions.
- Within the try block, convert the user's input to an integer and store it in a variable.
- Use an if statement to check if the age is less than 0 or greater than 150.
- If the age is invalid, raise an `AgeError` with an appropriate error message.
- If the age is valid, return it.

6. Create a function that takes a list of numbers as input and calculates their geometric mean. Handle the
   ZeroDivisionError if the list contains a zero.

Task:

- Define a function that accepts one parameter (a list).
- Check if the list contains zero using an if statement.
- If the list contains zero, raise a `ZeroDivisionError` with an appropriate error message.
- If the list does not contain zero, calculate the product of all the numbers in the list using a loop.
- Use the `math.pow()` function to calculate the geometric mean by raising the product to the power of 1 divided by the
  length of the list.
- Return the

geometric mean as the result.

# RO

1. Scrie o funcție care primește o listă ca intrare și returnează suma elementelor sale. Gestionează eroarea de tip
   TypeError dacă intrarea nu este o listă.

Task:

- Definește o funcție care acceptă un singur parametru.
- Verifică dacă parametrul este de tip listă folosind o instrucțiune if.
- Dacă parametrul este o listă, calculează suma elementelor sale folosind funcția `sum()` și returnează rezultatul.
- Dacă parametrul nu este o listă, generează o eroare de tip `TypeError` cu un mesaj de eroare adecvat.

2. Creează o funcție care primește o șir de caractere ca intrare și verifică dacă este un palindrom. Gestionează eroarea
   de tip ValueError dacă se furnizează un șir de caractere gol.

Task:

- Definește o funcție care acceptă un singur parametru.
- Verifică dacă șirul de caractere de intrare este gol folosind o instrucțiune if.
- Dacă șirul este gol, generează o eroare de tip `ValueError` cu un mesaj de eroare adecvat.
- Dacă șirul nu este gol, compară-l cu oglinditul său și returnează `True` dacă sunt egale (un palindrom) sau `False` în
  caz contrar.

3. Scrie un program care cere utilizatorului să introducă două numere și calculează împărțirea lor. Gestionează eroarea
   de tip ZeroDivisionError dacă al doilea număr este zero.

Task:

- Cere utilizatorului să introducă primul număr și stochează-l într-o variabilă.
- Cere utilizatorului să introducă al doilea număr și stochează-l într-o altă variabilă.
- Convertiți ambele intrări în numere cu zecimale folosind funcția `float()`.
- Împarte primul număr la al doilea număr și stochează rezultatul într-o variabilă.
- Folosește un bloc try-except pentru a gestiona eroarea `ZeroDivisionError` și afișează un mesaj de eroare adecvat dacă
  al doilea număr este zero.
- Dacă împărțirea este reușită, afișează rezultatul.

4. Creează o funcție care calculează factorialul unui număr întreg pozitiv dat. Gestionează eroarea de tip ValueError
   dacă este furnizat un număr care nu este întreg sau este negativ.

Task:

- Definește o funcție care acceptă un singur parametru.
- Verifică dacă parametrul este un număr întreg mai mare sau egal cu zero folosind o instrucțiune if.
- Dacă parametrul nu este un număr întreg sau este negativ, generează o eroare de tip `ValueError` cu un mesaj de eroare
  adecvat.
- Dacă parametrul este un număr întreg pozitiv valid, calculează factorialul acestuia folosind o buclă.
-

Returnează factorialul ca rezultat.

5. Scrie un program care cere utilizatorului să introducă vârsta lor și gestionează eroarea AgeError dacă vârsta este
   mai mică de 0 sau mai mare de 150. Defineste o clasă de excepție personalizată numită AgeError în acest scop.

Task:

- Defineste o clasă de excepție personalizată numită `AgeError` care moștenește clasa de bază `Exception`.
- Defineste o funcție care cere utilizatorului să introducă vârsta lor și returnează vârsta ca număr întreg.
- Folosește un bloc try-except pentru a gestiona excepțiile potențiale.
- În blocul try, converteste intrarea utilizatorului la un număr întreg și stochează rezultatul într-o variabilă.
- Folosește o instrucțiune if pentru a verifica dacă vârsta este mai mică de 0 sau mai mare de 150.
- Dacă vârsta este invalidă, generează o eroare `AgeError` cu un mesaj de eroare adecvat.
- Dacă vârsta este validă, returnează-o.

6. Creează o funcție care primește o listă de numere ca intrare și calculează media geometrică a acestora. Gestionează
   eroarea de tip ZeroDivisionError dacă lista conține un zero.

Task:

- Definește o funcție care acceptă un singur parametru (o listă).
- Verifică dacă lista conține zero folosind o instrucțiune if.
- Dacă lista conține zero, generează o eroare `ZeroDivisionError` cu un mesaj de eroare adecvat.
- Dacă lista nu conține zero, calculează produsul tuturor numerelor din listă folosind o buclă.
- Folosește funcția `math.pow()` pentru a calcula media geometrică prin ridicarea produsului la puterea 1 împărțită la
  lungimea listei.
- Returnează media geometrică ca rezultat.
