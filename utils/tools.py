#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This module contains several useful tools


import sys,re,os,numpy
from history import History
from PIL import Image
from config import *


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
        hist = self.getHistory().getHistory()
        for event in hist:
            action = event.getContent()
            self.smallpic = everyFunction(self,action)
            
        return


    def export(self,path):
        hist = self.getHistory().getHistory()
        for event in hist:
            action = event.getContent()
            self.pic = everyFunction(self,action)
        try:
            self.pic.save(path)            
        except:
            raise NameError('PhotoWizard Error: Unable to save file in export')
        return


    def close(self):
        return




    def histogram(self,channel):
        matrices = getChannel(self.getSmallImage(),channel)
        hist = []
        precision = 4
        for elt in matrices:
            [H,B] = numpy.histogram(elt,bins=round(256/precision),range=(0,255))
            hist.append(H)
        return hist




def getChannel(image,channel): # Channel can be H, S, V, R, G, B or ALL - Note: if BW, should use V or ALL?
 
    if isinstance(image,Image.Image) and (type(channel) is str):
        if len(channel) == 1:
            if channel == 'H':
                image = image.convert('HSV')
                image = numpy.asarray(image,dtype=numpy.uint8)
                image = [image[:,:,0]]
            elif channel == 'S':
                image = image.convert('HSV')
                image = numpy.asarray(image,dtype=numpy.uint8)
                image = [image[:,:,1]]
            elif channel == 'V':
                image = image.convert('HSV')
                image = numpy.asarray(image,dtype=numpy.uint8)
                image = [image[:,:,2]]
            elif channel == 'R':
                image = image.convert('RGB')
                image = numpy.asarray(image,dtype=numpy.uint8)
                image = [image[:,:,0]]
            elif channel == 'G':
                image = image.convert('RGB')
                image = numpy.asarray(image,dtype=numpy.uint8)
                image = [image[:,:,2]]
            elif channel == 'B' :
                image = image.convert('RGB')
                image = numpy.asarray(image,dtype=numpy.uint8)
                image = [image[:,:,2]]
            else:
                raise NameError('PhotoWizard Error: unexpected argument in getChannel')
        elif len(channel) == 3:
            if channel == 'ALL':
                image = image.convert('HSV')
                image = numpy.asarray(image,dtype=numpy.uint8)
                image = [image[:,:,0],image[:,:,1],image[:,:,2]]
            else:
                raise NameError('PhotoWizard Error: unexpected argument in getChannel')
        else:
            raise NameError('PhotoWizard Error: unexpected argument in getChannel')
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in getChannel')

    return image



def recompose(image,channel,matrices): # Recomposes the image after modifications on one or several of its channels
    #print(isinstance(image,Image.Image),type(channel) is str,type(matrices) is list)
    if (isinstance(image,Image.Image)) and (type(channel) is str) and (type(matrices) is list):
       
        if len(matrices) == len(channel):

            if len(channel) == 1 :
                
                try:
                    matrices = numpy.asarray(matrices[0],dtype=numpy.uint8)
                except:
                    raise NameError('PhotoWizard Error: Wrong argument type in recompose - 2')

                if channel == 'R':
                    img = image.convert('RGB')
                    img = numpy.asarray(img,dtype=numpy.uint8)
                    img.setflags(write=True)
                    img[:,:,0] = matrices
                    image = Image.fromarray(img,'RGB')
                elif channel == 'G':
                    img = image.convert('RGB')
                    img = numpy.asarray(img,dtype=numpy.uint8)
                    img.setflags(write=True)
                    img[:,:,1] = matrices
                    image = Image.fromarray(img,'RGB')
                elif channel == 'B':
                    img = image.convert('RGB')
                    img = numpy.asarray(img,dtype=numpy.uint8)
                    img.setflags(write=True)
                    img[:,:,2] = matrices
                    image = Image.fromarray(img,'RGB')
                elif channel == 'H':
                    img = image.convert('HSV')
                    img = numpy.asarray(img,dtype=numpy.uint8)
                    img.setflags(write=True)
                    img[:,:,0] = matrices
                    image = Image.fromarray(img,'HSV')
                elif channel == 'S':
                    img = image.convert('HSV')
                    img = numpy.asarray(img,dtype=numpy.uint8)
                    img.setflags(write=True)
                    img[:,:,1] = matrices
                    image = Image.fromarray(img,'HSV')
                elif channel == 'V':
                    img = image.convert('HSV')
                    img = numpy.asarray(img,dtype=numpy.uint8)
                    img.setflags(write=True)
                    img[:,:,2] = matrices
                    image = Image.fromarray(img,'HSV')
                else:
                    raise NameError('PhotoWizard Error: unexpected argument in recompose')  

            elif len(channel) == 3:
                if channel == 'ALL': 
                    matrices2 = []
                    try:
                        matrices2.append(numpy.asarray(matrices[0],dtype=numpy.uint8))
                        matrices2.append(numpy.asarray(matrices[1],dtype=numpy.uint8))
                        matrices2.append(numpy.asarray(matrices[2],dtype=numpy.uint8))
                    except:
                        raise NameError('PhotoWizard Error: Wrong argument type in recompose - 3')

                    img = image.convert('HSV')
                    img = numpy.asarray(img,dtype=numpy.uint8)
                    img.setflags(write=True)
                    img[:,:,0] = matrices2[0]
                    img[:,:,1] = matrices2[1]
                    img[:,:,2] = matrices2[2]
                    image = Image.fromarray(img,'HSV')

                else:
                    raise NameError('PhotoWizard Error: unexpected argument in recompose')
            else:
                raise NameError('PhotoWizard Error: unexpected argument in recompose')
        else:
            raise NameError('PhotoWizard Error: arugments length mismatch in recompose')
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in recompose - 1')

    return image





def getInput(message): # Gets input from user - message is a message to display
    
    if type(message) is str :

        if sys.version_info[0] < 3 :
            string =  raw_input(str(message))
        else :
            string = input(str(message))
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in getInput')

    if re.search(r"^[0-9A-Za-z-_. \/]{0,60}$", string) is None :
        raise NameError('PhotoWizard Error: Unexpected input')
        return
    else :
        return string


def parseInput(string,expected): # Parses a string input to find the corresponding objects - expect is a list of expected types such as : [list,str,int,float]
    if type(string) is str and type(expected) is list:
        s = string.split(' ')
        stringFormated = []
        if len(s) == 2:
            if s[1] == '-h' or s[1] == '--help':
                print(helpm.help(s[0],LANG))
                return stringFormated

        if len(s) == len(expected):
            try :
                for i in range(0,len(s)):
                    if expected[i] is str:
                        tmp = str(s[i])
                    elif expected[i] is int:
                        tmp = int(s[i])
                    elif expected[i] is list:
                        tmp = str(s[i])
                        if tmp[0] == '[' and tmp[len(tmp)-1] == ']':
                            tmp = tmp[1:len(tmp)-1]
                            tmp = tmp.split(',')
                            tmp = numpy.asarray(tmp,dtype=numpy.float32)
                            tmp = list(tmp)
                        else:
                            raise NameError('PhotoWizard Error: Unable to parse delimiters in parseInput')
                    elif expected[i] is tuple:
                        tmp = str(s[i])
                        if tmp[0] == '(' and tmp[len(tmp)-1] == ')':
                            tmp = tmp[1:len(tmp)-1]
                            tmp = tmp.split(',')
                            tmp.numpy.asarray(tmp,dtype=numpy.asarray.float32)
                            tmp = tuple(tmp)
                        else:
                            raise NameError('PhotoWizard Error: Unable to parse delimiters in parseInput')

                    elif expected[i] is float:
                        tmp = float(s[i])
                    else:
                        raise NameError('PhotoWizard Error: Unsupported type in parseInput')
                    stringFormated.append(tmp)
            except:
                raise NameError('PhotoWizard Error: Wrong argument type in parseInput - 2')
        else:
            raise NameError('PhotoWizard Error: arguments length mismatch in parseInput')
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in parseInput - 1')
    return stringFormated



def resize(img,size): # Resizes an image to a given size and returns an Image.Image object
    if not isinstance(img, Image.Image):
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



def crop(image,parameters): # Crops an image
    
    if (isinstance(image,Image.Image) and (type(parameters) is tuple) and (len(parameters)==4)):
        try:
            coord = (int(parameters[0]),int(parameters[1]),int(parameters[2]),int(parameters[3]))
            if (min(coord)>=0 and coord[2]<= image.size[0] and coord[3] <= image.size[1]):
                image = image.crop(coord)
            else:
                raise NameError('PhotoWizard Error: Unexpected values in crop')
        except:
            raise NameError('PhotoWizard Error: Wrong argument format in crop')
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in crop')
    
    return image




def everyFunction(image,action): # Maps the action in the main or history to the real image editing functions
    if (isinstance(image,Image.Image)) and (type(action) is list):
        try:
            f = action[0]
            params = action[1]
            params = params[0]
        except:
            raise NameError('PhotoWizard Error: Wrong argument format in everyFunction')
            f = ""
            params = []
        if f == "levels":
            #print(f)
            try:
                params = parseInput(params,[str,str,int,int])
                params = params[1:]
                image = levels(image,params[0],params[1],params[2])
            except:
                raise NameError('PhotoWizard Error: Unable to call levels() in everyFunction')
        elif f == "curves":
            #print(f)
            try:
                params = parseInput(params,[str,str,int,int])
                params = params[1:len(params)-1]
                image = curves(image,params[0],params[1],params[2])
            except:
                raise NameError('PhotoWizard Error: Unable to call curves() in everyFunction')
        elif f == "normHist":
            #print(f)
            try:
                params = parseInput(params,[str,str])
                params = params[1:]
                image = normalizeHistogram(image,params[0])
            except:
                raise NameError('PhotoWizard Error: Unable to call normalizeHistogram() in everyFunction')
        elif f == "eqHist":
            #print(f)
            try:
                params = parseInput(params,[str,str])
                params = params[1:]
                image = equalizeHistogram(image,params[0])
            except:
                raise NameError('PhotoWizard Error: Unable to call equalizeHistogram() in everyFunction')
        elif f == "expHist":
            #print(f)
            try:
                params = parseInput(params,[str,str])
                params = params[1:]
                image = expHistogram(image,params[0])
            except:
                raise NameError('PhotoWizard Error: Unable to call expHistogram() in everyFunction')
        elif f == "logHist":
            #print(f)
            try:
                params = parseInput(params,[str,str])
                params = params[1:]
                image = logHistogram(image,params[0])
            except:
                raise NameError('PhotoWizard Error: Unable to call logHistogram() in everyFunction')
        elif f == "lowPass":    
            #print(f)
            try:
                params = parseInput(params,[str,str,int,float,str])
                params = params[1:]
                image = filterz(image,params[2],lowPass(params[0],params[1],params[2]))
            except:
                raise NameError('PhotoWizard Error: Unable to call filterz() and/or lowPass() in everyFunction')
        elif f == "highPass":
            #print(f)
            try:
                params = parseInput(params,[str,str,int,str])
                params = params[1:]
                image = filterz(image,params[2],highPass(params[0],params[1]))
            except:
                raise NameError('PhotoWizard Error: Unable to call filterz() and/or highPass() in everyFunction')
        elif f == "detectEdges":
            #print(f)
            try:
                params = parseInput(params,[str,str,str,int,float])
                params = params[1:]
                image = edgeDetection(image,params[0],params[1],params[2],params[3])
            except:
                raise NameError('PhotoWizard Error: Unable to call edgeDetection() in everyFunction')
        elif f == "enhanceEdges":
            #print(f)
            try:
                params = parseInput(params,[str,str,str,int,int,float])
                params = params[1:]
                image = edgeEnhancement(image,params[0],params[1],params[2],params[3],params[4])
            except:
                raise NameError('PhotoWizard Error: Unable to call edgeEnhancement() in everyFunction')
        elif f == "rotate":
            #print(f)
            try:
                params = parseInput(params,[str,float])
                params = params[1:]
                image = rotate(image,params[0])
            except:
                raise NameError('PhotoWizard Error: Unable to call rotate() in everyFunction')
        elif f == "crop":
            #print(f)
            try:
                params = parseInput(params,[str,list])
                params = params[1:]
                image = crop(image,params[0])
            except:
                raise NameError('PhotoWizard Error: Unable to call crop() in everyFunction')
        elif f == "resize":
            #print(f)
            try:
                params = parseInput(params,[str,list])
                params = params[1:]
                image = resize(image,params[0])
            except:
                raise NameError('PhotoWizard Error: Unable to call resize() in everyFunction')
        else:
            raise NameError('PhotoWizard Error: Unknown function in everyFunction')

    else:
        raise NameError('PhotoWizard Error: Wrong argument type in everyFunction')

    return image




def explore(path,options): # Explores a folder

    return



def unzip(paths): # Extracts an archive file
    # See zipfile @https://docs.python.org/3/library/zipfile.html
    return



def zip(paths): # Compresses files into an archive
    # See: zipfile @https://docs.python.org/3/library/zipfile.html
    return



def loadXMP(path):

    return


def saveXMP(path):

    return


