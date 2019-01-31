from tkinter import*
from tkinter import ttk
import time
import datetime
from tkinter import messagebox


root=Tk()
root.title("Attandance Monitoring")
root.configure(bg="black")
root.geometry("1350x650+0+0")

def exit():
    ans =messagebox.askyesno("Exit System","Do you want to quit?")
    if(ans):
        root.destroy()
        return
        
def reset():
    value0.set("")
    value1.set("")
    value2.set("")
    value3.set("")
    value4.set("")
    value5.set("")
    value6.set("")
    value7.set("")


def Mark_register():
    if value0.get()=="/":
        value1.set("/")
        value2.set("/")
        value3.set("/")
        value4.set("/")
        value5.set("/")
        value6.set("/")
        value7.set("/")

    elif value0.get()=="0":
        value1.set("0")
        value2.set("0")
        value3.set("0")
        value4.set("0")
        value5.set("0")
        value6.set("0")
        value7.set("0")

    elif value0.get()=="L":
        value1.set("L")
        value2.set("L")
        value3.set("L")
        value4.set("L")
        value5.set("L")
        value6.set("L")
        value7.set("L")

    elif value0.get()=="A":
        value1.set("A")
        value2.set("A")
        value3.set("A")
        value4.set("A")
        value5.set("A")
        value6.set("A")
        value7.set("A")
        
        
        

        
    
#--------------------------------Frames--------------------------
l1=Frame(root, width=1000, height=650, bd=8, relief="raise")
l1.pack(side=LEFT)

l2=Frame(root, width=350, height=650, bd=8, relief="raise")
l2.pack(side=RIGHT)


l11=Frame(l1, width=1000, height=100, bd=8, relief="raise")
l11.pack(side=TOP)

l12=Frame(l1, width=1000, height=550, bd=8, relief="raise")
l12.pack(side=TOP)

l21=Frame(l2, width=350, height=215, bd=8, relief="raise")
l21.pack(side=TOP)

l22=Frame(l2, width=350, height=600, bd=8, relief="raise")
l22.pack(side=TOP)

#-----------------------------------------------------------
con1= Canvas(l22, width=350, height= 425, bg="black",)
con1.grid(row=0,column=0)
image5= PhotoImage(file = "school.png")
con1.create_image(350,350, image=image5)

con = Canvas(l21, width=350, height= 215, bg="black",)
con.grid(row=0,column=0)

image1= PhotoImage(file = "l.png")
con1.create_image(200,200, image=image1)

def pic1():
    image=con.create_image(200,200, image= image1)
    
image2=PhotoImage(file="a.png")

def pic2():
    image=con.create_image(200,200, image= image2)
    
image3=PhotoImage(file="p.png")

def pic3():
    image=con.create_image(200,200, image= image3)
    
image4=PhotoImage(file="s.png")

def pic4():
    image=con.create_image(200,200, image= image4)
    












DateofOrder=StringVar()
value0=StringVar()
value1=StringVar()
value2=StringVar()
value3=StringVar()
value4=StringVar()
value5=StringVar()
value6=StringVar()
value7=StringVar()






DateofOrder.set(time.strftime("%d/%m/%Y"))
#-------------------------------0----------------------------------------
labn=Label(l11,font=("arial",10,"bold"),text="No.",bd=16)
labn.grid(row=0,column=0,sticky=W)




lab=Label(l11,font=("arial",10,"bold"),text="StudentNo.",bd=16)
lab.grid(row=0,column=1,sticky=W)


labs=Label(l11,font=("arial",10,"bold"),text="Student Name.",bd=16)
labs.grid(row=0,column=2,sticky=W)

labs=Label(l11,font=("arial",10,"bold"),text="Course Code",bd=16)
labs.grid(row=0,column=3,sticky=W)


box=ttk.Combobox(l11,textvariable=value0,state="readonly")
box["values"]=("","/","L","O","A","S")
box.current(0)
box.grid(row=0,column=4)





bFill=Button(l11,text="Fill",padx=2,pady=2,bd=2,fg="black",
              font=("arial",10,"bold"),width=12,height=1, command= Mark_register).grid(row=0,column=5)

breset=Button(l11,text="Reset",padx=2,pady=2,bd=2,
              font=("arial",10,"bold"),width=12,height=1, command= reset).grid(row=0,column=6)

bexit=Button(l11,text="EXIT",padx=2,pady=2,bd=2,
             font=("arial",10,"bold"),width=12,height=1, command= exit).grid(row=0,column=7)

labdateoforder=Label(l11,font=("arial",10,"bold"),textvariable=DateofOrder,padx=2
                     ,pady=2,bd=2,fg="black",bg="white",relief=SUNKEN)
labdateoforder.grid(row=0,column=8,sticky=W)

#----------------------------------1-----------------------------------------

labn1=Label(l12,font=("arial",10,"bold"),text="1",bd=16)
labn1.grid(row=0,column=0,sticky=W)




lab1=Label(l12,font=("arial",10,"bold"),text="101",bd=16)
lab1.grid(row=0,column=1,sticky=W)


labs1=Label(l12,font=("arial",10,"bold"),text="VISHAL",bd=16)
labs1.grid(row=0,column=2,sticky=W)

labs1=Label(l12,font=("arial",10,"bold"),text="COMPUTER",bd=16)
labs1.grid(row=0,column=3,sticky=W)


box=ttk.Combobox(l12,textvariable=value1,state="readonly")
box["values"]=("","/","L","O","A","S")
box.current(0)
box.grid(row=0,column=4)





barrow1=Button(l12,text="Fill",padx=2,pady=2,bd=2,fg="black",
              font=("arial",10,"bold"),width=12,height=1).grid(row=0,column=5)

breset1=Button(l12,text="Reset",padx=2,pady=2,bd=2,
              font=("arial",10,"bold"),width=12,height=1).grid(row=0,column=6)

bexit1=Button(l12,text="EXIT",padx=2,pady=2,bd=2,
             font=("arial",10,"bold"),width=12,height=1).grid(row=0,column=7)

labdateoforder1=Label(l12,font=("arial",10,"bold"),textvariable=DateofOrder,padx=2
                     ,pady=2,bd=2,fg="black",bg="white",relief=SUNKEN)
labdateoforder1.grid(row=0,column=8,sticky=W)


#------------------------------2---------------------------------------


labn2=Label(l12,font=("arial",10,"bold"),text="2",bd=16)
labn2.grid(row=1,column=0,sticky=W)




lab2=Label(l12,font=("arial",10,"bold"),text="102",bd=16)
lab2.grid(row=1,column=1,sticky=W)


labs2=Label(l12,font=("arial",10,"bold"),text="ABHI",bd=16)
labs2.grid(row=1,column=2,sticky=W)

labs2=Label(l12,font=("arial",10,"bold"),text="FINANCE",bd=16)
labs2.grid(row=1,column=3,sticky=W)


box=ttk.Combobox(l12,textvariable=value2,state="readonly")
box["values"]=("","/","L","O","A","S")
box.current(0)
box.grid(row=1,column=4)





barrow2=Button(l12,text="",padx=2,pady=2,bd=2,fg="black",
              font=("arial",10,"bold"),width=12,height=1,command= pic1).grid(row=1,column=5)

breset2=Button(l12,text="",padx=2,pady=2,bd=2,
              font=("arial",10,"bold"),width=12,height=1,command= pic2).grid(row=1,column=6)

bexit2=Button(l12,text="",padx=2,pady=2,bd=2,
             font=("arial",10,"bold"),width=12,height=1,command= pic3).grid(row=1,column=7)

bspace =Button(l12,text="", padx=2,pady=2,bd=2,
               font=("arial",10,"bold"),width=12,height=1,command= pic4).grid(row=1,column=8)

labdateoforder2=Label(l12,font=("arial",10,"bold"),textvariable=DateofOrder,padx=2
                     ,pady=2,bd=2,fg="black",bg="white",relief=SUNKEN)
labdateoforder2.grid(row=1,column=8,sticky=W)


#---------------------------------3-----------------------------------

labn3=Label(l12,font=("arial",10,"bold"),text="3",bd=16)
labn3.grid(row=2,column=0,sticky=W)




lab3=Label(l12,font=("arial",10,"bold"),text="103",bd=16)
lab3.grid(row=2,column=1,sticky=W)


labs3=Label(l12,font=("arial",10,"bold"),text="AJAY",bd=16)
labs3.grid(row=2,column=2,sticky=W)

labs3=Label(l12,font=("arial",10,"bold"),text="FINANCE",bd=16)
labs3.grid(row=2,column=3,sticky=W)


box=ttk.Combobox(l12,textvariable=value3,state="readonly")
box["values"]=("","/","L","O","A","S")
box.current(0)
box.grid(row=2,column=4)





barrow3=Button(l12,text="Fill",padx=2,pady=2,bd=2,fg="black",
              font=("arial",10,"bold"),width=12,height=1).grid(row=2,column=5)

breset3=Button(l12,text="Reset",padx=2,pady=2,bd=2,
              font=("arial",10,"bold"),width=12,height=1).grid(row=2,column=6)

bexit3=Button(l12,text="EXIT",padx=2,pady=2,bd=2,
             font=("arial",10,"bold"),width=12,height=1).grid(row=2,column=7)

labdateoforder3=Label(l12,font=("arial",10,"bold"),textvariable=DateofOrder,padx=2
                     ,pady=2,bd=2,fg="black",bg="white",relief=SUNKEN)
labdateoforder3.grid(row=2,column=8,sticky=W)

#----------------------------------4-----------------------------------------


labn4=Label(l12,font=("arial",10,"bold"),text="4",bd=16)
labn4.grid(row=3,column=0,sticky=W)




lab4=Label(l12,font=("arial",10,"bold"),text="104",bd=16)
lab4.grid(row=3,column=1,sticky=W)


labs4=Label(l12,font=("arial",10,"bold"),text="RUSHI",bd=16)
labs4.grid(row=3,column=2,sticky=W)

labs4=Label(l12,font=("arial",10,"bold"),text="TWITTER",bd=16)
labs4.grid(row=3,column=3,sticky=W)


box=ttk.Combobox(l12,textvariable=value4,state="readonly")
box["values"]=("","/","L","O","A","S")
box.current(0)
box.grid(row=3,column=4)





barrow4=Button(l12,text="Fill",padx=2,pady=2,bd=2,fg="black",
              font=("arial",10,"bold"),width=12,height=1).grid(row=3,column=5)

breset4=Button(l12,text="Reset",padx=2,pady=2,bd=2,
              font=("arial",10,"bold"),width=12,height=1).grid(row=3,column=6)

bexit4=Button(l12,text="EXIT",padx=2,pady=2,bd=2,
             font=("arial",10,"bold"),width=12,height=1).grid(row=3,column=7)

labdateoforder4=Label(l12,font=("arial",10,"bold"),textvariable=DateofOrder,padx=2
                     ,pady=2,bd=2,fg="black",bg="white",relief=SUNKEN)
labdateoforder4.grid(row=3,column=8,sticky=W)

#------------------------------5----------------------------------------

labn5=Label(l12,font=("arial",10,"bold"),text="5",bd=16)
labn5.grid(row=4,column=0,sticky=W)




lab5=Label(l12,font=("arial",10,"bold"),text="105",bd=16)
lab5.grid(row=4,column=1,sticky=W)


labs5=Label(l12,font=("arial",10,"bold"),text="HARSHA",bd=16)
labs5.grid(row=4,column=2,sticky=W)

labs5=Label(l12,font=("arial",10,"bold"),text="SALES",bd=16)
labs5.grid(row=4,column=3,sticky=W)


box=ttk.Combobox(l12,textvariable=value5,state="readonly")
box["values"]=("","/","L","O","A","S")
box.current(0)
box.grid(row=4,column=4)





barrow5=Button(l12,text="Fill",padx=2,pady=2,bd=2,fg="black",
              font=("arial",10,"bold"),width=12,height=1).grid(row=4,column=5)

breset5=Button(l12,text="Reset",padx=2,pady=2,bd=2,
              font=("arial",10,"bold"),width=12,height=1).grid(row=4,column=6)

bexit5=Button(l12,text="EXIT",padx=2,pady=2,bd=2,
             font=("arial",10,"bold"),width=12,height=1).grid(row=4,column=7)

labdateoforder1=Label(l12,font=("arial",10,"bold"),textvariable=DateofOrder,padx=2
                     ,pady=2,bd=2,fg="black",bg="white",relief=SUNKEN)
labdateoforder1.grid(row=4,column=8,sticky=W)

#---------------------------------6------------------------------------

labn6=Label(l12,font=("arial",10,"bold"),text="6",bd=16)
labn6.grid(row=5,column=0,sticky=W)




lab6=Label(l12,font=("arial",10,"bold"),text="106",bd=16)
lab6.grid(row=5,column=1,sticky=W)


labs6=Label(l12,font=("arial",10,"bold"),text="SHIVA",bd=16)
labs6.grid(row=5,column=2,sticky=W)

labs6=Label(l12,font=("arial",10,"bold"),text="COMPUTER",bd=16)
labs6.grid(row=5,column=3,sticky=W)


box=ttk.Combobox(l12,textvariable=value6,state="readonly")
box["values"]=("","/","L","O","A","S")
box.current(0)
box.grid(row=5,column=4)





barrow6=Button(l12,text="Fill",padx=2,pady=2,bd=2,fg="black",
              font=("arial",10,"bold"),width=12,height=1).grid(row=5,column=5)

breset6=Button(l12,text="Reset",padx=2,pady=2,bd=2,
              font=("arial",10,"bold"),width=12,height=1).grid(row=5,column=6)

bexit6=Button(l12,text="EXIT",padx=2,pady=2,bd=2,
             font=("arial",10,"bold"),width=12,height=1).grid(row=5,column=7)

labdateoforder6=Label(l12,font=("arial",10,"bold"),textvariable=DateofOrder,padx=2
                     ,pady=2,bd=2,fg="black",bg="white",relief=SUNKEN)
labdateoforder6.grid(row=5,column=8,sticky=W)

#-----------------------------------7----------------------------------

labn7=Label(l12,font=("arial",10,"bold"),text="7",bd=16)
labn7.grid(row=6,column=0,sticky=W)




lab7=Label(l12,font=("arial",10,"bold"),text="107",bd=16)
lab7.grid(row=6,column=1,sticky=W)


labs7=Label(l12,font=("arial",10,"bold"),text="UMYA",bd=16)
labs7.grid(row=6,column=2,sticky=W)

labs7=Label(l12,font=("arial",10,"bold"),text="GUTTA",bd=16)
labs7.grid(row=6,column=3,sticky=W)


box=ttk.Combobox(l12,textvariable=value7,state="readonly")
box["values"]=("","/","L","O","A","S")
box.current(0)
box.grid(row=6,column=4)





barrow7=Button(l12,text="Fill",padx=2,pady=2,bd=2,fg="black",
              font=("arial",10,"bold"),width=12,height=1).grid(row=6,column=5)

breset7=Button(l12,text="Reset",padx=2,pady=2,bd=2,
              font=("arial",10,"bold"),width=12,height=1).grid(row=6,column=6)

bexit7=Button(l12,text="EXIT",padx=2,pady=2,bd=2,
             font=("arial",10,"bold"),width=12,height=1).grid(row=6,column=7)

labdateoforder7=Label(l12,font=("arial",10,"bold"),textvariable=DateofOrder,padx=2
                     ,pady=2,bd=2,fg="black",bg="white",relief=SUNKEN)
labdateoforder7.grid(row=6,column=8,sticky=W)

root.mainloop()
  
