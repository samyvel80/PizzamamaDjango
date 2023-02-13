import requests
from getpass import getpass
endpoint = "http://127.0.0.1:8000/menu-pizza/create-list/"


endpoint_token ='http://127.0.0.1:8000/auth'
username= input("tapez votre login:\n")
password = getpass("Entrer votre password:\n")



auth_res = requests.post(endpoint_token, json = {'username': username, 'password': password})
print(auth_res.json())
#print(auth_res.json())
token = auth_res.json()
token_str = token['token']
if auth_res.status_code == 200:

    endpoint = "http://127.0.0.1:8000/menu-pizza/create-list/"

    headers = {
        'Authorization': f'Bearer {token_str}'
        #'Authorization' : 'Token 087e2c54735a07410c1e36fe34e42aae549fbe07'
    }
#endpoint = 'http://httpbin.org/anything'
res = requests.get(endpoint, headers=headers)
print(res.json())
print(res.status_code)