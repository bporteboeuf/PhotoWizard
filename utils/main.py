#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# This script is the main function for the command line version of the software

import sys,os
sys.path.insert(0,'utils/')

import display,helpm,mapping
from PIL import Image
from picture import Picture
from config import *
from tools import *



def main(args,testmode):

    try:
        testmode = bool(testmode)
        args = list(args)
    except:
        raise NameError('PhotoWizard Error: wrong argument type in main')


    if testmode: # We disable any print message
        #f = open(os.devnull, 'w')
        #sys.stdout = f
        args = args[::-1] # And we invert our args for easier access


    display.greetings(LANG)
    quitFlag = False
    First = True

    images = {}
    files = []
    ID_max = 0
    current = ""

    while not quitFlag:
        
        if testmode:
            try:
                request = str(args.pop())
            except:
                request = ''
        else:
            if First :
                #action = str(getInput(display.action(LANG)))
                try:
                    request = str(getInput("\n   h - help      q - quit\n"))
                except:
                    request = ""
                    next
                First = False
            else:
                try:
                    request = str(getInput(""))
                except:
                    request = ""
                    next
        

        ok = False
        while not ok:
            ok = True
        
            #print('ACTIONS: ',args[::-1])
            #print('REQUEST: ',request)

     
            request = request.split(' ')
            action = request[0]
            request = ' '.join(request)

            #print(request)

            if action == "h" or action == "help":
                display.disp(helpm.help("idle",LANG))
            
            elif action == "q" or action == "quit":
                quitFlag = True
            
            elif action == "open":
                try:
                    fileName = parseInput(request,[str,str])
                    fileName = fileName[1]
                    if fileName not in files:
                        #print("Opening "+str(fileName))
                        ID_max += 1
                        images[fileName] = Picture(ID_max,fileName)
                        files.append(fileName)
                        current = fileName
                        print(str(fileName) + ' opened\n')
                    else:
                        current = fileName
                        print('PhotoWizard Error: '+str(fileName)+' is already opened. Switched to '+str(fileName)+'\n')
                except Exception as e:
                    print(e)
                    ok = False
                    print('PhotoWizard Error: Unable to open '+str(fileName))
            
            elif action == "close":
                try:
                    fileName = parseInput(request,[str,str])
                    fileName = fileName[1]
                    #print("Closing "+str(fileName))
                    images[fileName].close()
                    del images[fileName]
                    files.remove(fileName)
                    if len(files) > 0:
                           nextFile = files[len(files)-1]
                           print(str(fileName)+' closed; switching to '+str(nextFile)+'\n')
                           current = images[nextFile]
                    else:
                        print(str(fileName)+' closed\n')
                except Exception as e:
                    print(e)
                    ok = False
                    print('PhotoWizard Error: Unable to close '+str(fileName)+'\n')

            elif action == "load":
                try:
                    fileName = parseInput(request,[str,str])
                    fileName = fileName[1]
                    #print("Loading XMP file "+str(fileName))
                    h = images[current].getHistory()
                    h.rebase(1)
                    xmp = []
                    # Handling XMP files is not supported yet
                    for event in xmp:
                           h.add(event)
                    images[current].setHistory(h)
                    images[current].reCompute()
                    print('XMP file '+str(fileName)+' loaded\n')
                except Exception as e:
                    print(e)
                    ok = False
                    print('PhotoWizard Error: Unable to load '+str(fileName))

            elif action == "save":
                try:
                    fileName = parseInput(request,[str,str])
                    fileName = fileName[1]
                    #print("Saving xmp file "+str(fileName))
                    saveXMP(fileName,images[current])
                    print('XMP file saved to '+str(fileName)+'\n')
                except Exception as e:
                    print(e)
                    ok = False
                    print('PhotoWizard Error: Unable to save file '+str(fileName))
            
            elif action == "export":
                try:
                    fileName = parseInput(request,[str,str])
                    fileName = fileName[1]
                    #print("Exporting "+str(fileName))
                    images[current].export(fileName)
                    print(str(fileName)+' exported\n')
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
                        print("Switched to "+str(fileName))
                    else:
                        print('PhotoWizard Error: no such file opened')
                except Exception as e:
                    print(e)
                    ok = False
                    print('PhotoWizard Error: Unable to switch to '+str(fileName)+'\n')

            elif action == "histogram":
                try:
                    channel = parseInput(request,[str,str])
                    channel = channel[1]
                    #print("Histogram")
                    H = images[current].histogram(channel)
                    #print(H)
                    for elt in H:
                        for k in range(0,11):
                            s = ''
                            for el in elt:
                                if int(el) >= round(255/10*(9-k)) and k != 10 :
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
                    parseInput(request,[str])
                    #print("preview")
                    images[current].preview()
                except Exception as e:
                    print(e)
                    ok = False
                    print('PhotoWizard Error: Unable to preview picture')
            
            elif action == "undo":
                try:
                    parseInput(request,[str])
                    #print("undo")
                    h = images[current].getHistory()
                    h.undo()
                    images[current].setHistory(h)
                    images[current].reCompute()
                    print('Last action revoked')
                except Exception as e:
                    print(e)
                    ok = False
                    print('PhotoWizard Error: Unable to undo action')

            elif action == "redo":
                try:
                    parseInput(request,[str])
                    #print("redo")
                    h = images[current].getHistory()
                    h.redo()
                    images[current].setHistory(h)
                    images[current].reCompute()
                    print('Last action restored')
                except Exception as e:
                    print(e)
                    ok = False
                    print('PhotoWizard Error: Unable to redo action')

            elif action == "rebase":
                try:
                    event = parseInput(request,[str,int])
                    event = event[1]
                    #print(rebase)
                    h = images[current].getHistory()
                    h.rebase(event)
                    images[current].setHistory(h)
                    images[current].reCompute()
                    print('History rebased to event '+str(event))
                except Exception as e:
                    print(e)
                    ok = False
                    print('PhotoWizard Error: Unable to rebase history to event '+str(event))

            elif action == "history":
                try:
                    parseInput(request,[str])
                    print("History:")
                    print(images[current].getHistory().getFullHistory())
                except Exception as e:
                    print(e)
                    ok = False
                    print('PhotoWizard Error: Unable to preview history')

            else:
                try:
                    # We try to compute the resized copy of the picture
                    image = Image.Image
                    function = action
                    #parameters = parseInput(request,[str,])
                    #everyFunction(image,[function,[parameters]])
                    img,parameters = mapping.everyFunction(images[current].getSmallImage(),[function,request])
                    images[current].setSmallImage(img)
                    h = images[current].getHistory()
                    h.add((function,parameters),function)
                    images[current].setHistory(h)
                except Exception as e:
                    print(e)
                    ok = False
                    print("PhotoWizard Error: Unexpected input value")
            
            if not ok:
                try:
                    if not testmode:
                        if len(action) > 0:
                            request = str(getInput(helpm.help("idle",LANG)))
                        else:
                            request = str(getInput(""))
                    else:
                        request = ''
                        ok = True
                except:
                    request = ''
                    ok = True



    display.bye(LANG)    

    return



if __name__=="__main__":
    main('',False)


