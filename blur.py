from PIL import ImageFilter


def user_input():
    value = eval(input("Blur Amount: "))
    return value


def blur(mod_img):
    for i in range(user_input()):
        mod_img = mod_img.filter(ImageFilter.BLUR)
    return mod_img
