from tkinter import *


root = Tk()
root.title('Entry height')
root.geometry("400x400")

def myDelete():
    myLabel.grid_forget()
    # myLabel.destroy()
    btn['state'] = NORMAL

def myClick():
    global myLabel


    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    
    e.delete(0,'end')
    myLabel.grid(row=3, column=0, pady=10)

    # btn['state'] = DISABLED



e = Entry(root, width=17, font=('Sanf-serief', 30))
e.grid(row=0, column=0, pady=10, padx=10)

btn = Button(root, text="Click me!", command=myClick)
btn.grid(row=1, column=0,pady=10)

deletebtn = Button(root, text="Delete Text", command=myDelete)
deletebtn.grid(row=2, column=0, pady=10)



root.mainloop()