import requests
from requests_oauthlib import OAuth1
import random
import string
letters = string.digits
random = "".join(random.choice(letters)for i in range(3))


url = 'http://localhost:8888/rose/wp-json/wc/v3/customers/2'
auth = OAuth1('ck_22bd8f5a8766395e0fb1ccf68ded616f7deec563', 'cs_27f23bcfda851936b7fa2f93f77699ccc045c47c')
update_data = {
    "first_name": "adil"+random,
    "last_name": "tasmid"+random}
res = requests.put(url, auth=auth, json=update_data)
assert res.status_code == 200, "invalid status code"
#assert res.status_code!= 200, "invalid status code"
print(res.status_code)

