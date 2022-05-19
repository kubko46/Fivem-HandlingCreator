#Program na vytvoření chování auta ve hře Gta 5.
#Vytvoří soubor s názvem "handling.meta" a v něm se zapíše vaše představa do formátu gta5.
# <Author = "Jakub Stříbrný"/>
# <Title = "Handling Creator"/>

from pydoc import text
from tkinter import *

root = Tk()
root.title('Handling Creator by Kubko')
root.geometry('900x600+50+50')
root.iconbitmap('handlingcreator.ico')
root.configure(bg='#474747')

file1 = open("handling.meta","w")
  
# \n (poznámka pro Developera)
file1.writelines("<?xml version=" + '"1.0"' + " encoding=" + '"UTF-8"' + "?>\n")
file1.writelines("<CHandlingDataMgr>\n")
file1.writelines(" <HandlingData>\n")
file1.writelines("    <Item type=" + '"CHandlingData"' + ">\n")

#Polozky v Menu
SpaceLabel = Label(root, text="", bg='#474747')
SpaceLabel.grid(row=0)

Namelabel = Label(root, text="1. Zadej jméno modelu vozidla:")
Namelabel.grid(row=1,column=0)
name_auta = Entry(root)
name_auta.grid(row=2,column=0)


VahaLabel = Label(root, text="2. Zadej váhu vozidla v KG a celých číslech :")
VahaLabel.grid(row=1,column=2)
vaha_auta = Entry(root)
vaha_auta.grid(row=2,column=2)

SpaceLabel2 = Label(root, text="", bg='#474747')
SpaceLabel2.grid(row=3)

OdporLabel = Label(root, text="3. Zadej odporovou silu (Normalni auta: 4, Tezka: 8):")
OdporLabel.grid(row=4,column=0)
odpor_auta = Entry(root)
odpor_auta.grid(row=5, column=0)

PotopiLabel = Label(root, text="4. Za jak dlouho se auto potopi?(%, default 85):")
PotopiLabel.grid(row=4, column=2)
potop_auta = Entry(root)
potop_auta.grid(row=5,column=2)

SpaceLabel2 = Label(root, text="", bg='#474747')
SpaceLabel2.grid(row=6)

def isChecked():
    if predokolka.get() == 1:
	nahon = ""1.000000\""
    elif zadokolka.get() == 1:
	nahon = ""0.000000\""
	elif ctyrkolka.get() == 1:
	nahon = ""0.500000\""
	elif predokola.get() == 1 and zadokolka.get() == 1 and ctyrkolka.get() == 1:
	print("Vyberte prosím jen jednu možnost!")

predokolka = intVar()
zadokolka = intVar()
ctyrkolka = intVar()

nahonLabel = Label(root, text="5. Jaký náhon má vozidlo ? (Přední, zadní, 4kolka)")
nahonLabel.grid(row=7,column=1)
Checkbutton(root, text="Předokolka", onvalue=1, offvalue=0, command=isChecked).pack()
Checkbutton(root, text="Zadokolka", onvalue=1, offvalue=0, command=isChecked).pack()
Checkbutton(root, text="Čtyřkolka", onvalue=1, offvalue=0, command=isChecked).pack()


def Click():
    file1.writelines("<handlingName>" + name_auta.get() + "</handlingName>\n")
    file1.writelines("<fMass value=\"" + vaha_auta.get() + ".000000\"" + " />\n")
    file1.writelines("<fInitialDragCoeff value="" + odpor_auta.get() + ".000000"" + " />\n")
    file1.writelines("<fPercentSubmerged value="" + potop_auta.get() + ".000000"" + " />\n")
	file1.writelines("<fDriveBiasFront value=" + nahon.get() + " />\n"
    file1.close() #uzavře soubor

Yobutton = Button(root, text="Uložit Handling", command=Click)
Yobutton.grid(row=6,column=1)

root.mainloop()
