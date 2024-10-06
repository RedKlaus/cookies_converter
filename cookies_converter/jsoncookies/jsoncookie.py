from datetime import datetime
from typing import Any, Dict

from pydantic import BaseModel


class JsonCookie(BaseModel):
    def __int__(self):
        super().__int__()

    name: str
    value: str
    domain: str
    hostOnly: bool
    path: str
    httpOnly: bool
    expires: datetime

    def to_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'value': self.value,
            'domain': self.domain,
            'hostOnly': self.hostOnly,
            'path': self.path,
            'httpOnly': self.httpOnly,
            'expires': int(self.expires.timestamp()),
        }
