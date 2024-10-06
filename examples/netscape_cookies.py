from cookies_converter import NetscapeCookies


def main() -> None:
    netscape_cookies = NetscapeCookies().from_file_content("netscapecookies.txt")
    print(netscape_cookies)


if __name__ == '__main__':
    main()
