from hamcrest import has_properties, assert_that

from config import settings as cfg

from apis.dm_api_account.apis.models import ChangeEmail



def test_put_v1_account_email(api, get_credentials):
    payload = {
        "get_credentials.login": get_credentials.login,
        "password": get_credentials.password,
        "email": 'changed' + cfg.user.email
    }
    response = api.account.put_v1_account_email(json=ChangeEmail(**payload))
    assert_that(response.resource, has_properties({'login': get_credentials.login}))
