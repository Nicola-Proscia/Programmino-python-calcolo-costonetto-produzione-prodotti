# calcolo del legno prezzo
hwood = int(input("inserisci l'altezza del pezzo da tagliare in mm:"))
lwood = int(input("inserisci la lunghezza del pezzo da tagliare in mm:"))


def areaprice(a, b):
    
    Ariawoodtagliato = a * b

    calcpricewood = ((Ariawoodtagliato / 4712400) * 107)
    
    return round(calcpricewood, 2)

risultatowood = areaprice(hwood , lwood)

#calcolo base legno

basewoodh = int(input("inserisci l'altezza della base del pezzo da tagliare in mm:"))

basewoodl = int(input("inserisci la lunchezza della base del pezzo da tagliare in mm:"))

risultatobase = areaprice(basewoodh , basewoodl)


# calcolo prezzo matassa cavo
cavlun = (int(input("inserisci la lunghezza del cavo in mm:")))

def cavoprice(c):
    
    calcpricecavo = ((c / 100000) * 20)
    
    return round(calcpricecavo, 2)

risultatocavo = cavoprice(cavlun)

#quante lampadine e prezzo

lamnum = int(input("inserisci il numero di lampadine che serviranno:"))

def lampaprice(d):
    
    calcpricelamp = d * 0.59
    
    return round(calcpricelamp, 2)

risultatolamp = lampaprice(lamnum)

# alimentazione 

alimnum = int(input("utilizzerai una alimentatore o un cavo 220? :   [1] per l'alimentatore /  [2] L'alimentazione 220 :"))
    

def alimprice(f):
    
    
    if f == 1:
        f = 2.20
        return f
    elif f == 2:
        f = 2.30
        return f
    else :
        return ("inserisci un valore corretto")
    
risultatoalim = alimprice(alimnum)
    

# calcolo tempo manodopera
tempman = int(input("inserisci il tempo di manodopera in minuti N.B: il valore deve essere in minuti:"))

def calctemp(c):
    
    pricetemp = c * 0.16
    
    return pricetemp

risultatotemp = calctemp(tempman)



#print finale generale
print (round(risultatocavo + risultatowood + risultatobase + risultatolamp + risultatoalim + risultatotemp , 2))


