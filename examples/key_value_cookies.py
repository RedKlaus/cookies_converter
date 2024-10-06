from cookies_converter import KeyValueCookies, JsonCookies, NetscapeCookies


def main() -> None:
    json_cookies = JsonCookies().from_file_content("jsoncookies.json")
    print(KeyValueCookies().from_json("netflix.com", json_cookies))
    netscape_cookies = NetscapeCookies().from_file_content("netscapecookies.txt")
    print(KeyValueCookies().from_netscape("netflix.com", netscape_cookies))


if __name__ == '__main__':
    main()
