from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="****************",database="PROJECT")
cur=mydb.cursor()
#cur.execute("create database PROJECT")
#cur.execute("create table typing(f_name varchar(50),l_name varchar(50),contact varchar(10),email varchar(50),question varchar(50),answer varchar(50),password varchar(50))")

class Register:
	def __init__(self,root):
		self.root=root
		self.root.title("REGISTRATION WINDOW")
		self.root.geometry("1350x700+0+0")
		#self.var_fname=StringVar()
		self.var_chk=IntVar()
		##############PATH OF IMAGE
		self.bg=ImageTk.PhotoImage(file="C:/Users/hp/OneDrive/Desktop/code/m3.jpg")
		bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
		self.left=ImageTk.PhotoImage(file="C:/Users/hp/OneDrive/Desktop/code/m1.jpg")
		left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

		frame1=Frame(self.root,bg="white")
		frame1.place(x=480,y=100,width=700,height=500)

		title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

		f_name=Label(frame1,text="First Name",font=("times new roman",20,),bg="white",fg="gray").place(x=50,y=100)
		self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_fname.place(x=50,y=130,width=250)

		l_name=Label(frame1,text="Last Name",font=("times new roman",20,),bg="white",fg="gray").place(x=370,y=100)
		self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_lname.place(x=370,y=130,width=250)

		contact=Label(frame1,text="Contact No.",font=("times new roman",20,),bg="white",fg="gray").place(x=50,y=170)
		self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_contact.place(x=50,y=200,width=250)


		email=Label(frame1,text="E-mail",font=("times new roman",20,),bg="white",fg="gray").place(x=370,y=170)
		self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_email.place(x=370,y=200,width=250)

		question=Label(frame1,text="Security Question",font=("times new roman",20,),bg="white",fg="gray").place(x=50,y=240)	
		self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
		self.cmb_quest['values']=("select","Your Frist Pet Name","Your Birth Place","Your Best Friend")
		self.cmb_quest.place(x=50,y=270,width=250)
		self.cmb_quest.current(0)



		answer=Label(frame1,text="Answer",font=("times new roman",20,),bg="white",fg="gray").place(x=370,y=240)
		self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_answer.place(x=370,y=270,width=250)



		password=Label(frame1,text="password",font=("times new roman",20,),bg="white",fg="gray").place(x=50,y=310)
		self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_password.place(x=50,y=340,width=250)

		cpassword=Label(frame1,text="Confirm Password",font=("times new roman",20,),bg="white",fg="gray").place(x=370,y=310)
		self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
		self.txt_cpassword.place(x=370,y=340,width=250)


		chk=Checkbutton(frame1,text="I Agree with terms and conditions",font=("times new roman",12),onvalue=1,offvalue=0,bg="white",variable=self.var_chk).place(x=50,y=380)



		self.btn_img=ImageTk.PhotoImage(file="C:/Users/hp/OneDrive/Desktop/code/re.jpg")
		btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)

		btn_login=Button(root,text="Sign in",font=("times new roman",20),bd=0,cursor="hand2",command=self.login_data).place(x=250,y=460,width=180)
	def clear(self):
		self.txt_fname.delete(0,END)
		self.txt_lname.delete(0,END)
		self.txt_email.delete(0,END)
		self.txt_contact.delete(0,END)
		self.txt_password.delete(0,END)
		self.txt_cpassword.delete(0,END)
		self.txt_answer.delete(0,END)
		self.cmb_quest.current(0)


	def register_data(self):
		if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="" or self.txt_contact.get()=="":
			messagebox.showerror("Error","All fields are required",parent=self.root)

		elif self.txt_password.get() != self.txt_cpassword.get():
			messagebox.showerror("Error","Password and Confirm password shoud be same",parent=self.root)
		elif self.var_chk.get()==0:
			messagebox.showerror("Error","Please accept our terms and conditions",parent=self.root)
		else:
			try:
				cur.execute("select * from typing ")
				r=cur.fetchall()
				result=None
				for i in r:
					if i[3]==self.txt_email.get():
						result=i
				if result!=None:
					messagebox.showerror("Error","User already exist, Please try with another email",parent=self.root)
				else:
					cur.execute(" insert into typing(f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",(self.txt_fname.get(),self.txt_lname.get(),self.txt_contact.get(),self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get(),self.txt_password.get()))
					mydb.commit()
					mydb.close()
					messagebox.showinfo("Success","Register Successfully",parent=self.root)
					self.clear()

				
			except Exception as es:
				messagebox.showerror("Error",f"Error due to: {es} ",parent=self.root)
	def check(self):
		cur.execute("select * from typing")
		r=cur.fetchall()
		p=0
		for i in r:
			if i[3]==self.e_email.get():
				p=1
				if i[6]==self.e_pass.get():

					messagebox.showinfo("Success","You have login Successfully",parent=self.Threemad)
					self.Threemad.destroy()
					import mainfile

				else:
					messagebox.showerror("Error","You have enter wrong password",parent=self.Threemad)
				break
		if p==0:
			messagebox.showinfo("ALERT","User doesnot exist",parent=self.Threemad)
	def login_data(self):
		self.root.destroy()
		self.Threemad=Tk()
		#e=StringVar()
		#p=StringVar()
		self.Threemad.geometry("400x400")
		self.Threemad.resizable(0,0)
		self.Threemad.title("..........LOGIN PAGE.........")
		Label(self.Threemad,text="USER LOGIN").pack()
		self.c=Canvas(self.Threemad,width=400,height=400,bg="black")
		self.c.create_rectangle(20,20,360,360,outline="red")
		Label(self.Threemad,text="Enter you registered email: ",bg="black",fg="cyan",font=("arial",10)).place(x=100,y=50)
		self.e_email=Entry(self.Threemad,width=30,bg="cyan",fg="red",font=("arial",10))
		self.e_email.place(x=100,y=70)
		Label(self.Threemad,text="Enter your password: ",bg="black",fg="cyan",font=("arial",10)).place(x=100,y=100)
		self.e_pass=Entry(self.Threemad,width=30,bg="cyan",font=("arial",10),show="*")		
		self.e_pass.place(x=100,y=130)

		Button(self.Threemad,text="FORGOT PASSWORD",bg="black",fg="cyan",font=("arial",10),command=self.forgot,cursor="hand2").place(x=130,y=160)
		Button(self.Threemad,text="LOGIN",bg="red",fg="cyan",font=("arial",20),command=self.check,cursor="hand2").place(x=130,y=210)
		Button(self.Threemad,text="YOU DON'T HAVE ACCOUNT, THEN CREATE",bg="black",fg="cyan",font=("arial",10),cursor="hand2",command=self.Threemad.destroy).place(x=40,y=280)
		self.c.pack()
		
		self.Threemad.mainloop()
	def forgot(self):
		self.Threemad.destroy()
		self.new=Tk()
		self.new.title("....RESET PASSWORD......")
		self.new.resizable(0,0)
		self.new.geometry("500x500+0+0")
		self.c=Canvas(self.new,height=500,width=500,bg="#FFFFBF")
		Label(self.new,text="Enter your email ",bg="cyan",font=('times new roman',15)).place(x=120,y=10)
		self.e1=Entry(self.new,font=("times new roman",15))
		self.e1.place(x=120,y=50)
		Label(self.new,text="Enter Security Question's Answer",bg="cyan",font=("times new roman",15)).place(x=120,y=100)
		self.e2=Entry(self.new,font=("times new roman",15))
		self.e2.place(x=120,y=140)
		Label(self.new,text="Enter new Password",bg="cyan",font=("times new roman",15)).place(x=120,y=190)
		self.e3=Entry(self.new,font=("times new roman",15))
		self.e3.place(x=120,y=230)
		Label(self.new,text="Confirm Password",bg="cyan",font=("times new roman",15)).place(x=120,y=280)
		self.e4=Entry(self.new,font=("times new roman",15))
		self.e4.place(x=120,y=320)

		Button(self.new,text="Reset Password",font=("times new roman",15),bg="black",fg="red",cursor="hand2",command=self.f).place(x=120,y=370)

		self.c.pack()

		self.new.mainloop()


	def f(self):
		cur.execute("select * from typing")
		r=cur.fetchall()
		p=0
		for i in r:
			if i[3]==self.e1:
				p=p+1
				if self.e2==i[5]:
					if self.e3==self.e4:
						cur.execute("update typing set email=self.e3 where email=self.e3")
						mydb.commit()
						messagebox.showinfo("INFO","Password reset Successfully",parent=self.new)
					else:
						messagebox.showerror("Error","Password dont match",parent=self.new)

				else:
					messagebox.showerror("ALERT","Security Answer Nont Match",parent=self.new)
		if p==0:
			messagebox.showerror("Error","User doesnot exist Please Sign up",parent=self.new)

			



root=Tk()
obj=Register(root)
root.mainloop()