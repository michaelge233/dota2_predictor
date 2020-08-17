from tkinter import *
import tkinter.font as tf
import json
import dota_bayes
import numpy as np

fo=open("id_name.json","r")
id_name_dic=json.loads(fo.read())
fo.close()
hero_num=0
for i in id_name_dic:
    if int(i)>hero_num:
        hero_num=int(i)

win=Tk()
imgs=[]
buttons={}
text0=Text(win,state=DISABLED)
text0.tag_add("tag1","0.0","0.1")
text0.tag_add("tag2","0.0","0.1")
font1=tf.Font(size=16)
font2=tf.Font(size=8)
text0.tag_config("tag1",font=font1)
text0.tag_config("tag2",font=font2)

choose_num=0
X=[]

def choose_hero(hi):
    #hi为英雄id，字符串
    global choose_num
    choose_num=choose_num+1
    text0.config(state=NORMAL)
    if choose_num==1:
        text0.insert(INSERT,"Our Heroes:\n","tag1")


    X.append(int(hi))
    text0.insert(INSERT,id_name_dic[hi]+", ","tag2")
    buttons[hi].config(state=DISABLED)
    if choose_num<=5:
        buttons[hi].config(bg="blue")
    else:
        buttons[hi].config(bg="red")
    if choose_num==10:
        for b in buttons:
            buttons[b].config(state=DISABLED)
    if choose_num==5:
        text0.insert(INSERT,"\n\nOpponents\' Heroes:\n","tag1")
    text0.config(state=DISABLED)

i=0
for hero_id in id_name_dic:

    filename='.\\hero_images\\'+hero_id+" "+id_name_dic[hero_id]+".png"
    try:
        imgBtn = PhotoImage(file=filename)
        imgs.append(imgBtn)
        buttons[hero_id]=Button(win,image=imgBtn,bg="white",command=lambda hi=hero_id:choose_hero(hi))
        buttons[hero_id].grid(row=i//16,column=i%16)
    except:
        buttons[hero_id]=Button(win,text=id_name_dic[hero_id],bg="white",command=lambda hi=hero_id:choose_hero(hi))
        buttons[hero_id].grid(row=i//16,column=i%16)
    i=i+1

def f1():
    if choose_num!=10:
        return
    text0.config(state=NORMAL)
    rx=np.zeros(hero_num*2,dtype = np.bool_)
    for i in range(0,5):
        rx[X[i]-1]=True
    for i in range(5,10):
        rx[X[i]+hero_num-1]=True
    p=dota_bayes.Dota_NB()
    text0.insert(INSERT,"\n\nShall we win?   ","tag1")
    if bool(p.predict_one(rx)):
        text0.insert(INSERT,"True","tag1")
    else:
        text0.insert(INSERT,"False","tag1")
    text0.insert(INSERT,"\n\nProbability:    "+str(p.predict_one_proba(rx)),"tag1")
    text0.config(state=DISABLED)

def f2():
    global choose_num,X
    X=[]
    choose_num=0
    for b in buttons:
        buttons[b].config(state=NORMAL)
        buttons[b].config(bg="white")
    text0.config(state=NORMAL)
    text0.delete(0.0, END)
    text0.config(state=DISABLED)
    
button1=Button(win,text="PREDICT",command=f1)
button2=Button(win,text="CLEAR",command=f2)


text0.grid(row=i//16+1,column=0,columnspan=16)
button1.grid(row=i//16+2,column=0,columnspan=8)
button2.grid(row=i//16+2,column=8,columnspan=8)
win.mainloop()
