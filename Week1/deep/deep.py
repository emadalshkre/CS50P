text = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
match text:
    case "42" | "forty-two" | "forty two":
        print("yes")
    case _:
        print("no")
