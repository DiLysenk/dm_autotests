from hamcrest import has_properties, assert_that

from apis.dm_api_account.apis.models.change_email_model import ChangeEmail
from config import settings as cfg




def test_put_v1_account_email(api, get_credentials):
    payload = {
        "login": get_credentials.login,
        "password": get_credentials.password,
        "email": 'changed' + cfg.user.email
    }
    response = api.account.put_v1_account_email(json=ChangeEmail(**payload))
    assert_that(response.resource, has_properties({'login': get_credentials.login}))
