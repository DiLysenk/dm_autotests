import requests
from config import settings as cfg

def post_v1_account_password():
    """
    Reset registered user password
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account/password"

    payload = {
        "login": cfg.user.login,
        "email": cfg.user.email
    }
    headers = {
        'X-Dm-Auth-Token': '',
        'X-Dm-Bb-Render-Mode': '',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="POST",
        url=url,
        headers=headers,
        json=payload
    )
    return response
