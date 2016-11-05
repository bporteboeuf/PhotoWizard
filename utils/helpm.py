#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This module generates various help messages in the shell



def help(matter,language): # Matter indicates the matter on which the user needs help, language indicates the language to use

    if str(language) == "EN" :
        if matter == "idle":
            hmess = "\nThis image editing software is still at an early stage development. More functionalities are to come soon."
            hmess += "\n\nTo open an image, simply type open [filePath]."
            hmess += " You can edit it using the different functionalities implemented, such as filters, levels, and much more."
            hmess += "\nTo switch between two opened images, simply type switch [filePath]. You can save your changes by typing save [filePath] and load previous changes by typing load [filePath]."
            hmess += " You can also export your final images using the export [fileName] command."
            hmess += "\nAn histogram can be displayed thanks to the histogram command, and a preview pop-up window appears with the preview command."
            hmess += "\n\nYou can have more informations on how to use the functionalities by typing [moduleName] -h or [moduleName] --help."
            hmess += "\n\nList of modules availables:\n\n"
            hmess += " -*- ".join(["lowPass","highPass","detectEdges","enhanceEdges","levels","curves","contrast","exposure","blackandwhite","histogram","rotate","crop","resize","normHist","eqHist","expHist","logHist","preview","history"])
            hmess += "\n"
        else:
            hmess = "Help"

    elif str(language) == "FR" :
        if matter == 'idle':
            hmess = "\nCe logiciel de traitement d'images est encore au stade de développement. Plus de fonctionnalités devraient bientôt arriver."
            hmess += '\n\nPour ouvrir une image, il suffit de taper open [filePath].'
            hmess += 'Vous pouvez alors modifier l\'image à l\'aide des fonctionnalités présentes, comme des filtres, niveaux et bien plus.'
            hmess += '\nPour sélectionner l\'image de travail parmi plusieurs images ouvertes, taper switch [filePath]. Vous pouvez enregistrer les changements effectués en tapant save [filePath] et charger des changements antérieurs avec load [filePath].'
            hmess += ' Vous pouvez aussi exporter vos images en utilisant la commande export [filePath].'
            hmess += '\nUn histogramme peut être affiché en tapant histogram, et une fenêtre de prévisualisation est disponible grâce à la commande preview.'
            hmess += '\n\nPour plus d\'informations sur la façon d\'utiliser les fonctionnalités, taper [moduleName] -h ou [moduleName] --help.'
            hmess += '\n\nListe des modules disponibles:\n\n'
            hmess += ' -*- '.join(['lowPass','highPass','detectEdges','enhanceEdges','levels','curves','contrast','exposure','blackandwhite','histogram','rotate','crop','resize','normHist','eqHist','expHist','logHist','preview','history'])
            hmess += '\n'
        else:
            hmess = 'Aide'
    
    elif str(language) == "DE" :
        hmess = "Hilfe"
    elif str(language) == "JA" :
        hmess = "てつだいましょうか？"
    else :
        raise NameError('PhotoWizard Error: Unsupported language')
    

    return hmess



