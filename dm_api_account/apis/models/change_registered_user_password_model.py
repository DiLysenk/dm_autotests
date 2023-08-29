from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, StrictStr, Field


class RequestRegisteredUserPassword(BaseModel):
    login: StrictStr
    token: StrictStr
    oldPassword: StrictStr
    newPassword: StrictStr


class Rating(BaseModel):
    enabled: bool
    quality: int
    quantity: int


class Resource(BaseModel):
    login: StrictStr
    roles: List[str]
    medium_picture_url: Optional[StrictStr] = Field(alias='mediumPictureUrl')
    small_picture_url: Optional[StrictStr] = Field(alias='smallPictureUrl')
    status: StrictStr
    rating: Rating
    online: StrictStr
    name: StrictStr
    location: StrictStr
    registration: StrictStr


class ResponseRegisteredUserPassword(BaseModel):
    resource: Resource
    metadata: StrictStr


class InvalidProperties(BaseModel):
    additional_prop1: List[str] = Field(alias='additionalProp1')
    additional_prop2: List[str] = Field(alias='additionalProp2')
    additional_prop3: List[str] = Field(alias='additionalProp3')


class BadResponseModel(BaseModel):
    message: StrictStr
    invalid_properties: InvalidProperties = Field(alias='invalidProperties')
