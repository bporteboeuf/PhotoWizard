#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This script is the one the user will launch. It will either launch the command line version or the GUI version.


import sys
sys.path.insert(0,'utils/')
import main


if __name__ == "__main__" :

    main.main(sys.argv)


