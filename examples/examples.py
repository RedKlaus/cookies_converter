from cookies_converter.cookies_converter import CookiesConverter


def read_file(file: str) -> str:
    with open(file, 'r', encoding='utf-8') as _open_file:
        cookies_content = _open_file.read()
    return cookies_content


def print_formats_cookies(converter: CookiesConverter, domain: str) -> None:
    print("Netscape cookies: ", converter.to_netscape(domain))
    print("Json cookies: ", converter.to_json(domain))
    print("Key value cookies: ", converter.to_key_value(domain))


def main() -> None:
    converter = CookiesConverter()
    domain = "netflix.com"

    converter.from_netscape(read_file("netscape_cookies.txt"))
    print_formats_cookies(converter, domain)
    converter.clear_cookies()
    print("----------------------------")

    converter.from_json(read_file("json_cookies.json"))
    print_formats_cookies(converter, domain)


if __name__ == '__main__':
    main()
