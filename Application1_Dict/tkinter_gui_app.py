from tkinter import *

def convKg():
    convToGrams = float(strToConvert.get()) * 1000
    txt_1.delete('1.0',END)
    txt_1.insert(END, convToGrams)
    convToPounds = float(strToConvert.get()) * 2.204
    txt_2.delete('1.0',END)
    txt_2.insert(END, convToPounds)
    convToOunce = float(strToConvert.get()) * 35.274
    txt_3.delete('1.0',END)
    txt_3.insert(END, convToOunce)

window = Tk()
lab = Label(window, text="kg", width = 10)
butt = Button(window,text="convert",command=convKg, width = 10)
strToConvert = StringVar()
ent = Entry(window,textvariable=strToConvert, width = 10)
txt_1 = Text(window, height=1,width = 20)
txt_2 = Text(window, height=1,width = 20)
txt_3 = Text(window, height=1,width = 20)

def createUI(window):
    lab.grid(row=0,column=0)
    ent.grid(row=0,column=1)
    butt.grid(row=0,column=2)
    txt_1.grid(row=1,column=0)
    txt_2.grid(row=1,column=1)
    txt_3.grid(row=1,column=2)


createUI(window)


window .mainloop()
