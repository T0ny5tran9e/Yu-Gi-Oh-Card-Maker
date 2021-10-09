from tkinter import *
from tkinter import ttk
state=True
def cstate(childList):
    global state
    if state:
        def enable(childList):
            
            for child in childList:
                child.configure(state='enable')
            state=False
    else:
        def disable(childList):
            for child in frame2.winfo_children():
                child.configure(state='disable')
            state=True

root = Tk()

#Creates top frame
frame1 = ttk.LabelFrame(root, padding=(10,10,10,10))
frame1.grid(column=0, row=0, padx=10, pady=10)

button2 = ttk.Button(frame1, text="This enables bottom frame", 
                     command=lambda: cstate(frame2.winfo_children()))
button2.pack()

#Creates bottom frame
frame2 = ttk.LabelFrame(root, padding=(10,10,10,10))
frame2.grid(column=0, row=1, padx=10, pady=10)

entry = ttk.Entry(frame2)
entry.pack()

button2 = ttk.Button(frame2, text="button")
button2.pack()



root.mainloop()