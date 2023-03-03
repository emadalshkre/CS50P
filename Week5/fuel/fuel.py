from sys import exit

def main():
    fuel = input("")
    gauge(convert(fuel))


def convert(fraction:str):
    try:
        x,y = fraction.split("/")
        return int(x) / int(y) * 100
    except (ValueError, ZeroDivisionError,TypeError):
        print("TypeError")
        exit()


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return str(percentage)


if __name__ == "__main__":
    main()
