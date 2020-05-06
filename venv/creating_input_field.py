from  tkinter import *
root = Tk()
myentry1 = Entry(root,width = 60,borderwidth = 9)
myentry1.pack()
#get() is used to get what the user types is entry widget
myentry1.get()
#insert is used to give a default value to the  entry widget
#note: '0' is used to represent only one entry box
myentry1.insert(0,"Enter your name:")
def myclick():
    label = Label(root,text = "hello" + myentry1.get())
    label.pack()
#creating buttons
mybutton1 = Button(root,text = "Enter",bg= "grey",fg ="red",command = myclick)
mybutton1.pack()

root.mainloop()