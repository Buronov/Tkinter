from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")

# Creating Frame + text
frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=20, pady=20)

b = Button(frame, text="Don't click here!")
b2 = Button(frame, text="..or here")
b3 = Button(frame, text="here!")
# b.pack()
b2.grid(row=0, column=0)    
b3.grid(row=1, column=1)

root.mainloop()