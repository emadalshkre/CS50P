math = input("Expression: ")
x, z, y = math.split(" ")
x = int(x)
y = int(y)

match z:
    case "+":
        print(x + y)
    case "-":
        print(x - y)
    case "*":
        print(x * y)
    case "/":
        print( "{0:.1f}".format(x / y))