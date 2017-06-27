import frage
"""
ließt aus ..\Fragen.txt die fragen ein
 Syntax:
    # - Kommentar (Anfang der Zeile)
    
    ${ 
    ... - Beinhaltet Fragentext
    }{
    ... - Beinhaltet Hinweistext
    } 
    
    [ #Zeichen : #Zeilen ] - Textfeld (standart = 30:1)
    [ ... | ... ] - Ja-Nein Buttons (links rechts Text für Button. Default [|] ist Ja-Nein)
"""

#ließt solange fragen bis die Datei leer ist
def fragen_einlesen(fname):
    fragenf = open(fname, "r")
    flist = []
    for line in fragenf:
        if line.startswith("#"):
            continue
        if line.startswith("$"):
            flist.append(read_question(fragenf))
            flist.append(read_hinweis(fragenf))
    #for f in flist:
    #    print(f.get_texte(500))
    return flist

#ließt einen hinweis ein
def read_hinweis(fragenf):
    htext=""
    for line in fragenf:
        l=line.strip()
        if l=="}":
            break
        htext += "\n" +l
    return frage.Frage(-1,htext.strip('\n'))

#liest eine Frage ein
def read_question(fragenf):
    fragentext=""
    for line in fragenf:
        l=line.strip()
        if l=="}{":
            break
        fragentext += "\n" +l
    return frage.Frage(1,fragentext.strip('\n'))