from requests import session, Response

from dm_api_account.apis.models.activate_registered_user_model import ResponseActivated
from dm_api_account.apis.models.change_email_model import ResponseChangeEmailModel
from dm_api_account.apis.models.change_registered_user_password_model import ResponseRegisteredUserPassword
from dm_api_account.apis.models.get_currnt_user_model import UserDetailsEnvelopeModel
from dm_api_account.apis.models.regisration_user_model import RegistrationModel
from dm_api_account.apis.models.reset_registred_user_password_model import ResponseAccountPassword
from utilities import validate_request_json, validate_status_code_func


class AccountApi:

    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.session = session()
        self.session.headers.update(headers) if headers else None

    def post_v1_account(self, json: RegistrationModel, status_code=201, **kwargs) -> Response:
        """
        :param json registration_model
        Register new user
        :return:
        """
        response = self.session.post(
            url=f"{self.host}/v1/account",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code_func(response, status_code)
        return response

    def get_v1_account(self, status_code=200, **kwargs) -> UserDetailsEnvelopeModel | Response:
        """
        Get current user
        :return:
        """

        response: Response = self.session.get(
            url=f"{self.host}/v1/account",
            **kwargs
        )
        validate_status_code_func(response, status_code)
        if response.status_code == status_code:
            return UserDetailsEnvelopeModel.model_validate(response.json())
        return response

    def put_v1_account_token(self, token: str, status_code=200, **kwargs) -> ResponseActivated | Response:
        """
        Activate registered user
        :return:
        """

        response = self.session.put(
            url=f"{self.host}/v1/account/{token}",
            **kwargs
        )
        validate_status_code_func(response, status_code)
        if validate_status_code_func(response, status_code):
            return ResponseActivated.model_validate(response.json())
        return response

    def post_v1_account_password(self, json, status_code=201, **kwargs) -> Response:
        """
        Reset registered user password
        :param status_code:
        :param json: reset_password_model
        :return:
        """

        response = self.session.post(
            url=f"{self.host}/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code_func(response, status_code)
        if response.status_code == status_code:
            return ResponseAccountPassword.model_validate(response.json())
        return response

    def put_v1_account_password(self, json, status_code=200, **kwargs) -> Response:
        """
        Change registered user password
        :param :json change_password_model
        :return:
        """

        response = self.session.put(
            url=f"{self.host}/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code_func(response, status_code)
        if response.status_code == status_code:
            return ResponseRegisteredUserPassword.model_validate(response.json())
        return response

    def put_v1_account_email(self, json, status_code=200, **kwargs) -> Response:
        """
        Change registered user email
        :param status_code:
        :param json: change_email_model
        :return:
        """
        response = self.session.put(
            url=f"{self.host}/v1/account/email",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code_func(response, status_code)
        if response.status_code == status_code:
            return ResponseChangeEmailModel.model_validate(response.json())
        return response
