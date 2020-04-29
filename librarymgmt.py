student = {}
books = {}

def add_books(name, quantity):
    if get_books(name) == True:
        print("{}x books already in the library, adding {}x more books".format(books[name], quantity))
        books[name] = books[name] + quantity
        print("new count of {} books = {} ".format(name, books[name]))

    elif get_books(name) == False:
        print("{} not found in library so adding fresh books".format(name))
        books[name] = quantity
        print("Total {} books now is:{}".format(name,books[name]))

    else:
        print("unknown error")

def get_books(name):
    if name in books.keys():
        print(" {} books  found in library".format(name))
        #print(" Existing {} book count is :{}".format(name,book[name]))
        return True
    else:
        print("{} book not found in library".format(name))
        return False

def remove_books(name):
     if get_books(name)==True:
         books[name]= books[name] - rqty
         print("Existing {} books in the library is:{}".format(name,books[name]))
     else:
         print("No {} books were found in the library. ".format(rbook))
         print("Operation failed !")

def add_student(sname,stdbook,sbqty):
        if get_student(sname)==True:
            print("{} student already found in library".format(sname))
            student[sname][stdbook] = student[sname][stdbook] + sbqty
            print("Total {} books after adding again is: {}".format(stdbook,student[sname][stdbook]))
            #print(student)
        elif get_student(sname)==False:
            print(" No such {} student found in existing library".format(sname))
            student[sname] = {stdbook: sbqty}
            print("so adding new student {} with the book {} of count:{}".format(sname,stdbook,sbqty))
            print(student)
        else:
            print("Unknown error")

def get_student(searchstd):
    if searchstd in student.keys():
        print("{} student exists in library  with {}x {} book count..!".format(sname,sbqty,stdbook))
        return True
    else:
        print("{} student doesn't exits in library.".format(searchstd))

        return False

def remove_student(rstudent):
    if get_student(rstudent) == True:
        print("Total {} books the student {} has before leaving is :{}".format(stdbook,sname,student[sname][stdbook]))
        student[sname][stdbook] = student[sname][stdbook] - student[sname][stdbook]
        print("{} books  remaining with {} after removed is :{}".format(stdbook,sname,student[sname][stdbook]))
        student.popitem()
        print("{} student is removed from the library..".format(rstudent))
    else:
        print("No student named {} is found in library".format(rstudent))
        print("Operation failed !")

op = True
while op ==True:
    print("Welcome to Library management...!")

    print("1.Add books in library\n"
          "2.Get books from library\n"
          "3.Remove books from library\n"
          "4.Add students to the library\n"
          "5.Get students from the library\n"
          "6.Remove students from the library\n"
          "7.Lend books to students\n"
          "8.Return books to the library\n"
          "9.Exit from the library\n")

    choose = int(input("Enter the  choices in our Library Management:\n"
                       "use numbers to represent your choices!\n"))
    if choose == 1:
        bname = str(input("Enter book name: "))
        bqty = int(input("Enter {} book qty: ".format(bname)))
        add_books(bname, bqty)

    elif choose == 2:
        search = str(input("Enter book name to search in library: "))
        get_books(search)

    elif choose == 3:
        rbook = str(input("Enter book name to remove: "))
        rqty = int(input("Enter the amount of {} to be removed: ".format(bname)))
        remove_books(rbook)

    elif choose == 4:
        sname = str(input("Enter student name to be added:"))
        stdbook = str(input("Enter the book to be issued by the student {}:".format(sname)))
        sbqty = int(input("Enter the amount of books issued:"))
        add_student(sname,stdbook,sbqty)

    elif choose == 5:
        searchstd =  str(input("Enter the student name to be searched in library:"))

        get_student(searchstd)
    elif choose == 6:
        rstudent = str(input("Enter student name to remove: "))
        remove_student(rstudent)

    elif choose == 9:
        print("Good bye..! Have a nice day..!")
        op = False





'''
E:\githubprojects\myrepository1venv\Scripts\python.exe E:/githubprojects/myrepository1/librarymgmt.py
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