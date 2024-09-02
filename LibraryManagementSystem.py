from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class librarymanagementsystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1500x800+0+0")


        #====================================================================
        self.member_var = StringVar()
        self.prnno_var = StringVar()
        self.title_var = StringVar()
        self.name_var = StringVar()
        self.address_var = StringVar()
        self.postcode_var = StringVar()
        self.phoneno_var = StringVar()
        self.bookid_var = StringVar()
        self.bookname_var = StringVar()
        self.bookauthor_var = StringVar()
        self.dateofissue_var = StringVar()
        self.duedate_var = StringVar()
        self.daysonbook_var = StringVar()
        self.price_var = StringVar()



        lbtitle = Label(self.root,text="MY LIBRARY",bg="blue",fg="white",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbtitle.pack(side=TOP,fill=X)

        frame = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="blue")
        frame.place(x=0,y=130,width=1530,height=400)

        DataLeft = LabelFrame(frame,text="LIBRARY INFORMATION",bg="powder blue",fg="white",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataLeft.place(x=0,y=5,width=900,height=350)

        labelmember = Label(DataLeft,bg="light blue",text="Member type",font=("times new roman",15,"bold"),padx=2,pady=6)
        labelmember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataLeft,font=("times new roman",15,"bold"),textvariable=self.member_var,width = 27,state="readonly")
        comMember["value"]=("Admin","Student","Teacher")
        comMember.grid(row=0,column = 1)
        
        labelPRN_No = Label(DataLeft,bg="powder blue",text="PRN Number",font=("times new roman",15,"bold"),padx=2,pady=6)
        labelPRN_No.grid(row=1,column=0,sticky=W)
        textPRN = Entry(DataLeft,font=("times new roman",15,"bold"),textvariable=self.prnno_var,width=30)
        textPRN.grid(row=1,column=1)

        labelTitle = Label(DataLeft,bg="powder blue",text="Title",font=("times new roman",15,"bold"),padx=2,pady=6)
        labelTitle.grid(row=2,column=0,sticky=W)
        textTitle = Entry(DataLeft,font=("times new roman",15,"bold"),textvariable=self.title_var,width=30)
        textTitle.grid(row=2,column=1)

        labelName = Label(DataLeft,bg="powder blue",text="Name",font=("times new roman",15,"bold"),padx=2,pady=6)
        labelName.grid(row=3,column=0,sticky=W)
        textName = Entry(DataLeft,font=("times new roman",15,"bold"),textvariable=self.name_var,width=30)
        textName.grid(row=3,column=1)

        labelAddress = Label(DataLeft,bg="powder blue",text="Address",font=("times new roman",15,"bold"),padx=2,pady=6)
        labelAddress.grid(row=4,column=0,sticky=W)
        textAddress = Entry(DataLeft,font=("times new roman",15,"bold"),textvariable=self.address_var,width=30)
        textAddress.grid(row=4,column=1)

        labelPostCode = Label(DataLeft,bg="powder blue",text="Post Code",font=("times new roman",15,"bold"),padx=2,pady=6)
        labelPostCode.grid(row=5,column=0,sticky=W)
        textPostCode = Entry(DataLeft,font=("times new roman",15,"bold"),textvariable=self.postcode_var,width=30)
        textPostCode.grid(row=5,column=1)

        labelPhoneNo = Label(DataLeft,bg="powder blue",text="Phone No",font=("times new roman",15,"bold"),padx=2,pady=6)
        labelPhoneNo.grid(row=5,column=0,sticky=W)
        textPhoneNo = Entry(DataLeft,font=("times new roman",15,"bold"),textvariable=self.phoneno_var,width=30)
        textPhoneNo.grid(row=5,column=1)

        labelBookId = Label(DataLeft,bg="powder blue",text="BookId",font=("times new roman",15,"bold"),padx=2,pady=6)
        labelBookId.grid(row=6,column=0,sticky=W)
        textBookId = Entry(DataLeft,font=("times new roman",15,"bold"),textvariable=self.bookid_var,width=30)
        textBookId.grid(row=6,column=1)

        labelBookName = Label(DataLeft,bg="powder blue",text="Book Name",font=("times new roman",15,"bold"),padx=2,pady=6)
        labelBookName.grid(row=0,column=2,sticky=W)
        textBookName = Entry(DataLeft,font=("times new roman",15,"bold"),textvariable=self.bookname_var,width=30)
        textBookName.grid(row=0,column=3)

        labelAuthor = Label(DataLeft,bg="powder blue",text="Book Author",font=("times new roman",15,"bold"),padx=2,pady=6)
        labelAuthor.grid(row=1,column=2,sticky=W)
        textAuthor = Entry(DataLeft,font=("times new roman",15,"bold"),textvariable=self.bookauthor_var,width=30)
        textAuthor.grid(row=1,column=3)

        labelDateOfIssue = Label(DataLeft,bg="powder blue",text="Date of Issue",font=("times new roman",15,"bold"),padx=2,pady=6)
        labelDateOfIssue.grid(row=2,column=2,sticky=W)
        textDateOfIssue = Entry(DataLeft,font=("times new roman",15,"bold"),textvariable=self.dateofissue_var,width=30)
        textDateOfIssue.grid(row=2,column=3)

        labelDateDue = Label(DataLeft,bg="powder blue",text="Due Date",font=("times new roman",15,"bold"),padx=2,pady=6)
        labelDateDue.grid(row=3,column=2,sticky=W)
        textDateDue = Entry(DataLeft,font=("times new roman",15,"bold"),textvariable=self.duedate_var,width=30)
        textDateDue.grid(row=3,column=3)

        labelDaysOnBook = Label(DataLeft,bg="powder blue",text="Days On Book",font=("times new roman",15,"bold"),padx=2,pady=6)
        labelDaysOnBook.grid(row=4,column=2,sticky=W)
        textDaysOnBook = Entry(DataLeft,font=("times new roman",15,"bold"),textvariable=self.daysonbook_var,width=30)
        textDaysOnBook.grid(row=4,column=3)

        labelPrice = Label(DataLeft,bg="powder blue",text="Price",font=("times new roman",15,"bold"),padx=2,pady=6)
        labelPrice.grid(row=5,column=2,sticky=W)
        textPrice = Entry(DataLeft,font=("times new roman",15,"bold"),textvariable=self.price_var,width=30)
        textPrice.grid(row=5,column=3)


        #=========================================================================

        DataRight = LabelFrame(frame,text="BOOK DETAILS",bg="powder blue",fg="white",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataRight.place(x=910,y=5,width=540,height=350)

        self.txtBox=Text(DataRight,font=("times new roman",12,"bold"),width=30,height=15,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollBar = Scrollbar(DataRight)
        listScrollBar.grid(row=0,column=1,sticky="ns")

        listofbooks=['C++','Java','Python','DSA','DAA','Anatomy','Pathophysiology','Inorganic','C Language','Maths',
                 'Physics','Chemistry','Geography','History','Polity','Economics','Artificial Intelligence','Cryptography'
                 'Cloud Computing']
        
        def selectbook(event):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if(x=="C++"):
                self.bookid_var.set("BKID4531")
                self.bookname_var.set("C++")
                self.title_var.set("Practice")
                self.bookauthor_var.set("Paul Berry")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateofissue_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.price_var.set("Rs. 500")

        listBox=Listbox(DataRight,font=("times new roman",12,"bold"),width=30,height=15)
        listBox.bind("<<ListboxSelect>>",selectbook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollBar.config(command=listBox.yview)

        for item in listofbooks:
            listBox.insert(END,item)

        #================================================================

        buttonframe = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="light blue")
        buttonframe.place(x=0,y=530,width=1530,height=70)

        buttonaddData = Button(buttonframe,command=self.adddata,text="ADD DATA",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        buttonaddData.grid(row=0,column=0)

        buttonaddData = Button(buttonframe,command=self.showData,text="SHOW DATA",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        buttonaddData.grid(row=0,column=1)

        buttonupdateData = Button(buttonframe,command=self.update_data,text="UPDATE DATA",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        buttonupdateData.grid(row=0,column=2)

        buttonaddData = Button(buttonframe,command=self.delete_data,text="DELETE DATA",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        buttonaddData.grid(row=0,column=3)

        buttonaddData = Button(buttonframe,command=self.reset,text="RESET",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        buttonaddData.grid(row=0,column=4)

        buttonaddData = Button(buttonframe,command=self.Exit,text="EXIT",font=("times new roman",12,"bold"),width=26,bg="blue",fg="white")
        buttonaddData.grid(row=0,column=5)


        #================================================================

        detailsframe = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="light blue")
        detailsframe.place(x=0,y=600,width=1530,height=195)


        Table_frame = Frame(detailsframe,bd=6,relief=RIDGE,bg="light blue")
        Table_frame.place(x=0,y=2,width=1460,height=170)

        xscroll = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame,orient=VERTICAL)


        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","Title","Name","Address","PostCode",
                                                            "PhoneNo","BookID","BookName","Author","DateofIssue","DueDate",
                                                            "DaysOnBook","Price"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN Number")
        self.library_table.heading("Title",text="Title")
        self.library_table.heading("Name",text="Name")
        self.library_table.heading("Address",text="Address")
        self.library_table.heading("PostCode",text="Post Code")
        self.library_table.heading("PhoneNo",text="Phone Number")
        self.library_table.heading("BookID",text="Book ID")
        self.library_table.heading("BookName",text="Book Name")
        self.library_table.heading("Author",text="Author")
        self.library_table.heading("DateofIssue",text="Date Of Issue")
        self.library_table.heading("DueDate",text="Due Date")
        self.library_table.heading("DaysOnBook",text="Days On Book")
        self.library_table.heading("Price",text="Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("Title",width=100)
        self.library_table.column("Name",width=100)
        self.library_table.column("Address",width=100)
        self.library_table.column("PostCode",width=100)
        self.library_table.column("PhoneNo",width=150)
        self.library_table.column("BookID",width=100)
        self.library_table.column("BookName",width=100)
        self.library_table.column("Author",width=100)
        self.library_table.column("DateofIssue",width=150)
        self.library_table.column("DueDate",width=150)
        self.library_table.column("DaysOnBook",width=150)
        self.library_table.column("Price",width=100)

        self.fetch_data()
        self.library_table.bind("<<TreeviewSelect>>",self.get_cursor)

    def adddata(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="library")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into libraryinfo values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.member_var.get(),
                                                                                                    self.prnno_var.get(),
                                                                                                    self.title_var.get(),
                                                                                                    self.name_var.get(),
                                                                                                    self.address_var.get(),
                                                                                                    self.postcode_var.get(),
                                                                                                    self.phoneno_var.get(),
                                                                                                    self.bookid_var.get(),
                                                                                                    self.bookname_var.get(),
                                                                                                    self.bookauthor_var.get(),
                                                                                                    self.dateofissue_var.get(),
                                                                                                    self.duedate_var.get(),
                                                                                                    self.daysonbook_var.get(),
                                                                                                    self.price_var.get(),
                                                                                                    ))
        conn.commit()
        conn.close()
        self.fetch_data()                                                                                     

        messagebox.showinfo("success","data successfully added")

    def update_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="library")
        my_cursor=conn.cursor()
        my_cursor.execute("update libraryinfo set Member=%s,Title=%s,Name=%s,Address=%s,PostCode=%s,Phone_No=%s,Book_ID=%s,Book_Name=%s,Book_Author=%s,Date_Of_Issue=%s,Due_Date=%s,Days_On_Book=%s,Price=%s where PRN_No=%s",(
                                                                                                                                                                    self.member_var.get(),
                                                                                                                                                                    self.title_var.get(),
                                                                                                                                                                    self.name_var.get(),
                                                                                                                                                                    self.address_var.get(),
                                                                                                                                                                    self.postcode_var.get(),
                                                                                                                                                                    self.phoneno_var.get(),
                                                                                                                                                                    self.bookid_var.get(),
                                                                                                                                                                    self.bookname_var.get(),
                                                                                                                                                                    self.bookauthor_var.get(),
                                                                                                                                                                    self.dateofissue_var.get(),
                                                                                                                                                                    self.duedate_var.get(),
                                                                                                                                                                    self.daysonbook_var.get(),
                                                                                                                                                                    self.price_var.get(),
                                                                                                                                                                    self.prnno_var.get()
                                                                                                                                                                
                                                                                                                                                                 ))
                                                                                                                                                                            
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("success","data updated successfully")                                                                                                                                                                   
                                                                                              
                                                                                              
                                                                                              

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="library")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from libraryinfo")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0])
        self.prnno_var.set(row[1])
        self.title_var.set(row[2])
        self.name_var.set(row[3])
        self.address_var.set(row[4])
        self.postcode_var.set(row[5])
        self.phoneno_var.set(row[6])
        self.bookid_var.set(row[7])
        self.bookname_var.set(row[8])
        self.bookauthor_var.set(row[9])
        self.dateofissue_var.set(row[10])
        self.duedate_var.set(row[11])
        self.daysonbook_var.set(row[12])
        self.price_var.set(row[13])

    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRN NO:\t\t"+ self.prnno_var.get()+"\n")
        self.txtBox.insert(END,"Title:\t\t"+ self.title_var.get()+"\n")
        self.txtBox.insert(END,"Name:\t\t"+ self.name_var.get()+"\n")
        self.txtBox.insert(END,"Address:\t\t"+ self.address_var.get()+"\n") 
        self.txtBox.insert(END,"Post Code:\t\t"+ self.postcode_var.get()+"\n")
        self.txtBox.insert(END,"Phone No:\t\t"+ self.phoneno_var.get()+"\n")
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Name:\t\t"+ self.bookname_var.get()+"\n")
        self.txtBox.insert(END,"Book Author:\t\t"+ self.bookauthor_var.get()+"\n")
        self.txtBox.insert(END,"date of issue:\t\t"+ self.dateofissue_var.get()+"\n")
        self.txtBox.insert(END,"due date:\t\t"+ self.duedate_var.get()+"\n")
        self.txtBox.insert(END,"days on book:\t\t"+ self.daysonbook_var.get()+"\n")
        self.txtBox.insert(END,"Price:\t\t"+ self.price_var.get()+"\n")

    def reset(self):
        self.member_var.set("")
        self.prnno_var.set("")
        self.title_var.set("")
        self.name_var.set("")
        self.address_var.set("")
        self.postcode_var.set("")
        self.phoneno_var.set("")
        self.bookid_var.set("")
        self.bookname_var.set("")
        self.bookauthor_var.set("")
        self.dateofissue_var.set("")
        self.duedate_var.set("")
        self.daysonbook_var.set("")
        self.price_var.set("")

    def Exit(self):
        Exit=tkinter.messagebox.askyesno("MY LIBRARY","Do you want to exit ?")
        if Exit>0:
            self.root.destroy()
            return
        
    def delete_data(self):
        if self.prnno_var.get()=="" or self.bookid_var.get()=="":
            messagebox.showerror("Error","first select data")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="root",database="library")
            my_cursor=conn.cursor()
            my_cursor.execute("DELETE FROM libraryinfo WHERE PRN_No=%s AND Book_ID=%s", (self.prnno_var.get(), self.bookid_var.get()))
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()


            messagebox.showinfo("success","data deleted successfully")
            






if __name__ == "__main__":
    root=Tk()
    obj = librarymanagementsystem(root)
    root.mainloop()
