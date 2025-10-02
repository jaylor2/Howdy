#!/usr/bin/python3
import requests
r = requests.get('https://api.chucknorris.io/jokes/random')
data = r.json().get('value')
print(data)

