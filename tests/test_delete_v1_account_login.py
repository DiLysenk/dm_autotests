def test_delete_v1_account_login(api, get_credentials):
    api.account.register_new_user(
        login=get_credentials.login,
        email=get_credentials.email,
        password=get_credentials.password)
    api.account.activate_registered_user(login=get_credentials.login)
    api.login.login_user(
        login=get_credentials.login,
        password=get_credentials.password)
    token = api.login.get_auth_token(login=get_credentials.login, password=get_credentials.password)
    api.login.set_headers(headers=token)
    api.login.logout_user()
