#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# This module contains the resize related functionalities

import sys
sys.path.insert(0,'utils/')

from PIL import Image
from tools import *


def resize(img,size): # Resizes an image to a given size and returns an Image.Image object

    if type(img) != Image.Image:
        try:
            img = str(img)
            img = openf(img)
        except:
            raise NameError('PhotoWizard Error: Unable to load the object')
            img = None

        try:
            W = int(size[0])
            H = int(size[1])
        except:
            raise NameError('PhotoWizard Error: Wrong size format')
            W = 0
            H = 0
        
        
        img = img.resize((W,H),Image.ANTIALIAS)


    return img


