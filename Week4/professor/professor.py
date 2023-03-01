import random


def main():
    score = 0
    equl = 0
    level = get_level()
    for i in range(10):
        n1,n2,sum = generate_integer(level)

        for i in range(3):
            try:
                print(f"{n1} + {n2} = ",end="")
                equl =int(input())
                if equl != sum:
                    print("EEE")
                elif equl == sum:
                    score += 1
                    break
            except ValueError:
                print("EEE")
                pass

        if equl != sum:
            print(f"{n1} + {n2} = {sum}")
    print(f"score: {score}")



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
        except ValueError:
            pass


def generate_integer(level):
    num1 = random.randrange(10**(level-1),10**(level))
    num2 = random.randrange(10**(level-1),10**(level))
    return num1,num2,num1 + num2



if __name__ == "__main__":
    main()
