from  tkinter import *
# we are creating a root window
root = Tk()

mylabel1 = Label(root,text = "hello this is label widget")
mylabel2 = Label(root,text = "hello my name is jana prasanna")
#grid() function allows us to position any widget like label.
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=0)
# mainloop always runs in background. it regulates mouse pointer,
root.mainloop()