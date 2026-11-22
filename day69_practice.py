import time
import requests

time.sleep(1)
response = requests.get("https://api.github.com", timeout=10)

print(response.status_code)
print(response.json())
