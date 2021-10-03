import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, LEFT, RIGHT, SUNKEN, TOP, X, Y, YES
from tkinter.ttk import * 
from tkinter import filedialog
from PIL import Image,ImageTk
ui = tk.Tk() #ui as User Interface
#Monster Card Frame
#1Card Frame choice
monster_choice_frame=tk.Frame(ui,bg='white', width=280, height=585)
monster_choice_frame.place(x=10,y=50)
monster_choice_frame.pack_propagate(0)
monster_choice_frame.config(borderwidth=5, relief=SUNKEN)

#2Normal Monster
info_frame_Normal = tk.Frame(ui, bg='darkcyan', width=678, height=700)#Main Frame
info_frame_Normal.place(x=300,y=50)
info_frame_Normal.pack_propagate(0)

typfrm0 = tk.Frame(info_frame_Normal)#0 Types Frame
typfrm0.place(x=370,y=380,height=44,width=300)
typfrm1 = tk.Frame(info_frame_Normal)#1 Types Frame
typfrm1.place(x=370,y=380,height=44,width=300)
typfrm2 = tk.Frame(info_frame_Normal)#2 Types Frame
typfrm2.place(x=370,y=380,height=44,width=300)
typfrm3 = tk.Frame(info_frame_Normal)#3 Types Frame
typfrm3.place(x=370,y=380,height=44,width=300)
typfrm4 = tk.Frame(info_frame_Normal)#4 Types Frame
typfrm4.place(x=370,y=380,height=44,width=300)
normal_pendulam_frame = tk.Frame(info_frame_Normal, bg='red', width=678)#0 Types Frame
normal_switch_state = False#True=on False=off
def normal_Pendulam():
        #Pendulam Box Size
        bxsz = ['Large','Medium','Small']#Size List
        dbxsz = tk.StringVar(normal_pendulam_frame)#Display Pendulam Box Size
        dbxsz.set(bxsz[0])
        hbxsz = Label(normal_pendulam_frame, text="Pendulam Box Size", font=("SAO UI", 18))#Pendulam Box Size Heading
        hbxsz.place(x=10, y=5)
        ebxsz = tk.Spinbox(normal_pendulam_frame, values=bxsz, state='readonly', textvariable=dbxsz)#Pendulam Box Size Choice
        ebxsz.place(x=10, y=50, height=40, width=60)
        dscal = tk.IntVar(info_frame_Normal)#Display Pendulam Scale
        hscal = tk.Label(normal_pendulam_frame, text="Pendulam Scale", font=("SAO UI", 18))#Title Heading
        hscal.place(x=170, y=5)
        escal = tk.Spinbox(normal_pendulam_frame, from_=0 , to = 13 , state='readonly', textvariable=dscal)#Enter Title
        escal.place(x=170, y=50, height=40, width=60)
        #Effect Font Size
        defsz = tk.StringVar(normal_pendulam_frame, value="29")#Display Deck Code
        hefsz = Label(normal_pendulam_frame, text="Font Size", font=("SAO UI", 18))#Deck Code Heading
        hefsz.place(x=310, y=5)
        eefsz = tk.Spinbox(normal_pendulam_frame, from_=15 , to = 30, state = 'readonly', textvariable=defsz)#Card Type Choice#Enter Title
        eefsz.place(x=310, y=50, height=40, width=60)
        #Card Description
        hdscrbox = Label(normal_pendulam_frame, text="Card's Description", font=("SAO UI", 18))#Card Description Heading
        hdscrbox.place(x=400, y=5)
        dscrbox = tk.Text(normal_pendulam_frame)#Description Box
        dscrbox.place(x=400, y=50, height = 88, width = 200)
        dscrboxsb = tk.Scrollbar(dscrbox,orient='vertical', command=dscrbox.yview)#Description Box Scrollbar
        dscrboxsb.pack(side='right', fill='both')
        dscrbox['yscrollcommand'] = dscrboxsb.set
        #Serial ID
        did = tk.StringVar(info_frame_Normal, value='Enter Card ID')#Display Title
        hid = tk.Label(info_frame_Normal, text="Title", font=("SAO UI", 18))#Title Heading
        hid.place(x=10, y=485)
        eid = tk.Entry(info_frame_Normal, textvariable=did)#Enter Title
        eid.place(x=300, y=480, height=40, width=100)
        def switch():
                global normal_switch_state
                                
                # Determin is on or off
                if normal_switch_state:
                        info_frame_Normal.place_forget
                        info_frame_Normal.place(x=300,y=50)
                        on_button.config(image = off)
                        normal_pendulam_frame.place_forget()
                        hid.place_forget()
                        eid.place_forget()
                        hid.place(x=10, y=485)
                        eid.place(x=300, y=480, height=40, width=100)
                        normal_switch_state = False
                                                                
                else:
                        info_frame_Normal.place_forget
                        info_frame_Normal.place(x=300,y=5)
                        on_button.config(image = on)
                        normal_pendulam_frame.place(x=0,y=480,height=145)
                        hid.place(x=10, y=635)
                        eid.place(x=300, y=630, height=40, width=100)
                        normal_switch_state = True
                                            
        #Define Our Images
        onimg = Image.open("src\On.png")
        offimg = Image.open("src\Off.png") 
        onsz=onimg.resize((40,40))
        offsz=offimg.resize((40,40))
        on=ImageTk.PhotoImage(onsz)
        off=ImageTk.PhotoImage(offsz)
        hpend = Label(info_frame_Normal, text="Is this a Pendulum card?", font=("SAO UI", 18))#Card Frame Heading
        hpend.place(x=10, y=435)
        # Create A Button
        on_button = tk.Button(info_frame_Normal, image = off, bd = 0, command = switch)
        on_button.place(x=300,y=430)

#3Effect Monster
info_frame_Effect = tk.Frame(ui, bg='darkcyan', width=678, height=585)
info_frame_Effect.place(x=300,y=50)
info_frame_Effect.pack_propagate(0) 
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
        def info_Normal_Monster():
                info_frame_Normal.tkraise()
                #Title
                dtit = tk.StringVar(info_frame_Normal, value='Enter Title')#Display Title
                htitle = tk.Label(info_frame_Normal, text="Title", font=("SAO UI", 18))#Title Heading
                htitle.place(x=10, y=35)
                etitle = tk.Entry(info_frame_Normal, textvariable=dtit)#Enter Title
                etitle.place(x=300, y=30, height=40, width=200)
                #Card Attribute
                attrilst = ['Select an Attribute', 'Dark', 'Divine', 'Earth', 'Fire', 'Light', 'Water', 'Wind']# Frame List
                dat = tk.StringVar(info_frame_Normal)
                dat.set(attrilst[0])
                hattri = Label(info_frame_Normal, text="Card Frame", font=("SAO UI", 18))#Card Frame Heading
                hattri.place(x=10, y=85)
                eattri = OptionMenu(info_frame_Normal, dat, *attrilst)#Card Frame Choice
                eattri.place(x=300, y=80, height=40, width=200)
                #Card Level
                dlvl = tk.IntVar(info_frame_Normal)#Display DEF
                hlvl = tk.Label(info_frame_Normal, text="Level", font=("SAO UI", 18))#Title Heading
                hlvl.place(x=10, y=135)
                elvl = tk.Spinbox(info_frame_Normal, from_= 0 , to = 12, textvariable=dlvl)#Enter Title
                elvl.place(x=100, y=130, height=40, width=60)
                #Hologram
                hololst = ['None', 'None', 'Holo 1', 'Holo 2', 'Holo 3', 'Holo 4', 'Holo 5', 'Holo 6', 'Holo 7', 'Holo 8']#Level List
                dholo = tk.StringVar(info_frame_Normal)#Display Level
                dholo.set(hololst[0])
                hholo = Label(info_frame_Normal, text="Hologram", font=("SAO UI", 18))#Card Frame Heading
                hholo.place(x=170, y=135)
                eholo = OptionMenu(info_frame_Normal, dholo, *hololst)#Card Frame Choice
                eholo.place(x=280, y=130, height=40, width=80)
                #Rarity
                rarelst = ['Normal', 'Normal', 'Normal Rare', 'Super Rare', 'Ultra Rare', 'Secret Rare', 'Ultra Secret Rare', 'Gold Rare']#Rarity List
                drare = tk.StringVar(info_frame_Normal)#Display Rarity
                drare.set(rarelst[0])
                hrare = Label(info_frame_Normal, text="Rarity", font=("SAO UI", 18))#Rarity Heading
                hrare.place(x=370, y=135)
                erare = OptionMenu(info_frame_Normal, drare, *rarelst)#Rarity Choice
                erare.place(x=450, y=130, height=40, width=80)
                #Button for Selecting Image
                artbrws = tk.Button(info_frame_Normal, text = 'CLICK TO CHANGE THE ARTWORK', bd = '5', command = browseIMG)
                artbrws.place(x=100, y=180, height=40, width=500)
                #Deck Code
                ddcd = tk.StringVar(info_frame_Normal, value="Enter Code")#Display Deck Code
                hdkcod = Label(info_frame_Normal, text="Card's Deck Code", font=("SAO UI", 18))#Deck Code Heading
                hdkcod.place(x=10, y=235)
                edkcod = tk.Entry(info_frame_Normal, textvariable=ddcd)#Enter Title
                edkcod.place(x=300, y=230, height=40, width=200)
                #Card Description
                hdscrbox = Label(info_frame_Normal, text="Card's Description", font=("SAO UI", 18))#Card Description Heading
                hdscrbox.place(x=10, y=300)
                dscrbox = tk.Text(info_frame_Normal)#Description Box
                dscrbox.place(x=300, y=280, height = 88, width = 200)
                dscrboxsb = tk.Scrollbar(dscrbox,orient='vertical', command=dscrbox.yview)#Description Box Scrollbar
                dscrboxsb.pack(side='right', fill='both')
                dscrbox['yscrollcommand'] = dscrboxsb.set
                #Font Size
                dtsz = tk.StringVar(info_frame_Normal, value="29")#Display Deck Code
                htsz = Label(info_frame_Normal, text="Font Size", font=("SAO UI", 18))#Deck Code Heading
                htsz.place(x=540, y=280)
                etsz = tk.Spinbox(info_frame_Normal, from_=15 , to = 30, state = 'readonly', textvariable=dtsz)#Card Type Choice#Enter Title
                etsz.place(x=545, y=320, height=40, width=60)
                #Types
                dtypv = tk.StringVar(info_frame_Normal,"0 Type")
                dtyp1 = tk.StringVar(info_frame_Normal, value="Type 1")#Display Type1
                dtyp2 = tk.StringVar(info_frame_Normal, value="Type 2")#Display Type2
                dtyp3 = tk.StringVar(info_frame_Normal, value="Type 3")#Display Type3
                dtyp4 = tk.StringVar(info_frame_Normal, value="Type 4")#Display Type4
                htyp = Label(info_frame_Normal, text="Card Type", font=("SAO UI", 18))#Type Heading
                htyp.place(x=10, y=385)
                typlst = ['0 Types','1 Types', '2 Types', '3 Types', '4 Types']
                etyp1_1 = tk.Entry(typfrm1, textvariable=dtyp1)#1 Type 1
                etyp1_1.place(x=00, y=1, height=40, width=50)
                etyp2_1 = tk.Entry(typfrm2, textvariable=dtyp1)#2 Type 1
                etyp2_1.place(x=00, y=1, height=40, width=50)
                etyp2_2 = tk.Entry(typfrm2, textvariable=dtyp2)#2 Type 2
                etyp2_2.place(x=60, y=1, height=40, width=50)
                etyp3_1 = tk.Entry(typfrm3, textvariable=dtyp1)#3 Type 1
                etyp3_1.place(x=0, y=1, height=40, width=50)
                etyp3_2 = tk.Entry(typfrm3, textvariable=dtyp2)#3 Type 2
                etyp3_2.place(x=60, y=1, height=40, width=50)
                etyp3_3 = tk.Entry(typfrm3, textvariable=dtyp3)#3 Type 3
                etyp3_3.place(x=120, y=1, height=40, width=50)
                etyp4_1 = tk.Entry(typfrm4, textvariable=dtyp1)#4 Type 1
                etyp4_1.place(x=00, y=1, height=40, width=50)
                etyp4_2 = tk.Entry(typfrm4, textvariable=dtyp2)#4 Type 2
                etyp4_2.place(x=60, y=1, height=40, width=50)
                etyp4_3 = tk.Entry(typfrm4, textvariable=dtyp3)#4 Type 3
                etyp4_3.place(x=120, y=1, height=40, width=50)
                etyp4_4 = tk.Entry(typfrm4, textvariable=dtyp4)#4 Type 4
                etyp4_4.place(x=180, y=1, height=40, width=50)
                #No of Types
                typfrm0.tkraise()        
                def no_of_typs():
                        dtypvg = dtypv.get()
                        if dtypvg == '0 Types':
                                typfrm0.tkraise()
                        elif dtypvg == '1 Types':
                                typfrm1.tkraise()
                        elif dtypvg == '2 Types':
                                typfrm2.tkraise()
                        elif dtypvg == '3 Types':
                                typfrm3.tkraise()
                        elif dtypvg == '4 Types':
                                typfrm4.tkraise()
                etyp = tk.Spinbox(info_frame_Normal, values=typlst, state = 'readonly', textvariable=dtypv,command=no_of_typs)#Card Type Choice
                etyp.place(x=300, y=380, height=40, width=60)
                #ATK/DEF
                datk = tk.IntVar(info_frame_Normal)#Display ATK
                ddef = tk.IntVar(info_frame_Normal)#Display DEF
                hatk = tk.Label(info_frame_Normal, text="ATK", font=("SAO UI", 18))#Title Heading
                hatk.place(x=400, y=435)
                eatk = tk.Spinbox(info_frame_Normal, from_=0 , to = 9999, textvariable=datk)#Enter Title
                eatk.place(x=450, y=430, height=40, width=60)
                hdef = tk.Label(info_frame_Normal, text="DEF", font=("SAO UI", 18))#Title Heading
                hdef.place(x=550, y=435)
                edef = tk.Spinbox(info_frame_Normal, from_=0 , to = 9999, textvariable=ddef)#Enter Title
                edef.place(x=600, y=430, height=40, width=60)
                normal_Pendulam()
                #Serial ID
                did = tk.StringVar(info_frame_Normal, value='Enter Card ID')#Display Title
                hid = tk.Label(info_frame_Normal, text="Card ID", font=("SAO UI", 18))#Title Heading
                hid.place(x=10, y=35)
                eid = tk.Entry(info_frame_Normal, textvariable=dtit)#Enter Title
                eid.place(x=300, y=30, height=40, width=100)
                
                                
        def info_Effect_Monster():
                info_frame_Effect.tkraise()
                
                #Title
                dt = tk.StringVar(info_frame_Effect, value='Enter Title')#Display
                htitle = Label(info_frame_Effect, text="Title", font=("century gothic", 20))#Title Heading
                htitle.place(x=10, y=25)
                etitle = Entry(info_frame_Effect, textvariable=dt)#Enter Title
                etitle.place(x=300, y=35, height=40, width=200)
                #Card Frame
                frmlst = ['Normal Monster', 'Effect Monster', 'Ritual Monster', 'Fusion Monster', 'Synchro Monster', 'XYZ Monster' , 'Link', 'Token' , 'Token (No ATK/DEF)', 'Spell', 'Trap']# Frame List
                df = tk.StringVar(info_frame_Effect)
                df.set(frmlst[0])
                hframe = Label(info_frame_Effect, text="Card Frame", font=("century gothic", 20))#Card Frame Heading
                hframe.place(x=10, y=75)
                eframe = tk.OptionMenu(info_frame_Effect, df, *frmlst)#Card Frame Choice
                eframe.place(x=300, y=85, height=40, width=200)
                                
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
                           