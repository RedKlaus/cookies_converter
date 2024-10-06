import json
from datetime import datetime
from re import Match, match
from typing import List, Dict, Any

from .jsoncookie import JsonCookie
from ..netscapecookies import NetscapeCookies


class JsonCookies(List[JsonCookie]):
    def __init__(self, json_cookies: List[JsonCookie] = None) -> None:
        super().__init__()
        if json_cookies is None:
            self.__json_cookies: List[JsonCookie] = []
        else:
            self.__json_cookies: List[JsonCookie] = json_cookies

    def append(self, json_cookie: JsonCookie) -> None:
        self.__json_cookies.append(json_cookie)

    def from_netscape(self, netscape_cookies: NetscapeCookies) -> "JsonCookies":
        for cookie in netscape_cookies:
            re_match: Match[str] = match(
                r'^([ -~]*)\t(TRUE|FALSE)\t(/[ -~]*)\t(TRUE|FALSE)\t([-0-9]*)\t([ -~]*)\t(.*|)$',
                cookie)
            # If not cookie
            if re_match is None:
                continue

            if len(re_match.groups()) != 7:
                continue

            host_only: bool = False if re_match.group(2) == "TRUE" else True
            http_only: bool = True if re_match.group(4) == "TRUE" else False

            cookie_data = {
                "domain": re_match.group(1).replace("#HttpOnly_", ''),
                "hostOnly": host_only,
                "path": re_match.group(3),
                "httpOnly": http_only,
                "expires": datetime.fromtimestamp(float(re_match.group(5))),
                "name": re_match.group(6),
                "value": re_match.group(7),
            }

            self.__json_cookies.append(JsonCookie(**cookie_data))
        return self

    def to_json(self) -> str:
        json_list: List[Dict[str, Any]] = []
        for cookie in self.__json_cookies:
            json_list.append(cookie.to_dict())
        return json.dumps(json_list)

    def __iter__(self):
        return iter(self.__json_cookies)

    def __repr__(self) -> str:
        return f"JsonCookies({self.__json_cookies})"
