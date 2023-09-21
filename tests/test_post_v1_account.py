from collections import namedtuple

import pytest
import structlog
from hamcrest import assert_that, has_properties, not_none

from dm_api_account.apis.models.activate_registered_user_model import UserRole, UserEnvelope
from utilities import random_string


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


@pytest.mark.parametrize('login, email, password, status_code, check', [
    (random_string(3), '33@12.ru', random_string(6), 201, ''),
    (random_string(3), '333@12.ru', random_string(5), 400, {"Password": ["Short"]}),
    (random_string(1), '1111@12.ru', random_string(6), 400, {"Login": ["Short"]}),
    (random_string(3), '11@', random_string(6), 400, {"Email": ["Invalid"]}),
    (random_string(3), 'ru', random_string(6), 400, {"Email": ["Invalid"]}),
])
def test_post_v1_account(dm_api_facade, login, email, password, orm_db, prepare_user, status_code, check):
    login = prepare_user.login
    password = prepare_user.password
    dataset = orm_db.get_user_by_login(login=login)
    for row in dataset:
        assert row.Login == login, f'User {login} not registered'
        assert row.Activated is False, f'User {login} was activated'

    orm_db.set_activated_flag(login=login)
    dataset = orm_db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Activated'] is True, f'User {login} not activated'
    response = dm_api_facade.login.login_user(
        login=login,
        password=password)
    model = UserEnvelope.model_validate(response.json())
    assert_that(model.resource, has_properties(
        {
            "login": login,
            "roles": [UserRole.guest, UserRole.player]
        }
    ))
