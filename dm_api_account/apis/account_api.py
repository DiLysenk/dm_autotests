from requests import session, Response

from config import settings as cfg

payload = {
    "login": cfg.user.login,
    "email": cfg.user.email,
    "password": cfg.user.password
}
headers = {
    'X-Dm-Auth-Token': '',
    'X-Dm-Bb-Render-Mode': '',
    'Content-Type': 'application/json',
    'Accept': 'text/plain'
}


class AccountApi:

    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.session = session()
        self.session.headers.update(headers) if headers else None

    def post_v1_account(self, json, **kwargs) -> Response:
        """
        :param json registration_model
        Register new user
        :return:
        """
        response = self.session.post(
            url=f"{self.host}/v1/account",
            json=json,
            **kwargs
        )
        return response

    def post_v1_account_password(self, json, **kwargs) -> Response:
        """
        Reset registered user password
        :param json: reset_password_model
        :return:
        """

        response = self.session.post(
            url=f"{self.host}/v1/account/password",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_email(self, json, **kwargs) -> Response:
        """
        Change registered user email
        :param json: change_email_model
        :return:
        """
        response = self.session.put(
            url=f"{self.host}/v1/account/email",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_password(self, json, **kwargs) -> Response:
        """
        Change registered user password
        :param :json change_password_model
        :return:
        """

        response = self.session.put(
            url=f"{self.host}/v1/account/password",
            json=json,
            **kwargs
        )
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
        return response
