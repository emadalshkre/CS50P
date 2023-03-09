import sys

length = len(sys.argv)
if length < 2:
    print("Too few command-line arguments")
    sys.exit()
elif length > 2:
    print("Too many command-line arguments")
    sys.exit()
elif sys.argv[1][-3:] != ".py":
    print("Not a Python file")
    sys.exit()
else:
    try:
        file = open(sys.argv[1], "r")
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()

line = []
for row in file:
    if not row.startswith("#") and row != "\n":
        line.append(row)

print(len(line))
file.close()
