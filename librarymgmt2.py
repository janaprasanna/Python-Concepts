student = {}
books = {}

def add_books(name, quantity):
    book_name,book_quantity,books_status = get_books(name)
    if books_status == "ALREADYEXISTS" :
        print("{}x book exits already in the library, adding {}x more books".format(book_name, book_quantity))
        books[name] = books[name] + book_quantity
        print("new count of {} books = {} ".format(book_name, books[name]))
        return book_name,books[name],"BOOKSADDED"

    elif books_status == "NOTEXISTS":
        print("{} not found in library so adding fresh books".format(book_name))
        books[name] = quantity
        print("Total {} books now is:{}".format(book_name,quantity))
        return book_name, books[name], "NOTADDED"

    else:
        print("unknown error")
        return book_name, books[name], "ERROR"

def get_books(name):
    if name in books.keys():
        quantity = books[name]
        print(" {} books  found in library".format(name))
        print(" Existing {} book count is :{}".format(name,quantity))
        return name, quantity, "ALREADYEXISTS"
    else:
        print("{} book not found in library".format(name))
        return name, 0, "NOTEXISTS"

def remove_books(name,quantity):
    book_name, book_quantity, books_status = get_books(name)
    if books_status == "ALREADYEXISTS":
        if quantity <= books[name]:
            books[name]= books[name] - quantity
            print("Existing {} books in the library is:{}".format(book_name,books[name]))
            return books[name],"REMOVED SUCCESSFULLY"
        else:
            print("NOTE: The entered value is greater than the books available in the library.")
            print("Enter the  value which is less than or equal to the book count in the library !!")

    else:
        print("No {} books were found in the library. ".format(book_name))
        print("Operation failed !")
        return "ERROR"

def add_student(sname,stdbook,sbqty):
    book_name, book_quantity, books_status = get_books(stdbook)
    student_name,studentbook_quantity,student_status= get_student(sname)
    if books_status == "ALREADYEXISTS":
        if student_status==  "STUDENTALREADYEXISTS":
            if sbqty<= book_quantity:
                print("{} student already found in library".format(sname))
                student[sname][stdbook] = student[sname][stdbook] + sbqty
                squantity = student[sname][stdbook]
                print("Total {} books after adding again is: {}".format(stdbook,student[sname][stdbook]))
                print(student)
                return sname, squantity, "STUDENTADDED"

        elif student_status == "STUDENTNOTEXISTS":
            if sbqty <= book_quantity:
                print(" No such {} student found in existing library".format(sname))
                student[sname] = {stdbook: sbqty}
                print("so adding new student {} with the book {} of count:{}".format(sname,stdbook,sbqty))
                print(student)
                return sname, sbqty, "STUDENTNOTADDED"

            else:
                print("NOTE: The entered student book quantity is greater than the available books in lib.")
                print("Please enter a VALID book quantity !! ")
        else:
            print("Unknown Error!")
    else: #books_status == "NOTEXISTS":
        #else:
        print("NOTE: There are no books added in the library currently.")
        print("FIRST add some books to the library and try again.")
        print("operation failed")
        return sname, sbqty, "ERROR"


def get_student(searchstd):
    if searchstd in student.keys():
        print("{} student exists in library  with {}x {} book count..!".format(sname,sbqty,stdbook))
        return sname, sbqty, "STUDENTALREADYEXISTS"
    else:
        print("{} student doesn't exits in library.".format(searchstd))
        return sname, 0, "STUDENTNOTEXISTS"

def remove_student(rstudent,rbnstudent,rbstudent):
    book_name, book_quantity, books_status = get_books(rbnstudent)
    student_name, studentbook_quantity, student_status = get_student(sname)
    if student_status == "STUDENTALREADYEXISTS":
        if books_status == "ALREADYEXISTS":
            print("Total {} books the student {} has before leaving is :{}".format(stdbook,sname,student[sname][stdbook]))
            student[sname][stdbook] = student[sname][stdbook] - rbstudent
            squantity = student[sname][stdbook]
            print("{} books  remaining with {} after returned is :{}".format(stdbook,student_name,squantity))
            print("NOTE: The student holds still more books with him .")
            print("Therefore the student cannot be removed PERMANENTLY.")
            #student.popitem()
            #print("{} student is removed from the library..".format(rstudent))
            return squantity, "STUDENTNOTREMOVEDPERMANENTLY."
        elif books_status == "NOTEXISTS":
            print("NOTE: The student does not have any books with him.")
            print("Therefore  removing the student PERMANENTLY....")
            student.popitem()
            print("Student removed SUCCESSFULLY .")
            return 0, "STUDENTNOTREMOVEDPERMANENTLY."
        else:
            print("UNKNOWN ERROR!")
    else:
        print("No student named {} is found in library".format(rstudent))
        print("Operation failed !")
        return student[sname][stdbook], "REMOVEFAILED!"

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
        remove_books(rbook,rqty)

    elif choose == 4:
        sname = str(input("Enter student name to be added:"))
        stdbook = str(input("Enter the book name to be issued by the student {}:".format(sname)))
        sbqty = int(input("Enter the amount of books to be issued:"))
        add_student(sname,stdbook,sbqty)
       
    elif choose == 5:
        searchstd =  str(input("Enter the student name to be searched in library:"))

        get_student(searchstd)
    elif choose == 6:
        rstudent = str(input("Enter student name to remove: "))
        rbnstudent = str(input("Enter the book name to be returned:"))
        rbstudent = int(input("Enter the amount of {} books to be returned:".format(rbnstudent)))
        remove_student(rstudent,rbnstudent,rbstudent)

    elif choose == 9:
        print("Good bye..! Have a nice day..!")
        op = False





'''
E:\githubprojects\myrepository1venv\Scripts\python.exe E:/githubprojects/myrepository1/librarymgmt2.py
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