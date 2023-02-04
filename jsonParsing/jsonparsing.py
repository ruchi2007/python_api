import json
from pprint import pprint

user_data = {
    "page": 2,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [
        {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
        },
        {
            "id": 8,
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson",
            "avatar": "https://reqres.in/img/faces/8-image.jpg"
        },
        {
            "id": 9,
            "email": "tobias.funke@reqres.in",
            "first_name": "Tobias",
            "last_name": "Funke",
            "avatar": "https://reqres.in/img/faces/9-image.jpg"
        },
        {
            "id": 10,
            "email": "byron.fields@reqres.in",
            "first_name": "Byron",
            "last_name": "Fields",
            "avatar": "https://reqres.in/img/faces/10-image.jpg"
        },
        {
            "id": 11,
            "email": "george.edwards@reqres.in",
            "first_name": "George",
            "last_name": "Edwards",
            "avatar": "https://reqres.in/img/faces/11-image.jpg"
        },
        {
            "id": 12,
            "email": "rachel.howell@reqres.in",
            "first_name": "Rachel",
            "last_name": "Howell",
            "avatar": "https://reqres.in/img/faces/12-image.jpg"
        }
    ],
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}

#data = user_data["data"]
# print(user_data["page"])
# print(user_data["total"])
# pprint(user-data["data"])
#print(type(data))
#pprint(type(data["data"]))
#print(data[1]["email"])
#print(data[3]["email"])

json1_path = "C:\\Users\\takia\\Documents\\workspace_python\\python_api\\jsonParsing\\json1.json"
json2_path = "C:\\Users\\takia\\Documents\\workspace_python\\python_api\\jsonParsing\\json2.json"

with open(json1_path) as file1:
    data1 = json.load(file1)
    print(data1["page"])
    #pprint(data1)

with open(json2_path) as file2:
    data2 = json.load(file2)
    print(data2["page"])
    #pprint(data2)

    print(data1 == data2)