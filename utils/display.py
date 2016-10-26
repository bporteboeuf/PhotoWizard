#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This module displays various contents in the shell




def disp(message): # Displays message
    try:
        message = str(message)
    except:
        raise NameError('PhotoWizard Error: Cannot display a non str type object')
        
    print(message)

    return



def greetings(language): # Displays welcoming message
    
    if str(language) == "EN" :
        string0 = "        W E L C O M E\n"
    elif str(language) == "FR" :
        string0 = "      B I E N V E N U E\n"
    elif str(language) == "DE" :
        string0 = "      W I L K O M M E N\n"
    elif str(language) == "JA" :
        string0 = "            歓迎\n"
    else :
        raise NameError('PhotoWizard Error: Unsupported language')
 
    string = "\n\n#/////////////////////////////#\n# - P H O T O   W I Z A R D - #\n#/////////////////////////////#\n\n"+string0
    disp(string)

    return




def bye(language): # Displays message before quiting
    
    if str(language) == "EN" :
        string = "\n\n    S E E   Y O U   S O O N\n\n"
    elif str(language) == "FR" :
        string = "\n\n       A   B I E N T O T\n\n"
    elif str(language) == "DE" :
        string = "\n\n        T C H U S S\n\n"
    elif str(language) == "JA" :
        string = "\n\n        さ よ な ら\n\n"
    else :
        raise NameError('PhotoWizard Error: Unsupported language')
 
    disp(string)

    return




if __name__=="__main__":
    greetings()
