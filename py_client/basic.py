import requests

# endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(
    endpoint, json={"query": "Hello World"})  # Http Request
# print(get_response.text)  # print raw text response code

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
print(get_response.json())
print(get_response.status_code)
