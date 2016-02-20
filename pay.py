import datetime
import requests
import json

api_key = "2610132566305d8b2f9b57af3b0634e4"
pocket_change_id = "56c66be6a73e492741507b92"

def pay_pocket_change(payer_id, amount, service):
    url_payment = "http://api.reimaginebanking.com/accounts/{}/transfers?key={}".format(payer_id, api_key)

    payment_data = {
        "medium": "balance",
        "payee_id": pocket_change_id,
        "amount": amount,
        "transaction_date": datetime.datetime.now().strftime("%Y-%m-%d"),
        "status": "pending",
        "description": "Payment to Pocket Change for {}".format(service)
        }

    payment_response = requests.post(
        url_payment,
        data = json.dumps(payment_data),
        headers = {'content-type':'application/json'}
    )

    print(payment_response.text)

    print(requests.post(
        "http://api.reimaginebanking.com/transfers/{}?key={}".format(pocket_change_id, api_key),
    ).text)

pay_pocket_change("56c66be6a73e492741507b93", 1, "Spotify Premium")
