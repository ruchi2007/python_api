import requests
from requests_oauthlib import OAuth1

url = 'http://localhost:8888/optimum/wp-json/wc/v3/customers/3?force=true'
auth = OAuth1('ck_53d693e068ce9b011ed628de89a83693022c7156 ', 'cs_636bbbf7c608fb9d4c67fe605b3b5e95ab11c3c3')

res = requests.delete(url, auth = auth)
print(res.status_code)
assert res.status_code == 200, "invalid status code"
assert res.status_code != 201, "invalid status code"
print(res.status_code)
