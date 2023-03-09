'''{
    'firstName': 'Jon',
    'lastName': 'Doe',
    'age': 35,
    'children':[
        {
            'firstName' : 'Anna',
            'age':6
        },
        {
            'firstName' : 'Jake',
            'age':8
        }
    ]
}'''
import json

# процесс стерелизации
'''import json

data = {
    'president':{
                "name":'Abraham Linkoln',
                "country":'USA'
    }
}


with open('file.json','w') as write_file:
    json.dump(data,write_file)

# with open('file.json','a') as write_file:
#     json.dump(data,write_file,indent=4)

# json_string = json.dumps(data)
# print(type(json_string))
'''

#как менять json format ()
#import json
#
#
# json_str = """
# {
#     "group":{
#         "mentor":"Alisher",
#         "language":"Python",
#         "students":[
#                 {
#                     "name":"Damir",
#                     "direction":"beckend"
#                 },
#                 {
#                     "name":"Edil",
#                     "direction":"beckend"
#                 }
#         ]
#     }
# }"""
#
# data = json.loads(json_str)
# print(data)
'''Дeстерилизация'''
# with open('file.json', 'r') as readd_file:
#     data = json.load(readd_file)
#     print(type(data))


# card = (7,'Q')
# encode_card = json.dumps(card)
# decode_card = json.loads(encode_card)
#
# print(card == decode_card)
# print(type(card))
# print(type(decode_card))
# print(tuple(decode_card))