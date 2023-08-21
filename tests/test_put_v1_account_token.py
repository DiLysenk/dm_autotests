import requests
from config import settings as cfg

from services.dm_api_account import DmApiAccount


def test_put_v1_account_token():
    api = DmApiAccount(host=cfg.user.host)
    api.account.put_v1_account_token(token=cfg.user.token)
