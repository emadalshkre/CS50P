st = input("Input: ")
for s in st:
    letter = s.upper()
    if "A" != letter != "E" and "I" != letter != "O" and letter != "U":
        print(s, end="")
print()