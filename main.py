from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import filters as fl


def valid_name(image_name):
    if image_name.find(".png") != -1:
        return True
    if image_name.find(".gif") != -1:
        return True
    return False


def valid_open_name(image_name):
    if image_name.find(".png") != -1:
        return True
    if image_name.find(".jpg") != -1:
        return True
    if image_name.find(".jpeg") != -1:
        return True
    if image_name.find(".gif") != -1:
        return True
    return False


def get_file_path():
    Tk().withdraw()
    print("Please select a valid file, png, jpg, jpeg, or gif")
    filename = askopenfilename()
    if valid_open_name(filename) is not True:
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
    while values[2] > values[0]:
        values[2] = eval(input("Right value must be greater than left value "))
    while values[3] > values[1]:
        values[3] = eval(input("Lower value must be greater than upper value "))
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
    return im, cropped_im, values


def join_filter(image, cropped_image, values):
    image = image.convert('RGB')
    image.paste(cropped_image, values)
    image_name = input("Enter name for new image INCLUDING format i.e \"photo.png\" (.png, .gif)")
    is_valid = valid_name(image_name)
    while is_valid is False:
        image_name = input("Names must include file format at the end, please try again.")
        is_valid = valid_name(image_name)
    image.save(image_name)
    return image


def choose_filter():
    filters = ["blur", "red", "blue", "green", "purple", "yellow", "orange", "light", "dark", "sharpness", "contrast", "BW"]
    for (i, filt) in enumerate(filters):
        print("Type " + str(i) + " for " + str(filt))
    choice = input()
    return choice


def apply_filter(choice, image):
    if choice == '0':
        return fl.blur(image)
    elif choice == '1':
        return fl.red(image)
    elif choice == '2':
        return fl.blue(image)
    elif choice == '3':
        return fl.green(image)
    elif choice == '4':
        return fl.purple(image)
    elif choice == '5':
        return fl.yellow(image)
    elif choice == '6':
        return fl.orange(image)
    elif choice == '7':
        return fl.light(image)
    elif choice == '8':
        return fl.dark(image)
    elif choice == '9':
        return fl.sharpness(image)
    elif choice == '10':
        return fl.contrast(image)
    elif choice == '11':
        return fl.bw(image)
    else:
        print("Selection results in an identical image.")
        return image


def main():
    image, cropped_image, values = crop_image()
    partial = apply_filter(choose_filter(), cropped_image)
    result_image = join_filter(image, partial, values)
    result_image.show()
    print("This is the resulting image.")


main()
