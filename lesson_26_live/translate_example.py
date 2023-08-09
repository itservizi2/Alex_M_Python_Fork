import requests


def get_translated_text(text_to_translate, to_language='ro'):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    payload = {
        "q": text_to_translate,
        "target": to_language,
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "9fc02c456bmsh6626cffb86bc4a3p13dc03jsn476488b50c4e",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }
    response = requests.post(url, data=payload, headers=headers)
    data = response.json()
    return data['data']['translations'][0]['translatedText']


if __name__ == '__main__':
    while True:
        inpt = input('Text to translate to romanian :')
        if inpt == 'END':
            break
        print(get_translated_text(inpt))
