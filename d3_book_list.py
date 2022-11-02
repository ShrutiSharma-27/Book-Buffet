import connectivity as con
from tkinter import *
from tkinter import ttk
from tkinter import Canvas
from PIL import ImageTk
from PIL import Image

#------------------------------------------------------------------------------------------------------------------------------

def Av_list():
    query="select book_no, book_name, author, category, selling_price from book where no_of_copies <> 0 ;"
    List=con.Execute_multi(query)
    n=str(len(List))
    print(List)
    table_win= Toplevel()
    table_win.minsize(600,600)
    table_win.title('Available Books in BOOK BUFFET')
    head= Label(table_win, text='LIST OF AVAILABLE BOOKS' , bg='deep pink', font="comicsansns 40 bold", borderwidth=2)
    head.pack()

    frm= Frame(table_win)
    frm.pack(side=LEFT, padx=20)

    tv= ttk.Treeview(frm, columns=(1,2,3,4,5), show= 'headings', height=n)
    tv.pack(fill= BOTH, expand=1)

    tv.heading(1, text='Book No.')
    tv.heading(2, text='Book Name')
    tv.heading(3, text='Author')
    tv.heading(4, text='Category')
    tv.heading(5, text='Price')

    for a in List:
        tv.insert('','end', values=a)
    Exit= Button(table_win, text='EXIT', bg='lawn green',font="Helvetica 12 bold", command=table_win.destroy, padx=10, pady=10)
    Exit.pack(side=RIGHT)

    c1 = Canvas(table_win, width = 200, height = 500)
    c1.pack()
    i1 = ImageTk.PhotoImage(Image.open("C://Users//sujal//Desktop//MOLI//MOLI PYTHON//PROJECT//mickey.png"))
    c1.create_image(5, 5, anchor=NW, image=i1)

    table_win.mainloop()

#---------------------------------------------------------------------------------------------------------------------------------------------------

def Unav_list():
    query1="select book_no, book_name, author, category, selling_price from book where no_of_copies= 0 ;"
    List1=con.Execute_multi(query1)
    n1=str(len(List1))
    print(List1)
    table_win1= Toplevel()
    table_win1.minsize(600,600)
    table_win1.title('Unavailable Books in BOOK BUFFET')
    head1= Label(table_win1, text='LIST OF UNAVAILABLE BOOKS' , bg='deep pink', font="comicsansns 40 bold", borderwidth=2)
    head1.pack()

    frm1= Frame(table_win1)
    frm1.pack(side=LEFT, padx=20)

    tv1= ttk.Treeview(frm1, columns=(1,2,3,4,5), show= 'headings', height=n1)
    tv1.pack()

    tv1.heading(1, text='Book No.')
    tv1.heading(2, text='Book Name')
    tv1.heading(3, text='Author')
    tv1.heading(4, text='Category')
    tv1.heading(5, text='Price')

    for k in List1:
        tv1.insert('','end', values=k)
    Exit1= Button(table_win1, text='EXIT', bg='lawn green',font="Helvetica 12 bold", command=table_win1.destroy, padx=10, pady=10)
    Exit1.pack(side=RIGHT)

    c2 = Canvas(table_win1, width = 200, height = 500)
    c2.pack()
    i2 = ImageTk.PhotoImage(Image.open("C://Users//sujal//Desktop//MOLI//MOLI PYTHON//PROJECT//mickey.png"))
    c2.create_image(5, 5, anchor=NW, image=i2)

    table_win1.mainloop()

#---------------------------------------------------------------------------------------------------------------------------------------------------  
