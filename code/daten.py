from tkinter import *

class Daten:
    
    def __init__(self,saver, fragen):
        self.window = Tk() #fenster erstellen
        self.bgcolor ="#EEEEEE"
        self.saver=saver
        self.fragen=fragen
        self.antworten = [[] for x in range(len(fragen)//2+1)]
        
    
    def add_lfs(self,lf_l,lf_r):
        self.lf_l = lf_l
        self.lf_r = lf_r
    def add_gui(self,gui):
        self.gui = gui
    def add_window(self,w):
        self.window = w
    def add_fbogen(self,f):
        self.fbogen = f