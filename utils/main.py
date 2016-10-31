#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# This script is the main function for the command line version of the software

import sys
sys.path.insert(0,'utils/')

import display,helpm
from PIL import Image

from config import *
from tools import *



def main(args):

    display.greetings(LANG)
    quitFlag = False
    First = True

    while not quitFlag:
        
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
            elif action == "close":
                print("close file")
            elif action == "load":
                print("load xmp")
            elif action == "save":
                print("save xmp")
            elif action == "export":
                print("export")
            elif action == "switch":
                print("switch")
            elif action == "histogram":
                print("histogram")
            elif action == "preview":
                print("preview")
            elif action == "undo":
                print("undo")
            elif action == "redo":
                print("redo")
            elif action == "rebase":
                print(rebase)
            elif action == "history":
                print("history")
            else:
                try:
                    # We try to compute the resized copy of the picture
                    image = Image.Image
                    function = action
                    parameters = ""
                    everyFunction(image,[function,[parameters]])
                except:
                    ok = False
                    print("PhotoWizard Error: Unexpected input value")
                    try:
                        action = str(getInput(helpm.help("idle",LANG)))
                    except:
                        action = ""

    display.bye(LANG)    
    sys.exit(0)

    return



if __name__=="__main__":
    main("a")


