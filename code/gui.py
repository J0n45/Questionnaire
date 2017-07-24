from tkinter import *
"""
Regelt alles graphische
"""
class Gui:
    def __init__(self,dat):
        self.window=dat.window
        self.dat=dat
        
        nxp=Button(self.window, text="Start") #Button für nächste frage hinzufügen
        nxp.configure(command = lambda: nextPage(nxp, self.window, dat))
        nxp.pack(side=BOTTOM)
        
        lf_l,lf_r = self.fenster_erstellen(600,850,dat.bgcolor)
        self.dat.add_lfs(lf_l,lf_r)
        self.rbval = [] #für antworten von radio buttons

    #erstellt fenster mit scrollbar un MenuBar
    def fenster_erstellen(self,height,width,bgc):
        
        window = self.window ; saver=self.dat.saver
        window.title("Questionnaire")
        window.protocol("WM_DELETE_WINDOW", lambda: winbeenden(window))
        window.configure(background=bgc)
    
    
        # MENUBAR ERSTELLEN #
        ########TODO: Menubar verschönern, erweitern (eigene Klasse?)
        menubar=Menu(window)
        
        dateimenu=Menu(menubar, tearoff=0)
        dateimenu.add_command(label="Neu")
        dateimenu.add_command(label="Speichern",command=saver.save)
        dateimenu.add_command(label="Oeffnen")
        dateimenu.add_separator()
        dateimenu.add_command(label="Beenden", command=lambda: winbeenden(window))
        menubar.add_cascade(label="Datei", menu=dateimenu)
        
        window.config(menu=menubar)
        
        ##### Mainframe mit Scrollbar hinzufuegen #####
        underframe1 = Frame(window, background=bgc,width=width, height=height)
        underframe1.pack_propagate(0)
        underframe1.pack(side="left", fill="both")
        
        canvas_l = Canvas(underframe1, borderwidth=0, background=bgc)
        canvas_r = Canvas(underframe1, borderwidth=0, background=bgc)
        frame_l = Frame(canvas_l, background=bgc,width=(width//2)-10, height=height-35)
        frame_r = Frame(canvas_r, background=bgc,width=(width//2)-10, height=height-35)
        vsb = Scrollbar(window, orient="vertical", command=lambda canvas_l, canvas_r: view(canvas_l,canvas_r))
        canvas_l.configure(yscrollcommand=vsb.set)
        canvas_r.configure(yscrollcommand=vsb.set)
        
        def on_mousewheel(event):
            canvas_l.yview_scroll(-1*(event.delta//120), "units")
            canvas_r.yview_scroll(-1*(event.delta//120), "units")
        
        canvas_l.bind_all("<MouseWheel>", on_mousewheel)
        canvas_r.bind_all("<MouseWheel>", on_mousewheel)
        
        
        vsb.pack(side="right", fill="y")
        canvas_l.pack(side="left",fill="both", expand=True)
        canvas_r.pack(side="right",fill="both", expand=True)
        canvas_l.create_window((4,4), window=frame_l, anchor="nw")
        canvas_r.create_window((4,4), window=frame_r, anchor="nw")
        
        frame_l.bind("<Configure>", lambda event, canvas=canvas_l: onFrameConfigure(canvas_l))
        frame_r.bind("<Configure>", lambda event, canvas=canvas_r: onFrameConfigure(canvas_r))
        
        return frame_l,frame_r
    
    
    def get_antworten(self,antworten,frame_l):
        if self.rbval==[]: return
        widgs = frame_l.winfo_children()
        i=0
        while i < len(widgs):
            widget = widgs[i]
            if widget.winfo_class() == 'Text': 
                text = widget.get("1.0",END).strip("\n")
                if text == "": antworten.append("k.A.")
                else: antworten.append(text)
            elif widget.winfo_class() == "Radiobutton":
                if self.rbval[0].get() == int(widget.cget("value")):
                    antworten.append(widget.cget("text"))
                elif self.rbval[0].get() == int(widgs[i+1].cget("value")):
                    antworten.append(widgs[i+1].cget("text"))
                else:
                    antworten.append("k.A.")
                i+=1
                self.rbval=self.rbval[1:]
            i+=1


    #löscht alte fragen und fügt eine neue ein
    def neue_fragen(self,frame_l,frame_r,width,height,question):
        bgc=self.dat.bgcolor
        
        for child in frame_l.winfo_children()+frame_r.winfo_children():
            child.destroy()
        
        self.rbval = []
        #Die Labelframes mit Text füllen (durch Labels)
        self.add_label(frame_l,question.get_fragentexte(width),question.felder,bgc,width)
        self.add_label(frame_r,question.get_hinweistext(width),[],bgc,width)
        
    #von neue_fragen aufgerufen
    #fügt die texte und die Eingabefelder ein
    def add_label(self,frame, texte, felder,bgc,width):
        for i in range(0,len(texte)):
            lbl = Label(frame,text=texte[i],bg=bgc).pack()
            if i< len(felder):
                self.add_feld(frame,felder[i],bgc)
    
    #aufgerufen von add_label
    # fügt die eingabefelder ein
    def add_feld(self,frame,feld,bgc):
        if ':' in feld:
            [w,h] = ["30","1"]
            if feld != ":":
                [w,h] = feld.split(':', 2)
            t=Text(frame,width=int(w),height=int(h))
            t.pack()
            
        elif "|" in feld :
            [l,r] = ["Ja","Nein"]
            if feld != "|" and feld != "||":
                [l,r] = feld.split('|', 2)
            var = IntVar()
            self.rbval.append(var)
            R1 = Radiobutton(frame, text=l, variable=var, value=1,bg=bgc)
            R2 = Radiobutton(frame, text=r, variable=var, value=2,bg=bgc)
            R1.pack()
            R2.pack()


#nächste seite aufrufen
def nextPage(nxp, window, dat):  #wechselt die Seite des Fragebogens
    nxp.configure(text = "Next")
    dat.fbogen.update_wh(window.winfo_width(),window.winfo_height())    
    dat.fbogen.next()

#schließt fenster
def winbeenden(window): # Methode fuer 'Beenden' 
    window.destroy()

def onFrameConfigure(canvas):
    #Reset the scroll region to encompass the inner frame
    canvas.configure(scrollregion=canvas.bbox("all"))

def view(c1,c2):
    c1.yview()
    c2.yview()
    
