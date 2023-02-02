import requests

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)
print(response.json())
status_code = response.status_code
contentType = response.headers['Content-Type']
print(contentType)
assert contentType == 'application/json; charset=utf-8', "Content Type not matching"
print(status_code)
assert status_code == 200, "status_code is 200 "
