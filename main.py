from PIL import Image
def red_filter(r=0,image="frog.jpg"):
    newimagedata=[]
    while image.getdata():
        newimagedata.append(r,0,0)
    newimage=Image.new(image.size,image.mode)
    newimage.putdata(newimagedata)
    return newimage
def blue_filter(b=0,image="frog.jpg"):
    newimagedata = []
    while image.getdata():
        newimagedata.append(0, 0, b)
    newimage = Image.new(image.size, image.mode)
    newimage.putdata(newimagedata)
    return newimage
def green_filter(g=0,image="frog.jpg"):
    newimagedata = []
    while image.getdata():
        newimagedata.append(0, g, 0)
    newimage = Image.new(image.size, image.mode)
    newimage.putdata(newimagedata)
    return newimage
def purple_filter(r=0,b=0,image="frog.jpg"):
    newimagedata = []
    while image.getdata():
        newimagedata.append(r, 0, b)
    newimage = Image.new(image.size, image.mode)
    newimage.putdata(newimagedata)
    return newimage
def yellow_filter(g=0,b=0,image="frog.jpg"):
    newimagedata = []
    while image.getdata():
        newimagedata.append(0, g, b)
    newimage = Image.new(image.size, image.mode)
    newimage.putdata(newimagedata)
    return newimage
def lighter_filter(r=0,g=0,b=0,image="frog.jpg"):
    lighter=float(input("How much lighter would you like it (Enter number):"))
    newimagedata = []
    while image.getdata():
        newimagedata.append(r-lighter, g-lighter, b-lighter)
    newimage = Image.new(image.size, image.mode)
    newimage.putdata(newimagedata)
    return newimage
def darker_filter(r=0,g=0,b=0,image="frog.jpg"):
    darker=float(input("How dark would you like it (Enter number):"))
    newimagedata = []
    while image.getdata():
        newimagedata.append(r+darker, g+darker, b+darker)
    newimage = Image.new(image.size, image.mode)
    newimage.putdata(newimagedata)
    return newimage
def main():
    r,g,b=0,0,0
    image="frog.jpg"
    red_filter(r,image).save()

main()
