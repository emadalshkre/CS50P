import re

def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word:str):
    st = ""
    for i in range(len(word)):
        c = word[i]
        c = c.upper()
        if "A" != c != "E" and "I" != c != "O" and c != "U":
            st += word[i]
    return st

if __name__ == "__main__":
    main()
