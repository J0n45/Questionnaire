from tkinter import *
import gui
import speichern
"""
Steuert wie die nächste Frage angezeigt wird
TODO: Fragen Bedingungen
"""
class Ablauf:
    def __init__(self, dat):
        self.dat=dat
        self.height=dat.window.winfo_height()-35
        self.width=(dat.window.winfo_width()//2)-10
        self.pct=0
    
    #passt neu die proportionen an
    def update_wh(self, w,h):
        self.width=(w//2)-10
        self.height=h-35
    
    #schaltet auf die nächste frage
    def next(self):
        antworten=self.dat.antworten
        fragen=self.dat.fragen
        saver=self.dat.saver
        gui=self.dat.gui
        if len(fragen) > 2*self.pct:
            self.pct+=1
            gui.neue_fragen(self.dat.lf_l,self.dat.lf_r, self.width, self.height,
                            fragen[2*self.pct-2],fragen[2*self.pct-1],
                            antworten[self.pct-1])
            saver.write_all(antworten[1:])
        else:
            gui.get_antworten(antworten[len(antworten)-1],self.dat.lf_l)
            saver.write_all(antworten[1:])
            saver.save()
