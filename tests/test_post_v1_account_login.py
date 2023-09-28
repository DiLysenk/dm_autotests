from hamcrest import assert_that, has_properties

from apis.dm_api_account.apis.models import LoginCredentials, UserRole


def test_post_v1_account_login(api, get_credentials):
    payload = LoginCredentials(
        login=get_credentials.login,
        password=get_credentials.password,
        rememberMe=True
    )
    response = api.login.post_v1_account_login(json=payload)
    assert_that(response.resource, has_properties(
        {
            "login": get_credentials.login,
            "roles": [UserRole.guest, UserRole.player],
            "rating": has_properties({
                "enabled": True,
                "quality": 0,
                "quantity": 0
            }),
        }
    ))
