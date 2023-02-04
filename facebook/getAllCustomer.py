import requests
from requests_oauthlib import OAuth1

url = 'http://localhost:8888/rose/wp-json/wc/v3/customers'
auth = OAuth1('ck_22bd8f5a8766395e0fb1ccf68ded616f7deec563', 'cs_27f23bcfda851936b7fa2f93f77699ccc045c47c')

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
print(res.json()[1]['username'])
print(res.json()[1]['email'])

for a in res.json():
    # print(a["id"])
    # print(a['first_name'])
    print(a['username'])
