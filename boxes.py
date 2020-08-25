from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Message")


# showinfo, showwarning, showerror, askquestion, askokcancel,   askyesno


def popup():
    response = messagebox.askyesno("This is my Popur", "Hello world")
    # Label(text=response).pack()
    if response == 1:
        root.quit()
    else:
        Label(text="You don't click").pack()


buton = Button(root, text="Popur", command=popup).pack()

root.mainloop()