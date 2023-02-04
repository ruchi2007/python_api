import requests
from requests_oauthlib import OAuth1

url = 'http://localhost:8888/rose/wp-json/wc/v3/customers/3?force=true'
auth = OAuth1('ck_22bd8f5a8766395e0fb1ccf68ded616f7deec563', 'cs_27f23bcfda851936b7fa2f93f77699ccc045c47c')

res = requests.delete(url, auth = auth)
print(res.status_code)
assert res.status_code == 200, "invalid status code"
assert res.status_code != 201, "invalid status code"
print(res.status_code)
