from requests import session, Response


class LoginApi:

    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.session = session()
        self.session.headers.update(headers) if headers else None

    def post_v1_account_login(self, json, **kwargs) -> Response:
        """
        Authenticate via credentials
        :return:
        """

        response = self.session.post(
            url=f"{self.host}/v1/account/login",
            json=json,
            **kwargs
        )
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

    def delete_v1_account_login_all(self, **kwargs):
        """
        Logout from every device
        :return:
        """

        response = self.session.delete(
            url=f"{self.host}/v1/account/login/all",
            **kwargs
        )
        return response
