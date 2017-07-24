import question, questionblock
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
def qblocks_einlesen(fname):
    fragenf = open(fname, "r")
    qblocks = []
    for line in fragenf:
        if line.startswith("#"):
            continue
        if line.startswith("${"):
            qblock = read_questionblock(fragenf)
            qblocks.append(qblock)
    #for f in qblocks:  #zum testen
    #    print(f.topfrage.get_texte(1000))
    #    for (t,fg) in f.questions:
    #        print("         ->"+str(fg.get_texte(1000)))
    return qblocks

#ließt einen hinweis ein
def read_hinweis(fragenf):
    htext=""
    for line in fragenf:
        l=line.strip()
        if l=="}":
            break
        htext += "\n" +l
    return htext.strip('\n')

#liest eine Fragenabschnitt ein von $ umkreist
def read_questionblock(fragenf):
    ftext = read_question(fragenf)
    htext = read_hinweis(fragenf)
    qb = questionblock.QuestionBlock(ftext,htext)
    
    for line in fragenf:
        l=line.strip()
        if l=="$":
            break
        if line.startswith("#"):
            continue
        if line.startswith("{"):
            ftext = read_question(fragenf)
            htext = read_hinweis(fragenf)
            qb.add(question.Question(ftext,htext))
    return qb
    
#liest eine Frage ein
def read_question(fragenf):
    fragentext=""
    for line in fragenf:
        l=line.strip()
        if l=="}{":
            break
        fragentext += "\n" +l
    return fragentext.strip('\n')