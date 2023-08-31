import structlog

from config import settings as cfg
from services.dm_api_account import DmApiAccount

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    api = DmApiAccount(host=cfg.user.host)
    api.account.put_v1_account_token(token=cfg.user.token)
