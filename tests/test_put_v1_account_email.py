import structlog
from config import settings as cfg

from dm_api_account.apis.models.change_email_model import RequestChangeEmailModel

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email(api, get_credentials, activate_user):
    payload = {
        "login": get_credentials.login,
        "password": get_credentials.password,
        "email": 'changed' + cfg.user.email
    }
    response = api.account.put_v1_account_email(json=RequestChangeEmailModel(**payload))
    assert response.status_code == 200, f'expected 200 but equals {response.status_code}'
