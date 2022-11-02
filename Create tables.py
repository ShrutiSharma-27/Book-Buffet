import mysql.connector as sql

def CreateDT():
    New_Con= sql.connect(host="localhost",user="root",passwd="39#sharmas",database="donate")
    if New_Con.is_connected()==True:
        Cursor= New_Con.cursor()
        q1="create table book(book_no int primary key, book_name varchar(40), author char(40), category char(20), description varchar(200), no_of_copies int, no_of_copies_sold int, mrp float, selling_price float);"
        Cursor.execute(q1)
        q2="create table donor(donor_no int primary key, donor_name char(40), donor_address varchar(200), donor_phn bigint, donating char(30), money float, book_no int, quantity int, date_of_donation date, foreign key(book_no) references book(book_no));"
        Cursor.execute(q2)
        q3="create table recipient(rec_no int primary key, rec_name char(40), rec_address varchar(200), rec_phn bigint, book_no int, quantity int, amt_paid float, receiving_date date, foreign key(book_no) references book(book_no));"
        Cursor.execute(q3)
        q4="create table borrower(borrower_no int primary key, borrower_name char(40), borrower_address varchar(200), borrower_phn bigint, book_no int, quantity int, borrow_from date, borrow_till date, returned char(3), borrower_id varchar(6), foreign key(book_no) references book(book_no));"
        Cursor.execute(q4)
        q5="create table members(member_no int primary key, donor_no int, member_name char(40), member_address varchar(200), member_phn bigint, username varchar(40), password varchar(10), foreign key(donor_no) references donor(donor_no));"
        Cursor.execute(q5)
        print('All 5 tables are successfully created.')
    else:
        print("Connection error")

# Calling CreateDT function

CreateDT()
