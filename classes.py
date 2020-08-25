from tkinter import *


root = Tk()
root.title('Entry height')
root.geometry("400x400")

class John:

    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.btn = Button(master, text="Click me!", command=self.clicker)
        self.btn.pack(pady=20)

    def clicker(self):
        print("Look at you.. You clicked a button")

j = John(root)
root.mainloop()