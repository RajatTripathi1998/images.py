from tkinter import *
import tkinter.ttk
root=Tk()
root.configure(background='red')
root.geometry("700x400")

def f1():
    global index
    index-=1
    NEXT['state']='active'
    if index==0:
        PREVIOUS['state']='disable'        
    l['text']=f'{index+1}/31'
    m['image']=image_object[index]

def f2():
    global index
    index+=1
    PREVIOUS['state']='active'
    if index==30:
        NEXT['state']='disable'
    l['text']=f'{index+1}/19'
    m['image']=image_object[index]
    
def f3():
    global index,time
    index+=1
    s=text.get()
    if time!=1:
        time=int(s[19:])
    NEXT['state']='disable'
    PREVIOUS['state']='disable'
    FIRST['state']='disable'
    l['text']=f'{index+1}/31'
    m['image']=image_object[index]
    if index==30:
        FIRST['state']='active'
        PREVIOUS['state']='active'
        return
    root.after(time*1000,f3)

def f4():
    global index
    index=0
    s='enter time in sec.: '
    text.set(s)
    PREVIOUS['state']='disable'
    NEXT['state']='active'
    l['text']=f'{index+1}/31'
    m['image']=image_object[index]

time=1
image=['E1','I1','C1','I2','C2','I3','S2','I4','I5','V2','I6','I7','H1','BIG1',
       'K1','BIG2','E2','BIG3','K2','BIG4','BIG5','BIG6','LIG1',
       'LIG2','LIG3','V1','LIG4','S1','LIG5','H2','LIG6']
index=0
image_object=[]
for i in image:
    image_object.append(PhotoImage(file = f"{i}.gif"))
m = Label(root, image=image_object[index],bg='powder blue',height=210,width=300)
m.place(x=190,y=20)
l=Label(root,text=f'{index+1}/31',bg='powder blue',font=("italian",20,"bold"),
        height=1,width=5,relief='raised')
l.place(x=300,y=250)
PREVIOUS=Button(root,text="PREVIOUS",state='disable',bg='powder blue',command=f1,
                height=2,width=8,font=("italian",20,"bold"))
PREVIOUS.place(x=15,y=120)
NEXT=Button(root,text="NEXT",command=f2,bg='powder blue',font=("italian",20,"bold")
            ,height=2,width=8)
NEXT.place(x=520,y=120)
AUTO=Button(root,text="AUTO",command=f3,bg='light green',font=("italian",20,"bold")
            ,height=2,width=8)
AUTO.place(x=500,y=300)
FIRST=Button(root,text="FIRST",command=f4,bg='light green',font=("italian",20,"bold")
            ,height=2,width=8)
FIRST.place(x=15,y=300)
text=StringVar()
s='enter time in sec.: '
e=Entry(root,text=text,font=("italian",20,"bold"),width=18,bg='pink')
text.set(s)
e.place(x=200,y=330)
root.mainloop()
