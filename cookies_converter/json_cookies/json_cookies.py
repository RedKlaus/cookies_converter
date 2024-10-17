import json
from typing import List, Dict, Any

from cookies_converter.cookie_data import CookieData


class JsonCookies:
    def __init__(self, json_cookies: List[CookieData] = None) -> None:
        if json_cookies is None:
            self.cookies: List[CookieData] = []
        else:
            self.cookies: List[CookieData] = json_cookies

    def add_cookie(self, json_cookie: CookieData) -> None:
        self.cookies.append(json_cookie)

    def to_json(self) -> str:
        json_list: List[Dict[str, Any]] = []
        for cookie in self.cookies:
            json_list.append(cookie.to_dict())
        return json.dumps(json_list)

    def __iter__(self):
        return iter(self.cookies)

    def __str__(self):
        return self.to_json()

    def __getitem__(self, item: int) -> CookieData:
        return self.cookies[item]
