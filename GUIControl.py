from tkinter import *

root = Tk()

root.title("VGC Tournament Organizer")
root.geometry('1280x640')

lbl = Label(root, text = "Are you a Geek?")
lbl.grid()

playerNum = 1
listBox = Listbox(root, height = 10, width = 15, bg = "grey", activestyle = 'dotbox', font = "Helvetica", fg = "yellow")
listBox.grid(column=0, row = 1)

playerText = Entry(root, width= 150)
playerText.grid(column=0,row=10)

# function to display text when
# button is clicked
def addPlayer():
    listBox.insert(listBox.size()+1, playerText.get())

def removePlayer():
    idx = listBox.get(0, listBox.size()).index(playerText.get())
    listBox.delete(idx)


addPlayerToListButton = Button(root, text = "Add Player" ,fg = "red", command=addPlayer)
addPlayerToListButton.grid(column=1, row=0)

removePlayerFromListButton = Button(root, text = "Remove Player" ,fg = "red", command=removePlayer)
removePlayerFromListButton.grid(column=2, row=0)

root.mainloop()