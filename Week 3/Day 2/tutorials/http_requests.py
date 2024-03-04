import http.client

""" conn = http.client.HTTPSConnection("pokeapi.co")

conn.request("GET", "/api/v2/pokemon/ditto")

response = conn.getresponse()

print(f"Status Code: {response.status}")
print(f"Reason: {response.reason}")

 """
import urllib.request

url = "https://pokeapi.co/api/v2/pokemon/ditto"

""" with urllib.request.urlopen(url) as response:
    html = response.read()
 """
import requests

""" r = requests.get(url)

print(r.json()) """
