import random



while True:
    try:
        limit = int(input("Level: "))
        if limit < 1:
            pass
        num = random.randrange(1,limit)
        while True:
            try:
                com = int(input("Guess: "))
                if com < 1:
                    continue
                if num < com:
                    print("Too large!")
                elif num > com:
                    print("Too small!")
                elif num == com:
                    print("Just right!")
                    exit()
            except ValueError:
                pass
    except ValueError:
        pass



