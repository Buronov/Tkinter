from tkinter import *

root = Tk()

# Creating Input, width=eni, bg/fg, borderwidht=chet chiqizlar qalinligi
e = Entry(root, width=50,  fg="#fff", bg="#333", borderwidth=5 )
e.pack()
# Insert(index, text) - inputga yozib beradi.
e.insert(0, "Enter your name: ")



# e variabledan funksiya olib chiqazish.
def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Click Me!", padx=30,  command=myClick,  fg="#fff", bg="#333" )
myButton.pack()

root.mainloop()