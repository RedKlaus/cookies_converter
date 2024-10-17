import requests

from cookies_converter import CookiesConverter


def main() -> None:
    converter = CookiesConverter()
    converter.from_netscape(open('netscape_cookies.txt', 'r', encoding="utf-8").read())

    response = requests.get('https://www.netflix.com/', cookies=converter.to_key_value("netflix.com"))
    print(response.status_code)


if __name__ == '__main__':
    main()
