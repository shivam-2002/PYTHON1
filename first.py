
words=['Elephant','Mango','Apple','gun','Door','Phone','Ball','Garage','Laptop','doodle','google','curly','ugly','beautifull','short','work' ,'hard','easy','photo','particle','yesterday','tommorow','nowadays','never','ever','monitor','keyboard','printer','device','humble','naughty','cruel','nature','shivam','aamir','manthan','alok','weather','sunny','rainy','foggy']


def labelSlider():
    global count,sliderWords
    text='Welcome to Typing Speed Increaser Game'
    if(count>=len(text)):
        count=0
        sliderWords=''
    sliderWords += text[count]
    count+=1
    fontLabel.configure(text=sliderWords)
    fontLabel.after(150,labelSlider)
    
def time():
    global timeleft,score,miss
    if(timeleft<11):
        timeLabelCount.configure(fg='red')
    else:
        pass
        
    if(timeleft>0):
        timeleft-=1
        timeLabelCount.configure(text=timeleft)
        timeLabelCount.after(1000,time)
    else:
        gamePlayDetailLabel.configure(text="Hit={}|Miss={}|Total Score={}".format(score,miss,score-miss))
        rr=messagebox.askretrycancel('Notification','For Play Again Hit Retry Button')
        if(rr==True):
            score=0
            timeleft=60
            miss=0
            timeLabelCount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)
def startGame(event):
    global score,miss
    if(timeleft==60):
        time()
    gamePlayDetailLabel.configure(text='')
    if(wordEntry.get()==wordLabel['text']):
        score+=1
        scoreLabelCount.configure(text=score)
        print('score:',score)
    else:
        miss+=1
        print('miss:',miss)
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    print(wordEntry.get())
    wordEntry.delete(0,END)



from tkinter import *
import random
from tkinter import messagebox
#from tkinter.ttk import *
##########################################  ROOT METHOD
root=Tk()
root.geometry('800x600+400+100')
root.configure(bg='cyan')
root.title('Typing Speed Increaser Game')
##########################################Title ICON
#root.iconbitmap('pac.ico')

#master = Tk()

#p1 = PhotoImage(file ='pacc.png')
#master.iconphoto(False, p1)

#from PIL import Image
#filename = r'pac.ico'
#img = Image.open(filename)
#img.save('pac.ico')

##########################################  VARIABLES
score=0
timeleft=60
count=0
sliderWords=''
miss=0

##########################################  LABEL METHOD
fontLabel=Label(root,text='',font=('arial',20,'italic bold'),bg='cyan',fg='red',width=40)
fontLabel.place(x=10,y=10)

labelSlider()

random.shuffle(words)

wordLabel=Label(root,text=words[0],font=('arial',30,'italic bold'),bg='cyan')
wordLabel.place(x=350,y=200)

scoreLabel=Label(root,text='Your Score : ',font=('arial',20,'italic bold'),bg='cyan')
scoreLabel.place(x=10,y=100)

scoreLabelCount=Label(root,text=score,font=('arial',20,'italic bold'),bg='cyan',fg='blue')
scoreLabelCount.place(x=80,y=180)

timerLabel=Label(root,text='Time Left : ',font=('arial',20,'italic bold'),bg='cyan')
timerLabel.place(x=600,y=100)

timeLabelCount=Label(root,text=timeleft,font=('arial',20,'italic bold'),bg='cyan',fg='blue')
timeLabelCount.place(x=680,y=180)

gamePlayDetailLabel=Label(root,text='Type Word And Hit ENTER Button',font=('arial',20,'italic bold'),bg='cyan',fg='grey')
gamePlayDetailLabel.place(x=180,y=450)
########################################## ENTRY METHOD
wordEntry=Entry(root,font=('arial',30,'italic bold'),bd=8,justify='center')
wordEntry.place(x=250,y=300)
wordEntry.focus_set()
##########################################
root.bind('<Return>',startGame)
root.mainloop()