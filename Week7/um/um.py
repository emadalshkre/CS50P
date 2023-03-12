import re
import sys


def main():
    print(count(input("Text: ")))


def count(s:str):
    objpattren = re.compile(r"(\bum\b)",re.IGNORECASE)
    match = objpattren.findall(s)
    return len(match)



...


if __name__ == "__main__":
    main()
