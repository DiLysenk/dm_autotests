from random import randint

from pydantic import BaseModel, StrictStr, Field
from config import settings as cfg


class RegistrationModel(BaseModel):
    login: StrictStr = Field(default=cfg.user.login + str(randint(0, 555)))
    email: StrictStr = Field(default=cfg.user.email + str(randint(0, 555)))
    password: StrictStr = Field(default=cfg.user.password)
