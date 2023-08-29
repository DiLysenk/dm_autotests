from time import sleep

import pytest

import structlog

from dm_api_account.apis.models.regisration_user_model import RegistrationModel
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


@pytest.fixture()
def get_credentials():
    return RegistrationModel()


@pytest.fixture()
def api():
    return DmApiAccount()


@pytest.fixture()
def mailhog():
    return MailhogApi()


@pytest.fixture()
def create_user(api, get_credentials):
    """
    :param get_credentials:
    :param api:
    :return:
    """
    response = api.account.post_v1_account(json=get_credentials)
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
    return token
