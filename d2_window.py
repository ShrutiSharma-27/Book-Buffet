#FOR Recipient entry
# amt_paid would be reflect by me

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import connectivity as con
from tkinter import Canvas
from PIL import ImageTk
from PIL import Image
from datetime import datetime

#-----------------------------------------------------------------RECIPIENT PAGE------------------------------------------------------------------

def purchase():
    global d2
    global recipient_name
    global recipient_phn
    global recipient_address
    global book_name
    global author_name
    global quantity
    
    d2=Tk()
    recipient_name= StringVar()
    recipient_phn= IntVar()
    recipient_address= StringVar()
    book_name= StringVar()
    author_name= StringVar()
    quantity= IntVar()
    
    d2.title("BOOK ZONE-Recipient's Form")
    d2.geometry("300x300")
    d2.minsize(612,400)  
    
    ew_book=con.Execute_multi('select book_name from book where no_of_copies <> 0 group by book_name ;')
    n=len(ew_book)
    bookies=[]
    for i in range(n):
        bookies.append(ew_book[i][0])

    ew_author=con.Execute_multi('select author from book where no_of_copies <> 0 group by author ;')
    n1=len(ew_author)
    authors=[]
    for j in range(n1):
        authors.append(ew_author[j][0])
        
        
    
    entry_1= Entry(d2, textvariable= recipient_name)
    entry_2= Entry(d2, textvariable= recipient_phn)
    entry_2.insert(END,0)
    entry_3= Entry(d2, textvariable= recipient_address)
    entry_4= ttk.Combobox(d2, values=bookies)
    entry_5= ttk.Combobox(d2, values=authors)
    entry_6= Entry(d2, textvariable= quantity)
    entry_1.grid(row=0,column=3,columnspan=7)
    entry_2.grid(row=1,column=3,columnspan=7)              #E-east, W-west, N-north, S-south
    entry_3.grid(row=2,column=3,columnspan=7)
    entry_4.current(0)
    entry_4.grid(row=3,column=3,columnspan=7)
    
    entry_5.grid(row=4,column=3,columnspan=7)
    entry_5.current(0)
    entry_6.grid(row=5,column=3,columnspan=7)

    l1= Label(d2, text= "Recipient Name :",font="Helvetica 12 bold")
    l2= Label(d2, text= "Phn No. :",font="Helvetica 12 bold")
    l3= Label(d2, text= "Address :",font="Helvetica 12 bold")
    l4= Label(d2, text= "Book Name :",font="Helvetica 12 bold")
    l5= Label(d2, text= "Book Author :",font="Helvetica 12 bold")
    l6= Label(d2, text= "Quantity :",font="Helvetica 12 bold")
    
    l1.grid(row=0, sticky=W)            
    l2.grid(row=1, sticky=W)
    l3.grid(row=2, sticky=W)
    l4.grid(row=3, sticky=W)
    l5.grid(row=4, sticky=W)
    l6.grid(row=5, sticky=W)

#   ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    def mssgr():
        RNm=entry_1.get()
        RPn=entry_2.get()
        RAd=entry_3.get()
        BNm=entry_4.get()
        ANm=entry_5.get()
        BQt=entry_6.get()
        d2.destroy()
        messagebox.showinfo('Book Buffet: Message','We wish '+RNm+' this would help you. \n May you have a wonderful life ahead :)')
        book_auth=con.Execute_multi('select book_name, author, selling_price, book_no from book where no_of_copies <> 0 group by book_name ;')
        r=con.Execute_1('select max(rec_no) from recipient ;')
        print(r)
        if r[0]==None:
            r=0
        else:
            r=r[0]


            
        dt=str(datetime.today().strftime('%Y-%m-%d'))
        for a in book_auth:
            if a[0]==BNm and a[1]==ANm:
                if len(RNm) > 0 and int(RPn) > 0 and len(RAd) > 0 and len(BNm) > 0 and len(ANm) > 0 and int(BQt) >0 :
                    if a[3]==None:
                        a[3]=0
                    else:
                        pass
                    print("insert into recipient values({},'{}','{}',{},{},{},{},'{}') ;".format(r+1,RNm,RAd,int(RPn),a[3],int(BQt),float(a[2]),dt))
                    con.iua("insert into recipient values({},'{}','{}',{},{},{},{},'{}') ;".format(r+1,RNm,RAd,int(RPn),a[3],int(BQt),float(a[2]),dt))
                    con.iua("update book set no_of_copies=no_of_copies - 1, no_of_copies_sold=no_of_copies_sold + 1 where book_no={} ;".format(a[3]))
                    messagebox.showinfo('Book Buffet: BILL','Total Amount to be PAID={}'.format(a[2]))
                else:
                    messagebox.showwarning('Book Buffet: Warning', 'All fields are mandatory.')
                break
        else:
            messagebox.showwarning('Warning',"Book & Author aren't matching. Please check BOOK List once.")
    
    button11=Button(d2, text='Confirm your demands', bg='yellow', command= mssgr, padx=10, pady=10,font="Helvetica 12 bold")
    button11.grid(row=7, columnspan= 5)

    buttonl2=Button(d2, text='Back', fg='brown', bg='yellow', command= d2.destroy,font="Helvetica 12 bold",padx=6, pady=4)
    buttonl2.grid(row=10, columnspan=5)

    d2.mainloop()
#--------------------------------------------------------------BORROWER PAGE------------------------------------------------------------------------

def rent():
    global d_2
    global borrower_name
    global borrower_phn
    global borrower_address
    global book_nm
    global auth_nm
    global quant
    global From
    global to
    
    d_2=Tk()
    borrower_name= StringVar()
    borrower_phn= IntVar()
    borrower_address= StringVar()
    book_nm= StringVar()
    auth_nm= StringVar()
    quant= IntVar()
    From= StringVar()
    to= StringVar()
    
    d_2.title("BOOK ZONE-Borrower's Form")
    d_2.geometry("300x300")
    d_2.minsize(600,400)
    
    av_book=con.Execute_multi('select book_name from book where no_of_copies <> 0 group by book_name ;')
    N=len(av_book)
    bookies=[]
    for i in range(N):
        bookies.append(av_book[i][0])

    av_author=con.Execute_multi('select author from book where no_of_copies <> 0 group by author ;')
    n_1=len(av_author)
    authors=[]
    for j in range(n_1):
        authors.append(av_author[j][0])
           
    entry_1= Entry(d_2, textvariable= borrower_name)
    entry_2= Entry(d_2, textvariable= borrower_phn)
    entry_2.insert(END,0)
    entry_3= Entry(d_2, textvariable= borrower_address)
    entry_4= ttk.Combobox(d_2, values=bookies)
    entry_5= ttk.Combobox(d_2, values=authors)
    entry_6= Entry(d_2, textvariable=quant)
    entry_7= Entry(d_2, textvariable=From)
    entry_7.insert(END,'YYYY-MM-DD')
    entry_8= Entry(d_2, textvariable=to)
    entry_8.insert(END,'YYYY-MM-DD')
    entry_1.grid(row=0,column=3,columnspan=7)
    entry_2.grid(row=1,column=3,columnspan=7)              #E-east, W-west, N-north, S-south
    entry_3.grid(row=2,column=3,columnspan=7)
    entry_4.current(0)
    entry_4.grid(row=3,column=3,columnspan=7)
    entry_5.current(0)
    entry_5.grid(row=4,column=3,columnspan=7)
    entry_6.grid(row=5,column=3,columnspan=7)
    entry_7.grid(row=6,column=3,columnspan=7)
    entry_8.grid(row=7,column=3,columnspan=7)
    

    l1= Label(d_2, text= "Borrower Name :",font="Helvetica 12 bold")
    l2= Label(d_2, text= "Phn No. :",font="Helvetica 12 bold")
    l3= Label(d_2, text= "Address :",font="Helvetica 12 bold")
    l4= Label(d_2, text= "Book Name :",font="Helvetica 12 bold")
    l5= Label(d_2, text= "Book Author :",font="Helvetica 12 bold")
    l6= Label(d_2, text= "Quantity :",font="Helvetica 12 bold")
    l7= Label(d_2, text= "Borrow from :",font="Helvetica 12 bold")
    l8= Label(d_2, text= "Borrow till :",font="Helvetica 12 bold")
    
    
    l1.grid(row=0, sticky=W)            
    l2.grid(row=1, sticky=W)
    l3.grid(row=2, sticky=W)
    l4.grid(row=3, sticky=W)
    l5.grid(row=4, sticky=W)
    l6.grid(row=5, sticky=W)
    l7.grid(row=6, sticky=W)
    l8.grid(row=7, sticky=W)
#   ------------------------------------------------------------------------------------------------------------------------------------------------
    def mssg():
        BNM=entry_1.get()
        BPN=entry_2.get()
        BAD=entry_3.get()
        bkN=entry_4.get()
        bkA=entry_5.get()
        bkQ=entry_6.get()
        FROM=entry_7.get()
        TILL=entry_8.get()
        d_2.destroy()
        
        book_auth=con.Execute_multi('select book_name, author, selling_price, book_no from book where no_of_copies <> 0 group by book_name ;')
        b=con.Execute_1('select max(borrower_no) from borrower ;')
        print(b)
        if b[0]==None:
            b=0
        else:
            b=b[0]

        if len(str(b+1))==1:
            ID=BNM[0:3]+'00'+str(b+1)
        elif len(str(b+1))==2:
            ID=BNM[0:3]+'0'+str(b+1)
        else:
            ID=BNM[0:3]+str(b+1)
        
        for a in book_auth:
            if a[0]==bkN and a[1]==bkA:
                if a[3]==None:
                    a[3]=0
                else:
                    pass
                if len(BNM) > 0 and int(BPN) > 0 and len(BAD) > 0 and len(bkN) > 0 and len(bkA) > 0 and int(bkQ) >0 :
                    print("insert into borrower values({},'{}','{}',{},{},{},'{}','{}','no','{}') ;".format(b+1,BNM,BAD,int(BPN),a[3],int(bkQ),FROM,TILL,ID))
                    con.iua("insert into borrower values({},'{}','{}',{},{},{},'{}','{}','no','{}') ;".format(b+1,BNM,BAD,int(BPN),a[3],int(bkQ),FROM,TILL,ID))
                    con.iua("update book set no_of_copies=no_of_copies - 1 where book_no={} ;".format(a[3]))
                    messagebox.showinfo('Book Buffet: Info','''HURRAY..!! Book is yours for specified time.
Your Borrower id : {}
With this id only you can return the book.
We wish {} this would help you.'''.format(ID,BNM))
                else:
                    messagebox.showwarning('Book Buffet: Warning', 'All fields are mandatory.')
                break
        else:
            messagebox.showwarning('Book Buffet: Warning',"Book & Author aren't matching. Please check BOOK List once.")

    buttonL1=Button(d_2, text='Confirm your demands', bg='yellow', command= mssg, padx=9, pady=7,font="Helvetica 12 bold")
    buttonL1.grid(row=9, columnspan= 5)

    buttonL2=Button(d_2, text='Back', bg='yellow', command= d_2.destroy, padx=9, pady=7,font="Helvetica 12 bold")
    buttonL2.grid(row=10, columnspan=5)

    d_2.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------

def typ_rec():
    take=Toplevel()
    take.geometry('600x600')
    pch= Button(take, text='  FOR PURCHASE  ', bg='PaleVioletRed1',font="Helvetica 12 bold",padx=20, pady=20,command=purchase)
    rnt= Button(take, text='   FOR BORROW   ', bg='PaleVioletRed2',font="Helvetica 12 bold",padx=20, pady=20,command=rent)
    but= Button(take, text='BACK TO MAIN MENU', bg='PaleVioletRed3',font="Helvetica 12 bold",padx=20, pady=20,command=take.destroy) 
    pch.place(x=300,y=50, anchor=CENTER)
    rnt.place(x=300,y=150, anchor=CENTER)
    but.place(x=300,y=250, anchor=CENTER)

    c = Canvas(take, width = 1000, height = 140)
    c.place(x=30, y=400)
    i = ImageTk.PhotoImage(Image.open("C://Users//sujal//Desktop//MOLI//MOLI PYTHON//PROJECT//p_unite.png"))
    c.create_image(5, 5, anchor=NW, image=i)
    take.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------------------
def Return():
    global b_ID

    b_ID= StringVar()
    
    r_win=Tk()
    r_win.geometry('450x200')
    e1= Entry(r_win, textvariable= b_ID)
    l1= Label(r_win, text= "Borrower ID :",font="Helvetica 12 bold")

    l1.grid(row=0, sticky=W)
    e1.grid(row=0,column=3,columnspan=7)
#   ------------------------------------------------------------------------------------------------------------------------------
    def no_yes():
        bor_id=con.Execute_multi("select borrower_id, book_no from borrower ;")
        print("select borrower_id, book_no from borrower ;")

        for r in bor_id:
            if r[0]==e1.get():
                con.iua("update borrower set returned='yes' where borrower_id='{}' ;".format(r[0]))
                con.iua("update book set no_of_copies= no_of_copies+1 where book_no={} ;".format(r[1]))
                messagebox.showinfo('Book Buffet: Info','Your borrowed book returned successfully !')
            else:
                messagebox.showwarning('Book Buffet: Warning','Incorrect Borrower ID')

    b1=Button(r_win, text='SUBMIT', bg='PaleVioletRed1',font="Helvetica 14 bold",padx=6, pady=5,command= no_yes)
    b1.grid(row=6,column=1)
    b2=Button(r_win, text='Back to MAIN MENU', bg='PaleVioletRed1',font="Helvetica 14 bold",padx=6, pady=5,command= r_win.destroy)
    b2.grid(row=8,column=1)
