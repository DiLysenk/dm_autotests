from random import randint
from typing import Optional

from pydantic import BaseModel, StrictStr, Field, Extra
from config import settings as cfg


class Registration(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(..., description='Login')
    email: Optional[StrictStr] = Field(..., description='Email')
    password: Optional[StrictStr] = Field(..., description='Password')