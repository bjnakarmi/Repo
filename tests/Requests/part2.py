import requests

base_url = "https://jsonplaceholder.typicode.com/"
endpoint = "posts"
params = {
    'userId' : 1
}

response = requests.get(url= base_url + endpoint, params=params,)
print(response.status_code)
print(response.json())


