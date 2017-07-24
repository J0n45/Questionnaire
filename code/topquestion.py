from question import Question


class Topquestion(Question):
    
    def __init__(self,ftext,htext):
        super().__init__(ftext,htext)
    
    #gibt zurück welche felder welche unterfragen codieren
    def welche_felder(self):
        out = []
        for i in range(len(self.felder)):
            feld = self.felder[i]
            if feld.startswith("|") and len(feld) > 1:
                # (feld , welche frage betroffen)
                out.append((i,int(feld[1:-1])))
                self.felder[i] = "||"
        return out