#Calculator
from tkinter import *
from tkinter import messagebox
def calcSum():
    fn1=int(Fno.get())
    fn2=int(Sno.get())
    r=fn1+fn2
    messagebox.showinfo("OUTPUT","Result="+str(r))

def calcSub():
    fn1=int(Fno.get())
    fn2=int(Sno.get())
    s=fn1-fn2
    messagebox.showinfo("OUTPUT","Result="+str(s))

def calcMul():
    fn1=int(Fno.get())
    fn2=int(Sno.get())
    m=fn1*fn2
    messagebox.showinfo("OUTPUT","Result="+str(m))

def calcDiv():
    fn1=int(Fno.get())
    fn2=int(Sno.get())
    s=fn1/fn2
    messagebox.showinfo("OUTPUT","Result="+str(s))

root=Tk()
root.title("Calculator")
root.geometry("300x300")
Fno=StringVar()
Sno=StringVar()
add=Button(root,text="Add", command=calcSum, width=15)
subtraction=Button(root,text="Subtraction", command=calcSub, width=15)
multiplication=Button(root,text="Multiplication", command=calcMul, width=15)
divition=Button(root,text="Divition", command=calcDiv, width=15)
cancel=Button(root,text="Cancel", command=root.destroy, width=15)
Lbl1=Label(root,text="Calculation")
fst_no=Label(root,text="Enter first number")
lst_no=Label(root,text="Enter second number")
n1=Entry(root,width=25,textvariable=Fno)
n2=Entry(root,width=25,textvariable=Sno)
Lbl1.grid(column=1, row=1, columnspan=2)
fst_no.grid(column=1, row=2)
n1.grid(column=2, row=2)
lst_no.grid(column=1, row=3)
n2.grid(column=2, row=3)
add.grid(column=1, row=4)
subtraction.grid(column=2, row=4)
multiplication.grid(column=1, row=5)
divition.grid(column=2, row=5)
cancel.grid(column=1, row=6, columnspan=2)

root.mainloop()
