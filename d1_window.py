#FOR Donor entry
from tkinter import *
from tkinter import ttk
import connectivity as con
from tkinter import messagebox
from datetime import datetime
from tkinter import Canvas
from PIL import ImageTk
from PIL import Image

#-----------------------------------------------------------------DONOR PAGE------------------------------------------------------------------------

def dentries():
    global d1
    global donor_name
    global donor_phn
    global donor_address
    global amt
    global entry_4
    global book_name
    global book_author
    global quantity
    global mrp
    global category
    global descript
    global username
    global password
    global valid_pswd
    
    donor_name= StringVar()
    donor_address= StringVar() 
    donor_phn= IntVar()
    entry_4= StringVar()
    amt= IntVar()
    book_name= StringVar()
    book_author= StringVar()
    quantity= IntVar()
    mrp= IntVar()
    category= StringVar()
    descript= StringVar()
    username= StringVar()
    password= StringVar()
    valid_pswd= StringVar()

    opt= ['Book only', 'Money only', 'Both book & money']
    
    d1=Toplevel()
    d1.title("BOOK ZONE-Donor's Form")
    d1.geometry("600x700")
    d1.minsize(500,500)
    
    entry_1= Entry(d1, textvariable= donor_name)
    entry_2= Entry(d1, textvariable= donor_address)
    entry_3= Entry(d1, textvariable= donor_phn)
    entry_3.insert(END,0)
    entry_4= ttk.Combobox(d1, values=opt)
    entry_4.current(0)
    entry_5= Entry(d1, textvariable= amt)
    entry_5.insert(END,0)
    entry_6= Entry(d1, textvariable= book_name)
    entry_6.insert(END, '-')
    entry_7= Entry(d1, textvariable= book_author)
    entry_7.insert(END, '-')
    entry_8= Entry(d1, textvariable= quantity)
    entry_8.insert(END,0)
    entry_9= Entry(d1, textvariable= mrp)
    entry_9.insert(END,0)
    entry_10= Entry(d1, textvariable= category)
    entry_10.insert(END, '-')
    entry_11= Entry(d1, textvariable= descript)
    entry_11.insert(END, '-')
    entry_1.grid(row=0,column=2,columnspan=7)
    entry_2.grid(row=1,column=2,columnspan=7)
    entry_3.grid(row=2,column=2,columnspan=7)              #E-east, W-west, N-north, S-south
    entry_4.grid(row=3,column=2,columnspan=7)
    entry_5.grid(row=4,column=2,columnspan=7)
    entry_6.grid(row=5,column=2,columnspan=7)
    entry_7.grid(row=6,column=2,columnspan=7)
    entry_8.grid(row=7,column=2,columnspan=7)
    entry_9.grid(row=8,column=2,columnspan=7)
    entry_10.grid(row=9,column=2,columnspan=7)
    entry_11.grid(row=10,column=2,columnspan=7) 

    l1= Label(d1, text= "Donor Name :",font="Helvetica 12 bold")
    l2= Label(d1, text= "Donor Address :",font="Helvetica 12 bold")
    l3= Label(d1, text= "Phn No. :",font="Helvetica 12 bold")
    l4= Label(d1, text= "Donating :",font="Helvetica 12 bold")
    l5= Label(d1, text= "Enter Amount(Rs.) :",font="Helvetica 12 bold")
    l6= Label(d1, text= "Book Name :",font="Helvetica 12 bold")
    l7= Label(d1, text= "Book Author :",font="Helvetica 12 bold")
    l8= Label(d1, text= "Quantity :",font="Helvetica 12 bold")
    l9= Label(d1, text= "MRP of book :",font="Helvetica 12 bold")
    l10= Label(d1, text= "Category (Ex-Horror) :",font="Helvetica 12 bold")
    l11= Label(d1, text= "Book Description :",font="Helvetica 12 bold")
    l1.grid(row=0, sticky=W)            
    l2.grid(row=1, sticky=W)
    l3.grid(row=2, sticky=W)
    l4.grid(row=3, sticky=W)
    l5.grid(row=4, sticky=W)
    l6.grid(row=5, sticky=W)
    l7.grid(row=6, sticky=W)
    l8.grid(row=7, sticky=W)
    l9.grid(row=8, sticky=W)
    l10.grid(row=9, sticky=W)
    l11.grid(row=10, sticky=W)
   
#   ------------------------------------------------------Using UDF for Mysql Connection----------------------------------------------------------
    def mssgb():
        Nm=entry_1.get()
        Ad=entry_2.get()
        Pn=entry_3.get()
        Dt=entry_4.get()
        Am=entry_5.get()
        BN=entry_6.get()
        BA=entry_7.get()
        Qt=entry_8.get()
        Mrp=entry_9.get()
        Ct=entry_10.get()
        Ds=entry_11.get()
        Cb=c1.state()
        d1.destroy()
#       -------------------------------------------------------------------------------------------------------------------------------------------        
        def all_in_1():
            a=con.Execute_1('select max(donor_no) from donor ;')
            print(a)
            if a[0]==None:
                a=0
            else:
                a=a[0]
    
            bkn=con.Execute_1('select max(book_no) from book ;')
            print(bkn)
            if bkn[0]==None:
                bkn=0
            else:
                bkn=bkn[0]
            print(bkn)
            dt=str(datetime.today().strftime('%Y-%m-%d'))
            print(dt)
            print("insert into donor values ({},'{}','{}',{},'{}',{},{},{},'{}') ;".format(a+1,Nm, Ad, int(Pn), Dt, "NULL", bkn+1, int(Qt), dt))
            if Dt=='Book only':
                con.iua("insert into book values ({},'{}','{}','{}','{}',{},{},{},'{}') ;".format(bkn+1, BN, BA, Ct, Ds, int(Qt), 0, float(Mrp), (0.1*float(Mrp)) ))
                con.iua("insert into donor values ({},'{}','{}',{},'{}',{},{},{},'{}') ;".format(a+1, Nm, Ad, int(Pn), Dt, "NULL", bkn+1, int(Qt), dt))
            elif Dt=='Money only':
                con.iua("insert into donor values ({},'{}','{}',{},'{}',{},{},{},'{}') ;".format(a+1, Nm, Ad, int(Pn), Dt, float(Am), "NULL", "NULL", dt))
            else:
                con.iua("insert into book values ({},'{}','{}','{}','{}',{},{},{},'{}') ;".format(bkn+1, BN, BA, Ct, Ds, int(Qt), 0, float(Mrp), (0.1*float(Mrp)) ))
                con.iua("insert into donor values ({},'{}','{}',{},'{}',{},{},{},'{}') ;".format(a+1, Nm, Ad, int(Pn), Dt, float(Am), bkn+1, int(Qt), dt))


            print(Cb)
            if Cb == ('focus', 'selected') or c1.state() == ('selected',) :
                mno=con.Execute_1('select max(member_no) from members ;')
                print(mno[0])
                if mno[0]==None:
                    mno=0
                else:
                    mno=mno[0]
                    
                new_win=Tk()
                new_win.minsize(100,100)
                new_win.title('Create Account !!!')
                u_id= Entry(new_win, textvariable=username)
                pswd= Entry(new_win, textvariable=password, show='*')
                cpswd= Entry(new_win, textvariable=valid_pswd, show='*')
#               ------------------------------------------------------------------------------------------------------------------------------------
                def memb():
                    print(pswd.get(),cpswd.get())
                    if pswd.get()==cpswd.get() and len(pswd.get())<=10 :
                        messagebox.showinfo("Account_Info", "You are now our member !!!")
                        print("insert into members values({},{},'{}','{}',{},'{}','{}') ;".format(mno+1, a+1, Nm, Ad, int(Pn), u_id.get(),pswd.get()))
                        con.iua("insert into members values({},{},'{}','{}',{},'{}','{}') ;".format(mno+1, a+1, Nm, Ad, int(Pn), u_id.get(), pswd.get()))
                        new_win.destroy()
                        d1.destroy()
                    elif len(pswd.get())>10:
                        messagebox.showwarning('Warning','You have exceeded the password limit.')
                    else:
                        messagebox.showwarning('Warning','Your password and confirmation password do not match.')
                
                Button_memb= Button(new_win, text= 'Done', bg='pink', command=memb,font="Helvetica 12 bold",padx=6,pady=4)


                w1= Label(new_win, text= "User_name :",font="Helvetica 12 bold")
                w2= Label(new_win, text= "Password(atmost 10 char) :",font="Helvetica 12 bold")
                w3= Label(new_win, text= "Confirm Password :",font="Helvetica 12 bold") 
                w1.grid(row=0, sticky=W)
                w2.grid(row=1, sticky=W)
                w3.grid(row=2, sticky=W)
                u_id.grid(row=0,column=2)
                pswd.grid(row=1,column=2)
                cpswd.grid(row=2,column=2)
                Button_memb.grid(row=4,column=1)

        if len(Nm) != 0 and len(Ad) != 0 and int(Pn) > 0 and len(Dt) != 0  :
            if Dt=='Book only':
                if len(BN) <= 1 or len(BA) <= 1 or int(Qt)<= 0 or int(Mrp)<= 0 or len(Ct) <= 1 or len(Ds)<= 1:
                    messagebox.showwarning('Warning', 'All details of Book should be given.')
                else:
                    messagebox.showinfo('Book Buffet: Message',"Thank You "+Nm+" for donating.\n May you have a wonderful life ahead :)")
                    all_in_1()
            elif Dt=='Money only':
                if int(Am)<=0:
                    messagebox.showwarning('Warning', 'The amount you want to donate should be specified.')
                else:
                    messagebox.showinfo('Book Buffet: Message',"Thank You "+Nm+" for donating.\n May you have a wonderful life ahead :)")
                    all_in_1()
            else:
                if int(Am)<=0 or len(BN)<= 1 or len(BA)<= 1 or int(Qt)== 0 or int(Mrp)== 0 or len(Ct)<= 1 or len(Ds)<= 1:
                    messagebox.showwarning('Warning', 'All fields are mandatory.')
                else:
                    messagebox.showinfo('Book Buffet: Message',"Thank You "+Nm+" for donating.\n May you have a wonderful life ahead :)")
                    all_in_1()
        else:
            messagebox.showwarning('Warning', 'All fields are mandatory.')         

    c1= ttk.Checkbutton(d1, text='Want to become permanent member.')
    c1.grid(row=11, columnspan=2)

    button11=Button(d1, text='DONATE', bg='yellow', command= mssgb, padx=8, pady=8,font="Helvetica 12 bold")
    button11.grid(row=15)
    button12=Button(d1, text='BACK TO MAIN MENU', bg='yellow', command= d1.destroy, padx=8, pady=8,font="Helvetica 12 bold")
    button12.grid(row=17)

    c2 = Canvas(d1, width = 300, height = 300)
    c2.grid(row=23)
    i2 = ImageTk.PhotoImage(Image.open("C://Users//sujal//Desktop//MOLI//MOLI PYTHON//PROJECT//p_dnwin.png"))
    c2.create_image(20, 20, anchor=NW, image=i2)

    
    d1.mainloop()
