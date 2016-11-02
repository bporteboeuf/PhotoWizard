#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This module contains levels related functions

import numpy,math,scipy
from PIL import Image


def levels(image,channel,inputs,outputs): # Image can be an Image.Image object (same treatment for every selected channel) or a numpy.ndarray (same treatment for every layer)
    if (isinstance(image,Image.Image) or isinstance(image,numpy.ndarray)) and (type(channel) is str) and (type(inputs) is list) and (type(outputs) is list) :
        #print(len(inputs)==len(outputs),0<=min(inputs),0<=min(outputs),255>=max(inputs),255>=max(outputs))
        if (len(inputs) == len(outputs)) and (0<=min(inputs)) and (0<=min(outputs)) and (255>=max(inputs)) and (255>=max(outputs)):
    
            if isinstance(image,Image.Image):
                channels = getChannel(image,channel)
            elif image.size == image.shape[0]*image.shape[1]: # 2D numpy array
                channels = image
            else:
                raise NameError('PhotoWizard Error: Wrong argument format in levels')

            i = 0
            #matrices = numpy.zeros((channels[0].shape[0],channels[0].shape[1],len(channels)))
            #matrices.setflags(write=True)
            matrices = []
            for matrix in channels:

                # We first analyze which region of the matrix is in each inputs interval
                # And we normalize it (affine) so it fits in the corresponding outputs interval

                matrix2 = matrix
                matrix2.setflags(write=True)
                ib = 0
                ob = 0
                for k in range(0,len(inputs)):
                    # input interval
                    ia = ib
                    ib = inputs[k]

                    # output interval
                    oa = ob
                    ob = outputs[k]

                    # coefficients
                    if ib!=ia:
                        alpha = (ob-oa)/(ib-ia)
                    else:
                        alpha = 0
                    beta = ob - alpha*ib

                    # We get the indexes of elements in our inputs interval
                    under = numpy.where(matrix2<=ib)
                    over = numpy.where(matrix2>=ia)

                    # Then we build an indicator matrix
                    eltUnder = numpy.zeros(matrix2.shape,dtype=numpy.uint8)
                    eltUnder[under] = 1
                    eltOver = numpy.zeros(matrix2.shape,dtype=numpy.uint8)
                    eltOver[over] = 1

                    eltInterval = eltUnder*eltOver
                    indexes = numpy.where(eltInterval>0)

                    # And we finally compute the wanted values
                    matrix2[indexes] = matrix2[indexes]*alpha+beta
                matrices.append(matrix2)
                #matrices[:,:,i] = matrix2
                #i+=1
        else:
            raise NameError('PhotoWozard Error: Wrong argument format in levels')
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in levels')
    
    if isinstance(image,Image.Image):
        image = recompose(image,channel,matrices)
    else:
        image = matrices

    return image



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
    #print(isinstance(image,Image.Image),type(channel),type(matrices))
    if (isinstance(image,Image.Image)) and (type(channel) is str) and (type(matrices) is list):
       
        if len(matrices) == len(channel):

            if len(channel) == 1 :
                
                try:
                    matrices = numpy.asarray(matrices[0],dtype=numpy.uint8)
                except:
                    raise NameError('PhotoWizard Error: Wrong argument type in recompose')

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
                        raise NameError('PhotoWizard Error: Wrong argument type in recompose')

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
        raise NameError('PhotoWizard Error: Wrong argument type in recompose')

    return image



def normalizeHistogram(image,channel): # Automatic contrast adjustment
    if isinstance(image,Image.Image):
        images = getChannel(image,channel)
        #image = numpy.zeros((images[0].shape,images[1].shape,len(images)))
        #i = 0
        matrices = []
        for img in images:
            a = numpy.amin(img)
            b = numpy.amax(img)

            #image[:,:,i] = (img-a)*255/(b-a)
            #i+=1
            matrices.append(numpy.asarray((img-a)*255/(b-a),dtype=numpy.uint8))
        image = recompose(image,channel,matrices)
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in normalizeHistogram')

    return image




def equalizeHistogram(image,channel): # Automatic contrast adjustment
    if isinstance(image,Image.Image):
        precision = 4
        inputs = numpy.linspace(0,255,round(256/precision))
        
        images = getChannel(image,channel)
        #matrices = numpy.zeros((images[0].shape[0],images[0].shape[1],len(images)))
        #i = 0
        matrices = []
        for img in images:
            histogram, bins = numpy.histogram(img,bins=round(256/precision),range=(0,255))
            outputs = numpy.cumsum(histogram)
            outputs = outputs*255/outputs[outputs.shape[0]-1]
            #matrices[:,:,i] = levels(img,'',list(inputs),list(outputs))
            #i+=1
            matrices.append(levels(img,'',list(inputs),list(outputs)))
        image = recompose(image,channel,matrices)
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in equalizeHistogram')

    return image




def logHistogram(image,channel): # Automatic contrast adjustment recover details in low values
    if isinstance(image,Image.Image):
        precision = 4
        inputs = numpy.linspace(1,255,round(256/precision))
        outputs = numpy.log(inputs)
        outputs = outputs*255/outputs[len(outputs)-1]
        inputs = list(numpy.asarray(inputs,dtype=numpy.uint8))
        outputs = list(numpy.asarray(outputs,dtype=numpy.uint8))

        images = getChannel(image,channel)
        #matrices = numpy.zeros((images[0].shape[0],images[0].shape[1],len(images)))
        #i = 0
        matrices = []
        for img in images:
            #matrices[:,:,i] = levels(img,'',list(inputs),list(outputs))
            #i+=1
            matrices.append(levels(img,'',list(inputs),list(outputs)))
        image = recompose(image,channel,matrices)
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in logHistogram')

    return image




def expHistogram(image,channel): # Automatic contrast adjustment to recover details in high values
    if isinstance(image,Image.Image):
        precision = 4
        inputs = numpy.linspace(0,255,round(256/precision))
        outputs = numpy.exp(inputs)
        outputs = outputs*255/outputs[len(outputs)-1]
        inputs = list(numpy.asarray(inputs,dtype=numpy.uint8))
        outputs = list(numpy.asarray(outputs,dtype=numpy.uint8))
        
        images = getChannel(image,channel)
        #matrices = numpy.zeros((images[0].shape[0],images[0].shape[1],len(images)))
        #i = 0
        matrices = []
        for img in images:
            #matrices[:,:,i] = levels(img,'',list(inputs),list(outputs))
            #i+=1
            matrices.append(levels(img,'',list(inputs),list(outputs)))
        image = recompose(image,channel,matrices)
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in expHistogram')

    return image



def curves(image,channel,inputs,outputs): # S-curve function for more precise levels adjustment
    
    if (isinstance(image,Image.Image) or isinstance(image,numpy.ndarray)) and (type(inputs) is list) and (type(outputs) is list) and (len(inputs)==len(outputs)):
        precision = 4
        X = numpy.linspace(0,255,len(inputs))
        X2 = numpy.linspace(0,255,round(256/precision))
        # We interpolate inputs and outputs values to recreate the curves from the point the user selected
        f = scipy.interpolate.interp1d(X,inputs,kind='cubic')
        inputs = f(X2)
        f = scipy.interpolate.interp1d(X,outputs,kind='cubic')
        outputs = f(X2)

        inputs = list(numpy.asarray(inputs,dtype=numpy.uint8))
        outputs = list(numpy.asarray(outputs,dtype=numpy.uint8))

        # Those values are now transmitted to the levels function
        
        if isinstance(image,Image.Image):
            channels = getChannel(image,channel)
        elif image.size == image.shape[0]*image.shape[1]: # 2D numpy array
            channels = image
        else:
            raise NameError('PhotoWizard Error: Wrong argument format in levels')

        #matrices = numpy.zeros((channels[0].shape[0],channels[0].shape[1],len(channels)))
        #matrices.setflags(write=True)
        matrices = []
        #i = 0
        for img in channels:
            #matrices[:,:,i] = levels(img,'',list(inputs),list(outputs))
            #i+=1
            matrices.append(levels(img,'',inputs,outputs))
        if isinstance(image,Image.Image):
            image = recompose(image,channel,matrices)
        else:
            image = matrices
    else:
        raise NameError('PhotoWizard Error: Wrong argument format in curves')
    
    return image



