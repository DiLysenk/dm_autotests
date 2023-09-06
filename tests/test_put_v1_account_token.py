from datetime import datetime

import structlog
from hamcrest import assert_that, has_properties, not_none, has_string, starts_with

from config import settings as cfg
from dm_api_account.apis.models.activate_registered_user_model import UserRole
from services.dm_api_account import DmApiAccount

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token(api, activate_user, get_credentials):
    api = DmApiAccount(host=cfg.user.host)
    response = api.account.put_v1_account_token(token=activate_user)
    assert_that(response.resource, has_properties(
        {
            "login": get_credentials.login,
            "roles": [UserRole.guest, UserRole.player],
            "rating": has_properties({
                "enabled": True,
                "quality": 0,
                "quantity": 0
            }),
            "registration": has_string(starts_with(str(datetime.utcnow().date())))
        }
    ))
    assert_that(response.resource.rating, not_none())
