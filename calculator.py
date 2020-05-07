from tkinter import *


root = Tk()
root.title("Simple Calculator")
myentry = Entry(root,width= 40,borderwidth=10)
myentry.grid(row=0,column=0,columnspan=5)

def button_click(number):
    current = myentry.get()
    myentry.delete(0, END)
    myentry.insert(0, str(current) + str(number))

def button_clear():
    myentry.delete(0, END)

def button_add():
    first_number = myentry.get()
    global f_num
    global condition
    condition = "addition"
    f_num = int(first_number)
    myentry.delete(0, END)


def button_subract():
    first_number = myentry.get()
    global f_num
    global condition
    condition = "subraction"
    f_num = int(first_number)
    myentry.delete(0, END)


def button_multiply():
    first_number = myentry.get()
    global f_num
    global condition
    condition = "multiplication"
    f_num = int(first_number)
    myentry.delete(0, END)


def button_divide():
    first_number = myentry.get()
    global f_num
    global condition
    condition = "division"
    f_num = int(first_number)
    myentry.delete(0, END)


def button_equal():
    second_number = myentry.get()
    myentry.delete(0,END)
    if condition == "addition":
        myentry.insert(0, f_num+int(second_number))
    if condition == "subraction":
        myentry.insert(0, f_num-int(second_number))

    if condition == "multiplication":
        myentry.insert(0, f_num*int(second_number))
    if condition == "division":
        myentry.insert(0, f_num/int(second_number))


button_1 = Button(root,text = "1",padx=30,pady=30,command=lambda:button_click(1))
button_2 = Button(root,text = "2",padx=30,pady=30,command=lambda:button_click(2))
button_3 = Button(root,text = "3",padx=30,pady=30,command=lambda:button_click(3))
button_4 = Button(root,text = "4",padx=30,pady=30,command=lambda:button_click(4))
button_5 = Button(root,text = "5",padx=30,pady=30,command=lambda:button_click(5))
button_6 = Button(root,text = "6",padx=30,pady=30,command=lambda:button_click(6))
button_7 = Button(root,text = "7",padx=30,pady=30,command=lambda:button_click(7))
button_8 = Button(root,text = "8",padx=30,pady=30,command=lambda:button_click(8))
button_9 = Button(root,text = "9",padx=30,pady=30,command=lambda:button_click(9))
button_0 = Button(root,text = "0",padx=30,pady=30,command=lambda:button_click(0))
button_add = Button(root,text="+",padx=29,pady=30,command=button_add)
button_equal = Button(root,text="=",padx=80,pady=30,command=button_equal)
button_clear = Button(root,text="clear",padx=70,pady=30,command=button_clear)
button_subract = Button(root,text="-",padx=31,pady=30,command=button_subract)
button_multiply = Button(root,text="*",padx=31,pady=30,command=button_multiply)
button_divide = Button(root,text="/",padx=31,pady=30,command=button_divide)

button_0.grid(row=4,column=0)
button_9.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_7.grid(row=3,column=2)
button_6.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_4.grid(row=2,column=2)
button_3.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_1.grid(row=1,column=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=4,column=1,columnspan=2)
button_subract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)






root.mainloop()





