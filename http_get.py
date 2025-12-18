import requests

url = "https://api.github.com/users/octocat"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Header:", response.headers)
print("Response Body:", response.json())

