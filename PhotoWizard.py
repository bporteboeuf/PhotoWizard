#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This script is the one the user will launch. It will either launch the command line version or the GUI version.


import sys
sys.path.insert(0,'utils/')
import main,helpm
from config import *


if __name__ == "__main__" :

    # Possible launching options:
    # -v : Version
    # -h : Help
    # -c : Console mode
    # -g : Graphical User Interface mode

    launched = False
    
    if len(sys.argv) > 1 :
        try:
            options = str(sys.argv[1:])
        except:
            raise NameError('PhotoWizard Error: Wrong format for launching options')
            options = ""

        start = False
        for elt in options:
            
            if elt == "-":
                start = True
            
            if start:
                if elt == "v":
                    try:
                        print("Current Version of PhotoWizard: "+str(VER))
                    except:
                        raise NameError('PhotoWizard Error: Wrong version format in config')
                    launched = True

                elif elt == "h":
                    print(helpm.help("idle",LANG))
                    launched = True

                elif elt == "c":
                    main.main(sys.argv)
                    launched = True

                elif elt == "g":
                    print("PhotoWizard Error: Graphical User Interface not implemented yet")
                    main.main(sys.argv)
                    launched = True


    if not launched:
        if MODE == "g":
            print("PhotoWizard Error: Graphical User Interface not implemented yet")
            main.main(sys.argv)
        elif MODE == "c":
            main.main(sys.argv)
        else:
            raise NameError('PhotoWizard Error: Unknown default launching mode in config')
        

