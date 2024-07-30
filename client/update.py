import requests

endpoint = "http://localhost:8000/2/update/"


# endpoint = "https://httpbin.org/anything"
data = {"title": "490 GPU", "price": 90}

response = requests.put(endpoint, json=data)

print(response.json())
