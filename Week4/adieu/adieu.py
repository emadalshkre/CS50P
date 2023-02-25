import inflect
p = inflect.engine()
list  = []
while True:
    try:
        list.append(input("Name: ").replace(" ", ""))
    except EOFError:
        print("\nAdieu, adieu, to",p.join(list))
        exit()