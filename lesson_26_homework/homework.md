# Homework

## IMPORTANT

If you want to upload your project to GitHub, please save the credentials (example the API Keys) in a separate file, and
don't upload that file to GitHub.

## Task

Find an API you are interested in, and create a simple, and small console application that will use the API to do
something.

If you don't have any ideas, you can do the exercises below.

## Ex1

Using The [Google translate API](https://rapidapi.com/googlecloud/api/google-translate1)

Create an application that will translate text.

Application should prompt the user for the target language from a list of options. (You decide what the options are)

Application should allow user to input any length text, or can provide a path to a file (textual file to translate)

Write the code as a library, this way you can have functions such as:

* get_all_languages
* translate(text, to_language)
* translate_file(path, to_language)

## Ex2: Optional

Use a combination of 2 WEB APIs, to create an application that will find the country and city using the
IP [Example](https://rapidapi.com/xakageminato/api/ip-geolocation-ipwhois-io/) and will show the weather
data [using this](https://rapidapi.com/community/api/open-weather-map).

The program should automatically detect the location and display the weather when started.

It should show:

* City, Country
* Temperature (celsius)
* Weather (example: Cloudy/Clear/Snowing/Raining)

# Temă pentru acasă

## IMPORTANT

Dacă doriți să încărcați proiectul pe GitHub, vă rugăm să salvați credențialele (de exemplu, cheile API) într-un fișier
separat și să nu încărcați acel fișier pe GitHub.

## Sarcină

Găsiți o API care vă interesează și creați o aplicație simplă și mică în consolă care va folosi API-ul pentru a face
ceva.

Dacă nu aveți idei, puteți efectua exercițiile de mai jos.

## Exercițiul 1

Utilizând [Google Translate API](https://rapidapi.com/googlecloud/api/google-translate1)

Creați o aplicație care va traduce textul.

Aplicația ar trebui să ceară utilizatorului limba țintă dintr-o listă de opțiuni. (Puteți decide ce opțiuni sunt
disponibile)

Aplicația ar trebui să permită utilizatorului să introducă orice text de lungime sau să furnizeze calea către un
fișier (fișier textual pentru traducere)

Scrieți codul ca o bibliotecă, astfel puteți avea funcții precum:

* get_all_languages
* translate(text, to_language)
* translate_file(path, to_language)

## Exercițiul 2: Opțional

Utilizați o combinație de 2 API-uri WEB, pentru a crea o aplicație care va găsi țara și orașul
folosind [IP-ul](https://rapidapi.com/xakageminato/api/ip-geolocation-ipwhois-io/) și va afișa datele
meteorologice [folosind acest API](https://rapidapi.com/community/api/open-weather-map).

Programul ar trebui să detecteze automat locația și să afișeze vremea la pornire.

Ar trebui să afișeze:

* Oraș, Țară
* Temperatura (grade Celsius)
* Vremea (exemplu: Înnorat/Cer senin/Ninsoare/Ploaie)