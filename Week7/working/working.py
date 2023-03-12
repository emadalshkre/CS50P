import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s:str):
    matchpattren = re.compile(r"((?:[0-9]|[1][0-2])(?::[0-5][0-9]|:[6][0])?) (AM|PM) to ((?:[0-9]|[1][0-2])(?::[0-5][0-9]|:[6][0])?) (AM|PM)")
    if match := matchpattren.search(s):

        time1 = match.group(1)
        time2 = match.group(3)

        if ":" in time1:
            sthour1, stminute1 = time1.split(":")
        else:
            sthour1 = time1
            stminute1 = "00"
        if ":" in time2:
            sthour2, stminute2 = time2.split(":")
        else:
            sthour2 = time2
            stminute2 = "00"

        if match.group(2) == "PM":
            sthour1 = int(sthour1) + 12

        if match.group(4) == "PM":
            sthour2 = int(sthour2) + 12    

        sthour1 = int(sthour1)
        sthour2 = int(sthour2)
        stminute1 = int(stminute1)
        stminute2 = int(stminute2)
        return f"{sthour1:02}:{stminute1:02} to {sthour2:02}:{stminute2:02}"
    else:
        raise ValueError


...


if __name__ == "__main__":
    main()
