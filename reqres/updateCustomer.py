
import requests

url = 'https://reqres.in/api/users/2'
body = {
    "name": "morpheus",
    "job": "zion resident"
}

res = requests.put(url, json=body)
assert res.status_code == 200, "status code not matching"
print(res.status_code)
