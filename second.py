import tkinter as tk
from tkinter import ttk
import time as tm
import threading
import random



#initial variables
timeLimit=60
remainingTime=timeLimit
elapsedTime=0
elapsedTimeInMinute=0

totalWords=0
wrong_words=0

wpm=0
accuracy=0

#Functions
def start_timer():
    global elapsedTime
    
    entry.focus()
    entry.config(state='normal')
    btn_start.config(state='disabled')
    btn_reset.config(state='disabled')
    
    for time in range(1,timeLimit+1):
        elapsedTime=time
        lbl_elapsedTimer['text']=elapsedTime
        
        updatedRemainingTime=remainingTime-elapsedTime
        lbl_remainingTimer['text']=updatedRemainingTime
        
        tm.sleep(1)
        root.update()
    entry.config(state='disabled')
    btn_reset.config(state='normal')


def count():
    global wrong_words
    global elapsedTime
    global elapsedTimerInMinute
    
    para_words=lbl_para['text'].split()
    
    while elapsedTime!=timeLimit:
        enteredParagraph=entry.get(1.0,'end-1c').split()
        totalWords=len(enteredParagraph)
        
    #para_words
    #enteredParagraph
    for pair in list(zip(para_words,enteredParagraph)):
        #['hello','hello']
        if pair[0]!=pair[1]:
            wrong_words+=1
    elapsedTimeInMinute=elapsedTime/60
    
    #WPM
    #(totalwords-wrongwords)/time in minute
    
    wpm=(totalWords-wrong_words)/elapsedTimeInMinute
    lbl_wpm['text']=wpm
    
    #accuracy
    #accuracy=(wpm/gross_wpm)*100
    gross_wpm=totalWords/elapsedTimeInMinute
    accuracy=(wpm/gross_wpm)*100
    lbl_accuracy['text']=round(accuracy,2)
    
    #total words
    lbl_total_words['text']=totalWords
    
    #wrong words
    lbl_wrong_words['text']=wrong_words
    
    
def start():
    thr1=threading.Thread(target=start_timer)
    thr1.start()
    thr2=threading.Thread(target=count)
    thr2.start()
    
def reset():
    global remainingTime
    global elapsedTime
    
    btn_reset.config(state='disabled')
    btn_start.config(state='normal')
    
    entry.config(state='normal')
    entry.delete(1.0,tk.END)
    entry.config(state='disabled')
                 
    remainingTime=timeLimit
    elapsedTime=0
    
    lbl_elapsedTimer['text']=0
    lbl_remainingTimer['text']=0
    lbl_wpm['text']=0
    lbl_accuracy['text']=0
    lbl_total_words['text']=0
    lbl_wrong_words['text']=0
    
    
#Changing Paragraph
#PARAGRAPH TEXT FILE
with open('paragraph.txt') as f:
    paragraphs=f.readlines()
    selected_paragraph=random.choice(paragraphs)
    
###############################################################     GUI      ##################################################


root=tk.Tk()
root.title("Speed typing Increaser Game")
root.geometry('908x400+250+20')
root.resizable(False,False)


#Main Frame
main_frame=tk.Frame(root,bg='light green',bd=4)
main_frame.grid()

frame_title=tk.Frame(main_frame,bg='orange',relief='flat')
frame_title.grid(row=0,column=0)

lbl_title=tk.Label(frame_title,text='Speed Type',font='arial 35 bold',bg='yellow',fg='black',relief='flat',bd=10,width=30)
lbl_title.grid(row=0,column=0,pady=10)

#Test Frame
frame_test=tk.LabelFrame(main_frame,text='TEXT',font='arial 10 bold',bg='cyan',relief='groove')
frame_test.grid(row=1,column=0)

lbl_para=tk.Label(frame_test,text=selected_paragraph,wraplength=800,justify='left')
lbl_para.grid(row=0,column=0,pady=5)


#Input Box
entry=tk.Text(frame_test,height=8,width=110,bd=2)
entry.grid(row=1,column=0,pady=5,padx=5)
entry.config(state='disabled')


#Output Frame
frame_output=tk.Frame(main_frame,bg='white',relief='flat')
frame_output.grid(row=2,column=0)
frame_labels=tk.Frame(frame_output,bg='white')
frame_labels.grid(row=0,column=0)

#elsapsed time
lbl_elapsedTime=tk.Label(frame_labels,text='Elapsed Time:',font='Tahona 10 bold',fg='red',bg='white')
lbl_elapsedTime.grid(row=0,column=0,padx=10,pady=10)
lbl_elapsedTimer=tk.Label(frame_labels,text='0',font='Tahona 10 bold',fg='red',bg='white')
lbl_elapsedTimer.grid(row=0,column=1,padx=10,pady=10)

#remaining time
lbl_remainingTime=tk.Label(frame_labels,text='Remaining Time:',font='Tahona 10 bold',fg='red',bg='white')
lbl_remainingTime.grid(row=0,column=2,padx=10,pady=10)
lbl_remainingTimer=tk.Label(frame_labels,text='60',font='Tahona 10 bold',fg='red',bg='white')
lbl_remainingTimer.grid(row=0,column=3,padx=10,pady=10)

#wpm
lbl_wpmTitle=tk.Label(frame_labels,text='WPM:',font='Tahona 10 bold',fg='red',bg='white')
lbl_wpmTitle.grid(row=0,column=4,padx=10,pady=10)
lbl_wpm=tk.Label(frame_labels,text='0',font='Tahona 10 bold',fg='red',bg='white')
lbl_wpm.grid(row=0,column=5,padx=10,pady=10)

#accuracy
lbl_accuracy_title=tk.Label(frame_labels,text='Accuracy:',font='Tahona 10 bold',fg='red',bg='white')
lbl_accuracy_title.grid(row=0,column=6,padx=10,pady=10)
lbl_accuracy=tk.Label(frame_labels,text='0',font='Tahona 10 bold',fg='red',bg='white')
lbl_accuracy.grid(row=0,column=7,padx=10,pady=10)

#total words
lbl_total_words_title=tk.Label(frame_labels,text='Total words:',font='Tahona 10 bold',fg='red',bg='white')
lbl_total_words_title.grid(row=0,column=8,padx=10,pady=10)
lbl_total_words=tk.Label(frame_labels,text='0',font='Tahona 10 bold',fg='red',bg='white')
lbl_total_words.grid(row=0,column=9,padx=10,pady=10)

#wrong words
lbl_wrong_words_title=tk.Label(frame_labels,text='Wrong words:',font='Tahona 10 bold',fg='red',bg='white')
lbl_wrong_words_title.grid(row=0,column=10,padx=10,pady=10)
lbl_wrong_words=tk.Label(frame_labels,text='0',font='Tahona 10 bold',fg='red',bg='white')
lbl_wrong_words.grid(row=0,column=11,padx=10,pady=10)

#Control Frame
frame_controls=tk.Frame(frame_output,bg='white')
frame_controls.grid(row=1)


#Start
btn_start=ttk.Button(frame_controls,text='Start',command=start)
btn_start.grid(row=0,column=0,padx=10)

#Restart
btn_reset=ttk.Button(frame_controls,text='Reset',command=reset)
btn_reset.grid(row=0,column=1,padx=10)

root.mainloop()