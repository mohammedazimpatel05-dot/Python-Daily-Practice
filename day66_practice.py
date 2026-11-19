import requests

url = "https://wttr.in/London?format=j1"
response = requests.get(url)

# Ensure the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Extract current weather conditions
    current = data["current_condition"][0]
    temp_c = current["temp_C"]
    desc = current["weatherDesc"][0]["value"]
    
    print(f"London Weather: {temp_c}°C, {desc}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
 
response = requests.get(
    "https://wttr.in/London?format=j1",
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=10
  )
