from datetime import datetime
from enum import Enum
from typing import List, Optional, Any

from pydantic import BaseModel, StrictStr, Field, StrictBool, Extra


class PagingSettings(BaseModel):
    class Config:
        extra = Extra.forbid

    posts_per_page: Optional[int] = Field(
        None, alias='postsPerPage', description='Number of posts on a game room page'
    )
    comments_per_page: Optional[int] = Field(
        None,
        alias='commentsPerPage',
        description='Number of commentaries on a game or a topic page',
    )
    topics_per_page: Optional[int] = Field(
        None,
        alias='topicsPerPage',
        description='Number of detached topics on a forum page',
    )
    messages_per_page: Optional[int] = Field(
        None,
        alias='messagesPerPage',
        description='Number of private messages and conversations on dialogue page',
    )
    entities_per_page: Optional[int] = Field(
        None, alias='entitiesPerPage', description='Number of other entities on page'
    )


class Rating(BaseModel):
    class Config:
        extra = Extra.forbid

    enabled: Optional[bool] = Field(None, description='Rating participation flag')
    quality: Optional[int] = Field(None, description='Quality rating')
    quantity: Optional[int] = Field(None, description='Quantity rating')


class BbParseMode(Enum):
    common = 'Common'
    info = 'Info'
    post = 'Post'
    chat = 'Chat'


class InfoBbText(BaseModel):
    class Config:
        extra = Extra.forbid

    value: Optional[StrictStr] = Field(None, description='Text')
    parse_mode: Optional[BbParseMode] = Field(None, alias='parseMode')


class ColorSchema(Enum):
    modern = 'Modern'
    pale = 'Pale'
    classic = 'Classic'
    classic_pale = 'ClassicPale'
    night = 'Night'


class UserSettings(BaseModel):
    class Config:
        extra = Extra.forbid

    color_schema: Optional[ColorSchema] = Field(None, alias='colorSchema')
    nanny_greetings_message: Optional[StrictStr] = Field(
        None,
        alias='nannyGreetingsMessage',
        description="Message that user's newbies will receive once they are connected",
    )
    paging: Optional[PagingSettings] = None


class UserRole(Enum):
    guest = 'Guest'
    player = 'Player'
    administrator = 'Administrator'
    nanny_moderator = 'NannyModerator'
    regular_moderator = 'RegularModerator'
    senior_moderator = 'SeniorModerator'


class UserDetails(BaseModel):
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
    icq: Optional[StrictStr] = Field(None, description='User ICQ number')
    skype: Optional[StrictStr] = Field(None, description='User Skype login')
    original_picture_url: Optional[StrictStr] = Field(
        None, alias='originalPictureUrl', description='URL of profile picture original'
    )
    info: Optional[InfoBbText] = None
    settings: Optional[UserSettings] = None


class UserDetailsEnvelope(BaseModel):
    class Config:
        extra = Extra.forbid

    resource: Optional[UserDetails] = None
    metadata: Optional[Any] = Field(None, description='Additional metadata')

#
# # ffffffffffffffffffffffffffffff
# class Roles(Enum):
#     GUEST = 'Guest'
#     PLAYER = 'Player'
#     ADMINISTRATOR = 'Administrator'
#     NANNY_MODERATOR = 'NannyModerator'
#     REGULAR_MODERATOR = 'RegularModerator'
#     SENIOR_MODERATOR = 'SeniorModerator'
#
#
# class ParseMode(Enum):
#     COMMON = 'Common'
#     INFO = 'Info'
#     POST = 'Post'
#     CHAT = 'Chat'
#
#
# class ColorSchema(Enum):
#     MODERN = 'Modern'
#     PALE = 'Pale'
#     CLASSIC = 'Classic'
#     CLASSIC_PALE = 'ClassicPale'
#     NIGHT = 'Night'
#
#
# class Rating(BaseModel):
#     enabled: StrictBool
#     quality: int
#     quantity: int
#
#
# class PagingSettings(BaseModel):
#     posts_per_page: Optional[int] = Field(alias='postsPerPage')
#     comments_per_page: Optional[int] = Field(alias='commentsPerPage')
#     topics_per_page: Optional[int] = Field(alias='topicsPerPage')
#     messages_per_page: Optional[int] = Field(alias='messagesPerPage')
#     entities_per_page: Optional[int] = Field(alias='entitiesPerPage')
#
#
# class InfoBbText(BaseModel):
#     value: StrictStr
#     parse_mode: List[ParseMode] = Field(alias='parseMode')
#
#
# class UserSettings(BaseModel):
#     color_schema: List[ColorSchema] = Field(alias='ColorSchema')
#     nanny_greetings_message: Optional[StrictStr] = Field(alias='nannyGreetingsMessage')
#     paging: PagingSettings
#
#
# class UserDetails(BaseModel):
#     login: StrictStr
#     roles: List[Roles]
#     medium_picture_url: Optional[StrictStr] = Field(alias='mediumPictureUrl')
#     small_picture_url: Optional[StrictStr] = Field(alias='smallPictureUrl')
#     status: Optional[StrictStr]
#     rating: Rating
#     online: Optional[str]
#     name: Optional[StrictStr]
#     location: Optional[StrictStr]
#     registration: Optional[str]
#     icq: Optional[StrictStr]
#     skype: Optional[StrictStr]
#     original_picture_url: Optional[StrictStr] = Field(alias='originalPictureUrl')
#     info: Optional[InfoBbText]
#     settings: Optional[UserSettings]
#
#
# class UserDetailsEnvelopeModel(BaseModel):
#     resource: UserDetails
#     metadata: Optional[StrictStr]
