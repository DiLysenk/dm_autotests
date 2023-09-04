from random import randint
from typing import Optional

from pydantic import BaseModel, StrictStr, Field, Extra
from config import settings as cfg


class Registration(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(default=cfg.user.login + str(randint(0, 555)), description='Login')
    email: Optional[StrictStr] = Field(default=cfg.user.email + str(randint(0, 555)), description='Email')
    password: Optional[StrictStr] = Field(default=cfg.user.password, description='Password')
