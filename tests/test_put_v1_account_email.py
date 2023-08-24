from random import randint

from config import settings as cfg

from services.dm_api_account import DmApiAccount
import structlog
from services.mailhog import MailhogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

payload = {
    "login": cfg.user.login,
    "email": cfg.user.email + str({randint(0, 55)}),
    "password": cfg.user.password
}

def test_put_v1_account_email():
    mailhog = MailhogApi()
    api = DmApiAccount()
    response = api.account.put_v1_account_email(json=payload)
    assert response.status_code == 200, f'expected 200 but equals {response.status_code}'
    token = mailhog.get_token_from_last_email()
    api.account.put_v1_account_token(token=token)
