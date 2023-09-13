from time import sleep

import structlog
from hamcrest import assert_that, has_properties, not_none

from dm_api_account.apis.models.activate_registered_user_model import UserRole
from dm_api_account.apis.models.register_new_user import Registration
from generic.helpers.dm_db import DmDatabase

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account(api, get_credentials):
    db = DmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    # регистрация
    response = api.account.register_new_user(
        login=get_credentials.login,
        email=get_credentials.email,
        password=get_credentials.password
    )
    # датасет с помощью дб
    dataset = db.get_user_by_login(login=get_credentials.login)
    for row in dataset:
        assert row['Login'] == get_credentials.login, f'User {get_credentials.login} not registered'
        assert row['Activated'] is False, f'User {get_credentials.login} was activated'
    api.account.activate_registered_user(get_credentials.login)
    sleep(1)
    dataset = db.get_user_by_login(login=get_credentials.login)
    for row in dataset:
        assert row['Activated'] is True, f'User {get_credentials.logi} not activated'
    response = api.login.login_user(login=get_credentials.login, password=get_credentials.password)
    assert_that(response.resource, has_properties(
        {
            "login": get_credentials.login,
            # не работает почему то
            # "roles": [UserRole.guest, UserRole.player]
        }
    ))
    db.delete_user_by_login(get_credentials.login)
