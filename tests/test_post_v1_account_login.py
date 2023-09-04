import structlog
from hamcrest import assert_that, has_properties

from dm_api_account.apis.models.auth_via_credentials import LoginCredentials

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login(api, activate_user, get_credentials):
    payload = {
        "login": get_credentials.login,
        "password": get_credentials.password,
        "rememberMe": True
    }
    response = api.login.post_v1_account_login(json=LoginCredentials(**payload))
    assert_that(response.resource,has_properties({"login": get_credentials.login}))
