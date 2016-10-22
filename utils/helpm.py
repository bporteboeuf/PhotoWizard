#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This module generates various help messages in the shell



def help(matter,language): # Matter indicates the matter on which the user needs help, language indicates the language to use

    if str(language) == "EN" :
        if matter == "idle":
            hmess = "This image editing software is still at an early stage development. More functionalities are to come soon."
        else:
            hmess = "Help"
    elif str(language) == "FR" :
        hmess = "Aide"
    elif str(language) == "DE" :
        hmess = "Hilfe"
    elif str(language) == "JA" :
        hmess = "Tasuketekure"
    else :
        raise NameError('PhotoWizard Error: Unsupported language')
    

    return hmess



