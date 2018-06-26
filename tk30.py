import tkinter
import tkinter.messagebox

top = tkinter.Tk()
top.minsize(100,200)

def helloCallback():
   tkinter.messagebox.showinfo( "Hello Python", "python")
photo= PhotoImage(file="images.jpg")

B = tkinter.Button(top,activebackground="black",activeforeground="blue",bg="green",fg="pink",state="active",image=photo,command = helloCallBack)

B.pack()
top.mainloop()
