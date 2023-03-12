import sys, os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    print("Too few command-line arguments") 
    sys.exit()
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit()

root1,ext1 = os.path.splitext(sys.argv[1])
root2,ext2 = os.path.splitext(sys.argv[2])

if ext1 != ".jpg" and ext1 != ".jpeg" and ext1 != ".png":
    print("Invalid output")
    sys.exit()
elif ext2 != ext1:
    print("Input and output have different extensions")
    sys.exit()
else:
    try:
        before = Image.open(sys.argv[1])
    except FileNotFoundError:
        print("Input does not exist")
        sys.exit()

wid = 500
hei = 550

width,height = before.size
shirt = Image.open("shirt.png")
widshirt, heishirt = shirt.size
shirt = shirt.resize((widshirt + wid, heishirt + hei))
widshirt, heishirt = shirt.size

left = (width - widshirt)/2 
top = (height - heishirt)/2 
right = (width + widshirt)/2 
bottom = (height + heishirt)/2 

before = before.crop((left, top, right , bottom))

before.paste(shirt,shirt)



root3,ext3 = os.path.splitext(sys.argv[2])
before.save(f"{root3}.png")