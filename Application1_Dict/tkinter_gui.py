from tkinter import *

window = Tk()

butt = Button(window, text = "Cosmos")
butt.grid(row=0,column=0)

txt = Text(window)
txt.grid(row=0,column = 1)

ent = Entry(window)
ent.grid(row = 0, column = 2)

window.mainloop()
