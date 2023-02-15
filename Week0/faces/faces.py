def main():
    text = face(input())
    print(text)

def face(to):
    to = to.replace(':)','🙂').replace(':(','🙁')
    return to

main()