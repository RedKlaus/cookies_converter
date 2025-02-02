import json
import re
from datetime import datetime
from typing import Self, List, Dict, Any, Optional

from cookies_converter.json_cookies import CookieData, JsonCookies
from cookies_converter.netscape_cookies import NetscapeCookies


class CookiesConverter(object):
    def __init__(self):
        self.__cookies: List[CookieData] = []

    def from_netscape(self, netscape_cookies: str) -> Self:
        found_cookies = re.findall(
            r'^([ -~]*)\t(TRUE|FALSE)\t(/[ -~]*)\t(TRUE|FALSE)\t([-0-9]*)\t([ -~]*)\t(.*|)$',
            netscape_cookies, re.RegexFlag.MULTILINE)
        for netscape_cookie_params in found_cookies:
            cookie_data = CookieData(
                domain=netscape_cookie_params[0],
                hostOnly=bool(netscape_cookie_params[1]),
                path=netscape_cookie_params[2],
                httpOnly=bool(netscape_cookie_params[3]),
                expirationDate=netscape_cookie_params[4],
                name=netscape_cookie_params[5],
                value=netscape_cookie_params[6])
            self.__add_cookie(cookie_data)
        return self

    def from_json(self, json_cookies: str) -> Self:
        try:
            json_content: List[Dict[str, Any]] = json.loads(json_cookies)
        except json.decoder.JSONDecodeError:
            return self

        for json_cookie in json_content:
            expiration_date: Optional[datetime] = None
            if json_cookie.get("expirationDate") is not None:
                expiration_date: datetime = datetime.fromtimestamp(float(json_cookie["expirationDate"]))
            elif json_cookie.get("expirationDate") is not None:
                expiration_date: datetime = datetime.fromtimestamp(float(json_cookie["expirationDate"]))

            host_only = None
            if json_cookie.get("secure"):
                host_only = bool(json_cookie.get("secure"))
            elif json_cookie.get("hostOnly"):
                host_only = bool(json_cookie.get("hostOnly"))

            self.__add_cookie(CookieData(
                domain=json_cookie["domain"],
                hostOnly=host_only,
                path=json_cookie["path"],
                httpOnly=bool(json_cookie["httpOnly"]),
                expirationDate=expiration_date,
                name=json_cookie["name"],
                value=json_cookie["value"],
            ))
        return self

    def __get_cookies_from_domain(self, domain: str) -> List[CookieData]:
        cookies: List[CookieData] = []
        for cookie in self.__cookies:
            if cookie.domain.endswith(domain):
                cookies.append(cookie)
        return cookies

    def to_json(self, domain: str) -> JsonCookies:
        return JsonCookies(self.__get_cookies_from_domain(domain))

    def to_netscape(self, domain: str) -> NetscapeCookies:
        return NetscapeCookies(self.__get_cookies_from_domain(domain))

    def to_key_value(self, domain: str) -> Dict[str, Any]:
        cookies_buffer: Dict[str, Any] = {}
        for cookie in self.__cookies:
            if cookie.domain.endswith(domain):
                cookies_buffer[cookie.name] = cookie.value
        return cookies_buffer

    def __add_cookie(self, cookie: CookieData) -> None:
        self.__cookies.append(cookie)

    def clear_cookies(self) -> None:
        self.__cookies.clear()
