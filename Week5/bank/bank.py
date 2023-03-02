def main():
    word = input("Input: ")
    print(value(word))


def value(greeting:str):
    greeting =greeting.lower()
    if "hello" in greeting:
        return 0 
    elif "h" == greeting[0]:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
