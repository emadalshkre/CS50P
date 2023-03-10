import sys
import csv


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
        before = open(sys.argv[1], "r")
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()

fieldname = ["first","last","house"]
with open("after.csv", "w") as after:
    writer = csv.DictWriter(after, fieldnames=fieldname)
    writer.writeheader()
    reader = csv.DictReader(before)
    for line in reader:
        first,last = line["name"].split(", ")
        writer.writerow({"first":first,"last":last,"house":line['house']})

before.close()