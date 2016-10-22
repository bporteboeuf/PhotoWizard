#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This module contains several useful tools


import sys,re,os
from PIL import Image



def getInput(message): # Message is a message to display

    if sys.version_info[0] < 3 :
        string =  raw_input(str(message))
    else :
        string = input(str(message))

    if re.search(r"^[0-9A-Za-z-_. \/]{1,60}$", string) is None :
        raise NameError('PhotoWizard Error: Unexpected input')
        return
    else :
        return string



def explore(path,options): # Explores a folder


    return





def openf(path): # Opens a image and returns an Image.Image object


    return




def unzip(paths): # Extracts an archive file


    return





def zip(paths): # Compresses files into an archive


    return

