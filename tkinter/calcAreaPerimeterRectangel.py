from tkinter import *

window = Tk()

def calcArea():
    area = float(e1_value.get())*float(e2_value.get())
    t1.insert(END,area)

def calcPerimeter():
    perimeter = 2*(float(e1_value.get())+float(e2_value.get()))
    t2.insert(END,perimeter)


text = Label(window,text="Rectangle")
text.grid(row=0, column=1)

text = Label(window,text="Area")
text.grid(row=4, column=1)

text = Label(window,text="Perimeter")
text.grid(row=4, column=3)

b1 = Button(window, text = "Calculate", command = lambda:[calcArea(),calcPerimeter()])
b1.grid(row=0,column=2)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row=0,column=3)

e2_value = StringVar()
e2 = Entry(window, textvariable = e2_value)
e2.grid(row=0,column=4)

t1 = Text(window,height=1,width=20)
t1.grid(row=4,column=2)

t2 = Text(window, height=1,width=20)
t2.grid(row=4,column=4)


window.mainloop()
