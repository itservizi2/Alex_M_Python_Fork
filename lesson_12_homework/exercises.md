Exercise 1: Temperature Conversion

Write a Python function called `convert_temperature` that converts temperature values between Celsius and Fahrenheit.
The function should take two arguments: `temperature` (float) and `unit` (string) indicating the current temperature
unit ("C" for Celsius or "F" for Fahrenheit). The function should return the converted temperature value.

Hint: To convert Celsius to Fahrenheit, use the formula: `F = (C * 9/5) + 32`. To convert Fahrenheit to Celsius, use the
formula: `C = (F - 32) * 5/9`.

Write a program that uses the `convert_temperature` function to do the following:

1. Prompt the user to enter a temperature value.
2. Prompt the user to enter the current temperature unit ("C" or "F").
3. Call the `convert_temperature` function with the provided inputs.
4. Print the converted temperature value with the corresponding unit.

Example Output:

```
Enter the temperature: 25
Enter the current unit (C/F): C
Converted temperature: 77.0 F

Enter the temperature: 98.6
Enter the current unit (C/F): F
Converted temperature: 37.0 C
```

Exercise 2: Fibonacci Sequence

Write a Python function called `generate_fibonacci` that generates the Fibonacci sequence up to a given number of terms.
The function should take one argument: `terms` (integer) indicating the number of Fibonacci terms to generate. The
function should return a list containing the Fibonacci sequence.

Hint: The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding numbers.

Write a program that uses the `generate_fibonacci` function to do the following:

1. Prompt the user to enter the number of Fibonacci terms to generate.
2. Call the `generate_fibonacci` function with the provided input.
3. Print the generated Fibonacci sequence.

Example Output:

```
Enter the number of Fibonacci terms to generate: 8
Generated Fibonacci sequence: [0, 1, 1, 2, 3, 5, 8, 13]

Enter the number of Fibonacci terms to generate: 5
Generated Fibonacci sequence: [0, 1, 1, 2, 3]
```

Exercise 3: Password Strength Checker

Write a Python function called `check_password_strength` that checks the strength of a given password. The function
should take one argument: `password` (string) representing the password to be checked. The function should return a
boolean value indicating whether the password meets the specified strength criteria.

The password strength criteria are as follows:

- At least 8 characters long
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit
- Contains at least one special character (e.g., !@#$%^&*)

Write a program that uses the `check_password_strength` function to do the following:

1. Prompt the user to enter a password.
2. Call the `check_password_strength` function with the provided input.
3. Print whether the password meets the strength criteria or not.

Example Output:

```
Enter a password: MyPass123
Password strength: True (meets the criteria)

Enter a password: abcdefg
Password strength: False (does not meet the criteria)
```

Note: You can enhance the password strength checker by adding additional criteria or customizing the requirements
according to your preference.

Exercise 4: Prime Number Checker

Write a Python function called `is_prime` that checks whether a given number is prime or not. The function should take
one argument: `number` (integer) representing the number to be checked. The function should return a boolean value
indicating whether the number is prime.

Hint: A prime number is a number greater than 1 that has no divisors other than 1 and itself.

Write a program that uses the `is_prime` function to do the following:

1. Prompt the user to enter a number.
2. Call the `is_prime` function with the provided input.
3. Print whether the number is prime or not.

Example Output:

```
Enter a number: 17
Prime number: True

Enter a number: 8
Prime number: False
```

Exercise 5: Email Validator

Write a Python function called `is_valid_email` that validates the format of a given email address. The function should
take one argument: `email` (string) representing the email address to be validated. The function should return a boolean
value indicating whether the email address is valid.

The email address validation criteria are as follows:

- Contains a single "@" symbol.
- Contains at least one dot (.) after the "@" symbol.
- The domain name (after the last dot) has at least two characters.

Write a program that uses the `is_valid_email` function to do the following:

1. Prompt the user to enter an email address.
2. Call the `is_valid_email` function with the provided input.
3. Print whether the email address is valid or not.

Example Output:

```
Enter an email address: john@example.com
Valid email address: True

Enter an email address: johndoe@example
Valid email address: False
```

Exercise 6: Palindrome Checker

Write a Python function called `is_palindrome` that checks whether a given string is a palindrome. The function should
take one argument: `text` (string) representing the text to be checked. The function should return a boolean value
indicating whether the text is a palindrome.

Hint: A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward,
disregarding spaces, punctuation, and capitalization.

Write a program that uses the `is_palindrome` function to do the following:

1. Prompt the user to enter a text.
2. Call the `is_palindrome` function with the provided input.
3. Print whether the text is a palindrome or not.

Example Output:

```
Enter a text: radar
Palindrome: True

Enter a text: Hello
Palindrome: False
```

Note: The palindrome checker can be customized to ignore or consider spaces, punctuation, or capitalization based on
your preference.

## RO:

Exercițiul 1: Conversie de Temperatură

Scrieți o funcție Python numită `convert_temperature` care convertește valorile temperaturii între Celsius și
Fahrenheit.
Funcția ar trebui să primească două argumente: `temperature` (float) și `unit` (șir de caractere) care indică unitatea
actuală a temperaturii
("C" pentru Celsius sau "F" pentru Fahrenheit). Funcția ar trebui să returneze valoarea temperaturii convertite.

Sugestie: Pentru a converti Celsius în Fahrenheit, utilizați formula: `F = (C * 9/5) + 32`. Pentru a converti Fahrenheit
în Celsius, utilizați
formula: `C = (F - 32) * 5/9`.

Scrieți un program care utilizează funcția `convert_temperature` pentru a face următoarele:

1. Solicitați utilizatorului să introducă o valoare a temperaturii.
2. Solicitați utilizatorului să introducă unitatea actuală a temperaturii ("C" sau "F").
3. Apelați funcția `convert_temperature` cu valorile introduse.
4. Afișați valoarea temperaturii convertite împreună cu unitatea corespunzătoare.

Exemplu de rezultat:

```
Introduceți temperatura: 25
Introduceți unitatea curentă (C/F): C
Temperatura convertită: 77.0 F

Introduceți temperatura: 98.6
Introduceți unitatea curentă (C/F): F
Temperatura convertită: 37.0 C
```

Exercițiul 2: Secvența Fibonacci

Scrieți o funcție Python numită `generate_fibonacci` care generează secvența Fibonacci până la un număr dat de termeni.
Funcția ar trebui să primească un singur argument: `terms` (integer) care indică numărul de termeni Fibonacci de
generat.
Funcția ar trebui să returneze o listă care conține secvența Fibonacci.

Sugestie: Secvența Fibonacci începe cu 0 și 1, iar fiecare număr ulterior este suma celor două numere precedente.

Scrieți un program care utilizează funcția `generate_fibonacci` pentru a face următoarele:

1. Solicitați utilizatorului să introducă numărul de termeni Fibonacci de generat.
2. Apelați funcția `generate_fibonacci` cu valoarea introdusă.
3. Afișați secvența Fibonacci generată.

Exemplu de rezultat:

```
Introduceți numărul de termeni Fibonacci de generat: 8
Secvența Fibonacci generată: [0, 1, 1, 2, 3, 5, 8, 13]

Introduceți numărul de termeni Fibonacci de generat: 5
Secvența Fibonacci generată: [0, 1, 1, 2, 3]
```

Exercițiul 3: Verificator de Putere a Parolei

Scrieți o funcție

Python numită `check_password_strength` care verifică puterea unei parole date. Funcția ar trebui să primească
un singur argument: `password` (șir de caractere) care reprezintă parola de verificat. Funcția ar trebui să returneze o
valoare booleană
care indică dacă parola respectă criteriile de putere specificate.

Criteriile de putere ale parolei sunt următoarele:

- Cel puțin 8 caractere lungime
- Conține cel puțin o literă majusculă
- Conține cel puțin o literă minusculă
- Conține cel puțin o cifră
- Conține cel puțin un caracter special (de exemplu, !@#$%^&*)

Scrieți un program care utilizează funcția `check_password_strength` pentru a face următoarele:

1. Solicitați utilizatorului să introducă o parolă.
2. Apelați funcția `check_password_strength` cu valoarea introdusă.
3. Afișați dacă parola respectă criteriile de putere sau nu.

Exemplu de rezultat:

```
Introduceți o parolă: MyPass123
Puterea parolei: True (respectă criteriile)

Introduceți o parolă: abcdefg
Puterea parolei: False (nu respectă criteriile)
```

Notă: Puteți îmbunătăți verificatorul de putere a parolei prin adăugarea de criterii suplimentare sau personalizarea
cerințelor
în funcție de preferințele dvs.

Exercițiul 4: Verificator de Număr Prim

Scrieți o funcție Python numită `is_prime` care verifică dacă un număr dat este prim sau nu. Funcția ar trebui să
primească
un singur argument: `number` (integer) care reprezintă numărul de verificat. Funcția ar trebui să returneze o valoare
booleană
care indică dacă numărul este prim.

Sugestie: Un număr prim este un număr mai mare decât 1 și care nu are divizori în afară de 1 și el însuși.

Scrieți un program care utilizează funcția `is_prime` pentru a face următoarele:

1. Solicitați utilizatorului să introducă un număr.
2. Apelați funcția `is_prime` cu valoarea introdusă.
3. Afișați dacă numărul este prim sau nu.

Exemplu de rezultat:

```
Introduceți un număr: 17
Număr prim: True

Introduceți un număr: 8
Număr prim: False
```

Exercițiul 5: Validare Adresă de Email

Scrieți o funcție Python numită `is_valid_email` care validează formatul unei adrese de email date. Funcția ar trebui să
primească
un singur argument: `email` (șir de caractere) care reprezintă adresa de email de validat. Funcția ar tre

bui să returneze o valoare booleană
care indică dacă adresa de email este validă.

Criteriile de validare ale adresei de email sunt următoarele:

- Conține un singur simbol "@".
- Conține cel puțin un punct (.) după simbolul "@".
- Domeniul (după ultimul punct) are cel puțin două caractere.

Scrieți un program care utilizează funcția `is_valid_email` pentru a face următoarele:

1. Solicitați utilizatorului să introducă o adresă de email.
2. Apelați funcția `is_valid_email` cu valoarea introdusă.
3. Afișați dacă adresa de email este validă sau nu.

Exemplu de rezultat:

```
Introduceți o adresă de email: john@example.com
Adresă de email validă: True

Introduceți o adresă de email: johndoe@example
Adresă de email validă: False
```

Exercițiul 6: Verificator de Palindrom

Scrieți o funcție Python numită `is_palindrome` care verifică dacă un șir de caractere dat este un palindrom. Funcția ar
trebui să primească
un singur argument: `text` (șir de caractere) care reprezintă textul de verificat. Funcția ar trebui să returneze o
valoare booleană
care indică dacă textul este un palindrom.

Sugestie: Un palindrom este un cuvânt, o frază, un număr sau o altă secvență de caractere care se citește la fel înainte
și înapoi,
fără a ține cont de spații, semne de punctuație și capitalizare.

Scrieți un program care utilizează funcția `is_palindrome` pentru a face următoarele:

1. Solicitați utilizatorului să introducă un text.
2. Apelați funcția `is_palindrome` cu valoarea introdusă.
3. Afișați dacă textul este un palindrom sau nu.

Exemplu de rezultat:

```
Introduceți un text: radar
Palindrom: True

Introduceți un text: Hello
Palindrom: False
```

Notă: Verificatorul de palindrom poate fi personalizat pentru a ignora sau considera spații, semne de punctuație sau
capitalizare
în funcție de preferințele dvs.