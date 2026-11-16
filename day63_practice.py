import requests

# Fetch the weather data in JSON format
response = requests.get("https://wttr.in/London?format=j1")

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Example: Print current temperature in Celsius and weather description
    current = data["current_condition"][0]
    temp_c = current["temp_C"]
    desc = current["weatherDesc"][0]["value"]
    
    print(f"Current weather in London: {temp_c}°C, {desc}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
  
