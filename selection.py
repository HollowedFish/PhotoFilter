from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def valid_name(image_name):
    found = image_name.find(".png")
    found = image_name.find(".JPG")
    found = image_name.find(".gif")
    found = image_name.find(".jpeg")
    if found != 0:
        return True
    return False


def get_file_path():
    Tk().withdraw()
    filename = askopenfilename()
    if valid_name(filename) is not True:
        print("Please select a valid file")
        filename = askopenfilename()
    return filename


def input_validation(width, height, left, upper, right, lower):
    values = [left, upper, right, lower]
    for direction in values:
        if direction < 1:
            values[direction] = eval(input("Enter a value greater than or equal to 1."))
    while values[2] > width:
        values[2] = eval(input("Enter a right value less than or equal to " + str(width)))
    while values[0] > width:
        values[0] = eval(input("Enter a left value less than or equal to " + str(width)))
    while values[1] > height:
        values[1] = eval(input("Enter an upper value less than or equal to " + str(height)))
    while values[3] > height:
        values[3] = eval(input("Enter a lower value less than or equal to " + str(height)))
    return values


def user_input(width, height):
    print("Enter 4 integers indicating the start and end pixels of your selection.")
    print("Values must be at least 1. Right/Lower must be less than " + str(width) + "/" + str(height) + ".")
    left, upper, right, lower = eval(input("Left, Upper, Right, Lower: "))
    values = input_validation(width, height, left, upper, right, lower)
    return values


def crop_image():
    im = Image.open(get_file_path())
    width, height = im.size
    values = user_input(width, height)
    crop_rectangle = (values[0], values[1], values[2], values[3])
    cropped_im = im.crop(crop_rectangle)
    cropped_im.show()
    return im, cropped_im, values


def join_filter(image, cropped_image, values):
    image.paste(cropped_image, values)
    image_name = input("Enter name for new image INCLUDING format i.e \"photo.png\" (.jpg, .png, .jpeg, .gif)")
    while valid_name(image_name) is not True:
        image_name = input("Names must include file format at the end, please try again.")
    image.save(image_name)
    return image


def main():
    image, cropped_image, values = crop_image()
    #Insert a filter here using cropped_image as image input
    result_image = join_filter(image, cropped_image, values)
    result_image.show()
    print("This is the resulting image.")


main()
