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
    
    try:
        language = str(language)
    except:
        raise NameError('PhotoWizard Error: Wrong argument type in greetings')
        language = ''

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
        
    try:
        language = str(language)
    except:
        raise NameError('PhotoWizard Error: Wrong argument type in bye')
        language = ''

    if str(language) == "EN" :
        string = "\n\n    S E E   Y O U   S O O N\n\n"
    elif str(language) == "FR" :
        string = "\n\n       À   B I E N T Ô T\n\n"
    elif str(language) == "DE" :
        string = "\n\n        T C H Ü S S\n\n"
    elif str(language) == "JA" :
        string = "\n\n        さ よ な ら\n\n"
    else :
        raise NameError('PhotoWizard Error: Unsupported language')
 
    disp(string)

    return



def dispm(state,args,language): # Displays informations relative to a state or function in the desired language

    try:
        state = str(state)
        args = str(args)
        language = str(language)
    except:
        raise NameError('PhotoWizard Error: Wrong argument type in dispm')
        state = ''
        language = ''

    # MainFunction
    if state == 'open':
        if language == 'EN':
            disp(args+' opened')
        elif language == 'FR':
            disp(args+' ouvert')
        elif language == 'DE':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        elif language == 'JA':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        else:
            raise NameError('PhotoWizard Error: Unsupported language')
    
    elif state == 'close':
        if language == 'EN':
            disp(args+' closed')
        elif language == 'FR':
            disp(args+' fermé')
        elif language == 'DE':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        elif language == 'JA':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        else:
            raise NameError('PhotoWizard Error: Unsupported language')
     
    elif state == 'export':
        if language == 'EN':
            disp(args+' exported')
        elif language == 'FR':
            disp(args+' exporté')
        elif language == 'DE':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        elif language == 'JA':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        else:
            raise NameError('PhotoWizard Error: Unsupported language')
      
    elif state == 'load':
        if language == 'EN':
            disp('XMD file '+args+' loaded')
        elif language == 'FR':
            disp('Fichier XMD '+args+' chargé')
        elif language == 'DE':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        elif language == 'JA':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        else:
            raise NameError('PhotoWizard Error: Unsupported language')
   
    elif state == 'save':
        if language == 'EN':
            disp('XMD file saved to '+args)
        elif language == 'FR':
            disp('Fichier XMD sauvegardé vers '+args)
        elif language == 'DE':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        elif language == 'JA':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        else:
            raise NameError('PhotoWizard Error: Unsupported language')
     
    elif state == 'switch':
        if language == 'EN':
            disp('Switched to '+args)
        elif language == 'FR':
            disp(args+' sélectionné')
        elif language == 'DE':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        elif language == 'JA':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        else:
            raise NameError('PhotoWizard Error: Unsupported language')
     
    elif state == 'undo':
        if language == 'EN':
            disp('Last action revoked')
        elif language == 'FR':
            disp('Dernière action annulée')
        elif language == 'DE':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        elif language == 'JA':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        else:
            raise NameError('PhotoWizard Error: Unsupported language')
     
    elif state == 'redo':
        if language == 'EN':
            disp('Last action restored')
        elif language == 'FR':
            disp('Dernière action rétablie')
        elif language == 'DE':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        elif language == 'JA':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        else:
            raise NameError('PhotoWizard Error: Unsupported language')
     
    elif state == 'rebase':
        if language == 'EN':
            disp('History rebased to '+args)
        elif language == 'FR':
            disp('Historique rebasé sur '+args)
        elif language == 'DE':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        elif language == 'JA':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        else:
            raise NameError('PhotoWizard Error: Unsupported language')
    
    # EveryFunction
    elif state == 'actionCompleted':
        if language == 'EN':
            disp('Done')
        elif language == 'FR':
            disp('Terminé')
        elif language == 'DE':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        elif language == 'JA':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        else:
            raise NameError('PhotoWizard Error: Unsupported language')
    
    
    else:
        raise NameError('PhotoWizard Error: Unknown state in dispm')
    
    return




if __name__=="__main__":
    greetings()
