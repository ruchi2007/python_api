import requests
from requests_oauthlib import OAuth1
import random
import string
letters = string.digits
random = "".join(random.choice(letters)for i in range(3))


url = 'http://localhost:8888/optimum/wp-json/wc/v3/customers/5'
auth = OAuth1('ck_53d693e068ce9b011ed628de89a83693022c7156 ', 'cs_636bbbf7c608fb9d4c67fe605b3b5e95ab11c3c3')
update_data = {
    "first_name": "masum"+random,
    "last_name": "tasmid"+random}

res = requests.put(url, auth=auth, json=update_data)
assert res.status_code == 200, "invalid status code"
#assert res.status_code!= 200, "invalid status code"
print(res.status_code)

