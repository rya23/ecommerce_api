import requests

endpoint = "http://localhost:8000/"


# endpoint = "https://httpbin.org/anything"
response = requests.get(endpoint, json={"title": "CPU", "content": "i9", "price": 900})

print(response.json())
