from __future__ import annotations

from pydantic import BaseModel, StrictStr


class ResponseLogout(BaseModel):
    message: StrictStr
