import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login(api, activate_user, credentials):
    payload = {
        "login": credentials['login'],
        "password": credentials['password'],
        "rememberMe": True
    }
    response = api.login.post_v1_account_login(json=payload)
    assert response.status_code == 200, f'expected 200 but equals {response.status_code}'
