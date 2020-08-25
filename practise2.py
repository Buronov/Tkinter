from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Practise")
root.geometry("600x400")


my_label = Label(root, text="Viloyatingizni tanlang")
my_label.grid(row=0, column=0)

var = StringVar()
var.set("Toshkent")
drop = OptionMenu(root, var, "Toshkent", "Andijon", "Farg'ona", "Namangan", "Samarqand", "Surxondaryo")
drop.grid(row=0, column=1)

my_label1 = Label(root, text="Ismingizni yozing: ")
my_label2 = Label(root, text="Familiyangizni yozing:")
my_label3 = Label(root, text="Yoshingizni kiritng:")

ent1 = Entry(root, width=30)
ent2 = Entry(root, width=30)
ent3 = Entry(root, width=30)

my_label1.grid(row=1, column=0)
my_label2.grid(row=2, column=0)
my_label3.grid(row=3, column=0)
ent1.grid(row=1, column=1, pady=15)
ent2.grid(row=2, column=1, pady=15)
ent3.grid(row=3, column=1, pady=15)

def show():
    ism = "Assalomu alaykum "+ ent3.get() + " yoshli " + var.get() + "da Yashaydigan " + ent2.get() +" " +  ent1.get()
    lbn1 = Label(root, text=ism)
    lbn1.grid(row=6, column=1)

btn = Button(root, text="Click Me!", command=show)
btn.grid(row=4, column=1, pady=10)




root.mainloop()