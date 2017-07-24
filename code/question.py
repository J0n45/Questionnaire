from tkinter import *
"""
Question speichert den Text und die Felder einer Frage
Kann auch als Hinweis benutzt werden
"""
class Question:
    def __init__(self,ftext,htext):
        self.felder = []
        
        self.ftexte = self.parse_ftext(ftext)
        self.antworten = []
        self.htext= [htext]
    
    #Zerteilt den Text zwischen den Eingabefeldern
    #ruft parse_felder auf
    def parse_ftext(self, ftxt):
        ret = [""]
        i =0
        c=0
        while i < len(ftxt):
            if ftxt[i] == "[":
                i = self.parse_felder(i,ftxt)
                ret.append("")
                c = c+1
            else:
                ret[c] += ftxt[i]
            i=i+1
        return ret
    
    #Ließt ein Eingabe feld ein und speichert es
    def parse_felder(self,i,ftxt):
        feld=""
        i=i+1
        while ftxt[i] != "]" :
            feld=feld+ftxt[i]
            i=i+1
        self.felder.append(feld)
        return i
    
    def get_fragentexte(self,w):
        return self.get_text(w,self.ftexte)
    def get_hinweistext(self,w):
        return self.get_text(w,self.htext)
    
    def alle_antworten_ka(self):
        self.antworten = ["k.A." for x in range(len(self.felder))]
    
    #gibt den text in eine liste unterteilt zurück
    #und fügt \n ein wenn die Zeile zu groß ist
    def get_text(self,w,texte):
        ret = []
        c= w//5 -10 #größer ist eine Zeile nicht
        for t in texte:
            if len(t)<c:
                ret.append(t)
                continue
            tmp = [] #solange es größer ist zertrennen
            while len(t) > c:
                cc = c
                while t[cc] != " ":
                    cc = cc-1 #findet das leerzeichen an dem es trennt
                tmp.append(t[0:cc])
                t=t[cc:len(t)]
            tmp.append(t)
            t=""
            for s in tmp:
                t=t+"\n"+s
            ret.append(t)
        return ret