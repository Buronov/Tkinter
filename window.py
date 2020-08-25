from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Window")

def open():
    global my_img
    top = Toplevel()
    top.title("Second Window")
    my_img = ImageTk.PhotoImage(Image.open("e:/조니벡/coding course/english course/TKINTER/practise/doktor3.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn = Button(top, text="Close", command=top.destroy).pack() # Close application

btn = Button(root, text="Open second Window", command=open).pack()



root.mainloop()