#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This module contains different filters related functionalities

import numpy
import math
from PIL import Image
from scipy import signal
from tools import *



def filterz(img,channel,F): # convolves the image by the 2D-filter F
    
    if (isinstance(img,Image.Image) and isinstance(F,numpy.ndarray) and (type(channel) is str)):
        
        images = getChannel(img,channel)
        matrices = []
        for elt in images:
            
            #tmp = signal.convolve(numpy.asarray((elt),dtype=numpy.uint8),F,mode='same',boundary='symm')
            tmp = numpy.asarray(elt,dtype=numpy.uint8)
            a = math.floor(F.shape[0]/2)
            b = math.floor(F.shape[1]/2)
            Atmp = tmp.shape[0]
            Btmp = tmp.shape[1]
            
            # We extend the array by symmetry before convolution by the kernel F
            tmp = numpy.pad(tmp,((a,a),(b,b)),mode='symmetric')
            tmp = signal.fftconvolve(tmp,F,mode='same')
           
            #tmp = signal.convolve(tmp,F,mode='same')
            if F.dtype==numpy.complex64:
               tmp = numpy.absolute(tmp)
           
            # And we crop it down to the original size
            tmp = tmp[a:Atmp+a,b:Btmp+b]
            
            matrices.append(numpy.asarray(tmp,dtype=numpy.uint8))
        
        image = recompose(img,channel,matrices)
    
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in filterz')
    
    return image




def lowPass(filterType,parameters): # Generates a low-pass filter


    try:
        filterType = str(filterType)
        parameters = list(parameters)
    except:
        raise NameError('PhotoWizard Error: Wrong filter type format')
        filterType = "NC"
        parameters = []


    #----------- 2D FILTERS ----------#
    if filterType == "GAUSSIAN-2D":
        try:
            radius = int(parameters[0])
            a = abs(float(parameters[1]))
        except:
            raise NameError('PhotoWizard Error: Wrong parameters for gaussian low-pass filter')
       
        F = []
        for elt in range(-radius,radius+1):
            F.append(math.exp(-a*elt**2))
        F1 = numpy.asarray([F],dtype=numpy.float16)
        F2 = F1.reshape((F1.size,1))
        F = numpy.multiply(F2,F1)
        F = F/numpy.sum(F)


    elif filterType == "MEAN-2D":
        try:
            radius = int(parameters[0])
            opacity = float(parameters[1])
        except:
            raise NameError('PhotoWizard Error: Wrong parameters for mean low-pass filter')
        
        F = opacity*numpy.ones((2*radius+1,2*radius+1),dtype=numpy.float16)
        F[radius,radius] = 1
        F = F/numpy.sum(F)
        

    elif filterType == "POISSON-2D":
        try:
            radius = int(parameters[0])
            a = abs(float(parameters[1]))
        except:
            raise NameError('PhotoWizard Error: Wrong parameters for poisson low-pass filter')

        F = []
        for elt in range(-radius,radius+1):
            F.append(a*abs(elt)*math.exp(-a*abs(elt)))
        F1 = numpy.asarray([F],dtype=numpy.float16)
        F2 = F1.reshape((F1.size,1))
        F = numpy.multiply(F2,F1)
        F = F/numpy.sum(F)


    #----------- 1D FILTERS ----------#
               # Horizontal #
    elif filterType == "GAUSSIAN-1D":
        try:
            radius = int(parameters[0])
            a = abs(float(parameters[1]))
            theta = float(parameters[2])
        except:
            raise NameError('PhotoWizard Error: Wrong parameters for gaussian low-pass filter')
       
        F = []
        for elt in range(-radius,radius+1):
            F.append(math.exp(-a*elt**2))
        F1 = numpy.asarray([F],dtype=numpy.float16)
        F2 = numpy.zeros((2*radius+1,2*radius+1),dtype=numpy.float16)
        F2[radius,:] = F1
        F = F2/numpy.sum(F2)
        if theta != 0:
            F = rotate(numpy.asarray(F,dtype=numpy.float32),theta)

    elif filterType == "MEAN-1D":
        try:
            radius = int(parameters[0])
            opacity = float(parameters[1])
            theta = float(parameters[2])
        except:
            raise NameError('PhotoWizard Error: Wrong parameters for mean low-pass filter')
        
        F1 = opacity*numpy.ones((1,2*radius+1),dtype=numpy.float16)
        F2 = numpy.zeros((2*radius+1,2*radius+1),dtype=numpy.float16)
        F2[radius,:] = F1
        F2[radius,radius] = 1
        F = F2/numpy.sum(F2)
        if theta != 0:
            F = rotate(numpy.asarray(F,dtype=numpy.float32),theta)

    elif filterType == "POISSON-1D":
        try:
            radius = int(parameters[0])
            a = abs(float(parameters[1]))
            theta = float(parameters[2])
        except:
            raise NameError('PhotoWizard Error: Wrong parameters for poisson low-pass filter')

        F = []
        for elt in range(-radius,radius+1):
            F.append(a*abs(elt)*math.exp(-a*abs(elt)))
        F1 = numpy.asarray([F],dtype=numpy.float16)
        F2 = numpy.zeros((2*radius+1,2*radius+1),dtype=numpy.float16)
        F2[radius,:] = F1
        F = F2/numpy.sum(F2)
        if theta != 0:
            F = rotate(numpy.asarray(F,dtype=numpy.float32),theta)


    else:
        raise NameError('PhotoWizard Error: Unknown low-pass filter type')
        
        F = numpy.asarray([1])
        

    return F




def highPass(filterType,parameters): # Generates a high-pass filter

    try:
        filterType = str(filterType)
    except:
        raise NameError('PhotoWizard Error: Wrong filter type format')
        filterType = "NC"



    #----------- 2D FILTERS ----------#
    
    if filterType == "DIFF-2D":
        try:
            radius = int(parameters[0])
        except:
            raise NameError('PhotoWizard Error: Wrong parameters for diff high-pass filter')
        
        F = numpy.zeros((2*radius+1,2*radius+1),dtype=numpy.complex64)
        F[0,:] += 1
        F[2*radius,:] += -1
        F[:,0] += 1j
        F[:,2*radius] += -1j
        F = F/(2*radius+1)**2
 
    
    #----------- 1D FILTERS ----------#
               # Horizontal #
    elif filterType == "DIFF-1D":
        try:
            radius = int(parameters[0])
            theta = float(parameters[1])
        except:
            raise NameError('PhotoWizard Error: Wrong parameters for diff high-pass filter')
        
        #F1 = numpy.ones((2*radius+1,1),dtype=numpy.float16)
        F = numpy.zeros((2*radius+1,3),dtype=numpy.float16)
        F[:,0] += 1
        F[:,2] += -1
        F = F/(2*radius+1)
        if theta !=0:
            F = rotate(numpy.asarray(F,dtype=numpy.float32),theta)
            F = numpy.asarray(F,dtype=numpy.float16)

        print(F)

    else:
        raise NameError('PhotoWizard Error: Unknown high-pass filter type')

        F = numpy.asarray([1])

    return F



def edgeDetection(img,channel,filterType,parameters,threshold):
    
    if(isinstance(img,Image.Image) and type(filterType) is str and type(parameters) is list and type(threshold) is int):
        
        if (threshold > 0) and (threshold < 255):

            #filter mat with a highpass filter
            image = filterz(img,channel,highPass(filterType,parameters))
            channels = getChannel(image,channel)

            shape = list(image.size)
            shape = tuple(shape[::-1])

            image = numpy.zeros(shape,dtype=numpy.uint8)
            for elt in channels:
                image += elt
            image = image/len(channels)

            #map the values to grayscale
            elt = 255*numpy.asarray(image>threshold,dtype=numpy.uint8)

            image = recompose(img,'ALL',[elt,elt,elt])

        else:
            raise NameError('PhotoWizard Error: Wrong argument format in edgeDetection')

    else:
        raise NameError('PhotoWizard Error: Wrong argument type in edgeDetection')
        image = img

    return image



def edgeEnhancement(img,channel,filterType,parameters,threshold,gain):
     
    if(isinstance(img,Image.Image) and (type(channel) is str) and (type(filterType) is str) and (type(parameters) is list) and (type(threshold) is int) and (type(gain) is float) and (gain<=1) and (gain>=0)):
        
        image = edgeDetection(img,channel,filterType,parameters,threshold)
        channels_old = getChannel(img,channel)
        channels_new = getChannel(image,channel)

        image = []
        for i in range(0,len(channels_old)):
            image.append(channels_old[i]*1-gain*((channels_new[i]>0)*channels_old[i]))

        image = recompose(img,channel,image)
        
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in edgeEnhancement')
        image = img
    
    return image




