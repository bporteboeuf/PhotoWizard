# -*- coding: utf-8 -*-

#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#


# This module contains levels related functions

import numpy,math,scipy
from PIL import Image
from tools import getChannel,recompose
from loadConfig import *


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

                # We make sure to cover all points
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



def normalizeHistogram(image,channel): # Automatic contrast adjustment by extending the dynamic range to a standard 256 width
    if isinstance(image,Image.Image):

        images = getChannel(image,channel)
        matrices = []
        for img in images:
            # We compute the coefficients
            a = numpy.amin(img)
            b = numpy.amax(img)
            if a==b :
                b = a+1
            alpha = 255/(b-a)

            # And we normalize the picture
            tmp = numpy.asarray((img-a)*alpha,dtype=numpy.uint8)
            matrices.append(tmp)

        image = recompose(image,channel,matrices)
    
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in normalizeHistogram')

    return image




def equalizeHistogram(image,channel): # Automatic contrast adjustment
    if isinstance(image,Image.Image):

        precision = EQHIST_RESOLUTION
        inputs = numpy.linspace(0,255,round(256/precision))
        
        images = getChannel(image,channel)
        matrices = []
        for img in images:
            # We get the histogram
            histogram, bins = numpy.histogram(img,bins=int(round(256/precision)),range=(0,255))
            outputs = numpy.cumsum(histogram)
            outputs = outputs*255/numpy.amax(outputs)
            # And we use the normalized cumulative summation of it as a tone-curve
            inputs = list(numpy.asarray(inputs,dtype=numpy.uint8))
            outputs = list(numpy.asarray(outputs,dtype=numpy.uint8))
            matrices.append(levels(img,'',list(inputs),list(outputs)))

        image = recompose(image,channel,matrices)
    
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in equalizeHistogram')

    return image




def logHistogram(image,channel): # Automatic contrast adjustment recover details in low values
    if isinstance(image,Image.Image):

        precision = LOGHIST_RESOLUTION
        # A normalized logarithmic tone-curve is generated
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

        precision = EXPHIST_RESOLUTION
        # A normalized exponential tone-curve is generated
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

        precision = CURVES_RESOLUTION
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
            #a = numpy.amin(img) + 1
            #b = numpy.amax(img) + 1
            m = numpy.mean(img)

            # We compute the coefficient
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
        # Exposure is modified by applying a tone-curve on the image. The curve is smoothed to reduce clipping effects and an offset is added to provide more natural looking results

        precision = EXPOSURE_RESOLUTION

        channels = getChannel(image,channel)

        matrices = []
        for img in channels:

            inputs = numpy.linspace(0,255,round(256/precision))
            X = inputs/255

            alpha = 1 + abs(ev) #This is the steep of the curve around 0 if ev > 0 or around 1 if ev < 0
            beta = numpy.log(alpha)/(6) # This is the absolute value of the offset of the curve around 0 if ev > 0 or around 1 if ev < 0

            # The curve f needs to satisfy the 5 following conditions, assuming ev > 0, and considering the interval I = [0,1]
            # 1) f(0) = beta      2) f'(0) = alpha     3) f(1) = 1      4) f' >= 0 sur I     5) f'' <= 0 sur I
            # It can be shown that no second order polynomial can satisfy all those conditions, and no trivial polynomial of degree three either.
            # We could however use an exponential curve, but this could not fit the tangent long enough, so we decide to to a continuous piecewise function

            # First, we compute the straight line for exposure correction
            Y1 = X*alpha + beta

            # And we stop it halfway up
            xM = .5*(1-beta)/alpha
            yM = xM*alpha+beta

            # Then we extend it by an exponential function for smoother results and avoid too rough clipping
            A = 1-yM
            B = A
            tau = B/alpha
            X2 = numpy.zeros(len(X))
            I = numpy.sum(X<=xM)-1
            X2[I:] = numpy.linspace(0,1-xM,len(X)-I)
            Y2 = B*(1-numpy.exp(-X2/tau))
            diff = numpy.amin(A-Y2)

            # We adjust the parameters B and tau to keep the same steep but reach 1 (in order to satisfy 3,5 and have a smooth transition)
            while abs(diff) > .001:
                B = B + diff
                tau = B/alpha
                Y2 = B*(1-numpy.exp(-X2/tau))
                diff = numpy.amin(A-Y2)

            Y2 = Y2+yM
            Y = Y1*(X<=xM) + Y2*(X>xM) # We merge the two functions into one piecewise function


            if ev < 0: # We perform a central symmetry (rotation of pi)
                Z = X +1j*Y
                Z = Z - .5*(1+1j)
                Z = Z*numpy.exp(-1j*numpy.pi)
                Z = Z + .5*(1+1j)
                X = numpy.real(Z)
                Y = numpy.imag(Z)
                X = X[::-1]
                Y = Y[::-1]

            inputs = numpy.asarray(255*X,dtype=numpy.uint8)
            outputs = numpy.asarray(255*Y,dtype=numpy.uint8) # We scale our results

            # And we apply it to our image
            # We can either do this using the levels function
            img = levels(img,'',list(inputs),list(outputs))

            # Or direclty apply our function to the image converted to an array

            matrices.append(img)
        
        image = recompose(image,channel,matrices)
    else:
        raise NameError('PhotoWizard Error: Wrong argument format in exposure')
    

    return image



def blackAndWhite(image,channel): # Converts a picture or part of it to a black and white image (grayscale)

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


