import requests
from config import settings as cfg

def put_v1_account_token():
    """
    Activate registered user
    :return:
    """
    token = 'c0fee269-5383-430d-855a-c87add9a6c6d'
    url = f"http://5.63.153.31:5051/v1/account/{token}"

    payload = {}
    headers = {
        'X-Dm-Auth-Token': '',
        'X-Dm-Bb-Render-Mode': '',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="PUT",
        url=url,
        headers=headers,
        json=payload
    )
    return response
