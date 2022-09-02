import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint,
                             json={
                                 "title": "Cricket Bat",
                                 "content": "Crickbat is a bat",
                                 "price": 20
                             }
                             )  # Http Request
# print(get_response.text)   # print raw text response code
# print(get_response.headers)   # print raw text response code

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
print(get_response.json())  # print json response code
# print(get_response.status_code)
