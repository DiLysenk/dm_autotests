import structlog
from hamcrest import assert_that, has_properties, not_none

from dm_api_account.apis.models.activate_registered_user_model import UserRole
from dm_api_account.apis.models.register_new_user import Registration

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account(api, get_credentials):
    response = api.account.register_new_user(
        login=get_credentials.login,
        email=get_credentials.email,
        password=get_credentials.password
    )
    assert_that(response.resource, has_properties(
        {
            "login": get_credentials.login,
            "roles": [UserRole.guest, UserRole.player]
        }
    ))
    assert_that(response.resource.rating, not_none())
    api.account.activate_registered_user()
    api.login.login_user(login=get_credentials.login, password=get_credentials.password)

