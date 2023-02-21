table = []
while True:
    try:
        name = input().upper()
        table.append(name)
    except EOFError:
        for i in range(len(table)):
            print(i + 1, table[i])
        break
