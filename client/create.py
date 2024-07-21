import requests

endpoint = "http://localhost:8000"


# endpoint = "https://httpbin.org/anything"
data = {"title": "i5 CPU", "price": 90}

response = requests.post(endpoint, json=data)

print(response.json())
