import structlog
from hamcrest import has_properties, assert_that

from config import settings as cfg

from dm_api_account.apis.models.change_email_model import ChangeEmail

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email(api, get_credentials):
    payload = {
        "login": get_credentials.login,
        "password": get_credentials.password,
        "email": 'changed' + cfg.user.email
    }
    response = api.account.put_v1_account_email(json=ChangeEmail(**payload))
    assert_that(response.resource, has_properties({'login': get_credentials.login}))
