import sys,re,inflect
from datetime import date, timedelta



def main():
    year, month, day = get_date()
    try:
        birthdate = date(int(year),int(month),int(day))
    except ValueError:
        sys.exit("Date out of range")

    time = get_minutes(birthdate)
    print(time)



def get_date():
    pattren = re.compile("(\d+)-(\d+)-(\d+)")
    if match := pattren.search(input("date: ")):
        return [match.group(1), match.group(2), match.group(3)]
    else:
        sys.exit("Not Valid date")

def get_minutes(birthdate:timedelta):
    deltatime = date.today() - birthdate
    minutes = deltatime.total_seconds() / 60 
    p = inflect.engine()
    return f"{p.number_to_words(minutes)}, minutes"



if __name__ == "__main__":
    main()
