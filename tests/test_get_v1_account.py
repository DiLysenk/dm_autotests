def test_get_v1_account(api, activate_user, get_token, get_credentials):
    """
    Get current user:
        - Регистрация пользователя
        - Активация пользователя
        - Авторизация пользователя и получение авторизационного токена
        - Получить информацию о пользователе (установить заголовки либо через клиент, передавая напрямую в метод)
    """
    token = api.login.get_auth_token(get_credentials.login, get_credentials.password)

    response = api.account_api.get_v1_account(activate_user)
    api.account_api.get_v1_account(response)
