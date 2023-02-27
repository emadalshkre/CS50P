import pyfiglet
from sys import argv, exit


if len(argv) == 3:
    if argv[1] == "-f":
        try:
            f = pyfiglet.Figlet(font=argv[2])
            print(f.renderText(input("Input: ")))
        except pyfiglet.FontNotFound:
            exit("Wroung_Font")
    else:
        exit("program_name -f font")
elif len(argv) == 1:
        f = pyfiglet.Figlet(font="slant")
        print(f.renderText(input("Input: ")))