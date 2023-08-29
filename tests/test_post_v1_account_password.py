from dm_api_account.apis.models.reset_registred_user_password_model import RequestAccountPassword


def test_post_v1_account_password(api, create_user, activate_user, get_credentials):
    """
    Reset registered user password
    :return:
    """

    payload = {
        "login": get_credentials.login,
        "email": get_credentials.password
    }
    headers = {
        'X-Dm-Auth-Token': '',
        'X-Dm-Bb-Render-Mode': '',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = api.account.post_v1_account_password(
        headers=headers,
        json=RequestAccountPassword(**payload)
    )
    assert response.status_code == 200
