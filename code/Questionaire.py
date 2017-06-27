from tkinter import *
import reader, ablauf, speichern, gui, daten

#Ausfueren:  U:\locallib\Python3\python.exe Questionaire.py

def main():
    fragen = reader.fragen_einlesen("..\Fragen.txt") #fragen einlesen und fragebogen erstellen
    saver = speichern.Save("..\Daten\Out-test.xlsx")
    dat = daten.Daten(saver, fragen)
    
    g = gui.Gui(dat)
    dat.add_gui(g)
    
    fbogen = ablauf.Ablauf(dat)
    dat.add_fbogen(fbogen)
    
    dat.window.mainloop()

if __name__ == "__main__":
    main()
