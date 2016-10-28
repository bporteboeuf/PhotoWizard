#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# This script is the main function for the command line version of the software

import sys
sys.path.insert(0,'utils/')

import display,helpm

from config import *
from tools import *



def main(args):

    display.greetings(LANG)
    quitFlag = False
    First = True

    while not quitFlag:
        
        if First :
            #action = str(getInput(display.action(LANG)))
            action = str(getInput("\n   h - help      q - quit\n"))
            First = False
        else:
            action = str(getInput(""))
        
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
            else:
                print("PhotoWizard Error: Unexpected input value")
                ok = False
                #try:
                #    everyFunction()
                #except:
                #    action = str(getInput(display.action(LANG)))
                action = str(getInput("\n   h - help      q - quit\n"))


    display.bye(LANG)    
    sys.exit(0)

    return



if __name__=="__main__":
    main("a")


