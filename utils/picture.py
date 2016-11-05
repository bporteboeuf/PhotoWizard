#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This module defines the picture class

import sys
sys.path.insert(0,'utils')
from history import History
from PIL import Image
from tools import *
import mapping


class Picture:

    def __init__(self,ID,name):
        self.ID = ID
        self.History = History(ID)
        self.EXIF = {}
        self.pic = None
        if os.path.exists(name):
            try:
                self.pic = Image.open(name)
            except:
                raise NameError('PhotoWizard Error: Unable to load file')
        else:
            raise NameError('PhotoWizard Error: Unable to find file')
        if self.pic is not None :
            self.smallpic = self.pic
            self.smallpic = self.smallpic.resize((30,30),Image.ANTIALIAS) # Makes a resized copy of the original image for optimized computing
        else :
            self.smallpic = None
        return


    def getImage(self):
        return self.pic


    def getSmallImage(self):
        return self.smallpic

    
    def setSmallImage(self,image):
        if isinstance(image,Image.Image):
            self.smallpic = image
        else:
            raise NameError('PhotoWizard Error: Wrong argument type in setSmallImage')
        return


    def resizeSmall(self,size): # Resizes the working miniature picture according to a given relative size (range 1/100 to 100)
        if type(size) is not tuple :
            raise NameError('PhotoWizard Error: Wrong argument type, must be tuple')
        else:
            if len(size) != 2 :
                raise NameError('PhotoWizard Error: Wrong argument size, must be of length 2')
            else :
                a = 1
                b = 1
                try:
                    a = int(size[0])
                    b = int(size[1])
                except:
                    raise NameError('PhotoWizard Error: Wrong argument type, must be integers')

                if (1<100*a<100*100) and (1<=100*b<=100*100):
                    self.smallpic = resize(self.getSmallImage(),(a,b))
                else:
                    raise NameError('PhotoWizard Error: Wrong argument range, must be between 1/100 and 100')
        return

    
    def getHistory(self):
        return self.History


    def setHistory(self,hist):
        if isinstance(hist,History):
            self.History = hist
        else:
            raise NameError('PhotoWizard Error: Wrong argument type in setHistory')
        return


    def reCompute(self): # Recompute the miniature image according to the current history
        try :
            hist = self.getHistory().getHistory()
            for event in hist:
                request = event.getContent()
                request = request.split(" ")
                function = request[0]
                request = " ".join(request)
                img,parameters = mapping.everyFunction(self.getSmallImage(),[function,request])
                self.setSmallImage(img)
        except Exception as e:
            print(e)
            raise NameError('PhotoWizard Error: Unable to reCompute')
        return


    def export(self,path):
        try:
            hist = self.getHistory().getHistory()
            picture = self.getImage()
            for event in hist:
                request = event.getContent()
                action = request.split(' ')
                function = action[0]
                picture,parameters = mapping.everyFunction(picture,[function,request])
            try:
                picture = picture.convert('RGB')
                picture.save(path)
            except Exception as e:
                print(e)
                raise NameError('PhotoWizard Error: Unable to save file in export')
        except Exception as e:
            print(e)
            raise NameError('PhotoWizard Error: Unable to export file')
        return


    def close(self):
        return




    def histogram(self,channel):
        matrices = getChannel(self.getSmallImage(),channel)
        hist = []
        precision = 4
        for elt in matrices:
            [H,B] = numpy.histogram(elt,bins=round(256/precision),range=(0,255))
            hist.append(H*255/numpy.amax(H))
        return hist


    def preview(self):
        return



