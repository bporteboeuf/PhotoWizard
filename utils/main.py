#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# This script is the main function for the command line version of the software

import sys
sys.path.insert(0,'utils/')

import display,helpm,inputs

from config import *



def main(args):

    display.greetings()
    action = str(inputs.getInput("\n   h - help      q - quit\n"))

    ok = False
    while not ok:
        if action == "h":
            display.disp(helpm.help("idle",LANG))
            ok = True
        elif action == "q":
            display.bye()
            ok = True
            sys.exit(0)
        else:
            print("PhotoWizard Error: Unexpected input value")
            action = str(inputs.getInput("\n   h - help      q - quit\n"))


    

    if len(args) > 1 :

        print(args)

    

    return



if __name__=="__main__":
    main("a")


