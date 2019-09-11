from tkinter import *

window = Tk()

def kg_to_grams():
    grams = float(e1_value.get())*1000
    t1.insert(END,grams)

def kg_to_pounds():
    pounds = float(e1_value.get())*2.20462
    t2.insert(END,pounds)

def kg_to_ounces():
    ounces = float(e1_value.get())*35.274
    t3.insert(END,ounces)

text = Label(window,text="kg")
text.grid(row=0, column=1)

b1 = Button(window, text = "Convert", command = lambda:[kg_to_grams(),kg_to_pounds(),kg_to_ounces()])
b1.grid(row=0,column=3)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row=0,column=2)

t1 = Text(window,height=1,width=20)
t1.grid(row=1,column=1)

t2 = Text(window, height=1,width=20)
t2.grid(row=1,column=2)

t3 = Text(window,height=1,width=20)
t3.grid(row=1,column=3)

window.mainloop()
