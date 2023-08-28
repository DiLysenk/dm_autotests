from config import settings as cfg
from services.dm_api_account import DmApiAccount

payload = {
    "login": cfg.user.login,
    "email": cfg.user.email,
    "password": cfg.user.password
}


def test_post_v1_account():
    api = DmApiAccount(host=f'{cfg.user.host}')
    response = api.account.post_v1_account(
        json=payload
    )
    assert response.status_code == 201
