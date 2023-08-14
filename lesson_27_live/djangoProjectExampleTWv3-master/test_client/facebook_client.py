import requests

url = 'http://127.0.0.1:8000/'

register_url = url + '/facebook/register/'

response = requests.post(
    register_url,
    data={
        'username': 'mtricolici',
        'password': 'python'
    }
)

print(response.status_code)
