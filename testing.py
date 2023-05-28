import requests

url = "http://127.0.0.1:8000/stu/"

content = requests.get(url)

data = content.json()

print(data)