
'''GET'''
#import requests


#BASE_URL = 'http://fakestoreapi.com'

#query_params = {
#    'limit': 3
#}

#1Method#response = requests.get(f'{BASE_URL}/products')
#2Method#response = requests.get(f'{BASE_URL}/products', params=query_params)
#response = requests.get(f'{BASE_URL}/products/5')

#with open('product.txt','w') as file:
#    file.write(str(response.json()))

#print(response.json())


'''Post'''
# import requests
#2# import json
#
# BASE_URL = 'http://fakestoreapi.com'
#
#
# new_product = {
#     'title': 'Test product',
#     'price': '25',
#     'description': 'Loren ipsum',
#     'image': 'https://i.pravatar.cc/',
#     'category': 'Face Humans'
# }
#2# headers = {
#     'Content-Type': 'application/json'
# }
#
#2Method# response = requests.post(f'{BASE_URL}/products', data=json.dumps(new_product), headers=headers)
# print(response.json())

#1Method# response = requests.post(f'{BASE_URL}/products', json=new_product)
# print(response.json())


'''PUT'''
# import requests
#
#
# BASE_URL = 'http://fakestoreapi.com'
#
# updated_product = {
#     'title': 'Updated product',
#     'category': 'Toy'
# }
#
# response = requests.put(f'{BASE_URL}/products/21', json=updated_product)
# print(response.json())


'''PATCH'''
# import requests
#
#
# BASE_URL = 'http://fakestoreapi.com'
#
# updated_product = {
#     'category': 'Laptops'
# }
#
# response = requests.patch(f'{BASE_URL}/products/21', json=updated_product)
# print(response.json())


'''DELETE'''
# import requests
#
#
# BASE_URL = 'http://fakestoreapi.com'
# response = requests.delete(f'{BASE_URL}/products/21')
# print(response.json())