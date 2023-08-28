from time import sleep

import pytest
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


@pytest.fixture()
def credentials():
    return {
        "login": cfg.user.login + str({randint(0, 55)}),
        "email": cfg.user.email + str({randint(0, 55)}),
        "password": cfg.user.password
    }


@pytest.fixture()
def api():
    return DmApiAccount()


@pytest.fixture()
def mailhog():
    return MailhogApi()


@pytest.fixture()
def create_user(api, credentials):
    """
    :param api:
    :return:
    """
    response = api.account.post_v1_account(json=credentials)
    assert response.status_code == 201
    return response


@pytest.fixture()
def activate_user(api, mailhog, create_user):
    """
    :param api:
    :param mailhog:
    :return:
    """
    sleep(2)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    sleep(2)
    assert response.status_code == 200
    return response

