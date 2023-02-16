def main():
    text = face(input())
    print(text)

def face(to:str):
    to = to.replace(':)','🙂').replace(':(','🙁')
    return to

main()