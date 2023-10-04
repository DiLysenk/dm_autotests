import allure
import pytest
from hamcrest import assert_that, has_entries

from utilities import random_string


@allure.suite("Тесты на проверку метода POST /v1/account")
@allure.sub_suite("Позитивные проверки")
class TestsPostV1Account:
    @allure.title("Регистрация пользователя")
    @pytest.mark.parametrize(
        ('login', 'email', 'password', 'status_code', 'check'),
        [
            (random_string(3), random_string(3) + 'vh3fw3@12.ru', random_string(6), 201, ''),
            (random_string(3), '333@12.ru', random_string(5), 400, {"Password": ["Short"]}),
            (random_string(1), '1111@12.ru', random_string(6), 400, {"Login": ["Short"]}),
            (random_string(3), '11@', random_string(6), 400, {"Email": ["Invalid"]}),
            (random_string(3), 'ru', random_string(6), 400, {"Email": ["Invalid"]}),
        ])
    def test_create_and_activated_user_with_random_params(
            self,
            dm_api_facade,
            login,
            email,
            password,
            orm_db,
            status_code,
            check,
            dm_db,
            assertions
    ):
        orm_db.delete_user_by_login(login=login)
        response = dm_api_facade.account.register_new_user(
            login=login,
            email=email,
            password=password,
            status_code=status_code
        )
        if status_code == 201:
            assertions.check_user_was_created(login=login)
            orm_db.set_activated_flag(login=login)
            assertions.check_user_was_activated(login=login)
            dm_api_facade.login.login_user(
                login=login,
                password=password
            )
        else:
            error_message = response.json()['errors']
            assert_that(error_message, has_entries(check))
        orm_db.delete_user_by_login(login=login)
