from typing import Dict, Any

from ..jsoncookies import JsonCookies
from ..netscapecookies import NetscapeCookies


class KeyValueCookies(Dict[str, Any]):
    def __init__(self, key_value_cookies: Dict[str, Any] = None):
        super().__init__()
        if key_value_cookies is None:
            self.__key_value_cookies = {}
        else:
            self.__key_value_cookies = key_value_cookies

    def from_json(self, domain: str, json_cookies: JsonCookies) -> "KeyValueCookies":
        for cookie in json_cookies:
            if '.'.join(cookie.domain.split('.')[1:]) == domain:
                self.__key_value_cookies[cookie.name] = cookie.value
        return self

    def from_netscape(self, domain: str, netscape_cookies: NetscapeCookies) -> "KeyValueCookies":
        json_cookies = JsonCookies().from_netscape(netscape_cookies)
        return self.from_json(domain, json_cookies)

    def __str__(self) -> str:
        return str(self.__key_value_cookies)
