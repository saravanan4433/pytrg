from tkinter import *

from tkinter import messagebox

top = Tk()

C = Canvas(top, bg = "pink", height = 250, width = 300,bd=10)


coord = 10, 50, 240, 500

line = C.create_line(10,10,200,200,fill = 'white')
C.pack()
top.mainloop()
