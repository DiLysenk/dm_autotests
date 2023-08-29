from requests import session, Response

from dm_api_account.apis.models.activate_registered_user_model import ResponseActivated
from dm_api_account.apis.models.change_email_model import ResponseChangeEmailModel
from dm_api_account.apis.models.change_registered_user_password_model import ResponseRegisteredUserPassword
from dm_api_account.apis.models.get_currnt_user_model import UserDetailsEnvelopeModel
from dm_api_account.apis.models.regisration_user_model import RegistrationModel
from dm_api_account.apis.models.reset_registred_user_password_model import ResponseAccountPassword


class AccountApi:

    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.session = session()
        self.session.headers.update(headers) if headers else None

    def post_v1_account(self, json: RegistrationModel, **kwargs) -> Response:
        """
        :param json registration_model
        Register new user
        :return:
        """
        response = self.session.post(
            url=f"{self.host}/v1/account",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        return response

    def get_v1_account(self, **kwargs) -> Response:
        """
        Get current user
        :return:
        """

        response = self.session.get(
            url=f"{self.host}/v1/account",
            **kwargs
        )
        UserDetailsEnvelopeModel.model_validate(response.json())
        return response

    def put_v1_account_token(self, token: str, **kwargs) -> Response:
        """
        Activate registered user
        :return:
        """

        response = self.session.put(
            url=f"{self.host}/v1/account/{token}",
            **kwargs
        )
        ResponseActivated.model_validate(response.json())
        return response

    def post_v1_account_password(self, json, **kwargs) -> Response:
        """
        Reset registered user password
        :param json: reset_password_model
        :return:
        """

        response = self.session.post(
            url=f"{self.host}/v1/account/password",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        ResponseAccountPassword.model_validate(response.json())
        return response

    def put_v1_account_password(self, json, **kwargs) -> Response:
        """
        Change registered user password
        :param :json change_password_model
        :return:
        """

        response = self.session.put(
            url=f"{self.host}/v1/account/password",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        ResponseRegisteredUserPassword.model_validate(response.json())
        return response

    def put_v1_account_email(self, json, **kwargs) -> Response:
        """
        Change registered user email
        :param json: change_email_model
        :return:
        """
        response = self.session.put(
            url=f"{self.host}/v1/account/email",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        ResponseChangeEmailModel.model_validate(response.json())
        return response
