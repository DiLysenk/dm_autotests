from collections import namedtuple
from random import randint
from time import sleep

import pytest

import structlog

from dm_api_account.apis.models.register_new_user import Registration
from generic.helpers.dm_db import DmDatabase
from generic.helpers.mailhog import MailhogApi
from generic.helpers.orm_db import OrmDatabase
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


@pytest.fixture()
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


@pytest.fixture(scope="function")
def get_token(api, get_credentials):
    return api.mailhog.get_token_by_login(get_credentials.login)


@pytest.fixture()
def mailhog(api):
    return MailhogApi(cfg.user.host)


@pytest.fixture()
def dm_api_facade(mailhog):
    return Facade(cfg.user.host, mailhog=mailhog)


@pytest.fixture()
def dm_db() -> DmDatabase:
    db = DmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    return db


@pytest.fixture()
def orm_db(get_credentials):
    orm = OrmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    yield orm
    orm.delete_user_by_login(login=get_credentials.login)
    orm.db.close_connection()


@pytest.fixture()
def prepare_user(get_credentials, dm_api_facade, dm_orm):
    data = namedtuple('user', 'login, email, password')
    User = data(login=get_credentials.login,
                email=get_credentials.email,
                password=get_credentials.password
                )
    dm_orm.delete_user_by_login(login=User.login)
    dataset = dm_orm.get_user_by_login(login=User.login)
    assert len(dataset) == 0
    dm_api_facade.mailhog.delete_all_messages()
    return User