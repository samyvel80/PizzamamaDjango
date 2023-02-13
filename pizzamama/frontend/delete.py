import requests
id= input("Enter the Id of product you wante to delete:")

endpoint = f'http://127.0.0.1:8000/pizza/api/{id}'
#endpoint = 'http://httpbin.org/anything'
res = requests.delete(endpoint)
print(res.status_code,res.status_code==204)