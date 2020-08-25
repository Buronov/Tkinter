from tkinter import *


root = Tk()
root.title('Entry height')
root.geometry("400x400")

def clicker(event):
    myLabel = Label(root, text="You clicked a button!")
    myLabel.pack()

btn = Button(root, text="Click me!")
btn.bind("<Key>", clicker) # Button-1, Enter, Leave, FocusIn, Return, Key
btn.pack(pady=20)


root.mainloop()