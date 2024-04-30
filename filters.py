from PIL import Image, ImageFilter, ImageEnhance
def red(image):
    image.convert('RGB')
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            image.putpixel((x, y), (r, 0, 0))
    return image
def blue(image):
    image.convert('RGB')
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            image.putpixel((x, y), (0, 0, b))
    return image
def green(image):
    image.convert('RGB')
    width, height = image.size
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            image.putpixel((x, y), (0, g, 0))
    return image
def purple(image):
    image.convert('RGB')
    width, height = image.size
    for x in range(width):
        for y in range(height):
            cord1, cord2, r, g, b = image.getpixel((x, y), (red, green, blue))
            r = r*.63
            g = g*.13
            b = b*.94
            image.putpixel((x, y), (r, g, b))
    return image
def yellow(image):
    image.convert('RGB')
    width, height = image.size
    for x in range(width):
        for y in range(height):
            cord1, cord2, r, g, b = image.getpixel((x, y), (red, green, blue))
            image.putpixel((x, y), (r, g, 0))
    return image


def light(image):
    image.convert('RGB')
    width, height = image.size
    lighter = int(input("How much lighter would you like it (Enter number):"))
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            r = r-lighter
            g = g-lighter
            b = b-lighter
            image.putpixel((x, y), (r, g, b))
    return image


def dark(image):
    image.convert('RGB')
    width, height = image.size
    darker = int(input("How much lighter would you like it (Enter number):"))
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            r = r + darker
            g = g + darker
            b = b + darker
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
