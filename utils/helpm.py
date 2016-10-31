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
            hmess += "\nTo switch between two opened images, simply type switch [filePath]. You can save your changes by typing save [fileName] and load previous changes by typing load [filePath]."
            hmess += " You can also export your final images using the export [fileName] command."
            hmess += "\nAn histogram can be displayed thanks to the histogram command, and a preview pop-up window appears with the preview command."
            hmess += "\n\nYou can have more informations on how to use the functionalities by typing [moduleName] -h or [moduleName] --help."
            hmess += "\n\nList of modules availables:\n\n"
            hmess += " -*- ".join(["blur","sharpen","enhanceedges","levels","curves","contrast","exposition","edges","blackandwhite","histogram","preview","history"])
            hmess += "\n"
        else:
            hmess = "Help"
    elif str(language) == "FR" :
        hmess = "Aide"
    elif str(language) == "DE" :
        hmess = "Hilfe"
    elif str(language) == "JA" :
        hmess = "てつだいましょうか？"
    else :
        raise NameError('PhotoWizard Error: Unsupported language')
    

    return hmess



