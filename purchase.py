import datetime
import requests
import json

api_key = "2610132566305d8b2f9b57af3b0634e4"
pocket_change_id = "56c8f873061b2d440baf43f9"

def add_merchant(json_data):
    merchants_response = requests.post(
        url = "http://api.reimaginebanking.com/merchants?key={}".format(api_key),
        data = json.dumps(json_data),
        headers = {'content-type':'application/json'},
    )

    print(merchants_response.text)

def list_merchants():
    url_merchants = "http://api.reimaginebanking.com/merchants?lat={}&lng={}&rad={}&key={}".format(40.1095, -88.2123, 25, api_key)

    merchants_response = requests.get(url_merchants)

    for d in merchants_response.json():
        for key in d:
            print(key, "\t\t", d[key])

def purchase_from_pocket_change(payer_id, amount, service):
    url_purchase = "http://api.reimaginebanking.com/accounts/{}/purchases?key={}".format(payer_id, api_key)

    purchase_data = {
        "medium": "balance",
        "merchant_id": pocket_change_id,
        "amount": amount,
        "purchase_date": datetime.datetime.now().strftime("%Y-%m-%d"),
        "status": "pending",
        "description": "Payment to Pocket Change for {}".format(service)
        }

    purchase_response = requests.post(
        url_purchase,
        data = json.dumps(purchase_data),
        headers = {'content-type':'application/json'}
    )

    print(purchase_response.json())

pocket_change_merchant_data = {
    "name": "Pocket Change",
    "category": "string",
    "address": {
    "street_number": "12345678",
    "street_name": "W. Green St",
    "city": "Urbana",
    "state": "IL",
    "zip": "61801"
    },
    "geocode": {
        "lat": 40.1,
        "lng": -88.2
    }
}

def list_pocket_change_purchases():
    url = "http://api.reimaginebanking.com/merchants/{}/purchases?key={}".format(pocket_change_id, api_key)

    response = requests.get(url)
    for d in response.json():
        for key in d:
            print(key, "\t\t", d[key])

# add_merchant(pocket_change_merchant_data)
# list_merchants()
# purchase_from_pocket_change("56c66be6a73e492741507b92", 1, "Spotify Premium")
list_pocket_change_purchases()
