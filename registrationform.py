# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 17:59:42 2021

@author: HOME
"""

from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector



class Register:
    def __init__(self,scr):
        self.scr=scr
        #Title view on screen
        self.scr.title("Registration-page")

        #screen resolution
        self.scr.geometry('{}x{}'.format(*self.scr.maxsize()))

       # Background Image
        self.img=ImageTk.PhotoImage(file=r"F:\projects\wp2704825.jpg")
        img=Label(self.scr,image=self.img ).place(x=0,y=0,relwidth=1,relheight=1)


        # Frame
        f_register=Frame(self.scr,bg="mint cream",highlightbackground='Black',
                                               highlightthickness=2)
        f_register.place(x=330,y=20,height=660,width=700)


        #Title
        title=Label(f_register,text="Registration",font=("times new roman",35,"bold"),bg="mint cream")
        title.place(x=50)

        
        #User Label
        u_label=Label(f_register,text="First Name",font=("times new roman",20,"bold"),bg="mint cream",fg="gray")
        u_label.place(x=50,y=100)
        #Entry Field of User
        
        self.txt_first=Entry(f_register,font=("times",15),bg="White")
        self.txt_first.place(x=270,y=100,width=350,height=35)


        #Name
        name_label=Label(f_register,text="Last Name",font=("times new roman",20,"bold"),bg="mint cream",fg="gray")
        name_label.place(x=50,y=150)
        #Entry Field of User
        self.txt_last=Entry(f_register,font=("times new roman",15),bg="White")
        self.txt_last.place(x=270,y=150,width=350,height=35)



        #Password
        pw_label=Label(f_register,text="password",font=("times new roman",20,"bold"),bg="mint cream",fg="gray")
        pw_label.place(x=50,y=200)
        #Entry Field of User
        self.txt_pw=Entry(f_register,font=("times",15),bg="White")
        self.txt_pw.place(x=270,y=200,width=350,height=35)

        # confirm password
        cpw_label=Label(f_register,text="Re-password",font=("times new roman",20,"bold"),bg="mint cream",fg="gray")
        cpw_label.place(x=50,y=250)
        #Entry Field of User
        self.txt_cpw=Entry(f_register,font=("times",15),bg="White")
        self.txt_cpw.place(x=270,y=250,width=350,height=35)


        #Email
        email_label=Label(f_register,text="Email",font=("times new roman",20,"bold"),bg="mint cream",fg="gray")
        email_label.place(x=50,y=300)
        #Entry Field of User
        self.txt_email=Entry(f_register,font=("times",15),bg="White")
        self.txt_email.place(x=270,y=300,width=350,height=35)


        #Mobile Number
        m_num_label=Label(f_register,text="Mobile Number",font=("times new roman",20,"bold"),bg="mint cream",fg="gray")
        m_num_label.place(x=50,y=350)
        #Entry Field of User
        self.txt_m_num=Entry(f_register,font=("times",15),bg="White")
        self.txt_m_num.place(x=270,y=350,width=350,height=35)


        #Age
        age_label=Label(f_register,text="Age",font=("times new roman",20,"bold"),bg="mint cream",fg="gray")
        age_label.place(x=50,y=400)
        #Entry Field of User
        self.txt_age=Entry(f_register,font=("times",15),bg="White")
        self.txt_age.place(x=270,y=400,width=350,height=35)

        #COUNTRY
        Country_label=Label(f_register,text="Country",font=("times new roman",20,"bold"),bg="mint cream",fg="gray")
        Country_label.place(x=50,y=450)
        self.com=ttk.Combobox(f_register,font=("times new roman",12),state='readonly',justify=CENTER)
        self.com['values']=("select","india","usa","england")
        self.com.place(x=270,y=450,width=350,height=35)
        self.com.current(0)
       
        
        #check box
        self.var_chk=IntVar()
        chk=Checkbutton(f_register,text="I agree the terms and Conditions",variable=self.var_chk,bg="white",onvalue=1,offvalue=0,font=("times new roman",12)).place(x=50,y=520)
        


       
        #register button
        register_b=Button(f_register,text="Register",bg="light gray",fg="black", cursor="hand2",font=("times 12 bold"),command=self.register_data)
        register_b.place(x=250,y=580,width=200)
    #function for clear the data
    def clear(self):
        self.txt_first.delete(0,END)
        self.txt_last.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_pw.delete(0,END)
        self.txt_cpw.delete(0,END)
        self.txt_m_num.delete(0,END)
        self.txt_age.delete(0,END)
        self.com.current(0)
        self.var_chk=0
       
    #to display on console by using object(self)
    # def register_data(self):
    #    print(self.txt_first.get())
    def register_data(self):
   
        if self.txt_first.get()=="" or  self.txt_last.get()=="" or self.txt_email.get()=="" or self.txt_pw.get()=="" or self.txt_cpw.get()=="" or self.txt_m_num.get()=="" or self.txt_age.get()=="" or self.com.get()=="select" :

            messagebox.showerror("error","All fields are required",parent=self.scr)
        elif self.txt_pw.get()!= self.txt_cpw.get():
            messagebox.showerror("error","password and repassword should be same",parent=self.scr)
        elif  self.var_chk.get()==0:
            messagebox.showerror("error","please agree terms and conditions",parent=self.scr)
     
        else:
            try:
                con = mysql.connector.connect(host='localhost', user='root', password='9848')
                cur = con.cursor()
                cur.execute("CREATE DATABASE IF NOT EXISTS test")
                cur.execute("use test")
                cur.execute("create table if not exists teststable(first_name varchar(20),last_name varchar(20),password varchar(20),re_password varchar(20),email varchar(40),mobile_num varchar(20),Age varchar(10),country varchar(10))")
             
                cur.execute("select * from teststable where email=%s",(self.txt_email.get(), ))
                row=cur.fetchall()
                #print(row)
                if row!=[]:
                     messagebox.showerror("error","user already exists",parent=self.scr)
                else:
     

                
                
                
                   cur.execute("insert into teststable(first_name,last_name,password,re_password,email,mobile_num,Age,country) values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.txt_first.get(),self.txt_last.get()
                                                                            ,self.txt_pw.get(),self.txt_cpw.get(),self.txt_email.get()
                                                                            ,self.txt_m_num.get(),self.txt_age.get(),self.com.get()))
                
                   con.commit()
                   con.close()
                   messagebox.showinfo("success","Registration successful",parent=self.scr)
                self.clear();
                
                
            except Exception as es:
                messagebox.showerror("error",f"error de to :{str(es)}",parent=self.scr)
                
           
        
            
        


scr=Tk()
obj1=Register(scr)
scr.mainloop()
