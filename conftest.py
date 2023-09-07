from random import randint
from time import sleep

import pytest

import structlog

from dm_api_account.apis.models.register_new_user import Registration
from services.dm_api_account import Facade
from config import settings as cfg

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


@pytest.fixture(scope='function')
def get_credentials() -> Registration:
    return Registration(
        login=cfg.user.login + str(randint(0, 555)),
        email=cfg.user.email + str(randint(0, 555)),
        password=cfg.user.password
    )


@pytest.fixture(scope="function")
def api():
    return Facade(cfg.user.host)


@pytest.fixture(scope="function")
def create_user(api, get_credentials):
    """
    :param get_credentials:
    :param api:
    :return:
    """
    response = api.account.register_new_user(**get_credentials.model_dump())
    assert response.status_code == 201, 'Пользователь не создан'
    yield


#   todo удаление пользователя


@pytest.fixture(scope="function")
def activate_user(api, get_credentials, create_user):
    """
    :param api:
    :param get_credentials:
    :param create_user:
    :return:
    """
    response = api.account.activate_registered_user(get_credentials.login)
    assert response.status_code == 200


@pytest.fixture(scope="function")
def get_token(api, get_credentials):
    return api.mailhog.get_token_by_login(get_credentials.login)
