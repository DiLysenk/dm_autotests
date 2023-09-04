from requests import session, Response

from dm_api_account.apis.models.auth_via_credentials import LoginCredentials, UserEnvelope
from utilities import validate_request_json, validate_status_code


class LoginApi:

    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.session = session()
        self.session.headers.update(headers) if headers else None

    def post_v1_account_login(self, json, status_code=200, **kwargs) -> UserEnvelope | Response:
        """
        Authenticate via credentials
        :return:
        """

        response = self.session.post(
            url=f"{self.host}/v1/account/login",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == status_code:
            return UserEnvelope.model_validate(response.json())
        return response

    def delete_v1_account_login(self, **kwargs):
        """
        Logout as current user
        :return:
        """

        response = self.session.delete(
            url=f"{self.host}/v1/account/login",
            **kwargs
        )

        return response

    def delete_v1_account_login_all(self, status_code=204, **kwargs):
        """
        Logout from every device
        :return:
        """

        response = self.session.delete(
            url=f"{self.host}/v1/account/login/all",
            **kwargs
        )
        validate_status_code(response, status_code)

        return response
