from collections import namedtuple

import pytest
from hamcrest import assert_that, has_properties, has_entries

from dm_api_account.apis.models.activate_registered_user_model import UserRole, UserEnvelope
from utilities import random_string


class TestsPostV1Account:

    def test_post_v1_account(self, dm_api_facade, orm_db, prepare_user):
        login = prepare_user.login
        password = prepare_user.password
        dataset = orm_db.get_user_by_login(login=login)
        for row in dataset:
            assert row.Login == login, f'User {login} not registered'
            assert row.Activated is False, f'User {login} was activated'

        orm_db.set_activated_flag(login=login)
        dataset = orm_db.get_user_by_login(login=login)
        for row in dataset:
            assert row['Activated'] is True, f'User {login} not activated'
        response = dm_api_facade.login.login_user(
            login=login,
            password=password)
        model = UserEnvelope.model_validate(response.json())
        assert_that(model.resource, has_properties(
            {
                "login": login,
                "roles": [UserRole.guest, UserRole.player]
            }
        ))

    @pytest.mark.parametrize(
        ('login', 'email', 'password', 'status_code', 'check'),
        [
            (random_string(3), '33@12.ru', random_string(6), 201, ''),
            (random_string(3), '333@12.ru', random_string(5), 400, {"Password": ["Short"]}),
            (random_string(1), '1111@12.ru', random_string(6), 400, {"Login": ["Short"]}),
            (random_string(3), '11@', random_string(6), 400, {"Email": ["Invalid"]}),
            (random_string(3), 'ru', random_string(6), 400, {"Email": ["Invalid"]}),
        ])
    def test_create_and_activated_user_with_random_params(self,
                                                          dm_api_facade,
                                                          login,
                                                          email,
                                                          password,
                                                          orm_db,
                                                          status_code,
                                                          check,
                                                          assertions
                                                          ):
        response = dm_api_facade.account.register_new_user(
            login=login,
            email=email,
            password=password,
            status_code=status_code
        )
        if status_code == 201:
            assertions.check_ueser_was_created(login=login)
            # orm_db.set_user_activated_true_by_login(login=login)
            dm_api_facade.account.activate_registered_user(login=login)
            assertions.check_ueser_was_activated(login=login)
            dm_api_facade.login.login_user(login=login, password=password)
        else:
            error_message = response.json()['errors']
            assert_that(error_message, has_entries(check))
        orm_db.delete_user_by_login(login=login)
