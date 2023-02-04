import requests
from requests_oauthlib import OAuth1
import random
import string
letters = string.digits
random = "".join(random.choice(letters)for i in range(3))
url = 'http://localhost:8888/optimum/wp-json/wc/v3/customers'
auth = OAuth1('ck_53d693e068ce9b011ed628de89a83693022c7156 ', 'cs_636bbbf7c608fb9d4c67fe605b3b5e95ab11c3c3')
json_data = {
  "email": "bo.doee123"+random+"@example.com",
  "first_name": "Johnn",
  "last_name": "Doee",
  "username": "boo.doee"+random,
  "password": "johnne.doe"
}
res = requests.post(url, auth=auth, data = json_data)
print(res.json())
# assert res.status_code == 201, 'invalid status code'
# assert res.status_code!= 201, "invalid status code"
# print(res.status_code)

print(json_data["first_name"])
print(json_data["last_name"])
