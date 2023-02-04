from pprint import pprint

import requests

from config import config as cf
from resource import testData as td


def test_get_all_customer():
    res = requests.get(cf.url_op, auth=cf.auth_op)
    print(res.json())


def test_post_creat_customer():
    res = requests.post(cf.url_op, auth=cf.auth_op, json=td.json_data_op)
    print(res.json())


def test_put_all_customer():
    res = requests.put(cf.update_url_op, auth=cf.auth_op, json=td.update_data_op)
    print(res.json())


def test_delete_customer():
    res = requests.delete(cf.delete_url_op, auth=cf.auth_op)
    print(res.json())
