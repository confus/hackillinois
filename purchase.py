import datetime
import requests
import json

from nessie_urls import *

API_KEY = "2610132566305d8b2f9b57af3b0634e4"
POCKETCHANGE_ID = "56c8f873061b2d440baf43f9"

def nessie_add_merchant(json_data):
    merchants_response = requests.post(
        url = "http://api.reimaginebanking.com/merchants?key={}".format(API_KEY),
        data = json.dumps(json_data),
        headers = {'content-type':'application/json'},
    )

    print(merchants_response.text)

def nessie_list_merchants():
    url_merchants = "http://api.reimaginebanking.com/merchants?lat={}&lng={}&rad={}&key={}".format(40.1095, -88.2123, 25, API_KEY)

    merchants_response = requests.get(url_merchants)

    for d in merchants_response.json():
        for key in d:
            print(key, "\t\t", d[key])

def nessie_list_pocketchange_purchases():
    url = "http://api.reimaginebanking.com/merchants/{}/purchases?key={}".format(POCKETCHANGE_ID, API_KEY)

    response = requests.get(url)
    for d in response.json():
        for key in d:
            print(key, "\t\t", d[key])

def nessie_purchase_from_pocketchange(account_id, amount, service, time, time_unit):
    url_purchase = url_purchase_aid(account_id, API_KEY)

    purchase_data = {
        "medium": "balance",
        "merchant_id": POCKETCHANGE_ID,
        "amount": amount,
        "purchase_date": datetime.datetime.now().strftime("%Y-%m-%d"),
        "status": "pending",
        "description": "Payment to Pocket Change for {}".format(service),
        }

    purchase_response = requests.post(
        url_purchase,
        data = json.dumps(purchase_data),
        headers = {'content-type':'application/json'}
    )

    # return a full description of the purchase
    summary = purchase_data.copy()
    summary["time"] = time
    summary["time_unit"] = time_unit

    return summary

print(nessie_purchase_from_pocketchange("56c66be6a73e492741507b92", 5.3, "Spotify Premium", 7, "days"))
