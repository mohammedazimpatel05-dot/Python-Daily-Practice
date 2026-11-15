import requests

# Send form-encoded data
r = requests.post("https://httpbin.org/post", data={"key": "value"})

# Or send a JSON payload
# r = requests.post("https://httpbin.org/post", json={"key": "value"})

print(r.status_code)
print(r.json())
