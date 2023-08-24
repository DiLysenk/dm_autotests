from config import settings as cfg

from services.dm_api_account import DmApiAccount
import structlog

payload = {
    "login": cfg.user.login,
    "password": cfg.user.password,
    "rememberMe": True
}

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login():
    api = DmApiAccount()
    response = api.login.post_v1_account_login(json=payload)
    assert response.status_code == 200, f'expected 200 but equals {response.status_code}'