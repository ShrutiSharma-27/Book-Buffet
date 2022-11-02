
#curs.execute()    use it in your prog to run any mysql command

import mysql.connector as sql

#-------------------------------Connection with mysql-----------------------------------------

def connect_db():
    dcon=sql.connect(host="localhost",user="root",passwd="39#sharmas",database="donate")
    if dcon.is_connected() == False:
        print("connection error")
    else:
        print("connection successful")
        dcon.close()

#------------------------------To get only 1 row as a result---------------------------------
        
def Execute_1(query):
    connect_db()
    fresh_con=sql.connect(host="localhost",user="root",passwd="39#sharmas",database="donate")
    c=fresh_con.cursor(buffered=True)
    try:
        c.execute(query)
        data=c.fetchone()
        print(':)')
        fresh_con.close()
        return data
    except:
        fresh_con.close()
        print(':(')

#-------------------------------To get multi-rows as a result---------------------------------

def Execute_multi(query):
    connect_db()
    fresh_con=sql.connect(host="localhost",user="root",passwd="39#sharmas",database="donate")
    c=fresh_con.cursor(buffered=True)
    try:
        c.execute(query)
        data=c.fetchall()            #list of tuples(rows)
        print(':)')
        fresh_con.close()
        return data
    except:
        fresh_con.close()
        print(':(')

#-----------------------------To insert, update & alter---------------------------------------

def iua(query):
    connect_db()
    fresh_con=sql.connect(host="localhost",user="root",passwd="39#sharmas",database="donate")
    c=fresh_con.cursor(buffered=True)
    try:
        c.execute(query)
        fresh_con.commit()
        fresh_con.close()
        print('Task Done...!!!!')
    except:
        fresh_con.rollback()
        fresh_con.close()
        print('Oops !! Task incomplete.')
