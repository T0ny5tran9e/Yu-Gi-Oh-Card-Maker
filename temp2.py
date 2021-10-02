from tkinter import *
from tkinter.ttk import *

win=Tk()
win.geometry("500x500")

wrapper1=Labelframe(win)
wrapper2=Labelframe(win)

mycanvas=Canvas(wrapper1)
mycanvas.pack(side=LEFT,fill=)

wrapper1.pack(fill="both",expand="yes",padx=10,pady=10)
wrapper2.pack(fill="both",expand="yes",padx=10,pady=10)

win.mainloop()