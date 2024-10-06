from cookies_converter import JsonCookies


def main() -> None:
    json_cookies = JsonCookies().from_file_content("jsoncookies.json")
    print(json_cookies)
    print(json_cookies.to_json())


if __name__ == '__main__':
    main()
