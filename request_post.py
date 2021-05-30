import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)



# endpoint = "http://158.106.124.70:3023/matching?target_type=vendor&query=Apple&limit=11&acc_id=11091"
endpoint = "http://158.106.124.70:3023/matching?"
parameters = {"target_type":"vendor", "query":"chicken", "limit":3, "acc_id":11091}

endpoint = "http://127.0.0.1:5000/add/"
# endpoint = "http://127.0.0.1:5000/books/all"

data = '{"url": "https://www.amazons3.myrecipe_local.pdf"}'

response = requests.post(endpoint, data)

print(f'status code is {response.status_code}')
print(response)
# jprint(response.json())
# print(response.body)

# print(response.json().keys())