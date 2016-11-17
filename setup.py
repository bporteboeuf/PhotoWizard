#! /usr/bin/env python

#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#


# -*- coding: utf-8 -*-


# This module aims at resolving dependencies for PhotoWizard


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
    print("Installing dependancies for PhoWizard...")
    install('Pillow')
    install('Numpy')
    install('Scipy')
    install('Rawpy')
    print("Done")
    return


if __name__ == '__main__':
    main()
