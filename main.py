import tkinter as tk
import tkinter.font as font
from tkinter.ttk import * 
from Monster_Card_Frame import *

ui.title("YU-GI-OH! Card Maker")
screenwidth= ui.winfo_screenwidth()               
screenheight= ui.winfo_screenheight()               
ui.geometry("%dx%d" % (screenwidth, screenheight))#UI full size M2
ui.resizable(False,False)

myFont = font.Font(family='SAO UI')

df = tk.StringVar(ui,"0")
#Monster Card Choice
def card_frame_choice():
        tk.Radiobutton(monster_choice_frame, text = "  Normal Monster  ", variable = df, value = 0, indicator = 0, font=myFont,command=Monster_Info.info_Normal_Monster).place(x=40, y=10, height=40, width=200)
        tk.Radiobutton(monster_choice_frame, text = "  Effect Monster  ", variable = df, value = 1, indicator = 0,  font=myFont,command=Monster_Info.info_Effect_Monster).place(x=40, y=60, height=40, width=200)
        tk.Radiobutton(monster_choice_frame, text = "  Ritual Monster  ", variable = df, value = 2, indicator = 0,  font=myFont,command=Monster_Info.info_Ritual_Monster).place(x=40, y=110, height=40, width=200)
        tk.Radiobutton(monster_choice_frame, text = "  Fusion Monster  ", variable = df, value = 3, indicator = 0,  font=myFont,command=Monster_Info.info_Fusion_Monster).place(x=40, y=160, height=40, width=200)
        tk.Radiobutton(monster_choice_frame, text = " Synchro  Monster ", variable = df, value = 4, indicator = 0,  font=myFont,command=Monster_Info.info_Synchro_Monster).place(x=40, y=210, height=40, width=200)
        tk.Radiobutton(monster_choice_frame, text = "    XYZ Monster   ", variable = df, value = 5, indicator = 0,  font=myFont,command=Monster_Info.info_XYZ_Monster).place(x=40, y=260, height=40, width=200)
        tk.Radiobutton(monster_choice_frame, text = "       Link       ", variable = df, value = 6, indicator = 0,  font=myFont,command=Monster_Info.info_Link).place(x=40, y=310, height=40, width=200)
        tk.Radiobutton(monster_choice_frame, text = "       Token      ", variable = df, value = 7, indicator = 0,  font=myFont,command=Monster_Info.info_Token).place(x=40, y=360, height=40, width=200)
        tk.Radiobutton(monster_choice_frame, text = "Token (No ATK/DEF)", variable = df, value = 8, indicator = 0,  font=myFont,command=Monster_Info.info_Token_No_ATK_DEF).place(x=40, y=410, height=40, width=200)
        tk.Radiobutton(monster_choice_frame, text = "       Spell      ", variable = df, value = 9, indicator = 0,  font=myFont,command=Monster_Info.info_Spell).place(x=40, y=460, height=40, width=200)
        tk.Radiobutton(monster_choice_frame, text = "       Trap       ", variable = df, value = 10, indicator = 0,  font=myFont,command=Monster_Info.info_Trap).place(x=40, y=510, height=40, width=200)
Monster_Info.info_Normal_Monster()
card_frame_choice()



ui.mainloop()