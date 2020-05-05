from  tkinter import *
# we are creating a root window
root = Tk()
#we are creating a label widgey
mylabel1 = Label(root,text = "hello this is label widget")
# we are packing everything into the screen
mylabel1.pack()
# mainloop always runs in background. it regulates mouse pointer,
root.mainloop()