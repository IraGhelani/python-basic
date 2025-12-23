import requests

url="https://httpbin.org/post"

headers = {
    "Content-Type": "application/json",
}

data = {
    "name": "Ira",
    "topic": "HTTP practical",
    "tool": "Python requests"
}

response = requests.post(url, headers=headers, json=data)

print("Status Code:", response.status_code)
print("Response Body:", response.json())