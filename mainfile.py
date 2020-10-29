from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("400x400")
root.resizable(0,0)

def game():
    import first

def para():
    import second
root.geometry("600x600+0+0")
root.title(".......OPENING PHASE.......")
########################### WRITE PATH OF IMAGE##################
i=Image.open("C:/Users/hp/OneDrive/Desktop/code/manthan.jpg")
p=ImageTk.PhotoImage(i)

c=Canvas(root,height=600,width=600,bg="blue")
c.create_image(100,100,image=p)
Label(root,text="WELCOME TO LOVELY TYPE ",font=("arial",20,"italic")).place(x=100,y=10)
Label(root,text=" WRITING GAME",font=("arial",20,"italic")).place(x=170,y=50)
Label(root,text="DARE TO TYPE",font=("arial",15)).place(x=225,y=450)
Button(root,text="TYPING GAME",command=game,cursor="hand2",bd=10).place(x=150,y=500)
Button(root,text="PARAGRAPH TYPING",command=para,cursor="hand2",bd=10).place(x=300,y=500)

c.pack()
root.mainloop()