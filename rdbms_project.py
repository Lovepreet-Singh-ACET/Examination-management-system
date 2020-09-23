import tkinter as tk
from tkinter import font  as tkfont
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from tkinter import ttk
import cx_Oracle
import sys
u_p=[]
s_u_p=[]

def main():
    class SampleApp(tk.Tk):

        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)

            self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

            # the container is where we'll stack a bunch of frames
            # on top of each other, then the one we want visible
            # will be raised above the others
            container = tk.Frame(self)
            container.pack(side="top", fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}
            for F in (LoginPage,StartPage,Admin,Admin_LoginPage,Teacher,Teacher_LoginPage,Student,Student_LoginPage,Student_Details,Teacher_Details,Question_Details,Create_User,Courses_Branch,Result_Details):
                page_name = F.__name__
                frame = F(parent=container, controller=self)
                self.frames[page_name] = frame

                # put all of the pages in the same location;
                # the one on the top of the stacking order
                # will be the one that is visible.
                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame("LoginPage")

        def show_frame(self, page_name):
            '''Show a frame for the given page name'''
            frame = self.frames[page_name]
            frame.tkraise()
        
    ##############################################################################################################
            
    class LoginPage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            
            #self.title("login system")

            ##############ALL IMAGES########
            self.bg_icon=ImageTk.PhotoImage(file="bgg1.jpg")
            self.user_icon=PhotoImage(file="user.png")
            self.pass_icon=PhotoImage(file="pass.png")
            self.logo_icon=PhotoImage(file="logo.png")
            ######### variables############
            self.uname=StringVar()
            self.passw=StringVar()

            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="Login System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Login_Frame=tk.Frame(self,bg="white")
            Login_Frame.place(x=400,y=150)

            logolbl=tk.Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)

            lbluser=tk.Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(rows=1,column=0,padx=20,pady=10)
            txtuser=tk.Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

            lblpass=tk.Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(rows=2,column=0,padx=20,pady=10)
            txtpass=tk.Entry(Login_Frame,bd=5,textvariable=self.passw,relief=GROOVE,font=("",15),show="*").grid(row=2,column=1,padx=20)

            btn_log=tk.Button(Login_Frame,text="Login",width=10,command=self.login,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)
            btn_log=tk.Button(Login_Frame,text="Quit",width=10,command=self.logout,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=4,column=1,pady=10)





        def login(self):
            if self.uname.get()=="" or self.passw.get()=="":
                messagebox.showerror("Error","All fields are required!!!")
            elif self.uname.get()=="love" and self.passw.get()=="1234":
                 messagebox.showinfo("Successfull",f"welcome{self.uname.get()}")
                 self.passw.set('')
                 self.uname.set('')
                 self.controller.show_frame("StartPage")
                 
            else:
                messagebox.showerror("Error","Invalid Username or Password!!!")

        def logout(self):
            app.destroy()

################################################################################################################################            
    class StartPage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            
            self.bg_icon=ImageTk.PhotoImage(file="bgg1.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="MAIN MENU",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Menu_Frame=tk.Frame(self,bg="black")
            Menu_Frame.place(x=550,y=320)
            
            button = tk.Button(Menu_Frame, text="Go to Login Page",width=20,command=lambda: controller.show_frame("LoginPage"),font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=0,column=0,pady=10)
            button1 = tk.Button(Menu_Frame, text="ADMIN LOGIN",width=20,command=lambda: controller.show_frame("Admin_LoginPage"),font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=1,column=0,pady=10)
            button2 = tk.Button(Menu_Frame, text="TEACHER LOGIN",width=20,command=lambda: controller.show_frame("Teacher_LoginPage"),font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=2,column=0,pady=10)
            button3 = tk.Button(Menu_Frame, text="STUDENT LOGIN",width=20,command=lambda: controller.show_frame("Student_LoginPage"),font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=0,pady=10)

    ##################################################################################################

    class Admin_LoginPage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            
            ##############ALL IMAGES########
            self.bg_icon=ImageTk.PhotoImage(file="bgg1.jpg")
            self.user_icon=PhotoImage(file="user.png")
            self.pass_icon=PhotoImage(file="pass.png")
            self.logo_icon=PhotoImage(file="logo.png")
            ######### variables############

            self.uname=StringVar()
            self.passw=StringVar()

            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="Welcome To Admin System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Login_Frame=tk.Frame(self,bg="white")
            Login_Frame.place(x=400,y=150)

            logolbl=tk.Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)

            lbluser=tk.Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(rows=1,column=0,padx=20,pady=10)
            txtuser=tk.Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

            lblpass=tk.Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(rows=2,column=0,padx=20,pady=10)
            txtpass=tk.Entry(Login_Frame,bd=5,textvariable=self.passw,relief=GROOVE,font=("",15),show="*").grid(row=2,column=1,padx=20)
            btn_log=tk.Button(Login_Frame,text="Login",width=10,command=self.login,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)
            btn_log=tk.Button(Login_Frame,text="Back",width=10,command=lambda: controller.show_frame("StartPage"),font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=4,column=1,pady=10)


        def login(self):
            if self.uname.get()=="" or self.passw.get()=="":
                messagebox.showerror("Error","All fields are required!!!")
            elif self.uname.get()=="admin" and self.passw.get()=="1234":
                 messagebox.showinfo("Successfull",f"welcome{self.uname.get()}")
                 self.passw.set('')
                 self.uname.set('')
                 self.controller.show_frame("Admin")
                 
            else:
                messagebox.showerror("Error","Invalid Username or Password!!!")
                
    ######################################################################################################

    class Admin(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            
            self.bg_icon=ImageTk.PhotoImage(file="bgg1.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="ADMIN MENU",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Admin_Frame=tk.Frame(self,bg="black")
            Admin_Frame.place(x=0,y=85,width=1366,height=60)

            button = tk.Button(Admin_Frame, text="Student",width=10,command=lambda: controller.show_frame("Student_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=0,pady=10)
            button1 = tk.Button(Admin_Frame, text="Teacher",width=10,command=lambda: controller.show_frame("Teacher_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=1,pady=10)
            button2= tk.Button(Admin_Frame, text="Question Details",width=15,command=lambda: controller.show_frame("Question_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=2,pady=10)
            button3 = tk.Button(Admin_Frame, text="Create User",width=10,command=lambda: controller.show_frame("Create_User"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=3,pady=10)
            button4 = tk.Button(Admin_Frame, text="Course_info",width=12,command=lambda: controller.show_frame("Courses_Branch"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=4,pady=10)
            button5 = tk.Button(Admin_Frame, text="Result Details",width=12,command=lambda: controller.show_frame("Result_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=5,pady=10)
            button6 = tk.Button(Admin_Frame, text="Log Out",width=12,command=lambda: controller.show_frame("LoginPage"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=6,pady=10)
    ####################################################################################

    class Student_Details(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.bg_icon=ImageTk.PhotoImage(file="bgg1.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="Student Details",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Admin_Frame=tk.Frame(self,bg="black")
            Admin_Frame.place(x=0,y=85,width=1366,height=60)

            button  = tk.Button(Admin_Frame, text="Student",width=10,command=lambda: controller.show_frame("Student_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=0,pady=10)
            button1 = tk.Button(Admin_Frame, text="Teacher",width=10,command=lambda: controller.show_frame("Teacher_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=1,pady=10)
            button2 = tk.Button(Admin_Frame, text="Question Details",width=15,command=lambda: controller.show_frame("Question_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=2,pady=10)
            button3 = tk.Button(Admin_Frame, text="Create User",width=10,command=lambda: controller.show_frame("Create_User"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=3,pady=10)
            button4 = tk.Button(Admin_Frame, text="Course_info",width=12,command=lambda: controller.show_frame("Courses_Branch"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=4,pady=10)
            button5 = tk.Button(Admin_Frame, text="Result Details",width=12,command=lambda: controller.show_frame("Result_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=5,pady=10)
            button6 = tk.Button(Admin_Frame, text="Log Out",width=12,command=lambda: controller.show_frame("LoginPage"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=6,pady=10)

            self.Roll_No_var=tk.StringVar()
            self.name_var=tk.StringVar()
            self.course_var=tk.StringVar()
            self.branch_var=tk.StringVar()
            self.email_var=tk.StringVar()
            self.gender_var=tk.StringVar()
            self.contact_var=tk.StringVar()
            self.dob_var=tk.StringVar()
            self.city_var=tk.StringVar()
            self.state_var=tk.StringVar()
            self.search_by=tk.StringVar()
            self.search_txt=tk.StringVar()

            Student_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            Student_Frame.place(x=230,y=145,width=900,height=258)
            
            
            lbl_roll=Label(Student_Frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_roll.grid(row=1,column=0,pady=7,padx=20,sticky="w")

            txt_Roll=Entry(Student_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_Roll.grid(row=1,column=1,pady=7,padx=20,sticky="w")

            lbl_name=Label(Student_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_name.grid(row=1,column=4,pady=7,padx=20,sticky="w")

            txt_name=Entry(Student_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_name.grid(row=1,column=5,pady=7,padx=20,sticky="w")

            lbl_course=Label(Student_Frame,text="Course",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_course.grid(row=2,column=0,pady=7,padx=20,sticky="w")

            txt_course=Entry(Student_Frame,textvariable=self.course_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_course.grid(row=2,column=1,pady=7,padx=20,sticky="w")

            lbl_branch=Label(Student_Frame,text="Branch",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_branch.grid(row=2,column=4,pady=7,padx=20,sticky="w")

            txt_branch=Entry(Student_Frame,textvariable=self.branch_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_branch.grid(row=2,column=5,pady=7,padx=20,sticky="w")

            lbl_Email=Label(Student_Frame,text="Email",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Email.grid(row=3,column=0,pady=7,padx=20,sticky="w")

            txt_Email=Entry(Student_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_Email.grid(row=3,column=1,pady=7,padx=20,sticky="w")

            lbl_Gender=Label(Student_Frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Gender.grid(row=3,column=4,pady=7,padx=20,sticky="w")

            combo_gender=ttk.Combobox(Student_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state='readonly')
            combo_gender['values']=("Male","Female","Other")
            combo_gender.grid(row=3,column=5,pady=7,padx=20)
            

            lbl_Contact=Label(Student_Frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Contact.grid(row=4,column=0,pady=7,padx=20,sticky="w")

            txt_Contact=Entry(Student_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_Contact.grid(row=4,column=1,pady=7,padx=20,sticky="w")


            lbl_Dob=Label(Student_Frame,text="D.O.B",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Dob.grid(row=4,column=4,pady=7,padx=20,sticky="w")

            txt_Dob=Entry(Student_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_Dob.grid(row=4,column=5,pady=7,padx=20,sticky="w")


            lbl_City=Label(Student_Frame,text="City",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_City.grid(row=5,column=0,pady=7,padx=20,sticky="w")

            txt_City=Entry(Student_Frame,textvariable=self.city_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_City.grid(row=5,column=1,pady=7,padx=20,sticky="w")

            lbl_State=Label(Student_Frame,text="State",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_State.grid(row=5,column=4,pady=7,padx=20,sticky="w")

            txt_State=Entry(Student_Frame,textvariable=self.state_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_State.grid(row=5,column=5,pady=7,padx=20,sticky="w")

            
            #######################button frame##########################
            
            Addbtn=tk.Button(Student_Frame, text="Add",width=10,command=self.add_students,font=("times ne roman",10,"bold"),bg="crimson",fg="white").grid(row=1,column=6,pady=10)
            updatebtn=tk.Button(Student_Frame, text="Update",width=10,command=self.update_data,font=("times ne roman",10,"bold"),bg="crimson",fg="white").grid(row=2,column=6,pady=10)
            deletebtn=tk.Button(Student_Frame, text="Delete",width=10,command=self.delete_data,font=("times ne roman",10,"bold"),bg="crimson",fg="white").grid(row=3,column=6,pady=10)
            Clearbtn =tk.Button(Student_Frame, text="Clear",width=10,command=self.clear,font=("times ne roman",10,"bold"),bg="crimson",fg="white").grid(row=4,column=6,pady=10)

            ##########################detail frame#######################

            Detail_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            Detail_Frame.place(x=230,y=405,width=900,height=295)

            lbl_Search=Label(Detail_Frame,text="Search BY",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

            combo_Search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Search['values']=("Roll_No","Name","Contact")
            combo_Search.grid(row=0,column=1,pady=10,padx=20)

            txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
            txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

            Searchbtn=Button(Detail_Frame,text="Search",width=10,command=self.search_data,pady=5).grid(row=0,column=3,padx=10,pady=10)
            Showallbtn=Button(Detail_Frame,text="Show All",width=10,command=self.fetch_data,pady=5).grid(row=0,column=4,padx=10,pady=10)

            #################Table Frame#############################

            Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
            Table_Frame.place(x=10,y=60,width=870,height=225)

            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

            self.Student_Table=ttk.Treeview(Table_Frame,columns=("Roll No","Name","Course","Branch","Email","Gender","Contact","D.O.B","City","State"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.Student_Table.xview)
            scroll_y.config(command=self.Student_Table.yview)
            
            self.Student_Table.heading("Roll No",text="Roll No")
            self.Student_Table.heading("Name",text="Name")
            self.Student_Table.heading("Course",text="Course")
            self.Student_Table.heading("Branch",text="Branch")
            self.Student_Table.heading("Email",text="Email")
            self.Student_Table.heading("Gender",text="Gender")
            self.Student_Table.heading("Contact",text="Contact")
            self.Student_Table.heading("D.O.B",text="D.O.B")
            self.Student_Table.heading("City",text="City")
            self.Student_Table.heading("State",text="State")
       
            self.Student_Table['show']='headings'

            self.Student_Table.column("Roll No",width=100)
            self.Student_Table.column("Name",width=100)
            self.Student_Table.column("Course",width=100)
            self.Student_Table.column("Branch",width=100)
            self.Student_Table.column("Email",width=150)
            self.Student_Table.column("Gender",width=100)
            self.Student_Table.column("Contact",width=100)
            self.Student_Table.column("D.O.B",width=100)
            self.Student_Table.column("City",width=100)
            self.Student_Table.column("State",width=100)

            self.Student_Table.pack(fill=BOTH,expand=1)
            self.Student_Table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()

        def add_students(self):
            try:
                if self.Roll_No_var.get()=="" or\
                   self.name_var.get()=="" or\
                   self.course_var.get()=="" or\
                   self.branch_var.get()=="" or\
                   self.email_var.get()=="" or\
                   self.gender_var.get()=="" or\
                   self.contact_var.get()=="" or\
                   self.dob_var.get()=="" or\
                   self.city_var.get()=="" or\
                   self.state_var.get()=="":
                    messagebox.showerror("Error","All fields are required!!!")
                    self.clear()
                else:
                    con=cx_Oracle.connect('system/love@localhost/love')
                    cur=con.cursor()
                    if len(self.contact_var.get())!=10:
                        messagebox.showerror("Error","Enter a valid 10 digit contact number")
                        self.contact_var.set('')
                    else:
                        con=cx_Oracle.connect('system/love@localhost/love')
                        cur=con.cursor()
                        sql="insert into students(roll_no,name,course,branch,email,gender,contact,dob,city,state) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)"
                        cur.execute( sql ,(
                                            self.Roll_No_var.get(),
                                            self.name_var.get(),
                                            self.course_var.get(),
                                            self.branch_var.get(),
                                            self.email_var.get(),
                                            self.gender_var.get(),
                                            self.contact_var.get(),
                                            self.dob_var.get(),
                                            self.city_var.get(),
                                            self.state_var.get()
                                           ))
                        con.commit()
                        con.close()
                        self.clear()
                        self.fetch_data()
                        messagebox.showinfo("Success","Record is inserted successfully")
                    
            except cx_Oracle.IntegrityError:
                messagebox.showerror("Error"," Roll No. is a Unique Variable\n please give a different unique value to it")
                self.Roll_No_var.set('')
            except cx_Oracle.DatabaseError:
                messagebox.showerror("Error",str(sys.exc_info()[0])+"\n"+str(sys.exc_info()[1]))
                self.clear()
            
        def fetch_data(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()



            cur.execute("select * from students order by roll_no")
            rows=cur.fetchall()
            self.Student_Table.delete(*self.Student_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.Student_Table.insert('',END,values=row)
                con.commit()
            con.close()

        def clear(self):
            self.Roll_No_var.set('')
            self.name_var.set('')
            self.course_var.set('')
            self.branch_var.set('')
            self.email_var.set('')
            self.gender_var.set('')
            self.contact_var.set('')
            self.dob_var.set('')
            self.city_var.set('')
            self.state_var.set('')

        def get_cursor(self,ev):
            cursor_row=self.Student_Table.focus()
            contents=self.Student_Table.item(cursor_row)
            row=(contents['values'])
            self.Roll_No_var.set(row[0])
            self.name_var.set(row[1])
            self.course_var.set(row[2])
            self.branch_var.set(row[3])
            self.email_var.set(row[4])
            self.gender_var.set(row[5])
            self.contact_var.set(row[6])
            self.dob_var.set(row[7])
            self.city_var.set(row[8])
            self.state_var.set(row[9])
            
        def update_data(self):
            try:
                con=cx_Oracle.connect('system/love@localhost/love')
                cur=con.cursor()


                sql ="update students set name= :1,course= :2,branch= :3,email= :4,gender= :5,contact= :6,dob= :7,city= :8,state= :9 where roll_no= :10"
                cur.execute( sql,(
                                   self.name_var.get(),
                                   self.course_var.get(),
                                   self.branch_var.get(),
                                   self.email_var.get(),
                                   self.gender_var.get(),
                                   self.contact_var.get(),
                                   self.dob_var.get(),
                                   self.city_var.get(),
                                   self.state_var.get(),
                                   self.Roll_No_var.get()
                                   ))
                con.commit()
                con.close()
                self.fetch_data()
                self.clear()
                messagebox.showinfo("Success","Record is updated successfully")
                
            except cx_Oracle.DatabaseError:
                messagebox.showerror("Error",str(sys.exc_info()[0])+"\n"+str(sys.exc_info()[1]))
                self.clear()
            
        def delete_data(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("delete from students where roll_no= :1",{'1':self.Roll_No_var.get()})

            con.commit()
            con.close()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Success","Record is deleted successfully")
            
        def search_data(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            self.Student_Table.delete(*self.Student_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.Student_Table.insert('',END,values=row)
                con.commit()
            con.close()

        
            
    class Teacher_Details(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.bg_icon=ImageTk.PhotoImage(file="bgg1.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="Teacher Details",font=("times ne roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Admin_Frame=tk.Frame(self,bg="black")
            Admin_Frame.place(x=0,y=85,width=1366,height=60)

            button = tk.Button(Admin_Frame, text="Student",width=10,command=lambda: controller.show_frame("Student_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=0,pady=10)
            button1 = tk.Button(Admin_Frame, text="Teacher",width=10,command=lambda: controller.show_frame("Teacher_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=1,pady=10)
            button2= tk.Button(Admin_Frame, text="Question Details",width=15,command=lambda: controller.show_frame("Question_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=2,pady=10)
            button3 = tk.Button(Admin_Frame, text="Create User",width=10,command=lambda: controller.show_frame("Create_User"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=3,pady=10)
            button4 = tk.Button(Admin_Frame, text="Course_info",width=12,command=lambda: controller.show_frame("Courses_Branch"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=4,pady=10)
            button5 = tk.Button(Admin_Frame, text="Result Details",width=12,command=lambda: controller.show_frame("Result_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=5,pady=10)
            button6 = tk.Button(Admin_Frame, text="Log Out",width=12,command=lambda: controller.show_frame("LoginPage"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=6,pady=10)


            self.Id_var=StringVar()
            self.name_var=StringVar()
            self.course_var=StringVar()
            self.branch_var=StringVar()
            self.email_var=StringVar()
            self.gender_var=StringVar()
            self.contact_var=StringVar()
            self.dob_var=StringVar()
            self.city_var=StringVar()
            self.state_var=StringVar()
            self.search_by=tk.StringVar()
            self.search_txt=tk.StringVar()



            Teacher_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            Teacher_Frame.place(x=230,y=145,width=900,height=255)
            
            
            lbl_id=Label(Teacher_Frame,text="Id",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_id.grid(row=1,column=0,pady=5,padx=20,sticky="w")

            txt_id=Entry(Teacher_Frame,textvariable=self.Id_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_id.grid(row=1,column=1,pady=5,padx=20,sticky="w")

            lbl_name=Label(Teacher_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_name.grid(row=1,column=4,pady=5,padx=20,sticky="w")

            txt_name=Entry(Teacher_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_name.grid(row=1,column=5,pady=5,padx=20,sticky="w")

            lbl_course=Label(Teacher_Frame,text="Course",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_course.grid(row=2,column=0,pady=5,padx=20,sticky="w")

            txt_course=Entry(Teacher_Frame,textvariable=self.course_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_course.grid(row=2,column=1,pady=5,padx=20,sticky="w")

            lbl_branch=Label(Teacher_Frame,text="Branch",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_branch.grid(row=2,column=4,pady=5,padx=20,sticky="w")

            txt_branch=Entry(Teacher_Frame,textvariable=self.branch_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_branch.grid(row=2,column=5,pady=5,padx=20,sticky="w")

            lbl_Email=Label(Teacher_Frame,text="Email",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Email.grid(row=3,column=0,pady=5,padx=20,sticky="w")

            txt_Email=Entry(Teacher_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_Email.grid(row=3,column=1,pady=5,padx=20,sticky="w")

            lbl_Gender=Label(Teacher_Frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Gender.grid(row=3,column=4,pady=5,padx=20,sticky="w")

            combo_gender=ttk.Combobox(Teacher_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state='readonly')
            combo_gender['values']=("Male","Female","other")
            combo_gender.grid(row=3,column=5,pady=5,padx=20)
            

            lbl_Contact=Label(Teacher_Frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Contact.grid(row=4,column=0,pady=5,padx=20,sticky="w")

            txt_Contact=Entry(Teacher_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_Contact.grid(row=4,column=1,pady=5,padx=20,sticky="w")


            lbl_Dob=Label(Teacher_Frame,text="D.O.B",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Dob.grid(row=4,column=4,pady=5,padx=20,sticky="w")

            txt_Dob=Entry(Teacher_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_Dob.grid(row=4,column=5,pady=5,padx=20,sticky="w")


            lbl_City=Label(Teacher_Frame,text="City",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_City.grid(row=5,column=0,pady=5,padx=20,sticky="w")

            txt_City=Entry(Teacher_Frame,textvariable=self.city_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_City.grid(row=5,column=1,pady=5,padx=20,sticky="w")

            lbl_State=Label(Teacher_Frame,text="State",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_State.grid(row=5,column=4,pady=5,padx=20,sticky="w")

            txt_State=Entry(Teacher_Frame,textvariable=self.state_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_State.grid(row=5,column=5,pady=5,padx=20,sticky="w")

            #######################button####################

            Addbtn=tk.Button(Teacher_Frame,text="Add",width=10,command=self.add_teachers,font=("times new roman",11,"bold"),bg="crimson",fg="white").grid(row=1,column=6,pady=10)
            updatebtn=Button(Teacher_Frame,text="Update",width=10,command=self.update_data,font=("times new roman",11,"bold"),bg="crimson",fg="white").grid(row=2,column=6,pady=10)
            deletebtn=Button(Teacher_Frame,text="Delete",width=10,command=self.delete_data,font=("times new roman",11,"bold"),bg="crimson",fg="white").grid(row=3,column=6,pady=10)
            Clearbtn =Button(Teacher_Frame,text="Clear",width=10,command=self.clear,font=("times new roman",11,"bold"),bg="crimson",fg="white").grid(row=4,column=6,pady=10)



            ##########################detail frame#######################

            Detail_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            Detail_Frame.place(x=230,y=400,width=900,height=300)

            lbl_Search=Label(Detail_Frame,text="Search BY",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

            combo_Search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=12,font=("times new roman",13,"bold"),state='readonly')
            combo_Search['values']=("Id","Name","Course","Branch","Contact")
            combo_Search.grid(row=0,column=1,pady=10,padx=20)

            txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
            txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

            Searchbtn=Button(Detail_Frame,text="Search",width=10,command=self.search_data,pady=5).grid(row=0,column=3,padx=10,pady=10)
            Showallbtn=Button(Detail_Frame,text="Show All",width=10,command=self.fetch_data,pady=5).grid(row=0,column=4,padx=10,pady=10)

            #################Table Frame#############################

            Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
            Table_Frame.place(x=10,y=55,width=870,height=230)

            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

            self.Teacher_Table=ttk.Treeview(Table_Frame,columns=("Id","Name","Course","Branch","Email","Gender","Contact","D.O.B","City","State"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.Teacher_Table.xview)
            scroll_y.config(command=self.Teacher_Table.yview)
            self.Teacher_Table.heading("Id",text="Id")
            self.Teacher_Table.heading("Name",text="Name")
            self.Teacher_Table.heading("Course",text="Course")
            self.Teacher_Table.heading("Branch",text="Branch")
            self.Teacher_Table.heading("Email",text="Email")
            self.Teacher_Table.heading("Gender",text="Gender")
            self.Teacher_Table.heading("Contact",text="Contact")
            self.Teacher_Table.heading("D.O.B",text="D.O.B")
            self.Teacher_Table.heading("City",text="City")
            self.Teacher_Table.heading("State",text="State")
       
            self.Teacher_Table['show']='headings'

            self.Teacher_Table.column("Id",width=100)
            self.Teacher_Table.column("Name",width=100)
            self.Teacher_Table.column("Course",width=150)
            self.Teacher_Table.column("Branch",width=100)
            self.Teacher_Table.column("Email",width=350)
            self.Teacher_Table.column("Gender",width=100)
            self.Teacher_Table.column("Contact",width=100)
            self.Teacher_Table.column("D.O.B",width=100)
            self.Teacher_Table.column("City",width=100)
            self.Teacher_Table.column("State",width=100)

            self.Teacher_Table.pack(fill=BOTH,expand=1)

            self.Teacher_Table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()


        def add_teachers(self):
            try:
                if self.Id_var.get()=="" or \
                   self.name_var.get()=="" or \
                   self.course_var.get()=="" or \
                   self.branch_var.get()=="" or \
                   self.email_var.get()=="" or \
                   self.gender_var.get()=="" or \
                   self.contact_var.get()=="" or \
                   self.dob_var.get()=="" or \
                   self.city_var.get()=="" or \
                   self.state_var.get()=="":
                    
                    messagebox.showerror("Error","All fields are required!!!")
                else:
                    if len(self.contact_var.get())!=10:
                        messagebox.showerror("Error","Enter a valid 10 digit contact number")
                        self.contact_var.set('')
                    else:
                        con=cx_Oracle.connect('system/love@localhost/love')
                        cur=con.cursor()
                        sql= "insert into teachers(id,name,course,branch,email,gender,contact,dob,city,state) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)"
                        cur.execute(sql, (
                                           self.Id_var.get(),
                                           self.name_var.get(),
                                           self.course_var.get(),
                                           self.branch_var.get(),
                                           self.email_var.get(),
                                           self.gender_var.get(),
                                           self.contact_var.get(),
                                           self.dob_var.get(),
                                           self.city_var.get(),
                                           self.state_var.get()
                                           ))
                        con.commit()
                        con.close()
                        self.fetch_data()
                        self.clear()
                        messagebox.showinfo("Success","Record is inserted successfully")
            except cx_Oracle.IntegrityError:
                messagebox.showerror("Error"," ID is a Unique Variable\n please give a different unique value to it")
                self.Id_var.set('')
            except cx_Oracle.DatabaseError:
                messagebox.showerror("Error",str(sys.exc_info()[0])+"\n"+str(sys.exc_info()[1]))
                self.clear()
            
        def fetch_data(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()



            cur.execute("select * from teachers order by id")
            rows=cur.fetchall()
            self.Teacher_Table.delete(*self.Teacher_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.Teacher_Table.insert('',END,values=row)
                con.commit()
            con.close()

        def clear(self):
            self.Id_var.set('')
            self.name_var.set('')
            self.course_var.set('')
            self.branch_var.set('')
            self.email_var.set('')
            self.gender_var.set('')
            self.contact_var.set('')
            self.dob_var.set('')
            self.city_var.set('')
            self.state_var.set('')

        def get_cursor(self,ev):
            cursor_row=self.Teacher_Table.focus()
            contents=self.Teacher_Table.item(cursor_row)
            row=(contents['values'])
            self.Id_var.set(row[0])
            self.name_var.set(row[1])
            self.course_var.set(row[2])
            self.branch_var.set(row[3])
            self.email_var.set(row[4])
            self.gender_var.set(row[5])
            self.contact_var.set(row[6])
            self.dob_var.set(row[7])
            self.city_var.set(row[8])
            self.state_var.set(row[9])
            
        def update_data(self):
            try:
                con=cx_Oracle.connect('system/love@localhost/love')
                cur=con.cursor()

                sql="update teachers set name= :1,email= :2,course = :3,branch = :4,gender= :5,contact= :6,dob= :7,city= :8,state= :8 where id= :10"
                cur.execute(sql, (
                                   self.name_var.get(),
                                   self.email_var.get(),
                                   self.course_var.get(),
                                   self.branch_var.get(),
                                   self.gender_var.get(),
                                   self.contact_var.get(),
                                   self.dob_var.get(),
                                   self.city_var.get(),
                                   self.state_var.get(),
                                   self.Id_var.get()
                                  ))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Record is updated successfully")

            except cx_Oracle.DatabaseError:
                messagebox.showerror("Error",str(sys.exc_info()[0])+"\n"+str(sys.exc_info()[1]))
                self.clear()
            
        def delete_data(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("delete from teachers where id= :1",{'1':self.Id_var.get()})
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record is deleted successfully")

        def search_data(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("select * from teachers where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            self.Teacher_Table.delete(*self.Teacher_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.Teacher_Table.insert('',END,values=row)
                con.commit()
            con.close()

    ############################################################################################################################

    class Question_Details(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.bg_icon=ImageTk.PhotoImage(file="bgg1.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="Question Details",font=("times new roman",38,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Admin_Frame=tk.Frame(self,bg="black")
            Admin_Frame.place(x=0,y=83,width=1366,height=60)

            button = tk.Button(Admin_Frame, text="Student",width=10,command=lambda: controller.show_frame("Student_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=0,pady=10)
            button1 = tk.Button(Admin_Frame, text="Teacher",width=10,command=lambda: controller.show_frame("Teacher_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=1,pady=10)
            button2= tk.Button(Admin_Frame, text="Question Details",width=15,command=lambda: controller.show_frame("Question_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=2,pady=10)
            button3 = tk.Button(Admin_Frame, text="Create User",width=10,command=lambda: controller.show_frame("Create_User"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=3,pady=10)
            button4 = tk.Button(Admin_Frame, text="Course_info",width=12,command=lambda: controller.show_frame("Courses_Branch"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=4,pady=10)
            button5 = tk.Button(Admin_Frame, text="Result Details",width=12,command=lambda: controller.show_frame("Result_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=5,pady=10)
            button6 = tk.Button(Admin_Frame, text="Log Out",width=12,command=lambda: controller.show_frame("LoginPage"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=6,pady=10)


            self.branch_var=StringVar()
            self.sub_var=StringVar()
            self.Que_no_var=StringVar()
            self.Que_var=StringVar()
            self.op_1=StringVar()
            self.op_2=StringVar()
            self.op_3=StringVar()
            self.op_4=StringVar()
            self.ans_var=StringVar()
            self.search_by=tk.StringVar()
            self.search_txt=tk.StringVar()
            
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()
            cur.execute("select unique branch from course_branch")
            i=cur.fetchall()
            branches=[]
            for row in i:
                branches.append(row[0])
            cur.execute("select unique subject from course_branch")
            rows=cur.fetchall()
            subjects=[]
            for row in rows:
                subjects.append(row[0])
            con.commit()
            con.close()
            


            Question_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            Question_Frame.place(x=20,y=143,width=1300,height=265)

            lbl_Branch=Label(Question_Frame,text="Branch",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Branch.grid(row=1,column=0,pady=5,padx=10,sticky="w")

            combo_Branch=ttk.Combobox(Question_Frame,textvariable=self.branch_var,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Branch['values']=branches
            combo_Branch.grid(row=1,column=1,pady=5,padx=10,sticky="w")
            
            lbl_Subject=Label(Question_Frame,text="Subject",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Subject.grid(row=1,column=2,pady=5,padx=10,sticky="w")

            combo_Subject=ttk.Combobox(Question_Frame,textvariable=self.sub_var,width=18,font=("times new roman",13,"bold"),state='readonly')
            combo_Subject['values']=subjects
            combo_Subject.grid(row=1,column=3,pady=5,padx=10,sticky="w")
                    
            lbl_Q_No=Label(Question_Frame,text="Q_No",bg="crimson",fg="white",font=("times new roman",17,"bold"))
            lbl_Q_No.grid(row=2,column=0,pady=5,padx=10,sticky="w")

            txt_Q_No=Entry(Question_Frame,textvariable=self.Que_no_var,width=5,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Q_No.grid(row=2,column=1,pady=5,padx=10,sticky="w")

            lbl_Question=Label(Question_Frame,text="Question",bg="crimson",fg="white",font=("times new roman",17,"bold"))
            lbl_Question.grid(row=3,column=0,pady=5,padx=10,sticky="w")

            txt_Question=Entry(Question_Frame,textvariable=self.Que_var,width=80,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Question.grid(row=3,column=1,pady=5,padx=10,sticky="w")

            
            lbl_Option_1=Label(Question_Frame,text="Option 1",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Option_1.grid(row=4,column=0,pady=5,padx=10,sticky="w")

            txt_Option_1=Entry(Question_Frame,textvariable=self.op_1,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Option_1.grid(row=4,column=1,pady=5,padx=10,sticky="w")

            lbl_Option_2=Label(Question_Frame,text="Option 2",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Option_2.grid(row=4,column=2,pady=5,padx=10,sticky="w")

            txt_Option_2=Entry(Question_Frame,textvariable=self.op_2,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Option_2.grid(row=4,column=3,pady=5,padx=10,sticky="w")

            lbl_Option_3=Label(Question_Frame,text="Option 3",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Option_3.grid(row=5,column=0,pady=5,padx=10,sticky="w")

            txt_Option_3=Entry(Question_Frame,textvariable=self.op_3,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Option_3.grid(row=5,column=1,pady=5,padx=10,sticky="w")

            lbl_Option_4=Label(Question_Frame,text="Option 4",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Option_4.grid(row=5,column=2,pady=5,padx=10,sticky="w")

            txt_Option_4=Entry(Question_Frame,textvariable=self.op_4,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Option_4.grid(row=5,column=3,pady=5,padx=10,sticky="w")


            lbl_Answer=Label(Question_Frame,text="Answer",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Answer.grid(row=6,column=0,pady=5,padx=10,sticky="w")

            txt_Answer=Entry(Question_Frame,textvariable=self.ans_var,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Answer.grid(row=6,column=1,pady=5,padx=10,sticky="w")


            

            #######################button####################

            #Addbtn=tk.Button(Teacher_Frame, text="Add",width=10,command=self.add_teachers,font=("times ne roman",10,"bold"),bg="crimson",fg="white").grid(row=1,column=6,pady=10)
            updatebtn=Button(Question_Frame, text="Update",width=10,command=self.update_question,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=6,column=2,pady=10,sticky="w")
            #deletebtn=Button(Teacher_Frame, text="Delete",width=10,command=self.delete_data,font=("times ne roman",10,"bold"),bg="crimson",fg="white").grid(row=3,column=6,pady=10)
            Clearbtn =Button(Question_Frame, text="Clear",width=10,command=self.clear,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=6,column=3,pady=10,sticky="w")



            ##########################detail frame#######################
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("select branch from course_branch")
            branches=cur.fetchone()
            cur.execute("select subject from course_branch")
            subjects=cur.fetchone()
            con.commit()
            con.close()
            Detail_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            Detail_Frame.place(x=20,y=408,width=1300,height=292)

            lbl_Search=Label(Detail_Frame,text="Search BY",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Search.grid(row=0,column=0,pady=10,padx=15,sticky="w")

            combo_Search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=15,font=("times new roman",13,"bold"),state='readonly')
            combo_Search['values']=("Branch","Subject","Set_by")
            combo_Search.grid(row=0,column=1,pady=10,padx=15)

            txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
            txt_Search.grid(row=0,column=2,pady=10,padx=15,sticky="w")

            Searchbtn=Button(Detail_Frame,text="Search",width=9,command=self.search_data,pady=5).grid(row=0,column=3,padx=10,pady=10)
            Showallbtn=Button(Detail_Frame,text="Show All",width=9,command=self.fetch_data,pady=5).grid(row=0,column=4,padx=10,pady=10)

            #################Table Frame#############################

            Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
            Table_Frame.place(x=5,y=55,width=1270,height=222)

            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
            col=("Branch","Subject","Q.No","Question","Option 1","Option 2","Option 3","Option 4","Answer","Question set by")
            self.Question_Table=ttk.Treeview(Table_Frame,columns=col,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.Question_Table.xview)
            scroll_y.config(command=self.Question_Table.yview)
            self.Question_Table.heading("Branch",text="Branch")
            self.Question_Table.heading("Subject",text="Subject")
            self.Question_Table.heading("Q.No",text="Q.No")
            self.Question_Table.heading("Question",text="Question")
            self.Question_Table.heading("Option 1",text="Option 1")
            self.Question_Table.heading("Option 2",text="Option 2")
            self.Question_Table.heading("Option 3",text="Option 3")
            self.Question_Table.heading("Option 4",text="Option 4")
            self.Question_Table.heading("Answer",text="Answer")
            self.Question_Table.heading("Question set by",text="Question set by")
       
            self.Question_Table['show']='headings'

            self.Question_Table.column("Branch",width=50)
            self.Question_Table.column("Subject",width=50)
            self.Question_Table.column("Q.No",width=50)
            self.Question_Table.column("Question",width=800)
            self.Question_Table.column("Option 1",width=100)
            self.Question_Table.column("Option 2",width=100)
            self.Question_Table.column("Option 3",width=100)
            self.Question_Table.column("Option 4",width=100)
            self.Question_Table.column("Answer",width=100)
            self.Question_Table.column("Question set by",width=130)

            self.Question_Table.pack(fill=BOTH,expand=1)

            self.Question_Table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()


        def fetch_data(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("select * from question_details")
            rows=cur.fetchall()
            self.Question_Table.delete(*self.Question_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.Question_Table.insert('',END,values=row)
                con.commit()
            con.close()
            
        def clear(self):
            self.branch_var.set('')
            self.sub_var.set('')
            self.Que_no_var.set('')
            self.Que_var.set('')
            self.op_1.set('')
            self.op_2.set('')
            self.op_3.set('')
            self.op_4.set('')
            self.ans_var.set('')

            
        def get_cursor(self,ev):
            cursor_row=self.Question_Table.focus()
            contents=self.Question_Table.item(cursor_row)
            row=(contents['values'])
            self.branch_var.set(row[0])
            self.sub_var.set(row[1])
            self.Que_no_var.set(row[2])
            self.Que_var.set(row[3])
            self.op_1.set(row[4])
            self.op_2.set(row[5])
            self.op_3.set(row[6])
            self.op_4.set(row[7])
            self.ans_var.set(row[8])

            
        def update_question(self):
            try:
                con=cx_Oracle.connect('system/love@localhost/love')
                cur=con.cursor()
                sql="update question_details set question= :1,option_1= :2,option_2= :3,option_3= :4,option_4= :5,answer= :6 where branch= :7 and subject= :8 and q_no= :9"
                cur.execute(sql,(
                                 self.Que_var.get(),
                                 self.op_1.get(),
                                 self.op_2.get(),
                                 self.op_3.get(),
                                 self.op_4.get(),
                                 self.ans_var.get(),
                                 self.branch_var.get(),
                                 self.sub_var.get(),
                                 self.Que_no_var.get()
                                 ))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Record is updated successfully")

            except cx_Oracle.DatabaseError:
                messagebox.showerror("Error",str(sys.exc_info()[0])+"\n"+str(sys.exc_info()[1]))
                self.clear()
        
        def search_data(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("select * from question_details where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            self.Teacher_Table.delete(*self.Teacher_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.Teacher_Table.insert('',END,values=row)
                con.commit()
            con.close()

    ####################################################################################

    class Create_User(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.bg_icon=ImageTk.PhotoImage(file="bgg1.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="Create User",font=("times new roman",38,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Admin_Frame=tk.Frame(self,bg="black")
            Admin_Frame.place(x=0,y=83,width=1366,height=60)

            button = tk.Button(Admin_Frame, text="Student",width=10,command=lambda: controller.show_frame("Student_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=0,pady=10)
            button1 = tk.Button(Admin_Frame, text="Teacher",width=10,command=lambda: controller.show_frame("Teacher_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=1,pady=10)
            button2 = tk.Button(Admin_Frame, text="Question Details",width=15,command=lambda: controller.show_frame("Question_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=2,pady=10)
            button3 = tk.Button(Admin_Frame, text="Create User",width=10,command=lambda: controller.show_frame("Create_User"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=3,pady=10)
            button4 = tk.Button(Admin_Frame, text="Course_info",width=12,command=lambda: controller.show_frame("Courses_Branch"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=4,pady=10)
            button5 = tk.Button(Admin_Frame, text="Result Details",width=12,command=lambda: controller.show_frame("Result_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=5,pady=10)
            button6 = tk.Button(Admin_Frame, text="Log Out",width=12,command=lambda: controller.show_frame("LoginPage"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=6,pady=10)


            self.user_var=StringVar()
            self.Id_var=StringVar()
            self.Username_var=StringVar()
            self.Pass_var=StringVar()
            self.search_by=tk.StringVar()
            self.search_txt=tk.StringVar()
            

            User_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            User_Frame.place(x=300,y=143,width=800,height=250)

            lbl_User_type=Label(User_Frame,text="User type",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_User_type.grid(row=1,column=0,pady=10,padx=20,sticky="w")

            combo_User_type=ttk.Combobox(User_Frame,textvariable=self.user_var,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_User_type['values']=("Teacher","Student")
            combo_User_type.grid(row=1,column=1,pady=10,padx=20,sticky="w")
            
                    
            lbl_Id=Label(User_Frame,text="Id",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Id.grid(row=2,column=0,pady=10,padx=20,sticky="w")

            txt_Id=Entry(User_Frame,textvariable=self.Id_var,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Id.grid(row=2,column=1,pady=10,padx=20,sticky="w")

            lbl_Username=Label(User_Frame,text="Username",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Username.grid(row=3,column=0,pady=10,padx=20,sticky="w")

            txt_Username=Entry(User_Frame,textvariable=self.Username_var,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Username.grid(row=3,column=1,pady=10,padx=20,sticky="w")

            
            lbl_Password=Label(User_Frame,text="Password",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Password.grid(row=4,column=0,pady=10,padx=20,sticky="w")

            txt_Password=Entry(User_Frame,textvariable=self.Pass_var,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Password.grid(row=4,column=1,pady=10,padx=20,sticky="w")
            
            #######################button####################

            Addbtn=tk.Button(User_Frame, text="Add",width=10,command=self.add_user,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=1,column=4,pady=10)
            updatebtn=Button(User_Frame, text="Update",width=10,command=self.update_user,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=2,column=4,pady=10,sticky="w")
            deletebtn=Button(User_Frame, text="Delete",width=10,command=self.delete_user,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=3,column=4,pady=10)
            Clearbtn =Button(User_Frame, text="Clear",width=10,command=self.clear,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=4,column=4,pady=10,sticky="w")

            ##########################detail frame#######################

            Detail_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            Detail_Frame.place(x=300,y=393,width=800,height=308)

            lbl_Search=Label(Detail_Frame,text="Search By",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Search.grid(row=0,column=0,pady=10,padx=15,sticky="w")

            combo_Search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Search['values']=("Id","Username")
            combo_Search.grid(row=0,column=1,pady=10,padx=15)

            txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
            txt_Search.grid(row=0,column=2,pady=10,padx=15,sticky="w")

            Searchbtn=Button(Detail_Frame,text="Search",width=9,command=self.search_user,pady=5).grid(row=0,column=3,padx=10,pady=10)
            Showallbtn=Button(Detail_Frame,text="Show All",width=9,command=self.fetch_data,pady=5).grid(row=0,column=4,padx=10,pady=10)

            #################Table Frame#############################

            Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
            Table_Frame.place(x=6,y=55,width=780,height=240)

            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

            self.User_Table=ttk.Treeview(Table_Frame,columns=("User_type","Id","Username","Password"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.User_Table.xview)
            scroll_y.config(command=self.User_Table.yview)
            self.User_Table.heading("User_type",text="User_type")
            self.User_Table.heading("Id",text="Id")
            self.User_Table.heading("Username",text="Username")
            self.User_Table.heading("Password",text="Password")
       
            self.User_Table['show']='headings'

            self.User_Table.column("User_type",width=100)
            self.User_Table.column("Id",width=100)
            self.User_Table.column("Username",width=100)
            self.User_Table.column("Password",width=100) 

            self.User_Table.pack(fill=BOTH,expand=1)

            self.User_Table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()

        def add_user(self):
            try:
                if self.user_var.get()=="" or self.Id_var.get()=="" or self.Username_var.get()=="" or self.Pass_var.get()=="":
                    messagebox.showerror("Error","All fields are required!!!")
                else:
                    con=cx_Oracle.connect('system/love@localhost/love')
                    cur=con.cursor()
                    
                    cur.execute("insert into users(user_type,id,username,password) values (:1,:2,:3,:4)",(
                                                                                                          self.user_var.get(),
                                                                                                          self.Id_var.get(),
                                                                                                          self.Username_var.get(),
                                                                                                          self.Pass_var.get()
                                                                                                          ))
                    

                    con.commit()
                    con.close()
                    self.fetch_data()
                    self.clear()
                    messagebox.showinfo("Success","User created successfully")
            except cx_Oracle.IntegrityError:
                messagebox.showerror("Error"," Id is a Unique Variable\n please give a different unique value to it")
                self.Id_var.set('')
            except cx_Oracle.DatabaseError:
                messagebox.showerror("Error",str(sys.exc_info()[0])+"\n"+str(sys.exc_info()[1]))
                self.clear()
            
        def delete_user(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("delete from users where id =:1",({'1':self.Id_var.get()}))

            con.commit()
            con.close()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Success","User deleted successfully")
                    
        def fetch_data(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("select * from users order by id")
            rows=cur.fetchall()
            self.User_Table.delete(*self.User_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.User_Table.insert('',END,values=row)
                con.commit()
            con.close()

        def clear(self):
            self.user_var.set('')
            self.Id_var.set('')
            self.Username_var.set('')
            self.Pass_var.set('')
            
        def get_cursor(self,ev):
            cursor_row=self.User_Table.focus()
            contents=self.User_Table.item(cursor_row)
            row=(contents['values'])
            self.user_var.set(row[0])
            self.Id_var.set(row[1])
            self.Username_var.set(row[2])
            self.Pass_var.set(row[3])        

        def update_user(self):
            try:
                con=cx_Oracle.connect('system/love@localhost/love')
                cur=con.cursor()

                cur.execute("update users set username= :1,password= :2 where id= :3 and user_type =:4",(
                                                                                                         self.Username_var.get(),
                                                                                                         self.Pass_var.get(),
                                                                                                         self.Id_var.get(),
                                                                                                         self.user_var.get()
                                                                                                         ))

                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","User updated successfully")

            except cx_Oracle.DatabaseError:
                messagebox.showerror("Error",str(sys.exc_info()[0])+"\n"+str(sys.exc_info()[1]))
                self.clear()

        def search_user(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("select * from users where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            self.User_Table.delete(*self.User_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.User_Table.insert('',END,values=row)
                con.commit()
            con.close()
            
    ###################################################################
            
    class Courses_Branch(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.bg_icon=ImageTk.PhotoImage(file="bgg1.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="Add Courses",font=("times new roman",38,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Admin_Frame=tk.Frame(self,bg="black")
            Admin_Frame.place(x=0,y=83,width=1366,height=60)

            button = tk.Button(Admin_Frame, text="Student",width=10,command=lambda: controller.show_frame("Student_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=0,pady=10)
            button1 = tk.Button(Admin_Frame, text="Teacher",width=10,command=lambda: controller.show_frame("Teacher_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=1,pady=10)
            button2 = tk.Button(Admin_Frame, text="Question Details",width=15,command=lambda: controller.show_frame("Question_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=2,pady=10)
            button3 = tk.Button(Admin_Frame, text="Create User",width=10,command=lambda: controller.show_frame("Create_User"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=3,pady=10)
            button4 = tk.Button(Admin_Frame, text="Course_info",width=12,command=lambda: controller.show_frame("Courses_Branch"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=4,pady=10)
            button5 = tk.Button(Admin_Frame, text="Result Details",width=12,command=lambda: controller.show_frame("Result_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=5,pady=10)
            button6 = tk.Button(Admin_Frame, text="Log Out",width=12,command=lambda: controller.show_frame("LoginPage"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=6,pady=10)

            self.code=StringVar()
            self.course_name=StringVar()
            self.branch_name=StringVar()
            self.subject_name=StringVar()
            self.search_by=tk.StringVar()
            self.search_txt=tk.StringVar()


            User_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            User_Frame.place(x=160,y=170,width=500,height=440)

            
            lbl_Code_No=Label(User_Frame,text="Code-No",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Code_No.grid(row=0,column=0,pady=10,padx=20,sticky="w")

            txt_Code_No=Entry(User_Frame,textvariable=self.code,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Code_No.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
            lbl_Course=Label(User_Frame,text="Course",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Course.grid(row=1,column=0,pady=10,padx=20,sticky="w")

            txt_Course=Entry(User_Frame,textvariable=self.course_name,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Course.grid(row=1,column=1,pady=10,padx=20,sticky="w")

            lbl_Branch=Label(User_Frame,text="Branch",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Branch.grid(row=2,column=0,pady=10,padx=20,sticky="w")

            txt_Branch=Entry(User_Frame,textvariable=self.branch_name,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Branch.grid(row=2,column=1,pady=10,padx=20,sticky="w")

            lbl_Subject=Label(User_Frame,text="Subject",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Subject.grid(row=3,column=0,pady=10,padx=20,sticky="w")

            txt_Subject=Entry(User_Frame,textvariable=self.subject_name,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Subject.grid(row=3,column=1,pady=10,padx=20,sticky="w")
            
            #######################button####################

            Addbtn=tk.Button(User_Frame, text="Add",width=10,command=self.add_course,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=4,column=1,pady=10,sticky="nsew")
            updatebtn=Button(User_Frame, text="Update",width=10,command=self.update,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=5,column=1,pady=10,sticky="nsew")
            deletebtn=Button(User_Frame, text="Delete",width=10,command=self.delete_course,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=6,column=1,pady=10,sticky="nsew")
            Clearbtn =Button(User_Frame, text="Clear",width=10,command=self.clear,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=7,column=1,pady=10,sticky="nsew")

            ##########################detail frame#######################

            Detail_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            Detail_Frame.place(x=690,y=170,width=580,height=440)

            lbl_Search=Label(Detail_Frame,text="Search BY",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Search.grid(row=0,column=0,pady=10,padx=15,sticky="w")

            combo_Search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Search['values']=("Branch","Course","Subject")
            combo_Search.grid(row=0,column=1,pady=10,padx=15)

            txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=10,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
            txt_Search.grid(row=0,column=2,pady=10,padx=15,sticky="w")

            Searchbtn=Button(Detail_Frame,text="Search",width=8,command=self.search_user,pady=5).grid(row=0,column=3,padx=2,pady=10)
            Showallbtn=Button(Detail_Frame,text="Show All",width=8,command=self.fetch_data,pady=5).grid(row=0,column=4,padx=2,pady=10)


            #################Table Frame#############################

            Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
            Table_Frame.place(x=6,y=50,width=560,height=375)

            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

            self.User_Table=ttk.Treeview(Table_Frame,columns=("Code-No","Course","Branch","Subject"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.User_Table.xview)
            scroll_y.config(command=self.User_Table.yview)
            self.User_Table.heading("Code-No",text="Code-No")
            self.User_Table.heading("Course",text="Course")
            self.User_Table.heading("Branch",text="Branch")
            self.User_Table.heading("Subject",text="Subject")
       
            self.User_Table['show']='headings'

            self.User_Table.column("Code-No",width=100)
            self.User_Table.column("Course",width=100)
            self.User_Table.column("Branch",width=100)
            self.User_Table.column("Subject",width=100)
            
            self.User_Table.pack(fill=BOTH,expand=1)

            self.User_Table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()


        def add_course(self):
            try:
                if self.code.get()=="" or self.course_name.get()=="" or self.branch_name.get()=="":
                    messagebox.showerror("Error","All fields are required!!!")
                else:
                    con=cx_Oracle.connect('system/love@localhost/love')
                    cur=con.cursor()
                    
                    cur.execute("insert into course_branch(code_no,course,branch,subject) values (:1,:2,:3,:4)",(
                                                                                                      self.code.get(),
                                                                                                      self.course_name.get(),
                                                                                                      self.branch_name.get(),
                                                                                                      self.subject_name.get()
                                                                                                    ))
                    

                    con.commit()
                    self.fetch_data()
                    self.clear()
                    con.close()
                    messagebox.showinfo("Success","Course added successfully")
            except cx_Oracle.IntegrityError:
                messagebox.showerror("Error"," Code No. is a Unique Variable\n please give a different unique value to it")
                self.code.set('')
            except cx_Oracle.DatabaseError:
                messagebox.showerror("Error",str(sys.exc_info()[0])+"\n"+str(sys.exc_info()[1]))
                self.clear()
            
        def delete_course(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("delete from course_branch where code_no =:1",({'1':self.code.get()}))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Course deleted successfully")
            
            
        def fetch_data(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("select * from course_branch order by code_no")
            rows=cur.fetchall()
            self.User_Table.delete(*self.User_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.User_Table.insert('',END,values=row)
                con.commit()
            con.close()

        def clear(self):
            self.code.set('')
            self.course_name.set('')
            self.branch_name.set('')
            self.subject_name.set('')

            
        def get_cursor(self,ev):
            cursor_row=self.User_Table.focus()
            contents=self.User_Table.item(cursor_row)
            row=(contents['values'])
            self.code.set(row[0])
            self.course_name.set(row[1])
            self.branch_name.set(row[2])
            self.subject_name.set(row[3])
            
        def update(self):
            try:
                con=cx_Oracle.connect('system/love@localhost/love')
                cur=con.cursor()
                
                cur.execute("update course_branch set course= :1,branch= :2, subject= :3 where code_no = :4",(
                                                                                                self.course_name.get(),
                                                                                                self.branch_name.get(),
                                                                                                self.subject_name.get(),
                                                                                                self.code.get()
                                                                                               ))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Course updated successfully")

            except cx_Oracle.DatabaseError:
                messagebox.showerror("Error",str(sys.exc_info()[0])+"\n"+str(sys.exc_info()[1]))
                self.clear()

        def search_user(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("select * from course_branch where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            self.User_Table.delete(*self.User_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.User_Table.insert('',END,values=row)
                con.commit()
            con.close()

    ############################################################################################################

    class Result_Details(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            

            self.bg_icon=ImageTk.PhotoImage(file="bgg1.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="Result Details",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Admin_Frame=tk.Frame(self,bg="black")
            Admin_Frame.place(x=0,y=85,width=1366,height=60)

            button = tk.Button(Admin_Frame, text="Student",width=10,command=lambda: controller.show_frame("Student_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=0,pady=10)
            button1 = tk.Button(Admin_Frame, text="Teacher",width=10,command=lambda: controller.show_frame("Teacher_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=1,pady=10)
            button2= tk.Button(Admin_Frame, text="Question Details",width=15,command=lambda: controller.show_frame("Question_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=2,pady=10)
            button3 = tk.Button(Admin_Frame, text="Create User",width=10,command=lambda: controller.show_frame("Create_User"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=3,pady=10)
            button4 = tk.Button(Admin_Frame, text="Course_info",width=12,command=lambda: controller.show_frame("Courses_Branch"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=4,pady=10)
            button5 = tk.Button(Admin_Frame, text="Result Details",width=12,command=lambda: controller.show_frame("Result_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=5,pady=10)
            button6 = tk.Button(Admin_Frame, text="Log Out",width=12,command=lambda: controller.show_frame("LoginPage"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=6,pady=10)




            self.search_by=tk.StringVar()
            self.search_txt=tk.StringVar()
            
            ##########################detail frame#######################

            Detail_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            Detail_Frame.place(x=230,y=145,width=1000,height=600)

            lbl_Search=Label(Detail_Frame,text="Search BY",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

            combo_Search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Search['values']=("Roll_No","Name","Course","Branch","subject")
            combo_Search.grid(row=0,column=1,pady=10,padx=20)

            txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
            txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

            Searchbtn=Button(Detail_Frame,text="Search",width=10,command=self.search_data,pady=5).grid(row=0,column=3,padx=10,pady=10)
            Showallbtn=Button(Detail_Frame,text="Show All",width=10,command=self.fetch_data,pady=5).grid(row=0,column=4,padx=10,pady=10)



            #################Table Frame#############################


            Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
            Table_Frame.place(x=10,y=60,width=970,height=495)

            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

            col ="Roll No","Name","Gender","Course","Branch","Subject","No. of Ques.","Correct","Incorrect","Attempted On"
            self.Result_Table=ttk.Treeview(Table_Frame,columns=col,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.Result_Table.xview)
            scroll_y.config(command=self.Result_Table.yview)
            self.fetch_data()
            self.Result_Table.heading("Roll No",text="Roll No")
            self.Result_Table.heading("Name",text="Name")
            self.Result_Table.heading("Gender",text="Gender")
            self.Result_Table.heading("Course",text="Course")
            self.Result_Table.heading("Branch",text="Branch")
            self.Result_Table.heading("Subject",text="Subject")
            self.Result_Table.heading("No. of Ques.",text="No. of Ques.")
            self.Result_Table.heading("Correct",text="Correct")
            self.Result_Table.heading("Incorrect",text="Incorrect")
            self.Result_Table.heading("Attempted On",text="Attempted On")
       
            self.Result_Table['show']='headings'

            self.Result_Table.column("Roll No",width=120)
            self.Result_Table.column("Name",width=120)
            self.Result_Table.column("Gender",width=120)
            self.Result_Table.column("Course",width=120)
            self.Result_Table.column("Branch",width=120)
            self.Result_Table.column("Subject",width=120)
            self.Result_Table.column("No. of Ques.",width=150)
            self.Result_Table.column("Correct",width=120)
            self.Result_Table.column("Incorrect",width=120)
            self.Result_Table.column("Attempted On",width=120)

            self.Result_Table.pack(fill=BOTH,expand=1)
            #self.Result_Table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()

        def fetch_data(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()
            cur.execute("select * from result")
            rows=cur.fetchall()
            self.Result_Table.delete(*self.Result_Table.get_children())
            if len(rows)!=0:
                self.Result_Table.delete(*self.Result_Table.get_children())
                for row in rows:
                    self.Result_Table.insert('',END,values=row)
                con.commit()
            con.close()

        
        
        def search_data(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("select * from result where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            self.Result_Table.delete(*self.Result_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.Result_Table.insert('',END,values=row)
                con.commit()
            con.close()

        

    ################################################ Teacher System #################################################
    ######################################################################################################

    class Teacher_LoginPage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            

            ##############ALL IMAGES########
            self.bg_icon=ImageTk.PhotoImage(file="bgg1.jpg")
            self.user_icon=PhotoImage(file="user.png")
            self.pass_icon=PhotoImage(file="pass.png")
            self.logo_icon=PhotoImage(file="logo.png")
            ######### variables############
            self.uname=StringVar()
            self.passw=StringVar()

            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="Welcome To Teacher System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Login_Frame=tk.Frame(self,bg="white")
            Login_Frame.place(x=400,y=150)

            logolbl=tk.Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)

            lbluser=tk.Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(rows=1,column=0,padx=20,pady=10)
            txtuser=tk.Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

            lblpass=tk.Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(rows=2,column=0,padx=20,pady=10)
            txtpass=tk.Entry(Login_Frame,bd=5,textvariable=self.passw,relief=GROOVE,font=("",15),show="*").grid(row=2,column=1,padx=20)

            btn_log=tk.Button(Login_Frame,text="Login",width=10,command=self.login,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)
            btn_log=tk.Button(Login_Frame,text="Back",width=10,command=lambda: controller.show_frame("StartPage"),font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=4,column=1,pady=10)





        def login(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("select username,password from users where user_type = 'Teacher'")
            rows=cur.fetchall()
            print(rows)
            
            if self.uname.get()=="" or self.passw.get()=="":
                messagebox.showerror("Error","All fields are required!!!")
            elif (self.uname.get(),self.passw.get()) in rows:
                 messagebox.showinfo("Successfull",f"welcome {self.uname.get()}")
                 global u_p
                 u_p=[self.uname.get(),self.passw.get()]
                 self.passw.set('')
                 self.uname.set('')
                 con.commit()
                 con.close()
                 self.controller.show_frame("Teacher")
                 
            else:
                messagebox.showerror("Error","Invalid Username or Password!!!")


    #################################################################################################################

    class Teacher(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.bg_icon=ImageTk.PhotoImage(file="bgg1.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="Set Questions",font=("times new roman",38,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Admin_Frame=tk.Frame(self,bg="white")
            Admin_Frame.place(x=1020,y=83,width=300,height=39)

            button5 = tk.Button(Admin_Frame, text="Go to Login Page",width=40,command=lambda: controller.show_frame("LoginPage"),font=("times ne roman",14,"bold"),bg="crimson",fg="white").pack()

            self.branch_var=StringVar()
            self.sub_var=StringVar()
            self.Que_no_var=StringVar()
            self.Que_var=StringVar()
            self.op_1=StringVar()
            self.op_2=StringVar()
            self.op_3=StringVar()
            self.op_4=StringVar()
            self.ans_var=StringVar()
            self.search_by=tk.StringVar()
            self.search_txt=tk.StringVar()

            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("select unique branch from course_branch")
            i=cur.fetchall()
            branches=[]
            for row in i:
                branches.append(row[0])
            cur.execute("select unique subject from course_branch")
            rows=cur.fetchall()
            subjects=[]
            for row in rows:
                subjects.append(row[0])
            con.commit()
            con.close()

            Question_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            Question_Frame.place(x=20,y=122,width=1300,height=289)

            lbl_Branch=Label(Question_Frame,text="Branch",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Branch.grid(row=1,column=0,pady=5,padx=10,sticky="w")

            combo_Branch=ttk.Combobox(Question_Frame,textvariable=self.branch_var,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Branch['values']=branches
            combo_Branch.grid(row=1,column=1,pady=5,padx=10,sticky="w")
            
            lbl_Subject=Label(Question_Frame,text="Subject",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Subject.grid(row=1,column=2,pady=5,padx=10,sticky="w")

            combo_Subject=ttk.Combobox(Question_Frame,textvariable=self.sub_var,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Subject['values']=subjects
            combo_Subject.grid(row=1,column=3,pady=5,padx=10,sticky="w")
                    
            lbl_Q_No=Label(Question_Frame,text="Q_No",bg="crimson",fg="white",font=("times new roman",17,"bold"))
            lbl_Q_No.grid(row=2,column=0,pady=5,padx=10,sticky="w")

            txt_Q_No=Entry(Question_Frame,textvariable=self.Que_no_var,width=5,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Q_No.grid(row=2,column=1,pady=5,padx=10,sticky="w")

            lbl_Question=Label(Question_Frame,text="Question",bg="crimson",fg="white",font=("times new roman",17,"bold"))
            lbl_Question.grid(row=3,column=0,pady=5,padx=10,sticky="w")

            txt_Question=Entry(Question_Frame,textvariable=self.Que_var,width=80,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Question.grid(row=3,column=1,pady=5,padx=10,sticky="w")

            
            lbl_Option_1=Label(Question_Frame,text="Option 1",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Option_1.grid(row=4,column=0,pady=5,padx=10,sticky="w")

            txt_Option_1=Entry(Question_Frame,textvariable=self.op_1,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Option_1.grid(row=4,column=1,pady=5,padx=10,sticky="w")

            lbl_Option_2=Label(Question_Frame,text="Option 2",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Option_2.grid(row=4,column=2,pady=5,padx=10,sticky="w")

            txt_Option_2=Entry(Question_Frame,textvariable=self.op_2,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Option_2.grid(row=4,column=3,pady=5,padx=10,sticky="w")

            lbl_Option_3=Label(Question_Frame,text="Option 3",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Option_3.grid(row=5,column=0,pady=5,padx=10,sticky="w")

            txt_Option_3=Entry(Question_Frame,textvariable=self.op_3,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Option_3.grid(row=5,column=1,pady=5,padx=10,sticky="w")

            lbl_Option_4=Label(Question_Frame,text="Option 4",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Option_4.grid(row=5,column=2,pady=5,padx=10,sticky="w")

            txt_Option_4=Entry(Question_Frame,textvariable=self.op_4,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Option_4.grid(row=5,column=3,pady=5,padx=10,sticky="w")


            lbl_Answer=Label(Question_Frame,text="Answer",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Answer.grid(row=6,column=0,pady=5,padx=10,sticky="w")

            txt_Answer=Entry(Question_Frame,textvariable=self.ans_var,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Answer.grid(row=6,column=1,pady=5,padx=10,sticky="w")


            

            #######################button####################
        
            Addbtn=tk.Button(Question_Frame, text="Add",width=10,command=self.add_question,font=("times new roman",10,"bold"),bg="crimson",fg="white").grid(row=6,column=2,pady=5,sticky="w")
            updatebtn=Button(Question_Frame, text="Update",width=10,command=self.update_question,font=("times new roman",10,"bold"),bg="crimson",fg="white").grid(row=6,column=3,pady=5,sticky="w")
            deletebtn=Button(Question_Frame, text="Delete",width=10,command=self.delete_question,font=("times new roman",10,"bold"),bg="crimson",fg="white").grid(row=7,column=2,pady=1,sticky="w")
            Clearbtn =Button(Question_Frame, text="Clear",width=10,command=self.clear,font=("times new roman",10,"bold"),bg="crimson",fg="white").grid(row=7,column=3,pady=1,sticky="w")



            ##########################detail frame#######################

            Detail_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            Detail_Frame.place(x=20,y=410,width=1300,height=292)

            lbl_Search=Label(Detail_Frame,text="Search BY",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Search.grid(row=0,column=0,pady=10,padx=15,sticky="w")

            combo_Search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Search['values']=("Branch","Subject","Set_by")
            combo_Search.grid(row=0,column=1,pady=10,padx=15)

            txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
            txt_Search.grid(row=0,column=2,pady=10,padx=15,sticky="w")

            Searchbtn=Button(Detail_Frame,text="Search",width=9,command=self.search_data,pady=5).grid(row=0,column=3,padx=10,pady=10)
            Showallbtn=Button(Detail_Frame,text="Show All",width=9,command=self.fetch_data,pady=5).grid(row=0,column=4,padx=10,pady=10)



            #################Table Frame#############################


            Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
            Table_Frame.place(x=5,y=55,width=1270,height=222)

            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
            col = ("Branch","Subject","Q.No","Question","Option 1","Option 2","Option 3","Option 4","Answer","Question set by")
            self.Question_Table=ttk.Treeview(Table_Frame,columns=col,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.Question_Table.xview)
            scroll_y.config(command=self.Question_Table.yview)
            self.Question_Table.heading("Branch",text="Branch")
            self.Question_Table.heading("Subject",text="Subject")
            self.Question_Table.heading("Q.No",text="Q.No")
            self.Question_Table.heading("Question",text="Question")
            self.Question_Table.heading("Option 1",text="Option 1")
            self.Question_Table.heading("Option 2",text="Option 2")
            self.Question_Table.heading("Option 3",text="Option 3")
            self.Question_Table.heading("Option 4",text="Option 4")
            self.Question_Table.heading("Answer",text="Answer")
            self.Question_Table.heading("Question set by",text="Question set by")
       
            self.Question_Table['show']='headings'

            self.Question_Table.column("Branch",width=50)
            self.Question_Table.column("Subject",width=50)
            self.Question_Table.column("Q.No",width=50)
            self.Question_Table.column("Question",width=800)
            self.Question_Table.column("Option 1",width=80)
            self.Question_Table.column("Option 2",width=100)
            self.Question_Table.column("Option 3",width=100)
            self.Question_Table.column("Option 4",width=100)
            self.Question_Table.column("Answer",width=100)
            self.Question_Table.column("Question set by",width=140)


            self.Question_Table.pack(fill=BOTH,expand=1)

            self.Question_Table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()


        def add_question(self):
            try:
                if  self.branch_var.get() == "" or \
                    self.sub_var.get() == "" or \
                    self.Que_no_var.get() == "" or \
                    self.Que_var.get() == "" or \
                    self.op_1.get() == "" or \
                    self.op_2.get() == "" or \
                    self.op_3.get() == "" or \
                    self.op_4.get() == "" or \
                    self.ans_var.get() == "" :
                    
                    messagebox.showerror("Error","All fields are required!!!")
                else:
                    con=cx_Oracle.connect('system/love@localhost/love')
                    cur=con.cursor()
                    
                    global u_p
                    cur.execute("select id from users where username=:1 and password= :2",(u_p[0],u_p[1]))
                    idd =cur.fetchone()
                    cur.execute("select name from teachers where id=:1",{'1':idd[0]})
                    set_by=cur.fetchone()
                    cur.execute("select * from question_details where branch = :1 and subject = :2",(
                                                                                                     self.branch_var.get(),
                                                                                                     self.sub_var.get()
                                                                                                     ))
                    res = cur.fetchall()
                    if len(res) > 9:
                        messagebox.showinfo("Data Can not be added","Only 10 questions are allowed per subject")
                        self.clear()
                    else:
                        sql ="insert into question_details(branch,subject,q_no,question,option_1,option_2,option_3,option_4,answer,set_by) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)"
                        cur.execute(sql ,(
                                           self.branch_var.get(),
                                           self.sub_var.get(),
                                           self.Que_no_var.get(),
                                           self.Que_var.get(),
                                           self.op_1.get(),
                                           self.op_2.get(),
                                           self.op_3.get(),
                                           self.op_4.get(),
                                           self.ans_var.get(),
                                           str(set_by[0])
                                          ))
                        con.commit()
                        self.fetch_data()
                        self.clear()
                        con.close()
                        messagebox.showinfo("Success","Question added successfully")
                        
            except cx_Oracle.DatabaseError:
                messagebox.showerror("Error",str(sys.exc_info()[0])+"\n"+str(sys.exc_info()[1]))
                self.clear()


        def fetch_data(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("select * from question_details")
            rows=cur.fetchall()
            self.Question_Table.delete(*self.Question_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.Question_Table.insert('',END,values=row)
                con.commit()
            con.close()
            
        def clear(self):
            self.branch_var.set('')
            self.sub_var.set('')
            self.Que_no_var.set('')
            self.Que_var.set('')
            self.op_1.set('')
            self.op_2.set('')
            self.op_3.set('')
            self.op_4.set('')
            self.ans_var.set('')

            
        def get_cursor(self,ev):
            cursor_row=self.Question_Table.focus()
            contents=self.Question_Table.item(cursor_row)
            row=(contents['values'])
            self.branch_var.set(row[0])
            self.sub_var.set(row[1])
            self.Que_no_var.set(row[2])
            self.Que_var.set(row[3])
            self.op_1.set(row[4])
            self.op_2.set(row[5])
            self.op_3.set(row[6])
            self.op_4.set(row[7])
            self.ans_var.set(row[8])

            
        def update_question(self):
            try:
                con=cx_Oracle.connect('system/love@localhost/love')
                cur=con.cursor()
                sql ="update question_details set question= :1,option_1= :2,option_2= :3,option_3= :4,option_4= :5,answer= :6 where branch= :7 and subject= :8 and q_no= :9"
                cur.execute(sql,(
                                  self.Que_var.get(),
                                  self.op_1.get(),
                                  self.op_2.get(),
                                  self.op_3.get(),
                                  self.op_4.get(),
                                  self.ans_var.get(),
                                  self.branch_var.get(),
                                  self.sub_var.get(),
                                  self.Que_no_var.get()
                                  ))
                con.commit()
                con.close()
                self.clear()
                self.fetch_data()
                messagebox.showinfo("Success","Question updated successfully")

            except cx_Oracle.DatabaseError:
                messagebox.showerror("Error",str(sys.exc_info()[0])+"\n"+str(sys.exc_info()[1]))
                self.clear()

        def delete_question(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("delete from question_details where branch= :1 and subject= :2 and q_no= :3",(
                                                                                                       self.branch_var.get(),
                                                                                                       self.sub_var.get(),
                                                                                                       self.Que_no_var.get()
                                                                                                      ))
            con.commit()
            self.clear()
            self.fetch_data()
            con.close()
            messagebox.showinfo("Success","Question deleted successfully")

        def search_data(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("select * from question_details where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            self.Question_Table.delete(*self.Question_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.Question_Table.insert('',END,values=row)
                con.commit()
            con.close()


    ################################################# Student System ##############################################################
    class Student_LoginPage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
           

            ##############ALL IMAGES########
            self.bg_icon=ImageTk.PhotoImage(file="bgg1.jpg")
            self.user_icon=PhotoImage(file="user.png")
            self.pass_icon=PhotoImage(file="pass.png")
            self.logo_icon=PhotoImage(file="logo.png")
            ######### variables############
            self.uname=StringVar()
            self.passw=StringVar()

            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="Welcome To Student Login Page",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Login_Frame=tk.Frame(self,bg="white")
            Login_Frame.place(x=400,y=150)

            logolbl=tk.Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)

            lbluser=tk.Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(rows=1,column=0,padx=20,pady=10)
            txtuser=tk.Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

            lblpass=tk.Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(rows=2,column=0,padx=20,pady=10)
            txtpass=tk.Entry(Login_Frame,bd=5,textvariable=self.passw,relief=GROOVE,font=("",15),show="*").grid(row=2,column=1,padx=20)
            btn_log=tk.Button(Login_Frame,text="Login",width=10,command=self.login,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)
            btn_log=tk.Button(Login_Frame,text="Back",width=10,command=lambda: controller.show_frame("StartPage"),font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=4,column=1,pady=10)



        def login(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("select username,password from users where user_type = 'Student'")
            rows=cur.fetchall()
            con.commit()
            print(rows)
            con.close()
            if self.uname.get()=="" or self.passw.get()=="":
                messagebox.showerror("Error","All fields are required!!!")
            elif (self.uname.get(),self.passw.get()) in rows:
                 messagebox.showinfo("Successfull",f"welcome{self.uname.get()}")
                 global s_u_p
                 s_u_p=[self.uname.get(),self.passw.get()]
                 self.passw.set('')
                 self.uname.set('')
                 self.controller.show_frame("Student")
                 
            else:
                messagebox.showerror("Error","Invalid Username or Password!!!")

    ##################################################################################################
                
    class Student(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.bg_icon=ImageTk.PhotoImage(file="bgg1.jpg")
            self.bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            self.title=tk.Label(self,text="STUDENT EXAM MENU",font=("times new roman",40,"bold"),bg="yellow",fg="red",justify = "center",bd=10,relief=GROOVE)
            self.title.place(x=0,y=0,relwidth=1)


            self.instruction=tk.Label(self,text="Please select Branch and Subject \n Then press Next to start the exam",font=("times ne roman",20,"bold"),justify = "center",bg="white",fg="crimson",bd=10,relief=GROOVE)
            self.instruction.place(x=0,y=618,relwidth=1)

            #self.Questions=[]
            
            #self.Options=[]

            self.User_Answer=[]
            self.ques=1
            
            self.branch_var=StringVar()
            self.sub_var=StringVar()

            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("select unique branch from course_branch")
            i=cur.fetchall()
            branches=[]
            for row in i:
                branches.append(row[0])
            cur.execute("select unique subject from course_branch")
            rows=cur.fetchall()
            subjects=[]
            for row in rows:
                subjects.append(row[0])
            con.commit()
            con.close()
            
            self.Question_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            self.Question_Frame.place(x=500,y=200,width=400,height=300,)
            

            self.lbl_Branch=Label(self.Question_Frame,text="Branch",width=12,bg="crimson",fg="white",font=("times new roman",22,"bold"))
            self.lbl_Branch.pack(pady=(35,0))

            self.combo_Branch=ttk.Combobox(self.Question_Frame,textvariable=self.branch_var,width=14,font=("times new roman",15,"bold"),state='readonly')
            self.combo_Branch['values']=branches
            self.combo_Branch.pack(pady=(10,0))
            
            self.lbl_Subject=Label(self.Question_Frame,text="Subject",width=12,bg="crimson",fg="white",font=("times new roman",22,"bold"))
            self.lbl_Subject.pack(pady=(35,0))

            self.combo_Subject=ttk.Combobox(self.Question_Frame,textvariable=self.sub_var,width=16,font=("times new roman",15,"bold"),state='readonly')
            self.combo_Subject['values']=subjects
            self.combo_Subject.pack(pady=(10,0))

            self.button1 = tk.Button(self.Question_Frame, text="Next",command=self.next,width=8,font=("times ne roman",16,"bold"),bg="crimson",fg="white").pack(pady=(20,0))


            
        def next(self):
            self.questions()
            self.options()
            self.answers()
            self.instruction.destroy()
            self.Question_Frame.destroy()
            self.title.destroy()
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()
            global s_u_p
            cur.execute("select id from users where username=:1 and password= :2",(s_u_p[0],s_u_p[1]))
            idd =cur.fetchone()
            cur.execute("select  roll_no,name from result where roll_no= :1 and subject= :2",(idd[0],self.sub_var.get()))
            i=cur.fetchall()
            con.commit()
            con.close()
            if len(i)!= 0:
                messagebox.showerror("Error",str(i[0][1])+" has already given exam for this Subject")
                self.controller.show_frame("LoginPage")
            else:
                self.startexam()


        def startexam(self):
            
            messagebox.showinfo("Instructions","Imp instructions\n Read the questions carefully\n Once you select an option it can not be changed\n So choose your answer wisely\n \t ALL THE BEST DEAR STUDENT")
            self.lblQuestion = Label(self,text=self.Questions[0][0],font=("times new roman",20,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE,justify="center",wraplength=800)
            self.lblQuestion.place(x=0,y=0,relwidth=1)

            self.radiovar= StringVar()
            self.radiovar.set('')


            self.r1= Radiobutton(self,text=self.Options[0][0],font=("times",16),bg="white",fg="red",value=self.Options[0][0],variable=self.radiovar,command=self.selected,)
            self.r1.place(x=550,y=200,width=250)
            self.r2= Radiobutton(self,text=self.Options[0][1],font=("times",16),bg="white",fg="red",value=self.Options[0][1],variable=self.radiovar,command=self.selected,)
            self.r2.place(x=550,y=240,width=250)
            self.r3= Radiobutton(self,text=self.Options[0][2],font=("times",16),bg="white",fg="red",value=self.Options[0][2],variable=self.radiovar,command=self.selected,)
            self.r3.place(x=550,y=280,width=250)
            self.r4= Radiobutton(self,text=self.Options[0][3],font=("times",16),bg="white",fg="red",value=self.Options[0][3],variable=self.radiovar,command=self.selected,)
            self.r4.place(x=550,y=320,width=250)

            
        def questions(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("select question from question_details where branch= :1 and subject= :2",(
                                                                                          self.branch_var.get(),
                                                                                          self.sub_var.get()
                                                                                          ))
            self.Questions=cur.fetchall()
            con.commit()
            con.close()

            
        def options(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("select option_1,option_2,option_3,option_4 from question_details where branch= :1 and subject= :2",(
                                                                                          self.branch_var.get(),
                                                                                          self.sub_var.get()
                                                                                          ))
            self.Options=cur.fetchall()
            con.commit()
            con.close()


        def answers(self):
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            cur.execute("select answer from question_details where branch= :1 and subject= :2",(
                                                                                          self.branch_var.get(),
                                                                                          self.sub_var.get()
                                                                                          ))
            self.Answers=cur.fetchall()
            con.commit()
            con.close()

            
        def selected(self):
            self.x=self.radiovar.get()
            self.User_Answer.append(self.x)
            self.radiovar.set(-1)
            if self.ques < 10:
                self.lblQuestion.config(text= self.Questions[self.ques][0])
                self.r1['text'] = self.Options[self.ques][0]
                self.r2['text'] = self.Options[self.ques][1]
                self.r3['text'] = self.Options[self.ques][2]
                self.r4['text'] = self.Options[self.ques][3]
                self.r1['value'] = self.Options[self.ques][0]
                self.r2['value'] = self.Options[self.ques][1]
                self.r3['value'] = self.Options[self.ques][2]
                self.r4['value'] = self.Options[self.ques][3]
                self.ques += 1
            else:
                self.calc()

        def calc(self):
            self.correct = 0
            self.incorrect = 0
            for i in range(10):
                if self.User_Answer[i] == self.Answers[i][0]:
                    self.correct += 1
                else:
                    self.incorrect +=1
            self.show_result(self.correct,self.incorrect)


        def show_result(self,correct,incorrect):
            messagebox.showinfo("Exam Completed","Exam Completed successfully!!!\n Now result will be shown\n \tBEST OF LUCK")
            self.lblQuestion.destroy()
            self.r1.destroy()
            self.r2.destroy()
            self.r3.destroy()
            self.r4.destroy()
            total_question=correct+incorrect
            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()

            global s_u_p

            cur.execute("select id from users where username=:1 and password= :2",(s_u_p[0],s_u_p[1]))
            idd =cur.fetchone()
            cur.execute("select * from students where roll_no=:1",{'1':idd[0]})
            stu_data=cur.fetchone()
            con.commit()
            con.close()
            print(stu_data)

            Result_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            Result_Frame.place(x=450,y=150,width=500,height=430,)
            lbl_text=Label(Result_Frame,text="Result",font=("times new roman",30,"bold"),bg="black",fg="red",justify="center",bd=10,relief=GROOVE)
            lbl_text.place(x=0,y=0,relwidth=1)
            lbl_name=Label(Result_Frame,text=str(stu_data[1]),font=("times new roman",20,"bold"),bg="white",fg="black",justify="center").place(x=0,y=90,relwidth=1)
            lbl_roll_no=Label(Result_Frame,text="Roll No="+str(stu_data[0]),font=("times new roman",20,"bold"),bg="white",fg="black",justify="center").place(x=0,y=140,relwidth=1)
            lbl_branch=Label(Result_Frame,text=self.branch_var.get(),font=("times new roman",20,"bold"),bg="white",fg="black",justify="center").place(x=0,y=190,relwidth=1)
            lbl_subject=Label(Result_Frame,text=self.sub_var.get(),font=("times new roman",20,"bold"),bg="white",fg="black",justify="center").place(x=0,y=240,relwidth=1)
            lbl_correct=Label(Result_Frame,text="Correct = "+str(correct),font=("times new roman",20,"bold"),bg="white",fg="black",justify="center").place(x=0,y=290,relwidth=1)
            lbl_incorrect=Label(Result_Frame,text="Incorrect = "+str(incorrect),font=("times new roman",20,"bold"),bg="white",fg="black",justify="center").place(x=0,y=340,relwidth=1)
            

            con=cx_Oracle.connect('system/love@localhost/love')
            cur=con.cursor()
            sql="insert into result(roll_no,name,gender,course,branch,subject,no_of_question,correct,incorrect) values (:1,:2,:3,:4,:5,:6,:7,:8,:9)"
            cur.execute(sql,(
                             stu_data[0],
                             stu_data[1],
                             stu_data[5],
                             stu_data[2],
                             stu_data[3],
                             self.sub_var.get(),
                             str(total_question),
                             str(correct),
                             str(incorrect)))
            con.commit()
            con.close()
            button6 = tk.Button(Result_Frame, text="Log Out",width=12,command=self.logout,font=("times new roman",14,"bold"),bg="black",fg="white").place(x=345,y=380)
        def logout(self):
            app.destroy()
            main()

            

    app = SampleApp()
    app.title("EXAM MANAGEMENT SYSTEM")
    app.geometry("1366x768+0+0")
    app.mainloop()



main()
