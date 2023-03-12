import re,sys
from PIL import Image,ImageDraw,ImageFont
from fpdf import FPDF

def main():
    name = get_name()
    create_image(name+" took CS50")
    file = pdf()
    file.output("shirtificate.pdf")

class pdf(FPDF):
    def header(self):
        self.set_font("helvetica","B",size=42)
        self.cell(0,60,txt="CS50 Shirtificate",align="C",new_x="CENTER",new_y="NEXT")

    def footer(self):
        self.image("nameonshirtificate.png","C",w=170)


def create_image(name:str):
    img = Image.open("shirtificate.png")
    w = img.width
    h = img.height
    txt = ImageDraw.Draw(img)
    textw,texth = txt.textsize(name) 

    font = ImageFont.truetype("C:\Windows\Fonts\AdobeFanHeitiStd-Bold",35)
    txt.text((w/2 - textw - 45, h/2 - texth - 150),name,file=(0,0,0),font=font,align="center")
    img.save("nameonshirtificate.png")

def get_name():
    pattren = re.compile(r"(.{1,46})")
    if match := pattren.search(input("Name: ")):
        return match.group(1)
    else:
        sys.exit("'Name Invalid'")


if __name__ == "__main__":
    main()