from random import randint

import pytest

from config import settings as cfg

import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

def test_put_v1_account_email(api, credentials, activate_user):
    payload = {
        "login": credentials['login'],
        "password": credentials['password'],
        "email": 'changed' + cfg.user.email
    }
    response = api.account.put_v1_account_email(json=payload)
    assert response.status_code == 200, f'expected 200 but equals {response.status_code}'
