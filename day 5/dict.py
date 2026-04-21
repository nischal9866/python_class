boy = {
    "Name":"Ali",
    "Age":21,
    "Height": 6,
    "Weight": 68,
    "City": ["nepal","kathmandu"],
    "Religion":"Muslim",
    "Name":"hari"
}

# print(boy)
# print(type(boy))

# print(boy.keys())
# print(boy.values())
# print(boy['City'])

user_info = {
    "id": 1,
    "name":"Suman",
    "city":"Kathmandu"
    
}

# print(user_info)
# user_info.update({
#     "city":"dang",
#     "number":980,
#     "name":"Sudan"
# })
# print(user_info)

#del
#pop
#clear

user_data = {
    "city":"dang",
    "number":980,
    "name":"Sudan",
    "age":21,
    "height":6,
    "weight":68,
}
# del user_data['city']

# user_data.pop('name')
# user_data.popitem()
# print(user_data)

# print(user_data.get('weight','not found'))

data={
    "name":"Hari",
    "phone":[
        {
            "type":"NTC",
            "num":9844
        },
        {
            "type":"Ncell",
            "num":980
        }
    ]
}

# print(f"{data['name']} {data['phone'][0]['type']} number is {data['phone'][0]['num']}")
# print(f"{data['name']} {data['phone'][1]['type']} number is {data['phone'][1]['num']}")

user_address = {
    "name":"hari",
    "address":{
        "temp":"dang",
        "per":{
            "current":"imadol",
            "old":"balkumari"
        }
    }
}

print(user_address['address']['per']['current'])

print(user_address['address']['per']['old'])
 
# print(user_address.keys())
# print(user_address.values())


 