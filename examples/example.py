from datetime import datetime

from cookies_converter import JsonCookies, KeyValueCookies, NetscapeCookies
from cookies_converter.jsoncookies import JsonCookie


def main() -> None:
    netscape_cookies = NetscapeCookies().from_file_content("netscapecookies.txt")
    # or
    # netscape_cookies = NetscapeCookies([".netflix.com,	TRUE	/	TRUE	1759779995	NetflixId	value"])
    # print(netscape_cookies)

    json_cookies = JsonCookies().from_netscape(netscape_cookies)
    # or
    # json_cookies = JsonCookies([JsonCookie(
    #     name="NetflixId",
    #     value="value",
    #     domain=".netflix.com",
    #     hostOnly=False,
    #     path="/",
    #     httpOnly=True,
    #     expires=datetime.now()
    # )])
    # print(json_cookies)

    key_value_cookies = KeyValueCookies().from_json("netflix.com", json_cookies)
    # or
    # key_value_cookies = KeyValueCookies({"NetflixId": "value"})
    print(key_value_cookies)


if __name__ == '__main__':
    main()
