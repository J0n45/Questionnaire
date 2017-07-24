from tkinter import *
import reader, ablauf, speichern, gui, daten

#Ausfueren:  U:\locallib\Python3\python.exe Questionaire.py
"""
Naechstes Ziel:
    Fragen können andere ueberspringen
    Auswahlfragen: enthalten ja nein fuer mehrere unterfragen
        koennen alle unterfragen mit ja zurueck geben sodass diese als naechtes angezeigt werden
    antworten werden mit ins fragenobjekt reingezogen fuer bessere objektorientierung
    
    kommt bis AM in excel
"""
def main():
    qblocks = reader.qblocks_einlesen("..\Fragen.txt") #fragen einlesen und in bloecke unterteilen
    saver = speichern.Save("..\Daten\Out-test.xlsx")
    window = Tk() #fenster erstellen
    dat = daten.Daten(saver, qblocks, window) 
    
    g = gui.Gui(dat)
    dat.add_gui(g)
    
    fbogen = ablauf.Ablauf(dat)
    dat.add_fbogen(fbogen)
    
    dat.window.mainloop() # grafik starten

if __name__ == "__main__":
    main()
