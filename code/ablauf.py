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
        self.blockcounter=0
    
    #passt neu die proportionen an
    def update_wh(self, w,h):
        self.width=(w//2)-10
        self.height=h-35
    
    #schaltet auf die nächste frage
    def next(self):
        qblocks=self.dat.qblocks
        lf_l=self.dat.lf_l
        saver=self.dat.saver
        gui=self.dat.gui
        
        #wenn alle fragen durch sind die antworten speichern
        if len(qblocks) <= self.blockcounter:
            saver.reset_antworten()
            for q in qblocks:
                q.save_all_antworten(saver)
            saver.save()
            return
        
        #wenn noch fragen uebrig sind:
        # entweder im block die naechste frage oder ein neuer block
        qblock = qblocks[self.blockcounter]
        if qblock.hasnext():
            if qblock.fragencounter != -1:
                qblock.collect_antworten(gui,lf_l)
            someleft = qblock.neue_frage(self.dat, self.width, self.height)
            if not someleft:
                self.blockcounter+=1
                self.next()
        else:
            qblock.collect_antworten(gui, lf_l)
            self.blockcounter+=1
            self.next()