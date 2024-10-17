from typing import List

from cookies_converter.json_cookies import CookieData


class NetscapeCookies:
    def __init__(self, netscape_cookies: List[CookieData] = None) -> None:
        if netscape_cookies is None:
            self.__cookies: List[CookieData] = []
        else:
            self.__cookies: List[CookieData] = netscape_cookies

    def add_cookie(self, cookie: CookieData) -> None:
        self.__cookies.append(cookie)

    def to_multiline(self) -> List[str]:
        lines = []
        for cookie in self.__cookies:
            host_only = str(cookie.hostOnly).upper()
            http_only = str(cookie.httpOnly).upper()
            expiration_date = int(cookie.expirationDate.timestamp())
            lines.append(f"{cookie.domain}\t{host_only}\t{cookie.path}\t{http_only}"
                         f"\t{expiration_date}\t{cookie.name}\t{cookie.value}")
        return lines

    def to_file_format(self) -> str:
        lines = ["# Netscape HTTP Cookie File",
                 "# https://curl.se/rfc/cookie_spec.html"]
        lines.extend(self.to_multiline())
        return "\n".join(lines)

    def __iter__(self):
        return iter(self.__cookies)

    def __str__(self) -> str:
        return str(self.to_multiline())

    def __getitem__(self, item: int) -> CookieData:
        return self.__cookies[item]
