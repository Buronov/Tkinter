from tkinter import *
from PIL import ImageTk, Image



root = Tk()
root.title("Drop dawn")
root.geometry("400x400")

# Creating Drop dawn
# def show():
#     my_label = Label(root, text=clicked.get()).pack()

# clicked = StringVar()
# clicked.set("월")
# drop = OptionMenu(root, clicked, "월", "화", "수", "목", "금", "토", "일")
# drop.pack()

# btn = Button(root, text="Click me!", command=show).pack()

# Creating Drop dawn with list

def show():
    my_label = Label(root, text=clicked.get()).pack()

options = [
     "월",
     "화",
     "수",
     "목",
     "금",
     "토",
     "일"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

btn = Button(root, text="Click me!", command=show).pack()


root.mainloop()