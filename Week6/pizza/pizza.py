import sys
import csv
from tabulate import tabulate


list = []

length = len(sys.argv)
if length < 2:
    print("Too few command-line arguments")
    sys.exit()
elif length > 2:
    print("Too many command-line arguments")
    sys.exit()
elif sys.argv[1][-3:] != "csv":
    print("Not a Python file")
    sys.exit()
else:
    try:
        with open(sys.argv[1], "r") as csvfile:
            rows = csv.reader(csvfile)
            for line in rows:
                list.append(line)
            print(tabulate(list,headers="firstrow" ,tablefmt="grid"))
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()