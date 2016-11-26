#!/usr/bin/python
# -*- coding: utf-8 -*-

#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#


# This script is the one the user will launch. It will either launch the command line version or the GUI version.


import sys
sys.path.insert(0,'utils/')
import main,helpm
from config import *

VER = '0.6' # Current version of the software


if __name__ == "__main__" :

    # Possible launching options:
    # -v : Version
    # -h : Help
    # -c : Console mode
    # -g : Graphical User Interface mode

    if sys.version_info[0] < 3:
        print('PhotoWizard Warning: Python 2 compatibility mode launched - try running it with Python 3 for a better user experience')


    launched = False
    
    if len(sys.argv) > 1 :
        try:
            options = str(sys.argv[1:])
        except:
            raise NameError('PhotoWizard Error: Wrong format for launching options')
            options = ""

        
        start = False
        for elt in options:
            
            # We analyse the launching options

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
                    main.main(sys.argv,False)
                    launched = True

                elif elt == "g":
                    print("PhotoWizard Error: Graphical User Interface not implemented yet")
                    main.main(sys.argv,False)
                    launched = True

    if not launched:
        if MODE == "g":
            print("PhotoWizard Error: Graphical User Interface not implemented yet")
            main.main(sys.argv,False)
        elif MODE == "c":
            main.main(sys.argv,False)
        else:
            raise NameError('PhotoWizard Error: Unknown default launching mode in config')
        


    sys.exit(0)

