import requests
import json

api_key = "2610132566305d8b2f9b57af3b0634e4"
url_accounts = "http://api.reimaginebanking.com/customers?key={}".format(api_key)

def create_customer(first_name, last_name, street_number, street_name, city, state, zip):
    customer_data = {
        "first_name": first_name,
        "last_name": last_name,
        "address": {
            "street_number": street_number,
            "street_name": street_name,
            "city": city,
            "state": state,
            "zip": zip
        }
    }
    return customer_data

json_data = create_customer()
response_accounts = requests.post(
        url_accounts,
        data = json.dumps(json_data),
        headers = {'content-type':'application/json'},
        )

if response.status_code == 201:
    print('Customer created')
