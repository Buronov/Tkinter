from tkinter import *

root = Tk()

# Funsiyadan foydalanib chiqarish. bunda u buttonga command=berish kk.
def myClick():
    myLabel = Label(root, text="Look! I clicked")
    myLabel.pack()

#Creating Buttons, 
# state=DISABLED (Bosilgan turadi), 
# padx=eni, pady=bo'yi
# command buyrug'isiz ishmalaydi. () qoyilsa chiqib turadi.
# fg=text color, bg=background color
myButton = Button(root, text="Click Me!", padx=30,  command=myClick,  fg="#fff", bg="#333" )
myButton.pack()

root.mainloop()