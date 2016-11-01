#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This module contains levels related functions

import numpy,math,scipy
from PIL import Image


def levels(matrix,inputs,outputs):
    if (type(matrix) is numpy.array) and (type(inputs) is list) and (type(outputs) is list) :
        if (len(intputs) == len(outputs)) and (0<min(inputs)) and (0<min(outputs)) and (255>max(inputs)) and (255>max(outputs)):
    
            # We first analyze which region of the matrix is in each inputs interval
            # And we normalize it (affine) so it fits in the corresponding outputs interval

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
                alpha = (ob-oa)/(ib-ia)
                beta = ob - alpha*ib

                # We get the indexes of elements in our inputs interval
                under = numpy.where(matrix<=ib)
                over = numpy.where(matrix>=ia)

                # Then we build an indicator matrix
                eltUnder = zeros(matrix.shape,dtype=uint8)
                eltUnder[under] = 1
                eltOver = zeros(matrix.shape,dtype=uint8)
                eltOver[over] = 1

                eltInterval = eltUnder*eltOver
                indexes = where(eltInterval>0)

                # And we finally compute the wanted values
                matrix[indexes] = matrix[indexes]*alpha+beta

        else:
            raise NameError('PhotoWozard Error: Wrong argument format in levels')
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in levels')

    return matrix



def getChannel(image,channel): # Channel can be H, S, V, R, G, B or ALL - Note: if BW, should use V or ALL?
 
    if (type(image) is Image.Image) and (type(channel) is str):
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
                raise NameError('PhotoWizard Error: unexpected argument in channelLevels')
        elif len(channel) == 3:
            if channel == 'ALL':
                image = image.convert('HSV')
                image = numpy.asarray(image,dtype=numpy.uint8)
                image = [image[:,:,0],image[:,:,1],image[:,:,2]]
            else:
                raise NameError('PhotoWizard Error: unexpected argument in channelLevels')
        else:
            raise NameError('PhotoWizard Error: unexpected argument in channelLevels')
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in channelLevels')

    return image




def normalizeHistogram(image,channel): # Automatic contrast adjustment
    if (type(image) is Image.Image):
        images = getChannel(image,channel)
        image = numpy.zeros((images[0].shape,images[1].shape,len(images)))
        i = 0
        for img in images:
            a = numpy.amin(img)
            b = numpy.amax(img)

            image[:,:,i] = (img-a)*255/(b-a)
            i+=1
        image = Image.fromarray(image)
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in normalizedHistogram')

    return image




def equalizeHistogram(image,channel): # Automatic contrast adjustment
    if (type(image) is Image.Image):
        precision = 4
        inputs = numpy.linspace(0,255,math.round(256/precision))
        outputs = numpy.log(inputs)
        
        images = getChannel(image,channel)
        image = numpy.zeros((images[0].shape,images[1].shape,len(images)))
        i = 0
        for img in images:
            histogram, bins = numpy.histogram(img,bins=math.round(256/precision),range=(0,255))
            outputs = numpy.cumsum(histogram)
            outputs = outputs*256/outputs[outputs.shape[1]-1]
            image[:,:,i] = levels(img,inputs,outputs)
            i+=1
        image = Image.fromarray(image)
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in normaizedHistogram')

    return image




def logHistogram(image,channel): # Automatic contrast adjustment recover details in low values
    if (type(image) is Image.Image):
        precision = 4
        inputs = numpy.linspace(0,255,math.round(256/precision))
        outputs = numpy.log(inputs)
         
        images = getChannel(image,channel)
        image = numpy.zeros((images[0].shape,images[1].shape,len(images)))
        i = 0
        for img in images:
            image[:,:,i] = levels(img,inputs,outputs)
            i+=1
        image = Image.fromarray(image)
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in normaizedHistogram')

    return image




def expHistogram(image,channel): # Automatic contrast adjustment to recover details in high values
    if (type(image) is Image.Image):
        precision = 4
        inputs = numpy.linspace(0,255,math.round(256/precision))
        outputs = numpy.exp(inputs)
        
        images = getChannel(image,channel)
        image = numpy.zeros((images[0].shape,images[1].shape,len(images)))
        i = 0
        for img in images:
            image[:,:,i] = levels(img,inputs,outputs)
            i+=1
        image = Image.fromarray(image)
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in normaizedHistogram')

    return image



def curves(image,channel,inputs,outputs): # S-curve function for more precise levels adjustment
    
    if (type(image) is Image.Image) and (type(inputs) is list) and (type(outputs) is list) and (len(inputs)==len(outputs)):
        precision = 4
        X = numpy.linspace(0,255,len(inputs))
        X2 = numpy.linspace(0,255,math.round(256/precision))
        # We interpolate inputs and outputs values to recreate the curves from the point the user selected
        f = scipy.interpolate.interp1d(X,inputs,kind='cubic')
        inputs = f(X2)
        f = scipy.interpolate.interp1d(W,outputs,kind='cubic')
        outputs = f(X2)

        # Those values are now transmitted to the levels function
         
        images = getChannel(image,channel)
        image = numpy.zeros((images[0].shape,images[1].shape,len(images)))
        i = 0
        for img in images:
            image[:,:,i] = levels(img,inputs,outputs)
            i+=1
        image = Image.fromarray(image)
    else:
        raise NameError('PhotoWizard Error: Wrong argument format in curves')

    return image



