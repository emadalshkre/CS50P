def main():
    st = input("camelCase: ")
    if check_camelcase(st):
        convert_snakecase(st)
    else:
        print("Not camelCase")


def check_camelcase(s:str):
    return s[0].islower() and have_space(s) == False


def have_space(s:str):
    if ' ' in s:
        return True
    else:
        return False
    

def convert_snakecase(s:str):
    print("snake_case: ", end="")
    for c in s:
        if c.isupper():
            print("_", end="")
        print(c.lower(), end="")
    print()
    return


main()