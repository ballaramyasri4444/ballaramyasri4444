# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 18:03:35 2021

@author: HOME
"""

from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk

import mysql.connector

class login:
    def __init__(self,scr):
        self.scr=scr
        self.scr.title("login form")
        self.scr.geometry("{}x{}".format(*self.scr.maxsize()))
        #bg
        self.img=ImageTk.PhotoImage(file=r"F:\projects\wp2704825.jpg")
        img=Label(self.scr,image=self.img ).place(x=0,y=0,relwidth=1,relheight=1)
        #frame
        frame1=Frame(self.scr,bg="mint cream",highlightbackground='white',
                                               highlightthickness=2)
        frame1.place(x=400,y=100,width=600,height=500)
        #title in a frame
        title=Label(frame1,text="Login here",font=("times in roman",30,"bold"),bg="mint cream",fg="blue")
        title.place(x=30)
        #email address
        elable=Label(frame1,text="Email Address",font=("times",20,"bold"),bg="mint cream",fg="black")
        elable.place(x=30,y=100)
        self.txt_email=Entry(frame1,font=("times",15),bg="White")
        self.txt_email.place(x=30,y=150,width=350,height=35)

        

        #password
        plable=Label(frame1,text="Password",font=("times",20,"bold"),bg="mint cream",fg="black")
        plable.place(x=30,y=200)
        self.txt_pwd=Entry(frame1,show="*",font=("times",15),bg="White")
        self.txt_pwd.place(x=30,y=250,width=350,height=35)
        #regitser now label
        rbt=Button(frame1,text="Register new account?",cursor="hand2",font=("times",10,"bold"),bg="mint cream",fg="red",command=self.registration)
        rbt.place(x=30,y=300)
        
        #login btton
        loginbt=Button(frame1,text="login",bg="light gray",fg="black",cursor="hand2",font=("times,12,bold"),command=self.login_data)
        loginbt.place(x=230,y=360,width=100)
    
     #function for redirect to registrationnew   
    def registration(self):
        self.scr.destroy()
        import registrationform
    #function to clear the data
    def clearall(self):
        self.txt_email.delete(0,END)
        self.txt_pwd.delete(0,END)
    
        
        
        #data validation
    def login_data(self):
            
            if self.txt_email.get()=="" or self.txt_pwd.get()=="":
                messagebox.showerror("error","all feilds are reqired",parent=self.scr)
            else:
                try:
                    con=mysql.connector.connect(host="localhost",user="root",password="9848")
                    cur=con.cursor();
                   
                    cur.execute("CREATE DATABASE IF NOT EXISTS test")
                    cur.execute("use test")
                    
                    cur.execute("create table if not exists teststable(first_name varchar(20),last_name varchar(20),password varchar(20),re_password varchar(20),email varchar(40),mobile_num varchar(20),Age varchar(10),country varchar(10))")
             
                    cur.execute("select * from teststable where email=%s and password=%s",(self.txt_email.get(),self.txt_pwd.get(), ))
                    row=cur.fetchall()
                #print(row)
                    if row==[]:
                         messagebox.showerror("error","invalid email and password",parent=self.scr)
                         self.clearall()
                    else:
                        messagebox.showinfo("success","welcome",parent=self.scr)
                        #redirecting to dicesimlation
                        self.scr.destroy()
                        import calculatortkintergui
                        
                        
                    con.close()
                    
                    
                except Exception as es:
                    messagebox.showerror("error",f"error de to :{str(es)}",parent=self.scr)
        

 

scr=Tk()       
obj=login(scr)
scr.mainloop()
        