import requests

# ----- Get -----

# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print(response.status_code)
# print(response.json())

# ----- Post -----

# url = "https://jsonplaceholder.typicode.com/posts"
# payload = {
#     'title': "Hello",
#     'body' : 'This is a test post',
#     'userId' : 1
# }
#
# response = requests.post(url=url, json=payload)
# print(response.status_code)
# print(response.json())


# ----- A very Good Example for response.get -----

import requests

Base_url = "https://staging.dev.piiink.org"
endpoint = '/api/charity/getAll'
params = {
    'page': 1,
    'limit':10,
    'offset':0,
    'isPending': 'false',
    'countryId': 5

}

headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjY0LCJyb2xlIjoiY291bnRyeU93bmVyIiwicHJpbWFyeUNvbnRhY3ROYW1lIjoiSmFtZXMgTGllciIsImlhdCI6MTc1MDAyMjY4OCwiZXhwIjoxNzU3Nzk4Njg4fQ.DEUWQemQ1aIKLc7kKIw4mDrxrTL9O3CJNdk_i_FWDLA'
}

response = requests.get(url= Base_url + endpoint, params=params,headers=headers)
print(response.status_code)
print(response.json())


# ----- A very Good Example for response.post -----
# import requests
#
# base_url = 'https://jsonplaceholder.typicode.com'
# payload = {
#     'title': "Hello",
#     'body' : 'This is a test post',
#     'userId' : 1
# }
#
# response = requests.post(url=base_url + '/posts', json=payload)
# print(response.status_code)
# print(response.json())

# ----- A very good example of response.put ----
# import requests
#
# base_url = "https://jsonplaceholder.typicode.com"
# endpoint = '/posts/1'
# payload = {
#     "id": 1,
#     "title": "Updated Title",
#     "body": "Updated body content",
#     "userId": 1
# }
#
# response = requests.put(url = base_url + endpoint, json=payload)
# print(response.status_code)
# print(response.json())

# ----- A very good example of response.delete -----

# import requests
#
# base_url = "https://jsonplaceholder.typicode.com"
# endpoint = '/posts/1'
#
# response = requests.delete(url= base_url + endpoint)
# print(response.status_code)
# print(response.json())
