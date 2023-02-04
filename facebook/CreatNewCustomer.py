import requests
from requests_oauthlib import OAuth1
import random
import string
letters = string.digits
random = "".join(random.choice(letters)for i in range(3))
url = 'http://localhost:8888/rose/wp-json/wc/v3/customers'
auth = OAuth1('ck_22bd8f5a8766395e0fb1ccf68ded616f7deec563', 'cs_27f23bcfda851936b7fa2f93f77699ccc045c47c')
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
