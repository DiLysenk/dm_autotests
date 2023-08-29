from dm_api_account.apis.models.change_registered_user_password_model import RequestRegisteredUserPassword


def test_put_v1_account_password(api, create_user, activate_user, get_credentials):
    """
    Change registered user password
    :return:
    """
    payload = {
        "login": get_credentials.login,
        "token": create_user,
        "oldPassword": get_credentials.password,
        "newPassword": get_credentials.password + '99'
    }

    response = api.account.put_v1_account_password(
        json=RequestRegisteredUserPassword(**payload)
    )
    assert response.status_code == 200
