#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This module defines the picture class

import sys
import rawpy, numpy
sys.path.insert(0,'utils')
from history import History
from PIL import Image
from tools import *
import mapping
from loadConfig import *


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
                try:
                    tmp = rawpy.imread(name)
                    tmp = numpy.asarray(tmp.postprocess(),dtype=numpy.uint8)
                    self.pic = Image.fromarray(tmp)
                    rawpy.close()
                except Exception as e:
                    print(e)
                    raise NameError('PhotoWizard Error: Unable to load file')
        else:
            raise NameError('PhotoWizard Error: Unable to find file')
        
        try:
            self.EXIF = self.pic.info['exif']
        except:
            pass
       
        self.scaling = (1,1)

        if self.pic is not None :
            self.smallpic = self.pic
            (W,H) = self.pic.size
            if W < H:
                a = min(WIDTH_PREVIEW,W)
                a = round(a*H/W)
            else :
                b = min(HEIGHT_PREVIEW,H)
                a = round(b*W/H)
            
            self.scaling = (float(a/W),float(b/H)) # Scaling coefficient

            self.smallpic = self.smallpic.resize((a,b),Image.ANTIALIAS) # Makes a resized copy of the original image for optimized computing
            self.smallpic_ref =  self.smallpic # Keeps a reference copy for any possible history rebase
        else :
            self.smallpic = None
            self.smallpic_ref = None
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


    def getSmallImageRef(self):
        return self.smallpic_ref


    def setSmallImageRef(self,image):
        if isinstance(image,Image.Image):
            self.smallpic_ref = image
        else:
            raise NameError('PhotoWizard Error: Wrong argument type in setSmallImageRef')
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
                    oldScaling = self.getScaling()
                    shape = (oldScaling[0]*a,oldScaling[1]*b)
                    self.setScaling(shape)
                    img = self.getSmallImage()
                    shape2 = img.size
                    shape2 = (a*shape2[0],b*shape2[1])
                    self.smallpic = resize(img,shape2)
                else:
                    raise NameError('PhotoWizard Error: Wrong argument range, must be between 1/100 and 100')
        return

    
    def getScaling(self):
        return self.scaling

    def setScaling(self,shape):
        if (type(shape) is tuple) and (len(shape)==2) and (shape[0]!=0) and (shape[1]!=0):
            self.scaling = shape
        else:
            raise NameError('PhotoWizard Error: Wrong argument in setScaling')
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
            hist = self.getHistory()
            hist = hist.getHistory()
            img = self.getSmallImageRef()
            for event in hist:
                request = event.getContent()
                request = request.split(" ")
                function = request[0]
                request = " ".join(request)
                img,parameters = mapping.everyFunction(img,[function,request],self.getScaling())
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
                picture,parameters = mapping.everyFunction(picture,[function,request],(1,1))
            try:
                picture = picture.convert('RGB')
                if len(self.EXIF) > 0:
                    picture.save(path,quality=90,optimize=True,progressive=True,exif=self.EXIF)
                else:
                    picture.save(path,quality=90,optimize=True,progressive=True)
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
            hist.append(numpy.round(H*255/numpy.amax(H)))
        #print(hist)
        return hist


    def preview(self):
        self.getSmallImage().show() # temporary
        return



