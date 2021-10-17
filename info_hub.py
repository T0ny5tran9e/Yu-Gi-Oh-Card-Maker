def get_description(myText_Box):
    #global inputx
    inputx = myText_Box.get("1.0","end-1c")
    print (inputx)
def card_typs(typv,dtyp1,dtyp2,dtyp3,dtyp4):
    dtypvg = typv.get()
    if dtypvg == '0 Types':
            print('1 Types ')
    elif dtypvg == '1 Types':
            print('1 Types :',dtyp1.get())
    elif dtypvg == '2 Types':
            print('2 Types :',dtyp1.get(),dtyp2.get())
    elif dtypvg == '3 Types':
            print('3 Types :',dtyp1.get(),dtyp2.get(),dtyp3.get())
    elif dtypvg == '4 Types':
            print('4 Types :',dtyp1.get(),dtyp2.get(),dtyp3.get(),dtyp4.get())
def normal_info(tit,at,lvl,holo,rare,art,dcd,scrbox,tsz,typ,typ1,typ2,typ3,typ4,atck,defe,pend):
    print("Normal Monster")
    print (tit.get())
    print (at.get())
    print (lvl.get())
    print (holo.get())
    print (rare.get())
    print (art)
    print (dcd.get())
    get_description(scrbox)
    print (tsz.get())
    card_typs(typ,typ1,typ2,typ3,typ4)
    print ('ATk :',atck.get())
    print ('DEF :',defe.get())
    print (pend)
