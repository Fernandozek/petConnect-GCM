import requests

response = requests.post('http://127.0.0.1:8000/api/auth/token/', data={'username': 'admin', 'password': 'admin'})

if response.status_code == 200:
    token = response.json()['auth_token']
    print(token)
else:
    print(f"Error: {response.status_code}")