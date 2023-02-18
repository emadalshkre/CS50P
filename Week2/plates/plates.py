from string import punctuation

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s:str):
    if s[0:2].isalpha:
        if not s.isspace():
            if ispunctuation(s):
                if 2 <= len(s) <= 6:
                    if num_rules(s):
                        return True
    return False

def ispunctuation(s:str):
    for c in s:
        for t in punctuation:
            if c == t:
                return False
    return True

def num_rules(s:str):
    for i in range(len(s)):
        if s[i].isnumeric():
            if int(s[i]) == 0:
                return False
            for j in range(i,len(s)):
                if not s[j].isnumeric():
                    return False
            return True


main()
