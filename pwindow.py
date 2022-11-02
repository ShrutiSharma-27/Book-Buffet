from tkinter import *
import d1_window as d1
import d2_window as d2
from tkinter import ttk
from tkinter import Canvas
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
import d3_book_list as bl
import connectivity as con
from datetime import datetime

#-------------------------------------------------------------------------------------------------------------------------------

def org():
    info_org=Tk()
    info_org.title('Book Buffet Organisation')
    info_org.minsize(400,80)
    info= Label(info_org, background='cyan', font="comicsansns 18 bold", text= '''Established on 10th July, 2020
It is the biggest question mark after completing a book that what best can we do with this book.
Some people sell it for trash and other live in the dilemma.
So here we are with this platform to end up your this problem.
Our mission is to connect the people in need with those people who desires to help
either by donating a BOOK or MONEY. ''')
    info.pack()
    exit_bt= Button(info_org, text='EXIT', bg='lawn green',font="Helvetica 12 bold", command=info_org.destroy, padx=10, pady=10)
    exit_bt.pack()

#--------------------------------------------------------------------------------------------------------------------------------------------

def Diff_list():
    Slist=Tk()
    Slist.geometry("560x450")
    Slist.minsize(500,500)
    Slist.title('Book Buffet: Options')
    o1= Button(Slist, text='      AVAILABLE BOOKS      ', bg='PaleVioletRed1',font="Helvetica 12 bold",padx=20, pady=20,command=bl.Av_list)
    o2= Button(Slist, text='CURRENTLY UNAVAILABLE BOOKS', bg='PaleVioletRed2',font="Helvetica 12 bold",padx=20, pady=20,command=bl.Unav_list)
    o3= Button(Slist, text='     BACK TO MAIN MENU     ', bg='PaleVioletRed3',font="Helvetica 12 bold",padx=20, pady=20,command=Slist.destroy) 
    o1.place(x=290,y=100, anchor=CENTER)
    o2.place(x=290,y=200, anchor=CENTER)
    o3.place(x=290,y=300, anchor=CENTER)

    
    
#---------------------------------------------------------------------------------------------------------------------------------------------------

def log_in():
    global get_up
    get_up= Tk()
    get_up.geometry('600x100')
    get_up.minsize(300,300)
    get_up.title('Member Login')
    global un
    global pd

    un= StringVar()
    pd= StringVar()

    u= Entry(get_up, textvariable=un)
    p= Entry(get_up, textvariable=pd, show='*')

    def login():
        U=u.get()
        P=p.get()
        get_up.destroy()
        members=con.Execute_multi("select member_name,member_no,donor_no,member_phn,username,password from members;")
        for desired in members:
            if desired[4]==U and desired[5]==P:
                messagebox.showinfo("Account_Info", "Login Successful :)")
                login_win=Tk()
                login_win.minsize(300,300)
                login_win.title('Your page')
                lb_1= Label(login_win, text='Member Name :',font="Helvetica 12 bold")
                lb1= Label(login_win, text=desired[0],font="Helvetica 12 bold")
                lb_2= Label(login_win, text='Member No. :',font="Helvetica 12 bold")
                lb2= Label(login_win, text=desired[1],font="Helvetica 12 bold")
                lb_3= Label(login_win, text='Donor No. :',font="Helvetica 12 bold")
                lb3= Label(login_win, text=desired[2],font="Helvetica 12 bold")
                lb_4= Label(login_win, text="Phn No. :",font="Helvetica 12 bold")
                lb4= Label(login_win, text=desired[3],font="Helvetica 12 bold")
                lb_1.grid(row=1,column=3,sticky=W)
                lb1.grid(row=1,column=5)
                lb_2.grid(row=2,column=3,sticky=W)
                lb2.grid(row=2,column=5)
                lb_3.grid(row=3,column=3,sticky=W)
                lb3.grid(row=3,column=5)
                lb_4.grid(row=4,column=3,sticky=W)
                lb4.grid(row=4,column=5)
                fm= Frame(login_win)
                fm.grid(row=7, column=3,columnspan=5)

                tab_dt=list(con.Execute_1('select donating,money,book_no,quantity,date_of_donation from donor where donor_no={};'.format(desired[2])))
                bn=con.Execute_1('select book_name from book where book_no={};'.format(tab_dt[2]))
                if bn==None:
                    bn= '-'
                else:
                    bn=bn[0]
                if tab_dt[1]==None:
                    tab_dt[1]=0
                else:
                    pass
                if tab_dt[2]==None:
                    tab_dt[2]='-'
                else:
                    pass
                if tab_dt[3]==None:
                    tab_dt[3]='-'
                else:
                    pass                
                    
                lb_5=Label(login_win, text='Donated book name :',font="Helvetica 12 bold")
                lb5=Label(login_win, text=bn,font="Helvetica 12 bold")
                lb_5.grid(row=5,column=3,sticky=W)
                lb5.grid(row=5,column=5)
            
                tv_1= ttk.Treeview(fm, columns=(1,2,3,4,5), show= 'headings', height='3')
                tv_1.grid(row=9,column=3, columnspan=5)

                tv_1.heading(1, text='Donated')
                tv_1.heading(2, text='Amount donated')
                tv_1.heading(3, text='Book No.')
                tv_1.heading(4, text='Quantity')
                tv_1.heading(5, text='Date of donation')

                tv_1.insert('','end', values=tab_dt)
                B= Button(login_win, text= 'Back to main menu', bg='pink', command=login_win.destroy,font="Helvetica 12 bold", padx=7,pady=5)
                B.grid(row=11,column=4, columnspan=3)
                login_win.mainloop()
                break
                
        else:
            messagebox.showwarning('Error','Invalid username or password :(')
        
  
    Bton= Button(get_up, text= 'Done', bg='pink', command=login,font="Helvetica 12 bold")
    Bton1= Button(get_up, text= 'Back to main menu', bg='pink', command=get_up.destroy,font="Helvetica 12 bold")

    e1= Label(get_up, text= "User_name :",font="Helvetica 12 bold")
    e2= Label(get_up, text= "Password(atmost 10 char) :",font="Helvetica 12 bold")
    e1.grid(row=0, sticky=W)
    e2.grid(row=2, sticky=W)
    u.grid(row=0,column=2,columnspan=7)
    p.grid(row=2,column=2,columnspan=7)
    Bton.grid(row=5,column=1)
    Bton1.grid(row=7,column=1)

    get_up.mainloop()

#-------------------------------------------------------------------ADMIN---------------------------------------------------------------------------
    
def Admin():
    global choice
    global A
    Rcode= 'shru2707'
    code= StringVar()
    A=Tk()
    A.title('Book Buffet: Admin')
    A.geometry('600x100')
            
    def Ad_2():
        C=c.get()
        A.destroy()
#       -------------------------------------------------------------------------------------------------------------------------
        def D():

            DL=con.Execute_multi('select * from donor ;')
            n3=str(len(DL))
            dtable= Toplevel()
            dtable.minsize(600,600)
            dtable.title('Book Buffet: Donor List')
            Head= Label(dtable, text='LIST OF DONORS' , bg='deep pink', font="comicsansns 40 bold", borderwidth=2)
            Head.pack()
            Exit1= Button(dtable, text='EXIT', bg='lawn green',font="Helvetica 12 bold", command=dtable.destroy, padx=10, pady=10)
            Exit1.pack()

            fr= Frame(dtable)
            fr.pack(side=LEFT, padx=20)

            T= ttk.Treeview(fr, columns=(1,2,3,4,5,6,7,8,9), show= 'headings',height=n3)
            T.pack(fill= BOTH, expand=True)

            T.heading(1, text='Donor No.')
            T.heading(2, text='Name')
            T.heading(3, text='Address')
            T.heading(4, text='Phn No.')
            T.heading(5, text='Donated')
            T.heading(6, text='Money')
            T.heading(7, text='Book No.')
            T.heading(8, text='Quantity')
            T.heading(9, text='Donation Date')
            
            for m in DL:
                T.insert('','end', values=m)

            dtable.mainloop()
#       ---------------------------------------------------------------------------------------------------------------------------
        def R():
        
            DL1=con.Execute_multi('select * from recipient ;')
            n4=str(len(DL1))
            dtable1= Toplevel()
            dtable1.minsize(600,600)
            dtable1.title('Book Buffet: Recipient List')
            Head1= Label(dtable1, text='LIST OF RECIPIENTS' , bg='deep pink', font="comicsansns 40 bold", borderwidth=2)
            Head1.pack()
            Exit2= Button(dtable1, text='EXIT', bg='lawn green',font="Helvetica 12 bold", command=dtable1.destroy, padx=10, pady=10)
            Exit2.pack()


            fr1= Frame(dtable1)
            fr1.pack(side=LEFT, padx=20)

            T1= ttk.Treeview(fr1, columns=(1,2,3,4,5,6,7,8), show= 'headings',height=n4)
            T1.pack()

            T1.heading(1, text='Recipient No.')
            T1.heading(2, text='Name')
            T1.heading(3, text='Address')
            T1.heading(4, text='Phn No.')
            T1.heading(5, text='Book No.')
            T1.heading(6, text='Quantity')
            T1.heading(7, text='Amt. Paid')
            T1.heading(8, text='Date of purchase')

            for h in DL1:
                T1.insert('','end', values=h)

            dtable1.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------
        def B():
            
            DL2=con.Execute_multi('select * from borrower ;')
            n5=str(len(DL2))
            dtable2= Toplevel()
            dtable2.minsize(600,600)
            dtable2.title('Book Buffet: Borrower List')
            Head2= Label(dtable2, text='LIST OF BORROWERS' , bg='deep pink', font="comicsansns 40 bold", borderwidth=2)
            Head2.pack()
            Exit3= Button(dtable2, text='EXIT', bg='lawn green',font="Helvetica 12 bold", command=dtable2.destroy, padx=10, pady=10)
            Exit3.pack()


            fr2= Frame(dtable2)
            fr2.pack(side=LEFT, padx=20)

            T2= ttk.Treeview(fr2, columns=(1,2,3,4,5,6,7,8,9,10), show= 'headings',height=n5)
            T2.pack()

            T2.heading(1, text='Borrower No.')
            T2.heading(2, text='Name')
            T2.heading(3, text='Address')
            T2.heading(4, text='Phn No.')
            T2.heading(5, text='Book No.')
            T2.heading(6, text='Quantity')
            T2.heading(7, text='Borrowed from')
            T2.heading(8, text='Borrowed till')
            T2.heading(9, text='Returned')
            T2.heading(10, text='Borrower_id')
            
            for j in DL2:
                T2.insert('','end', values=j)

            dtable2.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------
        def Book_R():
    
            DL3=con.Execute_multi('select * from book ;')
            n6=str(len(DL3))
            dtable3= Toplevel()
            dtable3.minsize(600,600)
            dtable3.title('Book Buffet: Book List')
            Head3= Label(dtable3, text='LIST OF BOOKS' , bg='deep pink', font="comicsansns 40 bold", borderwidth=2)
            Head3.pack()
            Exit4= Button(dtable3, text='EXIT', bg='lawn green',font="Helvetica 12 bold", command=dtable3.destroy, padx=10, pady=10)
            Exit4.pack()

            fr3= Frame(dtable3)
            fr3.pack(side=LEFT, padx=20)

            T3= ttk.Treeview(fr3, columns=(1,2,3,4,5,6,7,8,9), show= 'headings',height=n6)
            T3.pack()

            T3.heading(1, text='Book No.')
            T3.heading(2, text='Name')
            T3.heading(3, text='Author')
            T3.heading(4, text='Category')
            T3.heading(5, text='Description')
            T3.heading(6, text='No. of copies')
            T3.heading(7, text='No. of copies sold')
            T3.heading(8, text='MRP')
            T3.heading(9, text='Selling Price')
            
            for g in DL3:
                T3.insert('','end', values=g)


            dtable3.mainloop()

                
        if Rcode==C:
            messagebox.showinfo('Book Buffet: Admin','WELCOME ! ADMIN :)')
            choice=Tk()
            choice.title('Book Buffet: Admin_Options')
            choice.geometry('600x600')
            Bo= Button(choice, text='   DONOR RECORD   ', bg='PaleVioletRed1',font="Helvetica 12 bold",padx=20, pady=20,command=D)
            Bo1= Button(choice, text=' RECIPIENT RECORD ', bg='PaleVioletRed2',font="Helvetica 12 bold",padx=20, pady=20,command=R)
            Bo2= Button(choice, text=' BORROWER RECORD ', bg='PaleVioletRed3',font="Helvetica 12 bold",padx=20, pady=20,command=B)
            Bo3= Button(choice, text='   BOOK RECORD   ', bg='PaleVioletRed3',font="Helvetica 12 bold",padx=20, pady=20,command=Book_R)
            Bo4= Button(choice, text='BACK TO MAIN MENU', bg='PaleVioletRed3',font="Helvetica 12 bold",padx=20, pady=20,command=choice.destroy)
            Bo.place(x=300,y=50, anchor=CENTER)
            Bo1.place(x=300,y=150, anchor=CENTER)
            Bo2.place(x=300,y=250, anchor=CENTER)
            Bo3.place(x=300,y=350, anchor=CENTER)
            Bo4.place(x=300,y=450, anchor=CENTER)
        else:
            messagebox.showwarning('Warning','Incorrect Code. Try again')
               
    lb= Label(A, text= "Enter CODE :",font="Helvetica 12 bold")
    c= Entry(A, textvariable=code, show='*')
    lb.grid(row=1,sticky=W)
    c.grid(row=1,column=2, columnspan=7)
    B1= Button(A, text= 'Back to main menu', bg='pink', command=A.destroy, font="Helvetica 12 bold")
    B2= Button(A, text= 'Done', bg='pink', command=Ad_2, font="Helvetica 12 bold")
    B1.grid(row=5)
    B2.grid(row=3)

    A.mainloop()
        
#-----------------------------------------------------------------MAIN WINDOW-------------------------------------------------------------------------------------------

root = Tk()
root.title("BOOK ZONE")
root.geometry("1500x700")
root.minsize(612,400)

header= Label(root, text= "WELCOME ! to BOOK BUFFET", bg='IndianRed1', fg='brown4', font="comicsansns 62 bold", borderwidth=5, relief=GROOVE,padx=74)
header.place(x=0,y=0)
button= Button(root, text= 'WANT TO DONATE', fg='dark green', bg='DarkOliveGreen1', command= d1.dentries, font="Helvetica 20 bold",padx=20,pady=10)
button1= Button(root, text= 'WANT A BOOK',fg='dark green', bg='DarkOliveGreen1', command= d2.typ_rec, font="Helvetica 20 bold",padx=20,pady=10)
button2= Button(root, text= 'WANT to KNOW About ORGANISATION', fg='dark green', bg='DarkOliveGreen1', command=org, font="Helvetica 20 bold",padx=20,pady=10)
button3= Button(root, text= 'EXIT', fg='dark green', bg='DarkOliveGreen1', font="Helvetica 20 bold",padx=20, pady=10, command=root.destroy)
button4= Button(root, text= 'MEMBERS LOGIN', fg='dark green', bg='DarkOliveGreen1', font="Helvetica 20 bold",padx=20, pady=10, command=log_in)
button5= Button(root, text= 'BOOK LIST', fg='dark green', bg='DarkOliveGreen1', font="Helvetica 20 bold",padx=20, pady=10, command= Diff_list)
button6= Button(root, text= 'RETURN BOOK', fg='dark green', bg='DarkOliveGreen1', font="Helvetica 20 bold",padx=20, pady=10, command= d2.Return)
button7= Button(root, text= 'ADMIN', fg='dark green', bg='DarkOliveGreen1', font="Helvetica 20 bold",padx=20, pady=10, command= Admin)

button.place(x=40,y=140)
button1.place(x=1000,y=140)
button2.place(x=380,y=400)
button3.place(x=600,y=600)
button4.place(x=515,y=300)
button5.place(x=550,y=500)
button6.place(x=530,y=200)
button7.place(x=590,y=110)

canvas = Canvas(root, width = 300, height = 300)
canvas.place(x=50, y=400)
img = ImageTk.PhotoImage(Image.open("C://Users//sujal//Desktop//MOLI//MOLI PYTHON//PROJECT//im1.png"))
canvas.create_image(20, 20, anchor=NW, image=img)

canvas1 = Canvas(root, width = 320, height = 320)
canvas1.place(x=1000, y=380)
img1 = ImageTk.PhotoImage(Image.open("C://Users//sujal//Desktop//MOLI//MOLI PYTHON//PROJECT//im5.png"))
canvas1.create_image(10, 10, anchor=NW, image=img1)

root.mainloop()
