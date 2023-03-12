import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s:str):
    matchpattren = re.compile(r"https?://(?:www\.)?youtube\.com/embed/(\w+|\d+)")

    if group := matchpattren.search(s):
        return f"https://youtu.be/{group.group(1)}"
    else:
        return None


...


if __name__ == "__main__":
    main()
