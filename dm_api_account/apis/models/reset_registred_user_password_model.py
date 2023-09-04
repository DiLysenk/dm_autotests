from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional, Any

from pydantic import BaseModel, StrictStr, Field, Extra


class ResetPassword(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='Login')
    email: Optional[StrictStr] = Field(None, description='Email')


class UserRole(Enum):
    guest = 'Guest'
    player = 'Player'
    administrator = 'Administrator'
    nanny_moderator = 'NannyModerator'
    regular_moderator = 'RegularModerator'
    senior_moderator = 'SeniorModerator'


class Rating(BaseModel):
    class Config:
        extra = Extra.forbid

    enabled: Optional[bool] = Field(None, description='Rating participation flag')
    quality: Optional[int] = Field(None, description='Quality rating')
    quantity: Optional[int] = Field(None, description='Quantity rating')


class User(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='Login')
    roles: Optional[List[UserRole]] = Field(None, description='Roles')
    medium_picture_url: Optional[StrictStr] = Field(
        None, alias='mediumPictureUrl', description='Profile picture URL M-size'
    )
    small_picture_url: Optional[StrictStr] = Field(
        None, alias='smallPictureUrl', description='Profile picture URL S-size'
    )
    status: Optional[StrictStr] = Field(None, description='User defined status')
    rating: Optional[Rating] = None
    online: Optional[datetime] = Field(None, description='Last seen online moment')
    name: Optional[StrictStr] = Field(None, description='User real name')
    location: Optional[StrictStr] = Field(None, description='User real location')
    registration: Optional[datetime] = Field(
        None, description='User registration moment'
    )


class UserEnvelope(BaseModel):
    class Config:
        extra = Extra.forbid

    resource: Optional[User] = None
    metadata: Optional[Any] = Field(None, description='Additional metadata')

# fffffffffffffffffffffff
#
#
#
# class RequestAccountPassword(BaseModel):
#     login: StrictStr
#     email: StrictStr
#
#
# class Rating(BaseModel):
#     enabled: bool
#     quality: int
#     quantity: int
#
#
# class Resource(BaseModel):
#     login: StrictStr
#     roles: List[StrictStr]
#     medium_picture_url: Optional[StrictStr] = Field(alias='mediumPictureUrl')
#     small_picture_url: Optional[StrictStr] = Field(alias='smallPictureUrl')
#     status: StrictStr
#     rating: Rating
#     online: StrictStr
#     name: StrictStr
#     location: StrictStr
#     registration: StrictStr
#
#
# class ResponseAccountPassword(BaseModel):
#     resource: Resource
#     metadata: StrictStr
#
#
# class InvalidProperties(BaseModel):
#     additional_prop1: List[str] = Field(alias='additionalProp1')
#     additional_prop2: List[str] = Field(alias='additionalProp2')
#     additional_prop3: List[str] = Field(alias='additionalProp3')
#
#
# class BadResponseModel(BaseModel):
#     message: StrictStr
#     invalid_properties: InvalidProperties = Field(alias='invalidProperties')
