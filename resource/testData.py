import random
import string
letters = string.digits
random = "".join(random.choice(letters)for i in range(3))

json_data_fa = {
  "email": "bo.doee123"+random+"@example.com",
  "first_name": "John",
  "last_name": "Doee",
  "username": "bo.doee"+random,
  "password": "johne.doe"
}


update_data_fa = {
  "first_name": "adil"+random,
    "last_name": "tasmid"+random}


json_data_op = {
  "email": "bo.doee123"+random+"@example.com",
  "first_name": "Johnn",
  "last_name": "Doee",
  "username": "boo.doee"+random,
  "password": "johnne.doe"
}

update_data_op = {
    "first_name": "masum"+random,
    "last_name": "tasmid"+random}