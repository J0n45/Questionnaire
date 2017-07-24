import question
import topquestion

'''
Ein Questionblock enthält eine topfrage und mehrere unterfragen
in der topfrage sind spezielle ja|nein felder ([||]) die bestimmen ob unterfragen angezeigt werden
'''
class QuestionBlock:
    
    def __init__(self,ftext,htext):
        self.questions = []
        self.topfrage = topquestion.Topquestion(ftext,htext)
        self.feldtoquestion = self.topfrage.welche_felder()
        self.fragencounter = -1
    
    # Fuegt eine neue frage in die frageliste hinzu
    def add(self,question):
        self.questions.append([True,question])
    
    def hasnext(self):
        if self.fragencounter < len(self.questions):
            return True
        return False
    
    #stellt die naechste frage graphisch daten
    #überspringt fragen mit false
    #returnt False wenn es danach keine Fragen mehr gibt. sonst True
    def neue_frage(self, daten, width, height):
        self.fragencounter+=1
        lf_l = daten.lf_l
        lf_r = daten.lf_r
        gui = daten.gui
        #fier den falls dass topfrage angezeigt werden soll
        if self.fragencounter == 0: 
            (display, question) = True,self.topfrage
        else:
            (display, question) = self.questions[self.fragencounter-1]
        # entscheiden ob anzeigen oder naechste frage oder abbruch
        if display: 
            gui.neue_fragen(lf_l, lf_r, width, height, question)
        elif (not display) and self.hasnext():
            return self.neue_frage(daten,width,height)
        else:
            return False
        return True
    
    #holt die antworten zu der derzeitigen Frage aus gui
    #und falls es die topfrage war raussuchen welche der anderen fragen angezeigt werden
    def collect_antworten(self,gui, lf_l):
        t,question = True,self.topfrage
        if self.fragencounter > 0:
            t,question = self.questions[self.fragencounter-1]
        if t:
            gui.get_antworten(question.antworten,lf_l)
        
        #wenn antworten von topfrage eingesammelt wurden
        #wird festgelegt welche fragen nicht angezeigt werden
        if self.fragencounter == 0:
            for feld,frage in self.feldtoquestion:
                if self.topfrage.antworten[feld] == "Nein" or self.topfrage.antworten[feld] == "k.A." :
                    self.questions[frage][0] = False
                    self.questions[frage][1].alle_antworten_ka()
    
    #speichert alle antworten aus allen fragen in saver
    def save_all_antworten(self,saver):
        allquestions = [(True,self.topfrage)]+self.questions
        for t,q in allquestions:
            print(q.ftexte[0][:10], q.antworten)
            saver.save_antworten(q.antworten)