"""
Projects Name: Student Management System (GUI)
Author : Udoy 
Language: Python 
Library : Tkinter  
"""
#import the librery 
from tkinter import *
from tkinter import ttk 
import pymysql
from tkinter import messagebox

#write the ui 
class Student:
    def __init__(self,root) -> None:
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1950x1200+0+0")
        
        #=======All Variables===============
        self.roll = StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.gender = StringVar()
        self.contact = StringVar()
        self.dob = StringVar()
        
        self.search_by = StringVar()
        self.search_txt = StringVar()
        
        
        #==============Frame Whole Projects Title===============
        title = Label(self.root,text="Student Management System",font=("times new roman",40,"bold"),bd=10,relief=GROOVE,bg="yellow",fg='red')
        title.pack(side=TOP,fill=X)
        
        #================Manage Frame =======================
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=1950,height=1200)
        
       
        
        #title
        m_title = Label(Manage_Frame,text="Manage Students",fg="white",bg="crimson",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)
        
        #name , roll, id 
        roll = Label(Manage_Frame,text="Roll No. ",fg="white",bg="crimson",font=("times new roman",20,"bold"))
        roll.grid(row=1,column=0,padx=20,pady=10,sticky='w')
        
        #text field 
        txt_field = Entry(Manage_Frame,textvariable=self.roll,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_field.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        
        #Name 
        name = Label(Manage_Frame,text="Name ",fg="white",bg="crimson",font=("times new roman",20,"bold"))
        name.grid(row=2,column=0,padx=20,pady=10,sticky='w')
        
        name_txt = Entry(Manage_Frame,textvariable=self.name,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        name_txt.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        #Email 
        email = Label(Manage_Frame,text="Email ",fg="white",bg="crimson",font=("times new roman",20,"bold"))
        email.grid(row=3,column=0,padx=20,pady=10,sticky='w')
        
        email_txt = Entry(Manage_Frame,textvariable=self.email,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        email_txt.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        
        #Gender
        gender = Label(Manage_Frame,text="Gender ",fg="white",bg="crimson",font=("times new roman",20,"bold"))
        gender.grid(row=4,column=0,padx=20,pady=10,sticky='w')
        
        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender,font=("time new roman",13,"bold"),state='readonly')
        combo_gender['values'] = ("Male","Female","Others")
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        
        
        #Contact No 
        contact = Label(Manage_Frame,text="Contact ",fg="white",bg="crimson",font=("times new roman",20,"bold"))
        contact.grid(row=5,column=0,padx=20,pady=10,sticky='w')
        
        contact_txt = Entry(Manage_Frame,textvariable=self.contact,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        contact_txt.grid(row=5,column=1,pady=10,padx=20,sticky="w")
        #dob 
        dob = Label(Manage_Frame,text="D.O.B ",fg="white",bg="crimson",font=("times new roman",20,"bold"))
        dob.grid(row=6,column=0,padx=20,pady=10,sticky='w')
        
        dob_txt = Entry(Manage_Frame,textvariable=self.dob,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        dob_txt.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        
        #Address 
        Address = Label(Manage_Frame,text="Address ",fg="white",bg="crimson",font=("times new roman",20,"bold"))
        Address.grid(row=7,column=0,padx=20,pady=10,sticky='w')
        
        self.Address_txt = Text(Manage_Frame,width=30,height=4,font=("",10))
        self.Address_txt.grid(row=7,column=1,pady=10,padx=20,sticky="w")
        
        #========Button Field===================
        button_frame = Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        button_frame.place(x=10,y=500,width=430) 
        
        #ad btn 
        AddBtn = Button(button_frame,text="Add",width=10,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
        UpdateBtn = Button(button_frame,text="Update",command=self.update_data,width=10).grid(row=0,column=1,padx=10,pady=10)
        DeleteBtn = Button(button_frame,text="Delete",command=self.delete_data,width=10).grid(row=0,column=2,padx=10,pady=10)
        ClearBtn = Button(button_frame,text="Clear",command=self.clear,width=10).grid(row=0,column=3,padx=10,pady=10)
        
        #======== Details Frame =============================
        Details_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Details_Frame.place(x=500,y=100,width=1393,height=890)
        
        lbl_search = Label(Details_Frame,text='Search By',bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,padx=20,pady=10,sticky="w")
        
        combo_search = ttk.Combobox(Details_Frame,textvariable=self.search_by,font=("time new roman",13,"bold"),state='readonly')
        combo_search['values'] = ("roll_no","Name","Contact")
        combo_search.grid(row=0,column=1,pady=10,padx=10,sticky="w")
        
        
        searchfield_txt = Entry(Details_Frame,textvariable=self.search_txt,width=30,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        searchfield_txt.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        
        SearchBtn = Button(Details_Frame,text="Search",command=self.search_data,width=10).grid(row=0,column=3,padx=10,pady=10)
        ShowAllBtn = Button(Details_Frame,text="Show All",width=10,command=self.show_data).grid(row=0,column=4,padx=10,pady=10)
        
        #============ Table Frame ===========================
        Table_Frame = Frame(Details_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=1360,height=789)
        
        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame,columns=("Roll","Name","Email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        
        self.Student_table.heading("Roll",text="Roll No. ")
        self.Student_table.heading("Name",text="Name ")
        self.Student_table.heading("Email",text="Email")
        self.Student_table.heading("Gender",text="Gender ")
        self.Student_table.heading("Contact",text="Contact ")
        self.Student_table.heading("DOB",text="D.O.B ")
        self.Student_table.heading("Address",text="Address ")
        self.Student_table['show'] = 'headings'
        
        #change the column height 
        self.Student_table.column("Roll",width=100)
        self.Student_table.column("Name",width=100)
        self.Student_table.column("Email",width=100)
        self.Student_table.column("Gender",width=100)
        self.Student_table.column("Contact",width=100)
        self.Student_table.column("DOB",width=100)
        self.Student_table.column("Address",width=140)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.show_data()
        
    #adding student to the database 
    def add_student(self):
        if self.roll.get()=="" or self.name.get()=="" or self.email.get()=="" or self.contact.get()=="" or self.dob.get()=="" or self.Address_txt.get('1.0',END) =="":
            messagebox.showerror("Error","All Fields are required!!")
        else:
            con =pymysql.connect(host='localhost',user="root",password="",database="studentmanagement")
            cur = con.cursor()
            
            cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(
                self.roll.get(),
                self.name.get(),
                self.email.get(),
                self.gender.get(),
                self.contact.get(),
                self.dob.get(),
                self.Address_txt.get('1.0',END)
            ))
            
            con.commit()
            self.show_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been Added Successfully")
    def show_data(self):
        con =pymysql.connect(host='localhost',user="root",password="",database="studentmanagement")
        cur = con.cursor()
        cur.execute("select * from student")
        rows = cur.fetchall()
        if len(rows)!= 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.roll.set("")
        self.name.set("")
        self.email.set("")
        self.gender.set("")
        self.contact.set("")
        self.dob.set("")
        self.Address_txt.delete("1.0",END)
        
    def get_cursor(self,r):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.roll.set(row[0])
        self.name.set(row[1])
        self.email.set(row[2])
        self.gender.set(row[3])
        self.contact.set(row[4])
        self.dob.set(row[5])
        self.Address_txt.delete("1.0",END)
        self.Address_txt.insert(END,row[6])
    
    def update_data(self):
        con =pymysql.connect(host='localhost',user="root",password="",database="studentmanagement")
        cur = con.cursor()
        if self.roll.get()=="" or self.name.get()=="" or self.email.get()=="" or self.contact.get()=="" or self.dob.get()=="" or self.Address_txt.get('1.0',END) =="":
            messagebox.showerror("Error","All Fields are required!!")
        else:
            cur.execute("update student set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
           
            self.name.get(),
            self.email.get(),
            self.gender.get(),
            self.contact.get(),
            self.dob.get(),
            self.Address_txt.get('1.0',END),
            self.roll.get()
            ))
        
            con.commit()
            self.show_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been Updated Successfully")
            
       
        
    def delete_data(self):
        if self.roll.get()=="" or self.name.get()=="" or self.email.get()=="" or self.contact.get()=="" or self.dob.get()=="" or self.Address_txt.get('1.0',END) =="":
            messagebox.showerror("Error","All Fields are required!!")
        else:
            con =pymysql.connect(host='localhost',user="root",password="",database="studentmanagement")
            cur = con.cursor()
            cur.execute("delete from student where roll_no=%s",self.roll.get())
            con.commit()
            con.close()
            self.show_data()
            self.clear()
            messagebox.showinfo("Success","Record has been Deleted Successfully")
            
        
       
    
    def search_data(self):
        con =pymysql.connect(host='localhost',user="root",password="",database="studentmanagement")
        cur = con.cursor()
        if self.search_by.get()=="" or self.search_txt.get() =="":
            messagebox.showwarning("Warning","Search Field should not be given Empty")
        else:
            cur.execute("select * from student where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows = cur.fetchall()
            if len(rows)!= 0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('',END,values=row)
                con.commit()
        con.close()
        
        
     
        
            
        
        
root = Tk()
ob = Student(root)
root.mainloop()
    
