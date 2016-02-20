import requests
import json

api_key = "2610132566305d8b2f9b57af3b0634e4"
url_accounts = "http://api.reimaginebanking.com/accounts?key={}".format(api_key)

response_accounts = requests.get(url_accounts)

print(response_accounts)

url_customers = "http://api.reimaginebanking.com/customers?key=2610132566305d8b2f9b57af3b0634e4"

payload_customers = {
    "nickname": "test"
}

response_customers = requests.get(
    url_customers,
    data = json.dumps(payload_customers),
    headers = {'content-type': 'application/json'}
)

print(response_customers)
