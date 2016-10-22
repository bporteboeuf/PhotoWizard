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



def greetings(): # Displays welcoming message

    string = "\n\n#/////////////////////////////#\n# - P H O T O   W I Z A R D - #\n#/////////////////////////////#\n\n        W E L C O M E\n"
    disp(string)

    return




def bye(): # Displays message before quiting

    string = "\n\n    S E E   Y O U   S O O N\n\n"
    disp(string)

    return




if __name__=="__main__":
    greetings()
