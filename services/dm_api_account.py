from apis.dm_api_account import AccountApi
from apis.dm_api_account import LoginApi
from generic.helpers.mailhog import MailhogApi
from generic.helpers.account import Account
from generic.helpers.login import Login


class Facade:

    def __init__(self, host, mailhog=None, headers=None):
        # mailhog зашит в helpers = mailhog
        self.account_api = AccountApi(host, headers)
        self.login_api = LoginApi(host, headers)
        self.mailhog = MailhogApi()
        # self передаётся для того что бы удобно было писать обертки
        self.account = Account(self)
        self.login = Login(self)

