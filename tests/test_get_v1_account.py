def test_get_v1_account(api, get_credentials):
    """
    Get current user:
        - Регистрация пользователя
        - Активация пользователя
        - Авторизация пользователя и получение авторизационного токена
        - Получить информацию о пользователе (установить заголовки либо через клиент, передавая напрямую в метод)
    """
    api.account.register_new_user(
        login=get_credentials.login,
        email=get_credentials.email,
        password=get_credentials.password,
    )
    api.account.activate_registered_user(login=get_credentials.login)
    token_like_header = api.login.get_auth_token(
        login=get_credentials.login,
        password=get_credentials.password,
    )
    api.account.set_headers(headers=token_like_header)
    api.login.set_headers(headers=token_like_header)



