import tkinter as tk
from tkinter.ttk import * 
from tkinter import filedialog
ui = tk.Tk() #ui as User Interface
ui.title("YU-GI-OH! Card Maker")
screenwidth= ui.winfo_screenwidth()               
screenheight= ui.winfo_screenheight()               
ui.geometry("%dx%d" % (screenwidth, screenheight))#UI full size M2
ui.resizable(False,False)

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"),
                                                       ("all files","*.*")))
    label_file_explorer.configure(text="File Opened: "+filename)
label_file_explorer = tk.Label(ui, text = "File Explorer using Tkinter", width = 100, height = 4, fg = "blue")
label_file_explorer.place(x=10, y=75)
button_explore = tk.Button(ui, text = "Browse Files", command = browseFiles)
button_explore.place(x=10, y=5)

frame_1 = tk.Frame(ui, width=1800, height=400)
frame_1.pack(pady=185)
frame_1.pack_propagate(0)  

def fnc1(): 
    monster_frame_info2.forget
    hattri = Label(monster_frame_info2, text="Attribute", font=("century gothic", 20))#Card Attribute Heading
    hattri.place(x=10)
    eattri = Menubutton(monster_frame_info2,text="Select an Attribute", )
    eattri.place(x=300,height=40, width=200)
    eattri.menu = tk.Menu(eattri)
    eattri["menu"] = eattri.menu

    #Attribute List
    eattri.menu.add_command(label="Dark", command=lambda: print("Normal Monster"))
    eattri.menu.add_command(label="Divine", command=lambda: print("Effect Monster"))
    eattri.menu.add_command(label="Earth", command=lambda: print("Effect Monster"))
    eattri.menu.add_command(label="Fire", command=lambda: print("Effect Monster"))
    eattri.menu.add_command(label="Light", command=lambda: print("Synchro Monster"))
    eattri.menu.add_command(label="Water", command=lambda: print("XYZ Monster"))
    eattri.menu.add_command(label="Wind", command=lambda: print("Link"))
    #return frame_1

def fnc2(): 
    frame_1.forget
    hattri = Label(monster_frame_info2, text="Attribute", font=("century gothic", 20))#Card Attribute Heading
    hattri.place(x=10)
    eattri = Menubutton(monster_frame_info2,text="Select an Attribute", )
    eattri.place(x=300,height=40, width=200)
    eattri.menu = tk.Menu(eattri)
    eattri["menu"] = eattri.menu

    #Attribute List
    eattri.menu.add_command(label="1Dark", command=lambda: print("Normal Monster"))
    eattri.menu.add_command(label="1Divine", command=lambda: print("Effect Monster"))
    eattri.menu.add_command(label="1Earth", command=lambda: print("Effect Monster"))
    eattri.menu.add_command(label="1Fire", command=lambda: print("Effect Monster"))
    eattri.menu.add_command(label="1Light", command=lambda: print("Synchro Monster"))
    eattri.menu.add_command(label="1Water", command=lambda: print("XYZ Monster"))
    eattri.menu.add_command(label="1Wind", command=lambda: print("Link"))

frmlst = [('Normal Monster',0), ('Effect Monster',1), ('Ritual Monster',2), ('Fusion Monster',3), ('Synchro Monster',4), ('XYZ Monster',5) , ('Link',6), ('Token',7) , ('Token (No ATK/DEF)',8), ('Spell',9), ('Trap',10)]# Frame List

#Monster Frame
monster_frame=tk.Frame(ui, width=285, height=786)
monster_frame.place(x=10,y=50)
monster_frame.pack_propagate(0)  
"""btn1 = tk.Button(monster_frame, text = 'Click me !', bd = '5', command = fnc1)
btn1.place(x=10,y=50)
btn2 = tk.Button(monster_frame, text = 'Click me !', bd = '5', command = fnc2)
btn2.place(x=10,y=100)"""
#2Frame for getting Card info
monster_frame_info2 = tk.Frame(ui, bg='cyan', width=678, height=585)
monster_frame_info2.place(x=300,y=50)
monster_frame_info2.pack_propagate(0)
"""def fun():
    tk.Radiobutton(monster_frame, text = "Normal Monster", variable = df, value = 0, indicator = 0, command=fnc1).pack(ipadx = 10,ipady=10, pady=5)
    tk.Radiobutton(monster_frame, text = "Effect Monster", variable = df, value = 1, indicator = 0, command=fnc2).pack(ipadx = 10,ipady=10, pady=5)
    tk.Radiobutton(monster_frame, text = "Ritual Monster", variable = df, value = 2, indicator = 0, command=fnc1).pack(ipadx = 10,ipady=10, pady=5)
    tk.Radiobutton(monster_frame, text = "Fusion Monster", variable = df, value = 3, indicator = 0, command=fnc2).pack(ipadx = 10,ipady=10, pady=5)
    tk.Radiobutton(monster_frame, text = "Synchro Monster", variable = df, value = 4, indicator = 0, command=fnc1).pack(ipadx = 10,ipady=10, pady=5)
    tk.Radiobutton(monster_frame, text = "XYZ Monster", variable = df, value = 5, indicator = 0, command=fnc1).pack(ipadx = 10,ipady=10, pady=5)
    tk.Radiobutton(monster_frame, text = "Link", variable = df, value = 6, indicator = 0, command=fnc2).pack(ipadx = 10,ipady=10, pady=5)
    tk.Radiobutton(monster_frame, text = "Token", variable = df, value = 7, indicator = 0, command=fnc1).pack(ipadx = 10,ipady=10, pady=5)
    tk.Radiobutton(monster_frame, text = "Token (No ATK/DEF)", variable = df, value = 8, indicator = 0, command=fnc2).pack(ipadx = 10,ipady=10, pady=5)
    tk.Radiobutton(monster_frame, text = "Spell", variable = df, value = 9, indicator = 0, command=fnc1).pack(ipadx = 10,ipady=10, pady=5)
    tk.Radiobutton(monster_frame, text = "Trap", variable = df, value = 10, indicator = 0, command=fnc2).pack(ipadx = 10,ipady=10, pady=5)
fun()"""
df = tk.StringVar(monster_frame, "1")
df.set(3)
for (text,value) in frmlst:
    tk.Radiobutton(monster_frame, text = text, variable = df, value = value, indicator = 0).pack(ipadx = 10,ipady=10, pady=5)


def radbut():
    radioval=df.get()
    if radioval=='0':
        fnc1()
    elif radioval=='1':
        fnc2()
    elif radioval=='2':
        fnc1()
    elif radioval=='3':
        fnc2()
    elif radioval=='4':
        fnc1()
    elif radioval=='5':
        fnc2()
    elif radioval=='6':
        fnc1()
    elif radioval=='7':
        fnc2()
    elif radioval=='8':
        fnc1()
    elif radioval=='9':
        fnc2()
    elif radioval=='10':
        fnc1()
    elif radioval=='11':
        fnc2()

radbut()

ui.mainloop()