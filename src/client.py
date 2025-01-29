import requests

server = "http://localhost:5000/p0ubelle"

data = "salutttt"

r = requests.post(server, json=data)
print(r)
