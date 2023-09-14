import structlog
from hamcrest import assert_that, has_properties, not_none

from dm_api_account.apis.models.activate_registered_user_model import UserRole
from generic.helpers.orm_db import OrmDatabase

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account2(api, get_credentials):
    orm = OrmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    api.account.register_new_user(
        login=get_credentials.login,
        email=get_credentials.email,
        password=get_credentials.password)
    dataset = orm.get_user_by_login(get_credentials.login)
    for row in dataset:
        assert row.Login == get_credentials.login, f'User {get_credentials.login} not registered'
        assert row.Activated is False, f'User {get_credentials.login} was activated'
    orm.set_activated_flag(login=get_credentials.login)
    dataset = orm.get_user_by_login(login=get_credentials.login)
    for row in dataset:
        assert row['Activated'] is True, f'User {get_credentials.login} not activated'
    response = api.login.login_user(
        login=get_credentials.login,
        password=get_credentials.password)
    assert_that(response.resource, has_properties(
        {
            "login": get_credentials.login,
            """
            todo поч не работает хз разбираюсь
            E       AssertionError: 
            E       Expected: an object with properties 'login' matching 'b423de33n3542' and 'roles' matching <[<UserRole.guest: 'Guest'>, <UserRole.player: 'Player'>]>
            E            but: property 'roles' was <[<UserRole.guest: 'Guest'>, <UserRole.player: 'Player'>]>
            """
            "roles": [UserRole.guest, UserRole.player]
        }
    ))
    assert_that(response.resource.rating, not_none())
    orm.delete_user_by_login(login=get_credentials.login)
    orm.db.close_connection()
