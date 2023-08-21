import requests
from config import settings as cfg

def put_v1_account_password():
    """
    Change registered user password
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account/password"

    payload = {
        "login": cfg.user.login,
        "token": "c0fee269-5383-430d-855a-c87add9a6c6d",
        "oldPassword": cfg.user.password,
        "newPassword": cfg.user.password + '99'
    }
    headers = {
        'X-Dm-Auth-Token': '',
        'X-Dm-Bb-Render-Mode': '',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="PUT",
        url=url,
        headers=headers,
        json=payload
    )
    return response
