def test_put_v1_account_password(api, get_credentials):
    api.account.register_new_user(
        login=get_credentials.login,
        email=get_credentials.email,
        password=get_credentials.password)
    api.account.activate_registered_user(login=get_credentials.login)
    api.account.reset_user_password(
        login=get_credentials.login,
        email=get_credentials.email
    )
    token_like_headers = api.mailhog.get_reset_password_token_by_login(login=get_credentials.login)
    api.account.change_user_password(
        login=get_credentials,
        token=token_like_headers,
        old_password=get_credentials.password,
        new_password=get_credentials.password + 'edited')
