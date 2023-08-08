import requests
from config import TRANSLATE_API

source_lang = input("Enter the source language (e.g. 'english', 'romanian', 'italian'): ")

target_lang = input("Enter the target language (e.g. 'english', 'romanian', 'italian'): ")

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

input_option = input("Enter 'text' to input the text in the console, or 'file' to enter a file path: ")

if input_option.lower() == 'text':

    text_to_translate = input("Enter the text you want to translate: ")
else:

    file_path = input("Enter the file path: ")
    with open(file_path, 'r', encoding='utf-8') as file:
        text_to_translate = file.read()

payload = {
    "q": text_to_translate,
    "source": source_lang.lower()[0:2],
    "target": target_lang.lower()[0:2]
}

headers = {
    "content-type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "application/gzip",
    "X-RapidAPI-Key": TRANSLATE_API,
    "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json()['data']['translations'][0]['translatedText'])
