import requests
import json

api_key = "2610132566305d8b2f9b57af3b0634e4"
url_accounts = "http://api.reimaginebanking.com/accounts?key={}".format(api_key)

response_accounts = requests.get(url_accounts)

print("\nAccounts:", "\n------------------------------------------")
for d in response_accounts.json():
    for key in d:
        print(key, "\t\t", d[key])

url_customers = "http://api.reimaginebanking.com/customers?key={}".format(api_key)

response_customers = requests.get(url_customers)

print("\nCustomers:", "\n------------------------------------------")
for d in response_customers.json():
    for key in d:
        print(key, "\t\t", d[key])
