import requests
import json

customer_id = "56c66be6a73e492741507b96"
api_key = "2610132566305d8b2f9b57af3b0634e4"

url = "http://api.reimaginebanking.com/customers/{}/accounts?key={}".format(
    customer_id, api_key)

response = requests.get(url)

print(response)
