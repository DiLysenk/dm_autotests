from __future__ import annotations

from pydantic import BaseModel, StrictStr


class ResponseLogoutEveryDevice(BaseModel):
    message: StrictStr
