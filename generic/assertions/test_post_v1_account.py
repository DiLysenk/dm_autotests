from generic.helpers.orm_db import OrmDatabase

class AssertionsPostV1Account:

    def __init__(self, db):
        self.db = db

    def check_ueser_was_created(self, login):
        dataset = orm_db.get_user_by_login(login)
        for row in dataset:
            assert_that(row, has_entries(
                {
                    "Login": login,
                    "Activated": False
                }
            ))

    def check_ueser_was_activated(self, login):
        dataset = orm_db.get_user_by_login(login)
        for row in dataset:
            assert_that(row, has_entries(
                {
                    "Activated": True
                }
            ))