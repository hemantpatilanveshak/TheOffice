import requests
import json

url = 'http://127.0.0.1:8000/stucreate/'

# content = requests.get(url)

data = {
    'first_name' : 'Ajinkya',
    'last_name' : 'Vibhute',
    'roll': 32,
    'city' : 'Satara'

}


json_data = json.dumps(data)


content = requests.post(url=url, data=json_data)

data = content.json()

print(data)
