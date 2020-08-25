from tkinter import *

root = Tk()

# Creating Label
label1 = Label(text="e-mail")
label2 = Label(text="code")
label1.grid(row=1, column=1)
label2.grid(row=2, column=1)

# Creating Input
e1 = Entry(root, width=18,   borderwidth=3, bg="#333", fg="white" )
e2 = Entry(root, width=18, borderwidth=3, bg="#333", fg="white")
e1.insert(0, "이메일을 입력" )
e2.insert(0, "비밀번호 입력" )
e1.grid(row=1, column=3)
e2.grid(row=2, column=3)

# Creating Button
button = Button(root, text="end", fg="blue")
button.place(x=80, y=60)

label3 = Label(text="Buronov Jonibek", fg="green")
label3.place(x=50, y=100)


root.mainloop()