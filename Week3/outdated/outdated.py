months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    while True:
        try:
            date = input()
            if prdate(date):
                break
        except EOFError:
            break



def prdate(s:str):
    count = 0
    space = 0
    comma = 0
    for i in range(len(s)):
        if s[i] == ' ':
            space += 1
        if s[i] == ',':
            comma += 1
        if s[i] == '/':
            count += 1
    if space == 2 and comma == 1:
        f1, year = s.split(',')
        month, day = f1.split(' ')
        month.title()
        try:
            for i in range(len(months)):
                if months[i] == month and 0 < int(day) <= 31 and 0 < int(year) < 2024:
                    print(f"{year}-{i + 1}-{day}")
                    return True
        except UnboundLocalError:
            pass
    if count == 2:
        month, day, year = s.split('/')
        try:
            if 0 < int(day) <= 31 and 0 < int(month) <= 12 and 0 < int(year) < 2024:
                print(f"{year}-{month}-{day}")
                return True
        except UnboundLocalError:
            pass

main()