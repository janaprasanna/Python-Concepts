show databases;
use  librarymgmt;
create table student(studentID integer not null primary key, studentname varchar(20));
select * from student;
insert into  student values(1,'janaprasanna');
insert into  student values(2,'jana');
insert into  student values(3,'janakumar');
show tables;
use librarymgmt;
create table books(bookID integer not null primary key, bookname varchar(20),studentID integer not null, Bookcount integer not null);
insert into books values(2000,'Godzilla',2,5);
insert into books values(2001,'HarryPotter',2,5);
insert into books values(2002,'Tintin',3,5);
insert into books values(2003,'Rings',1,5);
select * from books;

select student.studentname, books.bookname,books.bookcount from student inner join books on student.studentID=books.studentID;
select student.studentname, books.bookname,books.bookcount from student left join books on student.studentID=books.studentID;
select student.studentname, books.bookname,books.bookcount from student right join books on student.studentID=books.studentID;