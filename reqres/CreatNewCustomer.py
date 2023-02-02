import requests
url = "https://reqres.in/api/users"
body = {
    "name": "morpheus",
    "job": "leader"
}

response = requests.post(url, json=body)
assert response.status_code == 201, "status code not matching"
print(response.status_code)