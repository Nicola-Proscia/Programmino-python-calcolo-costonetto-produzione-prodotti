import tkinter as tk
from tkinter import messagebox


#hwood = int(input("inserisci l'altezza del pezzo da tagliare in mm:"))
#lwood = int(input("inserisci la lunghezza del pezzo da tagliare in mm:"))


def areaprice(a, b):
    
    Ariawoodtagliato = a * b

    calcpricewood = ((Ariawoodtagliato / 4712400) * 107.00)
    
    return round(calcpricewood, 2)

#risultatowood = areaprice(hwood , lwood)

#calcolo base legno

#basewoodh = int(input("inserisci l'altezza della base del pezzo da tagliare in mm:"))

#basewoodl = int(input("inserisci la lunchezza della base del pezzo da tagliare in mm:"))

#risultatobase = areaprice(basewoodh , basewoodl)


# calcolo prezzo matassa cavo
#cavlun = (int(input("inserisci la lunghezza del cavo in mm:")))

def cavoprice(c):
    
    calcpricecavo = (((c / 100000) * 20.00)*2)
    
    return round(calcpricecavo, 2)

#risultatocavo = cavoprice(cavlun)

#quante lampadine e prezzo

#lamnum = int(input("inserisci il numero di lampadine che serviranno:"))

def lampaprice(d):
    
    calcpricelamp = d * 0.60
    
    return round(calcpricelamp, 2)

#risultatolamp = lampaprice(lamnum)

# alimentazione 

#alimnum = int(input("utilizzerai una alimentatore o un cavo 220? :   [1] per l'alimentatore /  [2] L'alimentazione 220 :"))
    

def alimprice(f):
    
    
    if f == 1:
        f = 2.20
        return f
    elif f == 2:
        f = 2.50
        return f
    else :
        return ("inserisci un valore corretto")
    
#risultatoalim = alimprice(alimnum)
    

# calcolo tempo manodopera
#tempman = int(input("inserisci il tempo di manodopera in minuti N.B: il valore deve essere in minuti:"))

def calctemp(c):
    
    pricetemp = c * 0.16
    
    return pricetemp

#risultatotemp = calctemp(tempman)




#Tkinter
def calcola_prezzo_legno():
    hwood = int(entry_hwood.get())
    lwood = int(entry_lwood.get())
    return areaprice(hwood, lwood)

def calcola_prezzo_base_legno():
    basewoodh = int(entry_basewoodh.get())
    basewoodl = int(entry_basewoodl.get())
    return areaprice(basewoodh, basewoodl)

def calcola_prezzo_cavo():
    cavlun = int(entry_cavlun.get())
    return cavoprice(cavlun)

def calcola_prezzo_lampadine():
    lamnum = int(entry_lamnum.get())
    return lampaprice(lamnum)

def calcola_prezzo_alimentazione():
    alimnum = int(entry_alimnum.get())
    return alimprice(alimnum)

def calcola_prezzo_tempo_manodopera():
    tempman = int(entry_tempman.get())
    return calctemp(tempman)

def calcola_costo_totale():
    risultatowood = calcola_prezzo_legno()
    risultatobase = calcola_prezzo_base_legno()
    risultatocavo = calcola_prezzo_cavo()
    risultatolamp = calcola_prezzo_lampadine()
    risultatoalim = calcola_prezzo_alimentazione()
    risultatotemp = calcola_prezzo_tempo_manodopera()

    risultato_totale = round(risultatocavo + risultatowood + risultatobase + risultatolamp + risultatoalim + risultatotemp, 2)
    messagebox.showinfo("Risultato", f"Il costo totale del progetto è: {risultato_totale} euro")

# Creazione della finestra principale
root = tk.Tk()
root.title("Calcolatore Prezzo Progetto")

# Creazione degli elementi dell'interfaccia grafica
tk.Label(root, text="Altezza Legno (mm):").grid(row=0, column=0)
tk.Label(root, text="Lunghezza Legno (mm):").grid(row=1, column=0)

entry_hwood = tk.Entry(root)
entry_hwood.grid(row=0, column=1)
entry_lwood = tk.Entry(root)
entry_lwood.grid(row=1, column=1)

tk.Label(root, text="Altezza Base Legno (mm):").grid(row=2, column=0)
tk.Label(root, text="Lunghezza Base Legno (mm):").grid(row=3, column=0)

entry_basewoodh = tk.Entry(root)
entry_basewoodh.grid(row=2, column=1)
entry_basewoodl = tk.Entry(root)
entry_basewoodl.grid(row=3, column=1)

tk.Label(root, text="Lunghezza Cavo (mm):").grid(row=4, column=0)
entry_cavlun = tk.Entry(root)
entry_cavlun.grid(row=4, column=1)

tk.Label(root, text="Numero Lampadine:").grid(row=5, column=0)
entry_lamnum = tk.Entry(root)
entry_lamnum.grid(row=5, column=1)

tk.Label(root, text="Tipo Alimentazione (1 per Alimentatore, 2 per Cavo 220):").grid(row=6, column=0)
entry_alimnum = tk.Entry(root)
entry_alimnum.grid(row=6, column=1)

tk.Label(root, text="Tempo di Manodopera (minuti):").grid(row=7, column=0)
entry_tempman = tk.Entry(root)
entry_tempman.grid(row=7, column=1)

tk.Button(root, text="Calcola", command=calcola_costo_totale).grid(row=8, column=0, columnspan=2)

# Esegui la finestra
root.mainloop()
