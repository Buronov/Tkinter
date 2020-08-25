from tkinter import *
from random import *
root = Tk()
root.title("Random")
root.geometry("400x400")

def pick():
    entries = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'q', 'r', 's', 't',]
    
    entries_set = set(entries)

    unique_entries = list(entries_set)

    our_number = len(unique_entries) - 1

    rando = randint(0, our_number)

    winnerLabel = Label(root, text=len(unique_entries), font=("San-serief", 18))
    winnerLabel.pack(pady=50)

topLabel = Label(root, text="Win-O=Rama!", font=("San-serief", 24))
topLabel.pack(padx=20)

winButton = Button(root, text="PICK OUR WINNER!", font=("San-serief", 24), command=pick)
winButton.pack(padx=20)





root.mainloop()
