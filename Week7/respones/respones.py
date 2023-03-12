import validators

def main():
    print((validate(input("What's your email address? "))))

def validate(s:str):
    if validators.email(s):
        return "valid"
    else:
        return "invalid"

main()