import django
import requests
import json

customer_id = 1234567890
api_key = 0xc0799676f60520f37804de8f86f8b1ce

url = "http://api.reimaginebanking.com/customers/{}/accounts?key={}".format(
    customer_id, api_key)

payload = {
    "type": "Savings",
    "nickname": "test",
    "rewards": 10000,
    "balance": 10000
}

response = requests.post(
    url,
    data = json.dumps(payload),
    headers = {'content-type':'application/json'},
)

if  response.status_code == 201:
    print('account created')
else:
    print ('account not created with error', response)
