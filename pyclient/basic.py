import requests


endpoint = "http://localhost:8000/api/"

get_response = requests.get(
    endpoint, params={"param1": "value1"}, json={"1": "Hello"})  # API request sender
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())  # Response from the API
