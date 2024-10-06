from re import Match, match
from typing import List


class NetscapeCookies(List[str]):
    def __init__(self, netscape_cookies: List[str] = None) -> None:
        super().__init__()
        if netscape_cookies is None:
            self.__netscape_cookies: List[str] = []
        else:
            self.__netscape_cookies: List[str] = netscape_cookies

    def from_file_content(self, file: str) -> "NetscapeCookies":
        with open(file, "r", encoding="utf-8", errors="ignore") as opened_file:
            for netscape_cookie in opened_file:
                netscape_cookie = netscape_cookie.strip()
                re_match: Match[str] = match(
                    r'^([ -~]*)\t(TRUE|FALSE)\t(/[ -~]*)\t(TRUE|FALSE)\t([-0-9]*)\t([ -~]*)\t(.*|)$',
                    netscape_cookie)
                # If not cookie
                if re_match is None:
                    continue
                self.__netscape_cookies.append(netscape_cookie)
        return self

    def __iter__(self):
        return iter(self.__netscape_cookies)

    def __str__(self) -> str:
        return str(self.__netscape_cookies)
