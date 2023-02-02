from pprint import pprint

import requests

url = "https://reqres.in/api/users?page=2"
res = requests.get(url)
# print(res.status_code)
# status_code = res.status_code
# assert status_code!= 201 ,"invalid status code"
# print(status_code)
# print(res.json())
# print(res.headers)
# print(res.content)


# customer_list = res.json()
# assert customer_list!= [], "invalid cutomer lisl"

print(res.headers["Content-Type"])
content = res.headers["Content-Type"]
assert content == "application/json; charset=utf-8", "invalid cotent type"
