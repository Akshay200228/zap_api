import requests

api_url = 'http://213.210.36.208:9797/JSON/ajaxSpider/action/addExcludedElement/'

params = {
    'contextName': 'scalesecurezap',
    'description': 'Excluding element for testing',
    'element': 'https://example.com/some/resource'
}

headers = {
    'Accept': 'application/json'
}

try:
    with requests.Session() as session:
        response = session.post(api_url, data=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        print("Status Code:", response.status_code)
        print("Response Content:", response.content)

        try:
            print("Response JSON:", response.json())
        except ValueError:
            print("Response is not in JSON format.")
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
