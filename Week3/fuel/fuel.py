while True:
    try:
        x, y = input("Fraction: ").split("/")
        z = int(int(x) / int(y) * 100)
        if z > 100 or z < 0:
            continue
        if z >= 99:
            print("F")
        elif z <= 1:
            print("E")
        else:
            print(f"{z}%")
        break
    except (ValueError, ZeroDivisionError):
        pass
