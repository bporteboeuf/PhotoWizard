#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# This script is the main function for the command line version of the software

import sys,os
sys.path.insert(0,'utils/')

import display,helpm,mapping
from PIL import Image

from config import *
from tools import *



def main(args,mode):

    try:
        mode = str(mode)
        args = list(args)
    except:
        raise NameError('PhotoWizard Error: wrong argument type in main')


    display.greetings(LANG)
    quitFlag = False
    First = True

    images = {}
    files = []
    ID_max = 0
    current = ""

    while not quitFlag:
        
        if mode == 'TEST':
            try:
                request = str(args[::-1].pop())
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
                except:
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
                except:
                    ok = False
                    print('PhotoWizard Error: Unable to close '+str(fileName)+'\n')

            elif action == "load":
                try:
                    fileName = parseInput(request,[str,str])
                    fileName = fileName[1]
                    #print("Loading XMP file "+str(fileName))
                    h = images[current].getHistory()
                    h = h.rebase(1)
                    for event in xmp:
                           h = h.add(event)
                    images[current].setHistory(h)
                    print('XMP file '+str(fileName)+' loaded\n')
                except:
                    ok = False
                    print('PhotoWizard Error: Unable to load '+str(fileName))

            elif action == "save":
                try:
                    fileName = parseInput(request,[str,str])
                    fileName = fileName[1]
                    #print("Saving xmp file "+str(fileName))
                    saveXMP(fileName,images[current])
                    print('XMP file saved to '+str(fileName)+'\n')
                except:
                    ok = False
                    print('PhotoWizard Error: Unable to save file '+str(fileName))
            
            elif action == "export":
                try:
                    fileName = parseInput(request,[str,str])
                    fileName = fileName[1]
                    #print("Exporting "+str(fileName))
                    images[current].export(fileName)
                    print(str(fileName)+' exported\n')
                except:
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
                except:
                    ok = False
                    print('PhotoWizard Error: Unable to switch to '+str(fileName)+'\n')

            elif action == "histogram":
                try:
                    channel = parseInput(request,[str,str])
                    channel = channel[1]
                    #print("Histogram")
                    H = images[current].histogram(channel)
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
                except:
                    ok = False
                    print('PhotoWizard Error: Unable to preview histogram')
            
            elif action == "preview":
                try:
                    parseInput(request,[str])
                    #print("preview")
                    images[current].preview()
                except:
                    ok = False
                    print('PhotoWizard Error: Unable to preview picture')
            
            elif action == "undo":
                try:
                    parseInput(request,[str])
                    #print("undo")
                    h = images[current].getHistory()
                    images[current].setHistory(h.undo())
                    images[current].recompute()
                    print('Last action revoked')
                except:
                    ok = False
                    print('PhotoWizard Error: Unable to undo action')

            elif action == "redo":
                try:
                    parseInput(request,[str])
                    #print("redo")
                    h = images[current].getHistory()
                    images[current].setHistory(h.redo())
                    images[current].recompute()
                    print('Last action restored')
                except:
                    ok = False
                    print('PhotoWizard Error: Unable to redo action')

            elif action == "rebase":
                try:
                    event = parseInput(request,[str,int])
                    event = event[1]
                    #print(rebase)
                    h = images[current].getHistory()
                    images[current].setHistory(h.rebase(event))
                    images[current].recompute()
                    print('History rebased to event '+str(event))
                except:
                    ok = False
                    print('PhotoWizard Error: Unable to rebase history to event '+str(event))

            elif action == "history":
                try:
                    parseInput(request,[str])
                    print("History:")
                    print(images[current].getHistory().getFullHistory())
                except:
                    ok = False
                    print('PhotoWizard Error: Unable to preview history')

            else:
                try:
                    # We try to compute the resized copy of the picture
                    image = Image.Image
                    function = action
                    #parameters = parseInput(request,[str,])
                    #everyFunction(image,[function,[parameters]])
                    images[current].setSmallImage(mapping.everyFunction(images[current].getSmallImage(),[function,request]))
                    h = images[current].getHistory()
                    imags[current].setHistory(h.add([function,[parameters]],function))
                except Exception as e:
                    print(e)
                    ok = False
                    print("PhotoWizard Error: Unexpected input value")
            
            if not ok:
                try:
                    if mode != 'TEST':
                        if len(action) > 0:
                            request = str(getInput(helpm.help("idle",LANG)))
                        else:
                            request = str(getInput(""))
                    else:
                        request = ''
                except:
                    request = ''



    display.bye(LANG)    
    sys.exit(0)

    return



if __name__=="__main__":
    main("a")


