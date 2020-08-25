from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Drop bind")
root.geometry("400x400")

def selected(event):
    myLaleb = Label(root, text=clicked.get()).pack()


def comboclick():
    myLaleb = Label(root, text=myCombo.get()).pack()    


options = [
    "월요일",
    "화요일",
    "수요일",
    "목요일",
    "금요일",
    "토요일",
    "일요일"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command=selected)
drop.pack(pady=20)

myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)
myCombo.pack()

# mybtn = Button(root, text="Select from list", command=selected)
# mybtn.pack(pady=10)

root.mainloop()