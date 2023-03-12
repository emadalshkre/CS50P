import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip:str):
    obj = re.compile(r"^(?:(?:[0-2][0-5][0-5]|[0-1]?[0-9]?[0-9])\.){3}(?:[0-2][0-5][0-5]|[0-1]?[0-9]?[0-9])$")
    match = obj.search(ip)
    print(match)
    if match:
        return True
    else:
        return False

...


if __name__ == "__main__":
    main()
