student = {}
books = {}

op = True
while op ==True:
    print("Welcome to Library management...!")

    print("1.Add books in library\n"
          "2.Get books from library\n"
          "3.Remove books from library\n"
          "4.Add students to the libraryn\n"
          "5.Get students from the library\n"
          "6.Remove students from the library\n"
          "7.Lend books to students\n"
          "8.Return books to the library\n"
          "9.Exit from the library\n")

    choose = int(input("Enter the  choices in our Library Management:\n"
                       "use numbers to represent your choices!\n"))
    if choose == 1:
        bname = str(input("Enter book name: "))
        bqty = int(input("Enter {} qty: ".format(bname)))
        def add_books(name,quantity):
            books[name] = quantity
            add_books(bname, bqty)
    elif choose == 2:
        search = str(input("Enter book name to search in library: "))
        def get_books(name):

            if name in books.keys():
                print("{} book found in library".format(name))
            else:
                print("{} book not found in library".format(name))

            get_books(search)

    elif choose == 3:
        rbook = str(input("Enter book name to remove: "))
        def remove_books(name):
             if name in books.keys():
                 books.pop(name)
                 print("{} book is removed from the library..".format(name))
        remove_books(rbook)

    elif choose == 4:
        sname = str(input("Enter student name to be added:"))
        stdbook = str(input("Enter the book to be issued by the student {}:".format(sname)))
        bqty = int(input("Enter the amount of books issued:"))
        def add_student(sname,stdbook,bqty):
            student[sname] = {stdbook:bqty}
            print(student)
        add_student(sname,stdbook,bqty)

    elif choose == 5:
        searchstd =  str(input("Enter the student name to be searched in library:"))
        def get_student(searchstd):
            if searchstd in student.items():
                print("{} student found in library".format(searchstd))
                return True
            else:
                print("{} student not found in library".format(searchstd))
        get_student(searchstd)
    elif choose == 6:
        rstudent = str(input("Enter student name to remove: "))
        def remove_student():
            if rstudent in student.keys():
                books.pop(name)
                print("{} book is removed from the library..".format(rstudent))



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