import requests

url = "https://httpbin.org/post"
data = {
    "name": "Alice",
   "role": "intern",
    "skill": "python"
}
response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
