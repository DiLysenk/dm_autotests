import structlog

from dm_api_account.apis.models.auth_via_credentials import RequestLoginCredentials

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
    response = api.login.post_v1_account_login(json=RequestLoginCredentials(**payload))
    assert response.status_code == 200, f'expected 200 but equals {response.status_code}'
