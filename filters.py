from PIL import ImageFilter, ImageEnhance


def red(image):
    image = image.convert('RGB')
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            image.putpixel((x, y), (r, 0, 0))
    return image


def blue(image):
    image = image.convert('RGB')
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            image.putpixel((x, y), (0, 0, b))
    return image


def green(image):
    image = image.convert('RGB')
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            image.putpixel((x, y), (0, g, 0))
    return image


def purple(image):
    image = image.convert('RGB')
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            r = int(r*.63)
            g = int(g*.13)
            b = int(b*.94)
            image.putpixel((x, y), (r, g, b))
    return image
def orange(image):
    image.convert('RGB')
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            g= int(g*.65)
            image.putpixel((x, y), (r, g, 0))
    return image
def pink(image):
    image.convert('RGB')
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            r= int(r*.9)
            g = int(g*.45)
            b = int(b*.75)
            image.putpixel((x, y), (r, g, b))
    return image
def yellow(image):
    image = image.convert('RGB')
    width, height = image.size
    for x in range(width):
        for y in range(height):
<<<<<<< Updated upstream
            r, g, b = image.getpixel((x, y))
=======
            r, g, b = image.getpixel((x, y), (red, green, blue))
>>>>>>> Stashed changes
            image.putpixel((x, y), (r, g, 0))
    return image


def light(image):
    image = image.convert('RGB')
    width, height = image.size
    lighter = int(input("How much lighter would you like it (Enter number):"))
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            r = r-lighter
            if r < 0:
                r = 0
            g = g-lighter
            if g < 0:
                g = 0
            b = b - lighter
            if b < 0:
                b = 0
            image.putpixel((x, y), (r, g, b))
    return image


def dark(image):
    image = image.convert('RGB')
    width, height = image.size
    darker = int(input("How much darker would you like it (Enter number):"))
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            r = r - darker
            if r > 255:
                r = 255
            g = g - darker
            if g >255:
                g = 255
            b = b - darker
            if b > 255:
                b = 255
            image.putpixel((x, y), (r, g, b))
    return image


def blur(mod_img):
    value = eval(input("Blur Amount: "))
    new_img = (mod_img.convert('RGB'))
    for i in range(value):
        new_img = new_img.filter(ImageFilter.BLUR)
    return new_img


def sharpness(image):
    enhancer = ImageEnhance.Sharpness(image.convert('RGB'))
    value = eval(input("Sharpness Amount: "))
    return enhancer.enhance(value)


def contrast(image):
    enhancer = ImageEnhance.Contrast(image.convert('RGB'))
    value = eval(input("Contrast Amount: "))
    return enhancer.enhance(value)


def bw(image):
    return image.convert("L")
