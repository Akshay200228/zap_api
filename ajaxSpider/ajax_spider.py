import requests

# Define the headers to specify the response format
headers = {
  'Accept': 'application/json'
}

# Define the API endpoint and parameters
api_url = "http://213.210.36.208:9797/JSON/ajaxSpider/action/addAllowedResource/"
params = {
    "apikey": "scalesecurezap",
    "regex": "^http.*\\.js(?:\\?.*)?$"
}

# Make the GET request to add the allowed resource
response = requests.get(api_url, params=params, headers=headers)

# Print the response in JSON format
try:
    response_json = response.json()
    print("Response JSON:", response_json)
except requests.exceptions.JSONDecodeError as e:
    print("Failed to decode JSON response:", str(e))
    print("Response content:", response.content)
