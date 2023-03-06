from string import punctuation

def main():
    name = input("Input: ")
    print(is_valid(name))


def is_valid(s:str):
    le = len(s)
    if le < 2 or le > 6:
        return False
    if not s[0:2].isalpha() or 2 > le > 6:
        return False

    for i in range(le):
        if s[i] in punctuation:
            return False

    for i in range(le):
        if s[i].isnumeric():
            if s[i] == "0":
                return False
            for j in range(i,le):
                if s[j].isalpha():
                    return False
            return True
    return True


if __name__ == "__main__":
    main()
