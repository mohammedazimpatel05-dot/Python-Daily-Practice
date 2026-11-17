import requests

url = "https://api.example.com/data"
headers = {
    "Authorization": "Bearer YOUR_TOKEN",
    "Accept": "application/json"
}

r = requests.get(url, headers=headers, timeout=10)

# Check status and print JSON response
print(r.status_code)
print(r.json())
