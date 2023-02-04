import requests
from requests_oauthlib import OAuth1

url = 'http://localhost:8888/chase/wp-json/wc/v3/customers'
auth = OAuth1('ck_bbd634babc20ad5fdd5c0fa1a97d3b63c03e5f99', 'cs_8aecb177625f82f6bdde217c046afd133862680b')

res = requests.get(url, auth=auth)

print(res.json())
# assert res.status_code == 200, "invalid status code"
# print(res.status_code)

# content_type = res.headers["Content-type"]
# assert content_type == "application/json; charset=UTF-8", "invalid content type"
# print(content_type)
# customer_list = res.json()
# assert customer_list != [],"no existing customer"

print(res.json()[0]['id'])
print(res.json()[0]['first_name'])
print(res.json()[1]['last_name'])
print(res.json()[2]['username'])
print(res.json()[3]['email'])

for a in res.json():
    # print(a["id"])
    # print(a['first_name'])
    print(a['username'])
