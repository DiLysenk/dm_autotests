from apis.dm_api_account import ChangePassword


def test_put_v1_account_password(api, create_user, activate_user_and_get_token, get_credentials):
    """
    Change registered user password
    :return:
    создать -- активировать -- залогинить
    """
    payload = {
        "login": get_credentials.login,
        "token": activate_user_and_get_token,
        "oldPassword": get_credentials.password,
        "newPassword": get_credentials.password + '99'
    }
    api.account.put_v1_account_password(json=ChangePassword(**payload))
