import requests
from requests_oauthlib import OAuth1
import random
import string
letters = string.digits
random = "".join(random.choice(letters)for i in range(3))
url = 'http://localhost:8888/chase/wp-json/wc/v3/customers'
auth = OAuth1('ck_bbd634babc20ad5fdd5c0fa1a97d3b63c03e5f99', 'cs_8aecb177625f82f6bdde217c046afd133862680b')
json_data = {
  "email": "bo.doee123"+random+"@example.com",
  "first_name": "John",
  "last_name": "Doee",
  "username": "bo.doee"+random,
  "password": "johne.doe"
}
res = requests.post(url, auth=auth, data = json_data)
print(res.json())
# assert res.status_code == 201, 'invalid status code'
# assert res.status_code!= 201, "invalid status code"
# print(res.status_code)

print(json_data["first_name"])
print(json_data["last_name"])
