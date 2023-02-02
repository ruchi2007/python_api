import requests
from requests_oauthlib import OAuth1

url='http://localhost:8888/chase/wp-json/wc/v3/customers'
auth=OAuth1('ck_bbd634babc20ad5fdd5c0fa1a97d3b63c03e5f99','cs_8aecb177625f82f6bdde217c046afd133862680b')

json_data = {
  "email": "bo.doe123@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "username": "bo.doe",
  "password": "john.doe"
}
r = requests.post(url, auth=auth, data = json_data)
print(r.json())
