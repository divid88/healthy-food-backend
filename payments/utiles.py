import requests
import json

ZP_API_LOAPAGE = 'http://127.0.0.1:8080/zar/load_page/'
ZP_API_REQUEST = 'http://127.0.0.1:8080/zar/get_link_payment/'
ZP_API_VERIFY = f'http://127.0.0.1:8080/zar/verify_payment/'
MERCHANT = '347d65f1-1eed-4d86-b7fe-1c2be27c26fc'


def request_payment(request, amount, name, callback):
    req_header = {"accept": "application/json",
                  "content-type": "application/json'"
                  }
    req_data = {
        "merchant_id": MERCHANT,
        'amount': int(amount),
        'customer_name': name,
        'callback': callback
    }

    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
        req_data), headers=req_header)

    return ZP_API_LOAPAGE + req.json()['author'] + '/', req.json()['author']


def verify_payment(request, author):
    req_header = {"accept": "application/json",
                  "content-type": "application/json'"
                  }

    req_data = {
        "merchant_id": MERCHANT,
        "author": author
    }
    response = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
    return response
