import requests
from getpass import getpass

endpoint = 'http://127.0.0.1:8000/menu-pizza/api_view/'
res = requests.post(endpoint, json={'nom': 'cal', 'ingredients':'oeuf, fromage','prix':12})
print(res.json())

print(res.status_code)