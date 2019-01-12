from tkinter import *
root= Tk()
root.title("Find & Replace")
v=IntVar
root.geometry("400x400")
Label(root,text="FIND:-").grid(row=0, sticky=W)
Label(root,text="REPLACE:-").grid(row=1, sticky=W)
Entry(root).grid(row=0, column=1, padx=2, pady=2, columnspan=9)
Entry(root).grid(row=1, column=1, padx=2, pady=2, columnspan=15)
Button(root, text="FIND").grid( row=0, column=20, sticky=W, padx=2, pady=2)
Button(root,text="FIND ALL").grid(row=1, column=20, sticky=E, padx=2, pady=2)

Button(root, text="REPLACE").grid(row=2, column=20, sticky=W, padx=2, pady=2)
Button(root, text="REPLACE ALL").grid(row=3, column=20, sticky=W, padx=2, pady=2)
Checkbutton(root,text="Match whole word only").grid(row=4, column=2, sticky=W)
Checkbutton(root, text="Wrap round").grid(row=4, column=16, sticky=E)
Checkbutton(root, text="Match").grid(row=6, column=2, sticky=W)
Radiobutton(root, text="UP", variable=v,value=4).grid(row=6, column=6, sticky=NW)
Radiobutton(root,text="DOWN", variable=v,value=4).grid(row=6, column=15, sticky=SW)
