from PIL import Image
from PIL import ImageFilter

def red(r=0,image="frog.jpg"):
    newimagedata=[]
    while image.getdata():
        newimagedata.append(r,0,0)
    newimage=Image.new(image.size,image.mode)
    newimage.putdata(newimagedata)
    return newimage


def blue(b=0,image="frog.jpg"):
    newimagedata = []
    while image.getdata():
        newimagedata.append(0, 0, b)
    newimage = Image.new(image.size, image.mode)
    newimage.putdata(newimagedata)
    return newimage


def green(g=0,image="frog.jpg"):
    newimagedata = []
    while image.getdata():
        newimagedata.append(0, g, 0)
    newimage = Image.new(image.size, image.mode)
    newimage.putdata(newimagedata)
    return newimage


def purple(r=0,b=0,image="frog.jpg"):
    newimagedata = []
    while image.getdata():
        newimagedata.append(r, 0, b)
    newimage = Image.new(image.size, image.mode)
    newimage.putdata(newimagedata)
    return newimage


def yellow(g=0,b=0,image="frog.jpg"):
    newimagedata = []
    while image.getdata():
        newimagedata.append(0, g, b)
    newimage = Image.new(image.size, image.mode)
    newimage.putdata(newimagedata)
    return newimage


def light(r=0,g=0,b=0,image="frog.jpg"):
    lighter=float(input("How much lighter would you like it (Enter number):"))
    newimagedata = []
    while image.getdata():
        newimagedata.append(r-lighter, g-lighter, b-lighter)
    newimage = Image.new(image.size, image.mode)
    newimage.putdata(newimagedata)
    return newimage


def dark(r=0,g=0,b=0,image="frog.jpg"):
    darker=float(input("How dark would you like it (Enter number):"))
    newimagedata = []
    while image.getdata():
        newimagedata.append(r+darker, g+darker, b+darker)
    newimage = Image.new(image.size, image.mode)
    newimage.putdata(newimagedata)
    return newimage





def user_input():
    value = eval(input("Blur Amount: "))
    return value


def blur(mod_img):
    new_img = (mod_img.convert('RGB'))
    for i in range(user_input()):
        new_img = new_img.filter(ImageFilter.BLUR)
    return new_img
