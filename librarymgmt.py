student = {}
books = {}

def add_books(name,quantity):
    books[name] = quantity

def get_books(name):
    if name in books.keys():
        print("{} book found in library".format(name))
    else:
        print("{} book not found in library".format(name))

# def remove_books(name):
#     if name in books.keys():
#         books.pop(name)

bname = str(input("Enter book name: "))
bqty = int(input("Enter {} qty: ".format(bname)))
add_books(bname, bqty)


search = str(input("Enter book name to search: "))
get_books(search)

# rbook = str(input("Enter book name to remove: "))
# remove_books(rbook)
# get_books(rbook)

def add_student(sname,stdbook,bqty):


    student[sname] = {stdbook:bqty}
    print(student)



def get_student(searchstd):
    if searchstd in student.keys():
        print("{} student found in library".format(sname))
    else:
        print("{} student not found in library".format(sname))

#def remove_student():



sname = str(input("Enter student name to be added:"))
stdbook = str(input("Enter the book to be issued by the student {}:".format(sname)))
bqty = int(input("Enter the amount of books issued:"))
add_student(sname,bname,bqty)
searchstd =  str(input("Enter the student name to be searched in library:"))
get_student(searchstd)

'''
E:\githubprojects\myrepository1\venv\Scripts\python.exe E:/githubprojects/myrepository1/librarymgmt.py
Enter book name: math
Enter math qty: 2
Enter book name to search: math
math book found in library
Enter student name to be added:jana
Enter the book to be issued by the student jana:math
Enter the amount of books issued:2
{'jana': {'math': 2}}
Enter the student name to be searched in library:jana
jana student found in library

Process finished with exit code 0



'''