import requests

id = input("Enter id to delete : ")

try:
    id = int(id)
except:
    print(f"{id} is not a valid number")
    id = None

endpoint = f"http://localhost:8000/{id}/delete/"


# endpoint = "https://httpbin.org/anything"
data = {"title": "i5 CPU", "price": 90}

response = requests.delete(endpoint, json=data)

print(response.status_code)
