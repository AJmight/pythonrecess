import requests
import json

# API endpoint
response=requests.get("https://api.github.com")
# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print(f"Error: {response.status_code}")
