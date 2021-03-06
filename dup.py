import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, LEFT, RIGHT, SUNKEN, TOP, X, Y, YES
import tkinter.font as font
from tkinter.ttk import * 
from tkinter import filedialog
from PIL import Image,ImageTk
from NormalCard import *
ui = tk.Tk() #ui as User Interface
myFont = font.Font(family='SAO UI')
#Monster Card Frame
#1Card Frame choice
monster_choice_frame=tk.Frame(ui,bg='white', width=280, height=585)
monster_choice_frame.place(x=10,y=50)
monster_choice_frame.pack_propagate(0)
monster_choice_frame.config(borderwidth=5, relief=SUNKEN)

#2Normal Monster

#3Effect Monster
info_frame_Effect = tk.Frame(ui, bg='darkcyan', width=678, height=585)
info_frame_Effect.place(x=300,y=50)
info_frame_Effect.pack_propagate(0)
efftypfrm0 = tk.Frame(info_frame_Effect)#0 Types Frame
efftypfrm0.place(x=370,y=380,height=44,width=300)
efftypfrm1 = tk.Frame(info_frame_Effect)#1 Types Frame
efftypfrm1.place(x=370,y=380,height=44,width=300)
efftypfrm2 = tk.Frame(info_frame_Effect)#2 Types Frame
efftypfrm2.place(x=370,y=380,height=44,width=300)
efftypfrm3 = tk.Frame(info_frame_Effect)#3 Types Frame
efftypfrm3.place(x=370,y=380,height=44,width=300)
efftypfrm4 = tk.Frame(info_frame_Effect)#4 Types Frame
efftypfrm4.place(x=370,y=380,height=44,width=300)
effect_pendulam_frame = tk.Frame(info_frame_Effect, width=678)#0 Types Frame
effect_switch_state = False#True=on False=off
def Effect_Pendulam():
        #Pendulam Box Size
        bxsz = ['Large','Medium','Small']#Pendulam Box Size List
        dbxsz = tk.StringVar(effect_pendulam_frame)#Display Pendulam Box Size
        dbxsz.set(bxsz[0])
        hbxsz = Label(effect_pendulam_frame, text="Pendulam Box Size", font=("SAO UI", 18))#Pendulam Box Size Heading
        hbxsz.place(x=10, y=5)
        ebxsz = tk.Spinbox(effect_pendulam_frame, values=bxsz, state='readonly', textvariable=dbxsz)#Pendulam Box Size Choice
        ebxsz.place(x=10, y=50, height=40, width=60)
        #Pendulam Scale
        dscal = tk.IntVar(info_frame_Effect)#Display Pendulam Scale
        hscal = tk.Label(effect_pendulam_frame, text="Pendulam Scale", font=("SAO UI", 18))#Pendulam Scale Heading
        hscal.place(x=170, y=5)
        escal = tk.Spinbox(effect_pendulam_frame, from_=0 , to = 13 , state='readonly', textvariable=dscal)#Enter Pendulam Scale
        escal.place(x=170, y=50, height=40, width=60)
        #Effect Font Size
        defsz = tk.StringVar(effect_pendulam_frame, value="29")#Display Effect Font Size
        hefsz = Label(effect_pendulam_frame, text="Font Size", font=("SAO UI", 18))#Effect Font Size Heading
        hefsz.place(x=310, y=5)
        eefsz = tk.Spinbox(effect_pendulam_frame, from_=15 , to = 30, state = 'readonly', textvariable=defsz)#Effect Font Size Choice
        eefsz.place(x=310, y=50, height=40, width=60)
        #Card Effect
        hdscrbox = Label(effect_pendulam_frame, text="Card's Description", font=("SAO UI", 18))#Card Effect Heading
        hdscrbox.place(x=400, y=5)
        dscrbox = tk.Text(effect_pendulam_frame)#Card Effect Box
        dscrbox.place(x=400, y=50, height = 88, width = 200)
        dscrboxsb = tk.Scrollbar(dscrbox,orient='vertical', command=dscrbox.yview)#Card Effect Box Scrollbar
        dscrboxsb.pack(side='right', fill='both')
        dscrbox['yscrollcommand'] = dscrboxsb.set
        #Serial ID
        did = tk.StringVar(info_frame_Effect, value='Enter Card ID')#Display Serial ID
        hid = tk.Label(info_frame_Effect, text="Serial ID", font=("SAO UI", 18))#Serial ID Heading
        hid.place(x=10, y=485)
        eid = tk.Entry(info_frame_Effect, textvariable=did)#Enter Title
        eid.place(x=10, y=520, height=40, width=100)
        #Edition
        edilst = ['None', 'None', '1st Edition', 'Limited Edition', 'Anime Edition', 'Duel Terminal']# Frame List
        dedi = tk.StringVar(info_frame_Effect)
        dedi.set(edilst[0])
        hedi = Label(info_frame_Effect, text="Card Edition", font=("SAO UI", 18))#Card Frame Heading
        hedi.place(x=210, y=485)
        eedi = OptionMenu(info_frame_Effect, dedi, *edilst)#Card Frame Choice
        eedi.place(x=210, y=520, height=40, width=100)
        #Copyright
        dcprt = tk.StringVar(info_frame_Effect, value='??1996 KAZUKI TAKAHASHI')#Display Title
        hcprt = tk.Label(info_frame_Effect, text="Copyright", font=("SAO UI", 18))#Title Heading
        hcprt.place(x=400, y=485)
        ecprt = tk.Entry(info_frame_Effect, textvariable=dcprt)#Enter Title
        ecprt.place(x=400, y=520, height=40, width=200)
        def switch():
                global effect_switch_state
                                
                # Determin is on or off
                if effect_switch_state:
                        info_frame_Effect.place_forget#Forget Previous Effect Monster Frame if Exist
                        info_frame_Effect.place(x=300,y=50)#Update new Effect Monster Frame
                        on_button.config(image = off)
                        effect_pendulam_frame.place_forget()#Forget Previous Effect Monster Pendulam Frame if Exist
                        #Forget Previous Effect Monster ID if Exist
                        hid.place_forget()
                        eid.place_forget()
                        #Update Previous Normal Monster ID if Exist
                        hid.place(x=10, y=485)
                        eid.place(x=10, y=520, height=40, width=100)
                        #Forget Previous Normal Monster Edition if Exist
                        hedi.place_forget()
                        eedi.place_forget()
                        #Update Previous Normal Monster Edition if Exist
                        hedi.place(x=210, y=485)
                        eedi.place(x=210, y=520, height=40, width=100)
                        #Forget Previous Normal Monster Copyright if Exist
                        hcprt.place_forget
                        ecprt.place_forget
                        #Update Previous Normal Monster Copyright if Exist
                        hcprt.place(x=400, y=485)
                        ecprt.place(x=400, y=520, height=40, width=200)
                        effect_switch_state = False
                                                                
                else:
                        info_frame_Effect.place_forget#Forget Previous Effect Monster Frame if Exist
                        info_frame_Effect.place(x=300,y=1)#Update new Effect Monster Frame
                        on_button.config(image = on)
                        effect_pendulam_frame.place(x=0,y=480,height=145)
                        hid.place(x=10, y=625)
                        eid.place(x=10, y=660, height=40, width=100)
                        hedi.place(x=210, y=625)
                        eedi.place(x=210, y=660, height=40, width=100)
                        hcprt.place(x=400, y=625)
                        ecprt.place(x=400, y=660, height=40, width=200)
                        effect_switch_state = True
                                            
        #Define Our Images
        onimg = Image.open("src\On.png")
        offimg = Image.open("src\Off.png") 
        onsz=onimg.resize((40,40))
        offsz=offimg.resize((40,40))
        on=ImageTk.PhotoImage(onsz)
        off=ImageTk.PhotoImage(offsz)
        hpend = Label(info_frame_Effect, text="Is this a Pendulum card?", font=("SAO UI", 18))#Card Frame Heading
        hpend.place(x=10, y=435)
        # Create A Button
        on_button = tk.Button(info_frame_Effect, image = off, bd = 0, command = switch)
        on_button.place(x=300,y=430)
        
#4Ritual Monster
info_frame_Ritual = tk.Frame(ui, bg='darkcyan', width=678, height=585)
info_frame_Ritual.place(x=300,y=50)
info_frame_Ritual.pack_propagate(0) 
#5Fusion Monster
info_frame_Fusion = tk.Frame(ui, bg='darkcyan', width=678, height=585)
info_frame_Fusion.place(x=300,y=50)
info_frame_Fusion.pack_propagate(0) 
#6Synchro Monster
info_frame_Synchro = tk.Frame(ui, bg='darkcyan', width=678, height=585)
info_frame_Synchro.place(x=300,y=50)
info_frame_Synchro.pack_propagate(0) 
#7XYZ Monster
info_frame_XYZ = tk.Frame(ui, bg='darkcyan', width=678, height=585)
info_frame_XYZ.place(x=300,y=50)
info_frame_XYZ.pack_propagate(0)
#8Link
info_frame_Link = tk.Frame(ui, bg='darkcyan', width=678, height=585)
info_frame_Link.place(x=300,y=50)
info_frame_Link.pack_propagate(0)
#9Token
info_frame_Token = tk.Frame(ui, bg='darkcyan', width=678, height=585)
info_frame_Token.place(x=300,y=50)
info_frame_Token.pack_propagate(0)
#10Token (No ATK/DEF)
info_frame_Token_nil_atk_def = tk.Frame(ui, bg='darkcyan', width=678, height=585)
info_frame_Token_nil_atk_def.place(x=300,y=50)
info_frame_Token_nil_atk_def.pack_propagate(0)
#11Spell
info_frame_Spell = tk.Frame(ui, bg='darkcyan', width=678, height=585)
info_frame_Spell.place(x=300,y=50)
info_frame_Spell.pack_propagate(0)
#12Trap
info_frame_Trap = tk.Frame(ui, bg='darkcyan', width=678, height=585)
info_frame_Trap.place(x=300,y=50)
info_frame_Trap.pack_propagate(0)
#13Temp Card Img View
temp_card_img = tk.Frame(ui, width=350, height=485)
temp_card_img.place(x=999,y=50)
temp_card_img.pack_propagate(0) 
temp_card_img.config(borderwidth=5, relief=SUNKEN) 
 
#Browse Image for card Artwork
def browseIMG():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select an Image for Artwork", filetypes = 
    (
        ("PNG Files", "*.png*"), ("JPEG Files", "*.jpg*"), ("JPEG Files", "*.jpeg*"), ("SVG Files", "*.svg*"), 
        ("SVG Files", "*.svgz*"), ("GIF Files", "*.gif*"), ("ICON Files", "*.ico*"), ("WEBP Files", "*.webp*"), 
        ("BMP Files", "*.bmp*"),("All Files","*.*")
    ))

#Monster Card
class Monster_Info():
        N
                                
        def info_Effect_Monster():
                info_frame_Effect.tkraise()
                
                #Title
                dtit = tk.StringVar(info_frame_Effect, value='Enter Title')#Display Title
                htitle = tk.Label(info_frame_Effect, text="Title", font=("SAO UI", 18))#Title Heading
                htitle.place(x=10, y=35)
                etitle = tk.Entry(info_frame_Effect, textvariable=dtit)#Enter Title
                etitle.place(x=300, y=30, height=40, width=200)
                #Card Attribute
                attrilst = ['Select an Attribute', 'Dark', 'Divine', 'Earth', 'Fire', 'Light', 'Water', 'Wind']# Frame List
                dat = tk.StringVar(info_frame_Effect)
                dat.set(attrilst[0])
                hattri = Label(info_frame_Effect, text="Card Frame", font=("SAO UI", 18))#Card Frame Heading
                hattri.place(x=10, y=85)
                eattri = OptionMenu(info_frame_Effect, dat, *attrilst)#Card Frame Choice
                eattri.place(x=300, y=80, height=40, width=200)
                #Card Level
                dlvl = tk.IntVar(info_frame_Effect)#Display DEF
                hlvl = tk.Label(info_frame_Effect, text="Level", font=("SAO UI", 18))#Title Heading
                hlvl.place(x=10, y=135)
                elvl = tk.Spinbox(info_frame_Effect, from_= 0 , to = 12, textvariable=dlvl)#Enter Title
                elvl.place(x=100, y=130, height=40, width=60)
                #Hologram
                hololst = ['None', 'None', 'Holo 1', 'Holo 2', 'Holo 3', 'Holo 4', 'Holo 5', 'Holo 6', 'Holo 7', 'Holo 8']#Level List
                dholo = tk.StringVar(info_frame_Effect)#Display Hologram
                dholo.set(hololst[0])
                hholo = Label(info_frame_Effect, text="Hologram", font=("SAO UI", 18))#Hologram Heading
                hholo.place(x=170, y=135)
                eholo = OptionMenu(info_frame_Effect, dholo, *hololst)#Hologram Choice
                eholo.place(x=280, y=130, height=40, width=80)
                #Rarity
                rarelst = ['Normal', 'Normal', 'Normal Rare', 'Super Rare', 'Ultra Rare', 'Secret Rare', 'Ultra Secret Rare', 'Gold Rare']#Rarity List
                drare = tk.StringVar(info_frame_Effect)#Display Rarity
                drare.set(rarelst[0])
                hrare = Label(info_frame_Effect, text="Rarity", font=("SAO UI", 18))#Rarity Heading
                hrare.place(x=370, y=135)
                erare = OptionMenu(info_frame_Effect, drare, *rarelst)#Rarity Choice
                erare.place(x=450, y=130, height=40, width=150)
                #Button for Selecting Image
                artbrws = tk.Button(info_frame_Effect, text = 'CLICK TO CHANGE THE ARTWORK', bd = '5', font=myFont, command = browseIMG)
                artbrws.place(x=100, y=180, height=40, width=500)
                #Deck Code
                ddcd = tk.StringVar(info_frame_Effect, value="Enter Code")#Display Deck Code
                hdkcod = Label(info_frame_Effect, text="Card's Deck Code", font=("SAO UI", 18))#Deck Code Heading
                hdkcod.place(x=10, y=235)
                edkcod = tk.Entry(info_frame_Effect, textvariable=ddcd)#Enter Title
                edkcod.place(x=300, y=230, height=40, width=200)
                #Card Description
                hdscrbox = Label(info_frame_Effect, text="Card's Description", font=("SAO UI", 18))#Card Description Heading
                hdscrbox.place(x=10, y=300)
                dscrbox = tk.Text(info_frame_Effect)#Description Box
                dscrbox.place(x=300, y=280, height = 88, width = 200)
                dscrboxsb = tk.Scrollbar(dscrbox,orient='vertical', command=dscrbox.yview)#Description Box Scrollbar
                dscrboxsb.pack(side='right', fill='both')
                dscrbox['yscrollcommand'] = dscrboxsb.set
                #Font Size
                dtsz = tk.StringVar(info_frame_Effect, value="29")#Display Deck Code
                htsz = Label(info_frame_Effect, text="Font Size", font=("SAO UI", 18))#Deck Code Heading
                htsz.place(x=540, y=280)
                etsz = tk.Spinbox(info_frame_Effect, from_=15 , to = 30, state = 'readonly', textvariable=dtsz)#Card Type Choice#Enter Title
                etsz.place(x=545, y=320, height=40, width=60)
                #Types
                dtypv = tk.StringVar(info_frame_Effect,"0 Type")
                dtyp1 = tk.StringVar(info_frame_Effect, value="Type 1")#Display Type1
                dtyp2 = tk.StringVar(info_frame_Effect, value="Type 2")#Display Type2
                dtyp3 = tk.StringVar(info_frame_Effect, value="Type 3")#Display Type3
                dtyp4 = tk.StringVar(info_frame_Effect, value="Type 4")#Display Type4
                htyp = Label(info_frame_Effect, text="Card Type", font=("SAO UI", 18))#Type Heading
                htyp.place(x=10, y=385)
                typlst = ['0 Types','1 Types', '2 Types', '3 Types', '4 Types']
                etyp1_1 = tk.Entry(efftypfrm1, textvariable=dtyp1)#1 Type 1
                etyp1_1.place(x=00, y=1, height=40, width=50)
                etyp2_1 = tk.Entry(efftypfrm2, textvariable=dtyp1)#2 Type 1
                etyp2_1.place(x=00, y=1, height=40, width=50)
                etyp2_2 = tk.Entry(efftypfrm2, textvariable=dtyp2)#2 Type 2
                etyp2_2.place(x=60, y=1, height=40, width=50)
                etyp3_1 = tk.Entry(efftypfrm3, textvariable=dtyp1)#3 Type 1
                etyp3_1.place(x=0, y=1, height=40, width=50)
                etyp3_2 = tk.Entry(efftypfrm3, textvariable=dtyp2)#3 Type 2
                etyp3_2.place(x=60, y=1, height=40, width=50)
                etyp3_3 = tk.Entry(efftypfrm3, textvariable=dtyp3)#3 Type 3
                etyp3_3.place(x=120, y=1, height=40, width=50)
                etyp4_1 = tk.Entry(efftypfrm4, textvariable=dtyp1)#4 Type 1
                etyp4_1.place(x=00, y=1, height=40, width=50)
                etyp4_2 = tk.Entry(efftypfrm4, textvariable=dtyp2)#4 Type 2
                etyp4_2.place(x=60, y=1, height=40, width=50)
                etyp4_3 = tk.Entry(efftypfrm4, textvariable=dtyp3)#4 Type 3
                etyp4_3.place(x=120, y=1, height=40, width=50)
                etyp4_4 = tk.Entry(efftypfrm4, textvariable=dtyp4)#4 Type 4
                etyp4_4.place(x=180, y=1, height=40, width=50)
                #No of Types
                efftypfrm0.tkraise()        
                def no_of_typs():
                        dtypvg = dtypv.get()
                        if dtypvg == '0 Types':
                                efftypfrm0.tkraise()
                        elif dtypvg == '1 Types':
                                efftypfrm1.tkraise()
                        elif dtypvg == '2 Types':
                                efftypfrm2.tkraise()
                        elif dtypvg == '3 Types':
                                efftypfrm3.tkraise()
                        elif dtypvg == '4 Types':
                                efftypfrm4.tkraise()
                etyp = tk.Spinbox(info_frame_Effect, values=typlst, state = 'readonly', textvariable=dtypv,command=no_of_typs)#Card Type Choice
                etyp.place(x=300, y=380, height=40, width=60)
                #ATK/DEF
                datk = tk.IntVar(info_frame_Effect)#Display ATK
                ddef = tk.IntVar(info_frame_Effect)#Display DEF
                hatk = tk.Label(info_frame_Effect, text="ATK", font=("SAO UI", 18))#ATK Heading
                hatk.place(x=400, y=435)
                eatk = tk.Spinbox(info_frame_Effect, from_=0 , to = 9999, textvariable=datk)#Enter ATK
                eatk.place(x=450, y=430, height=40, width=60)
                hdef = tk.Label(info_frame_Effect, text="DEF", font=("SAO UI", 18))#DEF Heading
                hdef.place(x=550, y=435)
                edef = tk.Spinbox(info_frame_Effect, from_=0 , to = 9999, textvariable=ddef)#Enter DEF
                edef.place(x=600, y=430, height=40, width=60)
                Effect_Pendulam()
                #Generate Button
                effgen = tk.Button(ui, text = 'Generate', bd = '5', font=myFont)
                effgen.place(x=1100, y=550, height=40, width=100)
                #Save Button
                effsave = tk.Button(ui, text = 'Save', bd = '5', font=myFont)
                effsave.place(x=1200, y=550, height=40, width=100)
                                
        def info_Ritual_Monster():
                info_frame_Ritual.tkraise()
                
                #Title
                dt = tk.StringVar(info_frame_Ritual, value='Enter Title')#Display
                htitle = Label(info_frame_Ritual, text="Title", font=("century gothic", 20))#Title Heading
                htitle.place(x=10, y=25)
                etitle = Entry(info_frame_Ritual, textvariable=dt)#Enter Title
                etitle.place(x=300, y=35, height=40, width=200)
                #Card Frame
                frmlst = ['Normal Monster', 'Effect Monster', 'Ritual Monster', 'Fusion Monster', 'Synchro Monster', 'XYZ Monster' , 'Link', 'Token' , 'Token (No ATK/DEF)', 'Spell', 'Trap']# Frame List
                df = tk.StringVar(info_frame_Ritual)
                df.set(frmlst[0])
                hframe = Label(info_frame_Ritual, text="Card Frame", font=("century gothic", 20))#Card Frame Heading
                hframe.place(x=10, y=75)
                eframe = tk.OptionMenu(info_frame_Ritual, df, *frmlst)#Card Frame Choice
                eframe.place(x=300, y=85, height=40, width=200)
                                
        def info_Fusion_Monster():
                info_frame_Fusion.tkraise()
                
                #Title
                dt = tk.StringVar(info_frame_Fusion, value='Enter Title')#Display
                htitle = Label(info_frame_Fusion, text="Title", font=("century gothic", 20))#Title Heading
                htitle.place(x=10, y=25)
                etitle = Entry(info_frame_Fusion, textvariable=dt)#Enter Title
                etitle.place(x=300, y=35, height=40, width=200)
                #Card Frame
                frmlst = ['Normal Monster', 'Effect Monster', 'Ritual Monster', 'Fusion Monster', 'Synchro Monster', 'XYZ Monster' , 'Link', 'Token' , 'Token (No ATK/DEF)', 'Spell', 'Trap']# Frame List
                df = tk.StringVar(info_frame_Fusion)
                df.set(frmlst[0])
                hframe = Label(info_frame_Fusion, text="Card Frame", font=("century gothic", 20))#Card Frame Heading
                hframe.place(x=10, y=75)
                eframe = tk.OptionMenu(info_frame_Fusion, df, *frmlst)#Card Frame Choice
                eframe.place(x=300, y=85, height=40, width=200)

        def info_Synchro_Monster():
                info_frame_Synchro.tkraise()
                
                #Title
                dt = tk.StringVar(info_frame_Synchro, value='Enter Title')#Display
                htitle = Label(info_frame_Synchro, text="Title", font=("century gothic", 20))#Title Heading
                htitle.place(x=10, y=25)
                etitle = Entry(info_frame_Synchro, textvariable=dt)#Enter Title
                etitle.place(x=300, y=35, height=40, width=200)
                #Card Frame
                frmlst = ['Normal Monster', 'Effect Monster', 'Ritual Monster', 'Fusion Monster', 'Synchro Monster', 'XYZ Monster' , 'Link', 'Token' , 'Token (No ATK/DEF)', 'Spell', 'Trap']# Frame List
                df = tk.StringVar(info_frame_Synchro)
                df.set(frmlst[0])
                hframe = Label(info_frame_Synchro, text="Card Frame", font=("century gothic", 20))#Card Frame Heading
                hframe.place(x=10, y=75)
                eframe = tk.OptionMenu(info_frame_Synchro, df, *frmlst)#Card Frame Choice
                eframe.place(x=300, y=85, height=40, width=200)
                                
        def info_XYZ_Monster():
                info_frame_XYZ.tkraise()
                
                #Title
                dt = tk.StringVar(info_frame_XYZ, value='Enter Title')#Display
                htitle = Label(info_frame_XYZ, text="Title", font=("century gothic", 20))#Title Heading
                htitle.place(x=10, y=25)
                etitle = Entry(info_frame_XYZ, textvariable=dt)#Enter Title
                etitle.place(x=300, y=35, height=40, width=200)
                #Card Frame
                frmlst = ['Normal Monster', 'Effect Monster', 'Ritual Monster', 'Fusion Monster', 'Synchro Monster', 'XYZ Monster' , 'Link', 'Token' , 'Token (No ATK/DEF)', 'Spell', 'Trap']# Frame List
                df = tk.StringVar(info_frame_XYZ)
                df.set(frmlst[0])
                hframe = Label(info_frame_XYZ, text="Card Frame", font=("century gothic", 20))#Card Frame Heading
                hframe.place(x=10, y=75)
                eframe = tk.OptionMenu(info_frame_XYZ, df, *frmlst)#Card Frame Choice
                eframe.place(x=300, y=85, height=40, width=200)
                                
        def info_Link():
                info_frame_Link.tkraise()

                #Title
                dt = tk.StringVar(info_frame_Link, value='Enter Title')#Display
                htitle = Label(info_frame_Link, text="Title", font=("century gothic", 20))#Title Heading
                htitle.place(x=10, y=25)
                etitle = Entry(info_frame_Link, textvariable=dt)#Enter Title
                etitle.place(x=300, y=35, height=40, width=200)
                #Card Frame
                frmlst = ['Normal Monster', 'Effect Monster', 'Ritual Monster', 'Fusion Monster', 'Synchro Monster', 'XYZ Monster' , 'Link', 'Token' , 'Token (No ATK/DEF)', 'Spell', 'Trap']# Frame List
                df = tk.StringVar(info_frame_Link)
                df.set(frmlst[0])
                hframe = Label(info_frame_Link, text="Card Frame", font=("century gothic", 20))#Card Frame Heading
                hframe.place(x=10, y=75)
                eframe = tk.OptionMenu(info_frame_Link, df, *frmlst)#Card Frame Choice
                eframe.place(x=300, y=85, height=40, width=200)
                                
        def info_Token():
                info_frame_Token.tkraise()
                
                #Title
                dt = tk.StringVar(info_frame_Token, value='Enter Title')#Display
                htitle = Label(info_frame_Token, text="Title", font=("century gothic", 20))#Title Heading
                htitle.place(x=10, y=25)
                etitle = Entry(info_frame_Token, textvariable=dt)#Enter Title
                etitle.place(x=300, y=35, height=40, width=200)
                #Card Frame
                frmlst = ['Normal Monster', 'Effect Monster', 'Ritual Monster', 'Fusion Monster', 'Synchro Monster', 'XYZ Monster' , 'Link', 'Token' , 'Token (No ATK/DEF)', 'Spell', 'Trap']# Frame List
                df = tk.StringVar(info_frame_Token)
                df.set(frmlst[0])
                hframe = Label(info_frame_Token, text="Card Frame", font=("century gothic", 20))#Card Frame Heading
                hframe.place(x=10, y=75)
                eframe = tk.OptionMenu(info_frame_Token, df, *frmlst)#Card Frame Choice
                eframe.place(x=300, y=85, height=40, width=200)
                                
        def info_Token_No_ATK_DEF():
                info_frame_Token_nil_atk_def.tkraise()
                
                #Title
                dt = tk.StringVar(info_frame_Token_nil_atk_def, value='Enter Title')#Display
                htitle = Label(info_frame_Token_nil_atk_def, text="Title", font=("century gothic", 20))#Title Heading
                htitle.place(x=10, y=25)
                etitle = Entry(info_frame_Token_nil_atk_def, textvariable=dt)#Enter Title
                etitle.place(x=300, y=35, height=40, width=200)
                #Card Frame
                frmlst = ['Normal Monster', 'Effect Monster', 'Ritual Monster', 'Fusion Monster', 'Synchro Monster', 'XYZ Monster' , 'Link', 'Token' , 'Token (No ATK/DEF)', 'Spell', 'Trap']# Frame List
                df = tk.StringVar(info_frame_Token_nil_atk_def)
                df.set(frmlst[0])
                hframe = Label(info_frame_Token_nil_atk_def, text="Card Frame", font=("century gothic", 20))#Card Frame Heading
                hframe.place(x=10, y=75)
                eframe = tk.OptionMenu(info_frame_Token_nil_atk_def, df, *frmlst)#Card Frame Choice
                eframe.place(x=300, y=85, height=40, width=200)
                                
        def info_Spell():
                info_frame_Spell.tkraise()
                
                #Title
                dt = tk.StringVar(info_frame_Spell, value='Enter Title')#Display
                htitle = Label(info_frame_Spell, text="Title", font=("century gothic", 20))#Title Heading
                htitle.place(x=10, y=25)
                etitle = Entry(info_frame_Spell, textvariable=dt)#Enter Title
                etitle.place(x=300, y=35, height=40, width=200)
                #Card Frame
                frmlst = ['Normal Monster', 'Effect Monster', 'Ritual Monster', 'Fusion Monster', 'Synchro Monster', 'XYZ Monster' , 'Link', 'Token' , 'Token (No ATK/DEF)', 'Spell', 'Trap']# Frame List
                df = tk.StringVar(info_frame_Spell)
                df.set(frmlst[0])
                hframe = Label(info_frame_Spell, text="Card Frame", font=("century gothic", 20))#Card Frame Heading
                hframe.place(x=10, y=75)
                eframe = tk.OptionMenu(info_frame_Spell, df, *frmlst)#Card Frame Choice
                eframe.place(x=300, y=85, height=40, width=200)
                                
        def info_Trap():
                info_frame_Trap.tkraise()
                #Title
                dt = tk.StringVar(info_frame_Trap, value='Enter Title')#Display
                htitle = Label(info_frame_Trap, text="Title", font=("century gothic", 20))#Title Heading
                htitle.place(x=10, y=25)
                etitle = Entry(info_frame_Trap, textvariable=dt)#Enter Title
                etitle.place(x=300, y=35, height=40, width=200)
                #Card Frame
                frmlst = ['Normal Monster', 'Effect Monster', 'Ritual Monster', 'Fusion Monster', 'Synchro Monster', 'XYZ Monster' , 'Link', 'Token' , 'Token (No ATK/DEF)', 'Spell', 'Trap']# Frame List
                df = tk.StringVar(info_frame_Trap)
                df.set(frmlst[0])
                hframe = Label(info_frame_Trap, text="Card Frame", font=("century gothic", 20))#Card Frame Heading
                hframe.place(x=10, y=75)
                eframe = tk.OptionMenu(info_frame_Trap, df, *frmlst)#Card Frame Choice
                eframe.place(x=300, y=85, height=40, width=200)