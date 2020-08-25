from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()
root.title("Open files")
root.geometry("400x400")



def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="e:/조니벡/coding course/english course/TKINTER/practise", title="Select a file", filetypes=(("jpg files", "*.jpg"), ("All files", "*.*")))
    # my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


btn = Button(root, text="Open file", command=open).pack()

root.mainloop()