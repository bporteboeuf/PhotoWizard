#! /usr/bin/env python
# -*- coding: utf-8 -*-

#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#



# This module aims at resolving dependencies for PhotoWizard
# Because it tries to install dependancies using pip, this script should be run with admin privileges


string = "\n\n#/////////////////////////////#\n# - P H O T O   W I Z A R D - #\n#/////////////////////////////#\n\n"
string += '    S E T U P   S C R I P T\n\n'
print(string) 

import sys
try :
    import pip
except ImportError:
    from utils import getPip
    print("No module named pip - Error.")
    print("Installing Pip...")
    getPip.main()


def update():
    pip.main(['install','--upgrade','pip'])
    return


def install(package):
    pip.main(['install', package])
    return


def main() :
    print("Updating pip...")
    update()
    print("Installing dependancies for PhotoWizard...")
    install('Pillow')
    install('Numpy')
    install('Scipy')
    install('Rawpy')
    print("Done")
    return


if __name__ == '__main__':
    main()
