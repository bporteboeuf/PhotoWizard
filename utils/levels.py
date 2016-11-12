#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This module contains levels related functions

import numpy,math,scipy
from PIL import Image
from tools import getChannel,recompose


def levels(image,channel,inputs,outputs): # Image can be an Image.Image object (same treatment for every selected channel) or a numpy.ndarray (same treatment for every layer)
    if (isinstance(image,Image.Image) or isinstance(image,numpy.ndarray)) and (type(channel) is str) and (type(inputs) is list) and (type(outputs) is list) :
        if (len(inputs) == len(outputs)) and (0<=min(inputs)) and (0<=min(outputs)) and (255>=max(inputs)) and (255>=max(outputs)):
    
            if isinstance(image,Image.Image):
                channels = getChannel(image,channel)
            elif image.size == image.shape[0]*image.shape[1]: # 2D numpy array
                channels = [image]
            else:
                raise NameError('PhotoWizard Error: Wrong argument format in levels')

            matrices = []
            for matrix in channels:

                # We first analyze which region of the matrix is in each inputs interval
                # And we normalize it (affine) so it fits in the corresponding outputs interval

                if max(inputs)<255:
                    inputs.append(255)
                    outputs.append(255)

                if min(inputs)>0:
                    inputs.insert(0,0)
                    outputs.insert(0,0)
                
                matrix2 = numpy.array(matrix,dtype=numpy.uint8)
                matrix2.setflags(write=True)
                for k in range(1,len(inputs)):
                    
                    # input interval
                    if k == 1:
                        ia = float(inputs[0])
                    else:
                        ia = float(ib)
                    ib = float(inputs[k])

                    # output interval
                    if k == 1:
                        oa = float(outputs[0])
                    else:
                        oa = float(ob)
                    ob = float(outputs[k])

                    # coefficients
                    if ib!=ia:
                        alpha = float((ob-oa)/(ib-ia))
                    else:
                        alpha = 0
                    beta = float(oa - alpha*ia)
                  
                    # We build an indicator matrix
                    interval = (matrix<=ib)*(matrix>=ia)
                    indexes = numpy.where(interval)
                    
                    # And we finally compute the wanted values
                    matrix2[indexes] = matrix[indexes]*alpha+beta

                matrices.append(numpy.asarray(matrix2,dtype=numpy.uint8))
        else:
            raise NameError('PhotoWozard Error: Wrong argument format in levels')
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in levels')
    
    if isinstance(image,Image.Image):
        image = recompose(image,channel,matrices)
    else:
        image = matrices

    return image



def normalizeHistogram(image,channel): # Automatic contrast adjustment
    if isinstance(image,Image.Image):
        images = getChannel(image,channel)
        matrices = []
        for img in images:
            a = numpy.amin(img)
            b = numpy.amax(img)
            if a==b :
                b = a+1
            alpha = 255/(b-a)
            tmp = numpy.asarray((img-a)*alpha,dtype=numpy.uint8)
            matrices.append(tmp)
        image = recompose(image,channel,matrices)
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in normalizeHistogram')

    return image




def equalizeHistogram(image,channel): # Automatic contrast adjustment
    if isinstance(image,Image.Image):
        precision = 16
        inputs = numpy.linspace(0,255,round(256/precision))
        
        images = getChannel(image,channel)
        matrices = []
        for img in images:
            histogram, bins = numpy.histogram(img,bins=round(256/precision),range=(0,255))
            outputs = numpy.cumsum(histogram)
            outputs = outputs*255/numpy.amax(outputs)
            inputs = list(numpy.asarray(inputs,dtype=numpy.uint8))
            outputs = list(numpy.asarray(outputs,dtype=numpy.uint8))
            matrices.append(levels(img,'',list(inputs),list(outputs)))
        image = recompose(image,channel,matrices)
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in equalizeHistogram')

    return image




def logHistogram(image,channel): # Automatic contrast adjustment recover details in low values
    if isinstance(image,Image.Image):
        precision = 64
        inputs = numpy.linspace(0,255,round(256/precision))
        outputs = numpy.log(1+inputs/16)
        outputs = outputs*255/outputs[len(outputs)-1]
        inputs = list(numpy.asarray(inputs,dtype=numpy.uint8))
        outputs = list(numpy.asarray(outputs,dtype=numpy.uint8))

        images = getChannel(image,channel)
        matrices = []
        for img in images:
            matrices.append(levels(img,'',list(inputs),list(outputs)))
        image = recompose(image,channel,matrices)
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in logHistogram')

    return image




def expHistogram(image,channel): # Automatic contrast adjustment to recover details in high values
    if isinstance(image,Image.Image):
        precision = 8
        inputs = numpy.linspace(0,255,round(256/precision))
        outputs = numpy.exp(inputs/64)-1
        outputs = outputs*255/outputs[len(outputs)-1]
        inputs = list(numpy.asarray(inputs,dtype=numpy.uint8))
        outputs = list(numpy.asarray(outputs,dtype=numpy.uint8))
       
        images = getChannel(image,channel)
        matrices = []
        for img in images:
            matrices.append(levels(img,'',list(inputs),list(outputs)))
        image = recompose(image,channel,matrices)
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in expHistogram')

    return image



def curves(image,channel,inputs,outputs): # S-curve function for more precise levels adjustment
    if (isinstance(image,Image.Image) or isinstance(image,numpy.ndarray)) and (type(inputs) is list) and (type(outputs) is list) and (len(inputs)==len(outputs)):
        precision = 8
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

        matrices = []
        for img in channels:
            matrices.append(levels(img,'',inputs,outputs))
        if isinstance(image,Image.Image):
            image = recompose(image,channel,matrices)
        else:
            image = matrices
    else:
        raise NameError('PhotoWizard Error: Wrong argument format in curves')
    
    return image




def contrast(image,channel,percentage): # Increases the contrast of the image by the percentage given

    if (isinstance(image,Image.Image)) and (type(channel) is str) and (type(percentage) is int) and abs(percentage) < 100 :
       
        channels = getChannel(image,channel)

        matrices = []
        for img in channels:
            a = numpy.amin(img) + 1
            b = numpy.amax(img) + 1
            m = numpy.mean(img)

            alpha = (1+percentage/100)
            
            img = img*alpha - m*percentage/100 # We maitain the mean value
 
            img[numpy.where(img<0)] = 0 # And we make sure the result is still between 0 and 255
            img[numpy.where(img>255)] = 255
            img = numpy.asarray(img,dtype=numpy.uint8)

            matrices.append(img)
        
        image = recompose(image,channel,matrices)
    else:
        raise NameError('PhotoWizard Error: Wrong argument format in contrast')
 
    return image



def exposure(image,channel,ev):
 
    if (isinstance(image,Image.Image)) and (type(channel) is str) and ((type(ev) is float) or (type(ev) is int)) and (abs(ev) <= 8) :
       
        # A standard measure for exposure value consists of measuring the luminance of a medium 18% gray (ie about 210/255)
        # +1.00 eV means to double the quantity of light, -1.00 eV to divide it by two

        precision = 8

        channels = getChannel(image,channel)

        matrices = []
        for img in channels:

            inputs = numpy.linspace(0,255,round(256/precision))
            X = inputs/255

            alpha = 1 + abs(ev)

            if ev > 0:
                a = alpha-2
                b = 3-2*alpha
                c = alpha
            elif ev < 0:
                a = alpha-2
                b = 3-alpha
                c = 0
            else:
                a = 0
                b = 0
                c = 1

            outputs = 255*(a*X**3+b*X**2+c*X)

            img = levels(img,'',list(inputs),list(outputs))

            matrices.append(img)
        
        image = recompose(image,channel,matrices)
    else:
        raise NameError('PhotoWizard Error: Wrong argument format in exposure')
    

    return image



def blackAndWhite(image,channel):

    if (isinstance(image,Image.Image)) and (type(channel) is str):
       
        channels = getChannel(image,channel)

        if len(channel) == 1:
            channels = numpy.asarray(channels[0],dtype=numpy.uint8)
            image = Image.fromarray(channels,'L')
        
        elif len(channel) == 3:
            image = image.convert('L')

        else:
            raise NameError('PhotoWizard Error: Unsupported number of channels in blackAndWhite')
    else:
        raise NameError('PhotoWizard Error: Wrong argument format in blackAndWhite')
 
    return image

