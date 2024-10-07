from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel


class JsonCookie(BaseModel):
    name: str
    value: str
    domain: str
    hostOnly: bool
    path: str
    httpOnly: bool
    expirationDate: Optional[datetime]

    def to_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'value': self.value,
            'domain': self.domain,
            'hostOnly': self.hostOnly,
            'path': self.path,
            'httpOnly': self.httpOnly,
            'expirationDate': int(
                self.expirationDate.timestamp()) if self.expirationDate is not None else self.expirationDate,
        }
