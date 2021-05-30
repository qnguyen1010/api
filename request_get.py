import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


print('start testing requests')

# endpoint = "http://158.106.124.70:3023/matching?target_type=vendor&query=Apple&limit=11&acc_id=11091"
endpoint = "http://158.106.124.70:3023/matching?"
parameters = {"target_type":"vendor", "query":"chicken", "limit":3, "acc_id":11091}

# endpoint = "http://127.0.0.1:5000/books"
# # endpoint = "http://127.0.0.1:5000/books/all"
# parameters = {"author": "Ann Leckie "}

response = requests.get(endpoint, params=parameters)

jprint(response.json())
print(f'status code is {response.status_code}')
# print(response.body)

# print(response.json().keys())