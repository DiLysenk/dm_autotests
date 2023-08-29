from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, StrictStr, Field


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


class ResponseActivated(BaseModel):
    resource: Resource
    metadata: StrictStr


class TokenInvalid(BaseModel):
    massege: StrictStr


class TokenExpired(BaseModel):
    massege: StrictStr
