def word1():
    familiya = input("Familiyangizni kiriting: ")
    ism = input("Ismingizni kiriting: ")
    full_name = familiya + " " +  ism
    togri = 0
    notogri = 0

    soz = input("afraid?  ")
    if soz == "qo'rqmoq":
        print("To'g'ri javob")
        togri = togri + 1
    else:
        print("Xato")
        notogri = notogri + 1


    soz1 = input("agree?  ")
    if soz1 == "rozi bo'lmoq":
        print("To'g'ri javob")
        togri = togri + 1
    else:
        print("Xato")
        notogri = notogri + 1
    
    soz2 = input("angry?  ")
    if soz2 == "jahldor":
        print("To'g'ri javob")
        togri = togri + 1
    else:
        print("Xato")
        notogri = notogri + 1
    
    soz3 = input("arrive?  ")
    if soz3 == "yetib kelmoq":
        print("To'g'ri javob")
        togri = togri + 1
    else:
        print("Xato")
        notogri = notogri + 1

    soz20 = input("attack?  ")
    if soz20 == "hujum qilmoq":
        print("To'g'ri javob")
        togri = togri + 1
    else:
        print("Xato")
        notogri = notogri + 1

    soz4 = input("bottom?  ")
    if soz4 == "pastki qism":
        print("To'g'ri javob")
        togri = togri + 1
    else:
        print("Xato")
        notogri = notogri + 1

    soz5 = input("clever?  ")
    if soz5 == "aqilli":
        print("To'g'ri javob")
        togri = togri + 1
    else:
        print("Xato")
        notogri = notogri + 1

    soz6 = input("cruel?  ")
    if soz6 == "shafqatsiz":
        print("To'g'ri javob")
        togri = togri + 1
    else:
        print("Xato")
        notogri = notogri + 1

    soz7 = input("finally?  ")
    if soz7 == "nihoyat":
        print("To'g'ri javob")
        togri = togri + 1
    else:
        print("Xato")
        notogri = notogri + 1

    soz8 = input("hide?  ")
    if soz8 == "yashirmoq":
        print("To'g'ri javob")
        togri = togri + 1
    else:
        print("Xato")
        notogri = notogri + 1

    soz9 = input("hunt?  ")
    if soz9 == "ov qilmoq":
        print("To'g'ri javob")
        togri = togri + 1
    else:
        print("Xato")
        notogri = notogri + 1

    soz10 = input("lot?  ")
    if soz10 == "ko'p":
        print("To'g'ri javob")
        togri = togri + 1
    else:
        print("Xato")
        notogri = notogri + 1

    soz11 = input("middle?  ")
    if soz11 == "o'rtasi" :
        print("To'g'ri javob")
        togri = togri + 1
    else:
        print("Xato")
        notogri = notogri + 1

    soz13 = input("moment?  ")
    if soz13 == "lahza":
        print("To'g'ri javob")
        togri = togri + 1
    else:
        print("Xato")
        notogri = notogri + 1

    soz14 = input("pleased?  ")
    if soz14 == "hursand":
        print("To'g'ri javob")
        togri = togri + 1
    else:
        print("Xato")
        notogri = notogri + 1

    soz15 = input("promise?  ")
    if soz15 == "va'da bermoq":
        print("To'g'ri javob")
        togri = togri + 1
    else:
        print("Xato")
        notogri = notogri + 1

    soz16 = input("reply?  ")
    if soz16 == "javob qaytarmoq":
        print("To'g'ri javob")
        togri = togri + 1
    else:
        print("Xato")
        notogri = notogri + 1

    soz17 = input("safe?  ")
    if soz17 == "xavfsiz":
        print("To'g'ri javob")
        togri = togri + 1
    else:
        print("Xato")
        notogri = notogri + 1

    soz18 = input("trick?  ")
    if soz18 == "makr":
        print("To'g'ri javob")
        togri = togri + 1
    else:
        print("Xato")
        notogri = notogri + 1

    soz19 = input("well?  ")
    if soz19 == "yaxshi":
        print("To'g'ri javob")
        togri = togri + 1
    else:
        print("Xato")
        notogri = notogri + 1

    print("******************************\n")

    print("To'g'ri javoblar: ")
    print("""
    afraid	qo'rqmoq
    agree	rozi bo'lmoq
    angry	jahldor
    arrive	yetib kelmoq
    attack	hujum qilmoq
    bottom	pastki qism
    clever	aqilli
    cruel	shafqatsiz, zolim
    finally	nihoyat
    hide	yashirmoq
    hunt	ov qilmoq
    lot	    ko'p
    middle	o'rtasi, orasi
    moment	lahza, soniya
    pleased	xursand
    promise	va'da bermoq
    reply	javob qaytarmoq
    safe	xavfsiz
    trick	makr, hiyla
    well	yaxshi

    """ )

    print(f"Assalomu alaykum {full_name}!\nNatijalaringiz bilan tanishing:" )
    print(f"20 ta savoldan {togri} tasini to'g'ri topdingiz.")
    print(f"20 ta savoldan {notogri} tasini noto'g'ri topdingiz.")
    print("E'tiboringiz uchun Raxmat")

word1()










