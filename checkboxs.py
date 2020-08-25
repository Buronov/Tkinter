from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Sliders")
root.geometry("400x400")

def show():
    mylabel = Label(root, text=var.get()).pack()
    # if c == "on":
    #     Label(root, text="ok").pack()
    # else:
    #     Label(root, text="error").pack()
    
var = StringVar()

c = Checkbutton(root, text="Check it", variable=var, onvalue="on", offvalue="off")
c.deselect()
c.pack()


mybutton=Button(root, text="click me!", command=show).pack()

root.mainloop()