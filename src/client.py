import requests
import keyboard

server = "http://localhost:5000/p0ubelle"

data = "salutttt"

keyboard.KeyboardEvent
r = requests.post(server, json=data)
print(r)
