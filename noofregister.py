import mysql.connector
from tkinter import *
root=Tk()
root.geometry("1500x1000")
root.resizable(0,0)
mydb=mysql.connector.connect(host="localhost",user="root",password="***********",database="PROJECT")
cur=mydb.cursor()
cur.execute("select * from typing")
r=cur.fetchall()
Label(root,text="    Candidate First Name       ").grid(row=0,column=0)
Label(root,text="    Candidate Last Name        ").grid(row=0,column=1)
Label(root,text="    Candidate Contact Number   ").grid(row=0,column=2)
Label(root,text="    Candidate Email    ").grid(row=0,column=3)
Label(root,text="    Candidate Sequirity Question ").grid(row=0,column=4)
Label(root,text="    Candidate Security Answer   ").grid(row=0,column=5)
Label(root,text="     Candidate Password    ").grid(row=0,column=6)
v=1
############### IT WILL SHOW LIST OF ALL USER#######################
for i in r:
	Label(root,text=i[0]).grid(row=v,column=0)
	Label(root,text=i[1]).grid(row=v,column=1)
	Label(root,text=i[2]).grid(row=v,column=2)
	Label(root,text=i[3]).grid(row=v,column=3)
	Label(root,text=i[4]).grid(row=v,column=4)
	Label(root,text=i[5]).grid(row=v,column=5)
	Label(root,text=i[6]).grid(row=v,column=6)
	v=v+1


root.mainloop()