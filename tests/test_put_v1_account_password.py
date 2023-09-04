from dm_api_account.apis.models.change_registered_user_password_model import ChangePassword


def test_put_v1_account_password(api, create_user, activate_user, get_credentials):
    """
    Change registered user password
    :return:
    """
    payload = {
        "login": get_credentials.login,
        "token": activate_user,
        "oldPassword": get_credentials.password,
        "newPassword": get_credentials.password + '99'
    }
    api.account.put_v1_account_password(json=ChangePassword(**payload))
