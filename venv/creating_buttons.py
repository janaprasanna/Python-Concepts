from  tkinter import *
root = Tk()
def myclick():
    label = Label(root,text = "Look i clicked a button !")
    label.pack()
#creating buttons
mybutton1 = Button(root,text = "click me",bg= "yellow",fg ="red",command = myclick)
mybutton2 = Button(root,text = "dontclick",state = DISABLED)
#button fucktions has parameters to edit such as its colour, size ,foreground colour.
# 'state' makes the button to be diaabled.
#mybutton3 = Button(root,text = "click me",padx=50,pady=20)
# to resize the button , we use padx(xaxis) and pady(yaxis).
mybutton1.pack()
mybutton2.pack()
#mybutton3.pack()
root.mainloop()
