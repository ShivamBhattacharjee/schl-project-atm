from tkinter import *
import time

root=Tk()
root.geometry("900x850")
root.configure(bg="#23254a")

tops=Frame(root,bg="grey",width=800,height=50,relief=SUNKEN)
tops.pack(side=TOP)

f1=Frame(root,bg="black",width=300,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,bg="black",width=300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

localTime=time.asctime(time.localtime(time.time()))

lb1=Label(tops,text="ATM MACHINE",fg="Powder Blue",bg="black",bd=10,anchor="w")
lb1.grid(row=0,column=0)

lb2=Label(tops,text=localTime,fg="black",bg="grey",bd=10,anchor="w")
lb2.grid(row=1,column=0)

root.mainloop()