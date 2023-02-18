coins = 50
while True:
    cents = int(input("Insert Coin: "))
    if cents < 0:
        continue
    coins -= cents
    if coins <= 0:
        break
    print("Amount Due:",coins)