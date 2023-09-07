from dm_api_account.apis.models.change_email_model import ChangeEmail
from dm_api_account.apis.models.change_registered_user_password_model import ChangePassword
from dm_api_account.apis.models.register_new_user import Registration
from dm_api_account.apis.models.reset_registred_user_password_model import ResetPassword


class Account:
    def __init__(self, facade):
        from services.dm_api_account import Facade
        self.facade: Facade = facade

    def set_headers(self, headers):
        self.facade.account_api.client.session.headers.update(headers)

    def register_new_user(self, login: str, email: str, password: str):
        # проверки зашиты
        response = self.facade.account_api.post_v1_account(
            json=Registration(
                login=login,
                email=email,
                password=password

            )
        )
        return response

    def activate_registered_user(self, login: str):
        token = self.facade.mailhog.get_token_by_login(login=login)
        response = self.facade.account_api.put_v1_account_token(
            token=token
        )
        return response

    def get_current_user_info(self, **kwargs):
        response = self.facade.account_api.get_v1_account(**kwargs)
        return response

    def change_user_password(self, login: str, token, old_password: str, new_password: str):
        response = self.facade.account_api.put_v1_account_password(
            json=ChangePassword(
                login=login,
                token=token,
                old_password=old_password,
                new_password=new_password
            )
        )
        return response

    def change_user_email(self, login: str, password: str, email: str):
        response = self.facade.account_api.put_v1_account_email(
            json=ChangeEmail(
                login=login,
                password=password,
                email=email
            )
        )
        return response

    def reset_user_password(self, login: str, email: str):
        response = self.facade.account_api.post_v1_account_password(
            json=ResetPassword(
                login=login,
                email=email
            )
        )
        return response
