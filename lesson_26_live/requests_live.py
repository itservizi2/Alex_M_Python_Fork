import requests

data = requests.get('http://google.com/search', params={
    'q': 'poke'
})

print(data)

content = data.content

with open('google.html', 'w') as file:
    file.write(content.decode('ISO-8859-1'))
