#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# This script is the main function for the command line version of the software

import sys,os
sys.path.insert(0,'utils/')

import display,helpm
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
    ID_max = 0
    current = ""

    while not quitFlag:
        
        if mode == 'TEST':
            try:
                action = str(args[::-1].pop())
            except:
                action = ''
        else:
            if First :
                #action = str(getInput(display.action(LANG)))
                try:
                    action = str(getInput("\n   h - help      q - quit\n"))
                except:
                    action = ""
                    next
                First = False
            else:
                try:
                    action = str(getInput(""))
                except:
                    action = ""
                    next

        ok = False
        while not ok:
            ok = True

            if action == "h" or action == "help":
                display.disp(helpm.help("idle",LANG))
            elif action == "q" or action == "quit":
                quitFlag = True
            elif action == "open":
                print("open file")
                #ID_max += 1
                #images[fileName] = Picture(ID_max,fileName)
                #current = fileName
            elif action == "close":
                print("close file")
                #images[fileName].close()
                #current = ??
            elif action == "load":
                print("load xmp")
                #images[current].rebase(1)
                #for event in xmp:
                #       images[current].History.add(event)
            elif action == "save":
                print("save xmp")
                #save(xmp)
            elif action == "export":
                print("export")
                #images[current].export()
            elif action == "switch":
                print("switch")
                #current = fileName
            elif action == "histogram":
                print("histogram")
                #print(images[current].histogram())
            elif action == "preview":
                print("preview")
                #images[current].preview()
            elif action == "undo":
                print("undo")
                #images[current].History.undo()
            elif action == "redo":
                print("redo")
                #images[current].History.redo()
            elif action == "rebase":
                print(rebase)
                #images[current].rebase(event)
            elif action == "history":
                print("history")
                #print(images[current].History.getFullHistory)
            else:
                try:
                    # We try to compute the resized copy of the picture
                    image = Image.Image
                    function = action
                    parameters = ""
                    everyFunction(image,[function,[parameters]])
                    #images[current].setSmallPic = everyFunction(images[current].getSmallPic,[function,[parameters]])
                except:
                    ok = False
                    print("PhotoWizard Error: Unexpected input value")
                    try:
                        if mode != 'TEST':
                            if len(action) > 0:
                                action = str(getInput(helpm.help("idle",LANG)))
                            else:
                                action = str(getInput(""))
                        else:
                            action = ''
                    except:
                        action = ''

    display.bye(LANG)    
    sys.exit(0)

    return



if __name__=="__main__":
    main("a")


