import uuid
from typing import List

import allure
from sqlalchemy import select, delete, update
from generic.helpers.orm_models import User
from orm_client.orm_client import OrmClient


class OrmDatabase:
    def __init__(self, user, password, host, database):
        self.db = OrmClient(user, password, host, database)

    def get_all_users(self):
        query = select(User)
        dataset = self.db.send_query(query)
        return dataset

    def get_user_by_login(self, login: str) -> List[User]:
        query = (
            select(User)
            .where(User.Login == login)
        )
        dataset = self.db.send_query(query)
        return dataset

    def delete_user_by_login(self, login: str):
        query = (
            delete(User)
            .where(User.Login == login)
        )
        dataset = self.db.send_bulk_query(query)
        return dataset

    def set_activated_flag(self, login: str, value: bool = True):
        query = (
            update(User)
            .where(User.Login == login)
            .values(Activated=value)
        )
        dataset = self.db.send_bulk_query(query)
        return dataset
