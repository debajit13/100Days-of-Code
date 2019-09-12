from tkinter import *

window = Tk()

def celcius_fahrenheit():
    fahrenheit = (float(e1_value.get())*9/5)+32
    t1.insert(END,fahrenheit)

def celcius_kelvin():
    kelvin = (float(e1_value.get())+273)
    t2.insert(END,kelvin)

text = Label(window,text="Celcius")
text.grid(row=0, column=1)

b1 = Button(window, text = "Convert", command = lambda:[celcius_kelvin(),celcius_fahrenheit()])
b1.grid(row=0,column=3)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row=0,column=2)

t1 = Text(window,height=1,width=20)
t1.grid(row=1,column=1)

t2 = Text(window, height=1,width=20)
t2.grid(row=1,column=2)

window.mainloop()
