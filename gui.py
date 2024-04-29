from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("Python Final Image Editor")
root.geometry("800x600")
root.config(bg="black")
label=Label(root, text="Image: ", bg="black")
label.place(relx=.5,rely=.5, anchor = CENTER)
img_path=""

def openFile():
    global img_path
    img_path = filedialog.askopenfilename(title=" Open Image File", filetypes=[("Image Files","*.jpg *.gif *.jpg *.png *.jpeg")])
    print(img_path)
    img = ImageTk.PhotoImage(Image.open(img_path))
    label["image"]=img
    img.close()

btn = Button(root, text="Open Image", command = openFile)
btn.place(relx=.5, rely=.1, anchor = CENTER)

root.mainloop()