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
            disp(args+' opened\n')
        elif language == 'FR':
            disp(args+' ouvert\n')
        elif language == 'DE':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        elif language == 'JA':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        else:
            raise NameError('PhotoWizard Error: Unsupported language')
    
    elif state == 'close':
        if language == 'EN':
            disp(args+' closed\n')
        elif language == 'FR':
            disp(args+' fermé\n')
        elif language == 'DE':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        elif language == 'JA':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        else:
            raise NameError('PhotoWizard Error: Unsupported language')
    
    elif state == 'opened':
        try:
            args = args.split(' - ')
            args0 = args[0]
            args1 = args[1]
        except:
            raise NameError('PhotoWizard Error: Wrong argument format in dispm')

        if language == 'EN':
            if len(args0) == 0:
                disp('No file opened yet\n')
            else:
                disp('List of opened files: '+args0)
                disp('Current file: '+args1+'\n')
        elif language == 'FR':
            if len(args0) == 0:
                disp('Aucun fichier ouvert\n')
            else:
                disp('Liste des fichiers ouverts: '+args0)
                disp('Fichier courant : '+args1+'\n')
        elif language == 'DE':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        elif language == 'JA':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        else:
            raise NameError('PhotoWizard Error: Unsupported language')
    
    elif state == 'export':
        if language == 'EN':
            disp(args+' exported\n')
        elif language == 'FR':
            disp(args+' exporté\n')
        elif language == 'DE':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        elif language == 'JA':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        else:
            raise NameError('PhotoWizard Error: Unsupported language')
      
    elif state == 'load':
        if language == 'EN':
            disp('XMD file '+args+' loaded\n')
        elif language == 'FR':
            disp('Fichier XMD '+args+' chargé\n')
        elif language == 'DE':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        elif language == 'JA':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        else:
            raise NameError('PhotoWizard Error: Unsupported language')
   
    elif state == 'save':
        if language == 'EN':
            disp('XMD file saved to '+args+'\n')
        elif language == 'FR':
            disp('Fichier XMD sauvegardé vers '+args+'\n')
        elif language == 'DE':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        elif language == 'JA':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        else:
            raise NameError('PhotoWizard Error: Unsupported language')
     
    elif state == 'switch':
        if language == 'EN':
            disp('Switched to '+args+'\n')
        elif language == 'FR':
            disp(args+' sélectionné\n')
        elif language == 'DE':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        elif language == 'JA':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        else:
            raise NameError('PhotoWizard Error: Unsupported language')
     
    elif state == 'undo':
        if language == 'EN':
            disp('Last action revoked\n')
        elif language == 'FR':
            disp('Dernière action annulée\n')
        elif language == 'DE':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        elif language == 'JA':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        else:
            raise NameError('PhotoWizard Error: Unsupported language')
     
    elif state == 'redo':
        if language == 'EN':
            disp('Last action restored\n')
        elif language == 'FR':
            disp('Dernière action rétablie\n')
        elif language == 'DE':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        elif language == 'JA':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        else:
            raise NameError('PhotoWizard Error: Unsupported language')
     
    elif state == 'rebase':
        if language == 'EN':
            disp('History rebased to '+args+'\n')
        elif language == 'FR':
            disp('Historique rebasé sur '+args+'\n')
        elif language == 'DE':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        elif language == 'JA':
            disp('This language is not fully supported yet, please switch to EN or FR in the config file')
        else:
            raise NameError('PhotoWizard Error: Unsupported language')
    
    # EveryFunction
    elif state == 'actionCompleted':
        if language == 'EN':
            disp('Done\n')
        elif language == 'FR':
            disp('Terminé\n')
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
