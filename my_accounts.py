import requests
import json

api_key = 0xc0799676f60520f37804de8f86f8b1ce
url = "http://api.reimaginebanking.com/accounts?key={}".format(api_key)

payload = {
}

response = requests.post(
    url,
    data = json.dumps(payload),
    headers = {'content-type':'application/json'},
)

print(response)
