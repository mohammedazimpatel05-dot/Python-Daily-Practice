import requests

# Send a GET request to the GitHub API
r = requests.get("https://api.github.com")

# Check the HTTP status code (200 means success)
print("Status Code:", r.status_code)

# Parse and print the JSON response
print("Response Data:", r.json())
