import requests
from config import settings as cfg

def post_v1_account_login():
    """
    Authenticate via credentials
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account/login"

    payload = {
        "login": cfg.user.login,
        "password": cfg.user.password,
        "rememberMe": False
    }
    headers = {
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

r = post_v1_account_login()
print()