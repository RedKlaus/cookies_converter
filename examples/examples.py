from cookies_converter import JsonCookies, KeyValueCookies, NetscapeCookies


def main() -> None:
    netscape_cookies_from_file_content = NetscapeCookies().from_file_content("netscapecookies.txt")
    json_cookies_from_file_content = JsonCookies().from_file_content("jsoncookies.json")
    key_value_cookies_from_json = KeyValueCookies().from_json("netflix.com", json_cookies_from_file_content)
    key_value_cookies_from_netscape = KeyValueCookies().from_netscape("netflix.com", netscape_cookies_from_file_content)


if __name__ == '__main__':
    main()
