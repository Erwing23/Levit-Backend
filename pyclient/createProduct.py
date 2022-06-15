import requests


endpoint = "http://localhost:8000/api/products/"

get_response = requests.post(
    endpoint,  json={"Title": "Hello World", "price": 123})  # API request sender
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())  # Response from the API
