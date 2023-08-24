from random import randint

import structlog

from config import settings as cfg
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)
payload = {
    "login": cfg.user.login + str({randint(0, 55)}),
    "email": cfg.user.email + str({randint(0, 55)}),
    "password": cfg.user.password
}


def test_post_v1_account():
    mailhog = MailhogApi()
    api = DmApiAccount()
    response = api.account.post_v1_account(json=payload)
    assert response.status_code == 201, f'expected 201 but equals {response.status_code}, \n{response.json(indent=2)}'
    token = mailhog.get_token_from_last_email()
    api.account.put_v1_account_token(token=token)
