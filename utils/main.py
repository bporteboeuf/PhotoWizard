# -*- coding: utf-8 -*-

#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#


# This script is the main function for the command line version of the software

import sys,os
sys.path.insert(0,'utils/')

import display,helpm,mapping,loadConfig
from PIL import Image
from picture import Picture
from tools import *



def main(args,testmode):

    # We first check wether it has been launched in test mode or not
    try:
        testmode = bool(testmode)
        args = list(args)
    except:
        raise NameError('PhotoWizard Error: wrong argument type in main')

    # We then try to load the configuration file, which handles all default settings
    try:
        loadConfig.load()
    except Exception as e:
        print(e)


    if testmode: 
        # We invert our args for easier access
        args = args[::-1]
    else:
        display.greetings(loadConfig.LANG)


    # Initialization
    quitFlag = False
    First = True

    images = {}
    files = []
    ID_max = 0
    current = ""

    while not quitFlag:
        
        if testmode:
            try:
                request = str(args.pop()) # We get our next request
                print(request)
            except:
                request = ''
        else:
            if First : # The first action displays a small helping message
                #action = str(getInput(display.action(loadConfig.LANG)))
                try:
                    request = str(getInput("\n   h - help      q - quit\n\n > "))
                except:
                    request = ""
                    next
                First = False
            else: # Normal use, we try to get the user's input
                try:
                    request = str(getInput(' > '))
                except:
                    request = ""
                    next
        

        tries = 0
        ok = False
        while not ok: # ie while the input can not be properly understood
            
            ok = True
        
            #print('ACTIONS: ',args[::-1])
            #print('REQUEST: ',request)

     
            # First, we try to understand which function or module the user wants to call
            requestList = request.split(' ')
            action = requestList[0]

            helped = False
            try: # And we look if any help is needed, in which case a help message is displayed and no action is executed
                params = requestList[1]
                if (str(params) == '-h') or (str(params) == '--help'):
                    display.disp(helpm.help(action,loadConfig.LANG))
                    helped = True
            except Exception as e:
                #print(e)
                pass
            

            #print(request)

            if not helped:
                # And we act accordingly

                # Here is a switch for the actions that are linked to the main in itself (such as the files management for instance)

                if action == "h" or action == "help":
                    display.disp(helpm.help("idle",loadConfig.LANG))
                
                elif action == "q" or action == "quit":
                    if len(files) > 0:
                        for elt in files:
                            images[elt].close()
                            del images[elt]
                    quitFlag = True
                
                elif action == "open":
                    try:
                        fileName = parseInput(request,[str,str])
                        fileName = fileName[1]
                        if fileName not in files:
                            #print("Opening "+str(fileName))
                            ID_max += 1
                            images[fileName] = Picture(ID_max,fileName) # We create a new object
                            files.append(fileName)
                            current = fileName
                            #print(str(fileName) + ' opened\n')
                            display.dispm('open',fileName,loadConfig.LANG)
                        else:
                            current = fileName
                            print('PhotoWizard Error: '+str(fileName)+' is already opened. Switched to '+str(fileName)+'\n')
                    except Exception as e:
                        print(e)
                        ok = False
                        print('PhotoWizard Error: Unable to open '+str(fileName))
                
                elif action == "close":
                    try:
                        fileName0 = parseInput(request,[str,str])
                        fileName0 = fileName0[1]
                        if fileName0 == 'ALL': # We close all opened files
                            fileName = list(files)
                        else:
                            fileName = [fileName0]
                       
                        for elt in fileName:
                            #print("Closing "+str(fileName))
                            images[elt].close()
                            del images[elt] # The object is deleted
                            files.remove(elt)
                            if (len(files) > 0) and len(fileName) == 1: # There are still some files opened and we are not closing them all
                                nextFile = files[len(files)-1]
                                display.dispm('close',elt,loadConfig.LANG)
                                display.dispm('switch',str(nextFile),loadConfig.LANG)
                                #print(str(fileName)+' closed; switching to '+str(nextFile)+'\n')
                                current = nextFile
                            else:
                                #print(str(fileName)+' closed\n')
                                display.dispm('close',elt,loadConfig.LANG)
                                current = ''
                    
                    except Exception as e:
                        #print(e)
                        ok = False
                        print('PhotoWizard Error: Unable to close '+str(fileName0)+'\n')
                
                elif action == "opened":
                    try:
                        filesList = ', '.join(files)
                        filesList += ' - '+str(current)
                        display.dispm('opened',filesList,loadConfig.LANG)
                    except Exception as e:
                        print(e)
                        ok = False
                        print('PhotoWizard Error: Unable to display opened files list')

                elif action == "load":
                    try:
                    
                        fileName = parseInput(request,[str,str])
                        fileName = str(fileName[1])
                        
                        if current == '':
                            raise NameError('PhotoWizard Error: No picture opened')
                        
                        #print("Loading XMD file "+str(fileName))
                        h = images[current].getHistory()
                        h.rebase(0) # We start by restoring the history to its initial state
                        h = loadXMD(fileName,h) # Then we load the XMD file as a new history branch               
                        images[current].setHistory(h) # We update the history
                        images[current].reCompute() # And we update the working copy for faster preview
                        #print('XMD file '+str(fileName)+' loaded\n')
                        display.dispm('load',fileName,loadConfig.LANG)
                    except Exception as e:
                        print(e)
                        ok = False
                        print('PhotoWizard Error: Unable to load '+str(fileName))

                elif action == "save":
                    try:
                        
                        fileName = parseInput(request,[str,str])
                        fileName = fileName[1]
                        
                        if current == '':
                            raise NameError('PhotoWizard Error: No picture opened')
                        
                        #print("Saving xmd file "+str(fileName))
                        saveXMD(fileName,images[current].getHistory())
                        #print('XMD file saved to '+str(fileName)+'\n')
                        display.dispm('save',fileName,loadConfig.LANG)
                    except Exception as e:
                        print(e)
                        ok = False
                        print('PhotoWizard Error: Unable to save file '+str(fileName))
                
                elif action == "export":
                    try: 
                        
                        fileName = parseInput(request,[str,str])
                        fileName = fileName[1]

                        if current == '':
                            raise NameError('PhotoWizard Error: No picture opened')
                        
                        #print("Exporting "+str(fileName))
                        images[current].export(fileName)
                        #print(str(fileName)+' exported\n')
                        display.dispm('export',fileName,loadConfig.LANG)
                    except Exception as e:
                        print(e)
                        ok = False
                        print('PhotoWizard Error: Unable to export '+str(fileName))

                elif action == "switch":
                    try:
                        fileName = parseInput(request,[str,str])
                        fileName = fileName[1]

                        if fileName in files:
                            current = fileName
                            #print("Switched to "+str(fileName))
                            display.dispm('switch',fileName,loadConfig.LANG)
                        else:
                            print('PhotoWizard Error: no such file opened')
                    except Exception as e:
                        print(e)
                        ok = False
                        print('PhotoWizard Error: Unable to switch to '+str(fileName)+'\n')

                elif action == "histogram":
                    try: 

                        if current == '':
                            raise NameError('PhotoWizard Error: No picture opened')
                        
                        channel = parseInput(request,[str,str])
                        channel = channel[1]
                        #print("Histogram")
                        H = images[current].histogram(channel) # This returns a normalized histogram, covering a square of 256 by 256
                        #print(H)
                        for elt in H:
                            for k in range(0,11):
                                s = ''
                                for el in elt:
                                    if int(el) > round(255*(9-k)/10) and k != 10 :
                                        s += '#'
                                    elif k != 10:
                                        s += ' '
                                    else:
                                        s += '-'
                                print(s)
                    except Exception as e:
                        print(e)
                        ok = False
                        print('PhotoWizard Error: Unable to preview histogram')
                
                elif action == "preview":
                    try: 

                        if current == '':
                            raise NameError('PhotoWizard Error: No picture opened')
                        
                        parseInput(request,[str])
                        #print("preview")
                        images[current].preview()
                    except Exception as e:
                        print(e)
                        ok = False
                        print('PhotoWizard Error: Unable to preview picture')
                
                elif action == "undo":
                    try: 

                        if current == '':
                            raise NameError('PhotoWizard Error: No picture opened')
                        
                        parseInput(request,[str])
                        #print("undo")
                        h = images[current].getHistory()
                        h.undo()
                        images[current].setHistory(h)
                        images[current].reCompute()
                        #print('Last action revoked')
                        display.dispm('undo','',loadConfig.LANG)
                    except Exception as e:
                        print(e)
                        ok = False
                        print('PhotoWizard Error: Unable to undo action')

                elif action == "redo":
                    try: 

                        if current == '':
                            raise NameError('PhotoWizard Error: No picture opened')
                        
                        parseInput(request,[str])
                        #print("redo")
                        h = images[current].getHistory()
                        h.redo()
                        images[current].setHistory(h)
                        images[current].reCompute()
                        #print('Last action restored')
                        display.dispm('redo','',loadConfig.LANG)
                    except Exception as e:
                        print(e)
                        ok = False
                        print('PhotoWizard Error: Unable to redo action')

                elif action == "rebase":
                    try: 

                        event = parseInput(request,[str,int])
                        event = event[1]
                        
                        if current == '':
                            raise NameError('PhotoWizard Error: No picture opened')
                        
                        #print(rebase)
                        h = images[current].getHistory()
                        h.rebase(event)
                        images[current].setHistory(h)
                        images[current].reCompute()
                        #print('History rebased to event '+str(event))
                        display.dispm('rebase',str(event),loadConfig.LANG)
                    except Exception as e:
                        print(e)
                        ok = False
                        try:
                            event = request.split(' ')
                            event = event[1]
                            print('PhotoWizard Error: Unable to rebase history to event '+str(event))
                        except:
                            print('PhotoWizard Error: Unable to rebase history')

                elif action == "history": # Displays the current history
                    try:

                        if current == '':
                            raise NameError('PhotoWizard Error: No picture opened')
                        
                        parseInput(request,[str])
                        print("History:")
                        print(images[current].getHistory().getFullHistory())
                    except Exception as e:
                        print(e)
                        ok = False
                        print('PhotoWizard Error: Unable to preview history')



                else: # We assume the wanted module is not part of the main functions and try to access it with our modules mapping function: everyFunction
                    
                    try:
                       
                        if current == '':
                            raise NameError('PhotoWizard Error: No picture opened')
                        
                        # We try to compute the resized copy of the picture
                        function = action
                        # The action is mapped to the proper image processing modules
                        img,parameters = mapping.everyFunction(images[current].getSmallImage(),[function,request],images[current].getScaling())
                        images[current].setSmallImage(img) # We update the working copy
                        h = images[current].getHistory()
                        h.add(request,function)
                        images[current].setHistory(h) # And we update the history
                        display.dispm('actionCompleted','',loadConfig.LANG)
                        
                    except Exception as e:
                        print(e)
                        ok = False
                        print("PhotoWizard Error: Unexpected input value")

                if not ok:
                    try:
                        if not testmode: # We ask the user to try again
                            if tries > 3:
                                request = str(getInput(helpm.help("idle",loadConfig.LANG)+'\n > ')) # A help message is displayed
                            else:
                                request = str(getInput(' > '))
                            tries += 1
                        else: # We pass and move on to the next request for automatic test
                            request = ''
                            ok = True
                    except:
                        request = ''
                        ok = True


    if not testmode:
        display.bye(loadConfig.LANG)    
        
    return



if __name__=="__main__":
    main('',False)


