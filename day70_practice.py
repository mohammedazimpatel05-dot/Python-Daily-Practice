import requests

city = input("City: ")
r = requests.get(f"https://wttr.in/{city}?format=3")
print(r.text)
