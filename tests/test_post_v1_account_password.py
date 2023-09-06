from dm_api_account.apis.models.reset_registred_user_password_model import ResetPassword


def test_post_v1_account_password(api, create_user, activate_user, get_credentials):
    """
    Reset registered user password
    :return:
    """

    payload = {
        "login": get_credentials.login,
        "email": get_credentials.email
    }
    headers = {
        'X-Dm-Auth-Token': '',
        'X-Dm-Bb-Render-Mode': '',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    api.account.post_v1_account_password(
        headers=headers,
        json=ResetPassword(**payload)
    )

