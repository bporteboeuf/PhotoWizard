#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This module contains different filters related functionalities

import numpy
import math
from PIL import Image
from scipy import signal,ndimage




def filterz(mat,F): # convolves the 2D-matrix mat by the 2D-filter F
    mat = signal.convolve2d(mat,F,mode='same',boundary='symm')
    return mat




def lowPass(filterType,parameters): # Generates a low-pass filter

    try:
        filterType = str(filterType)
    except
        raise NameError('PhotoWizard Error: Wrong filter type format')
        filterType = "NC"


    #----------- 2D FILTERS ----------#
    if filterType == "GAUSSIAN-2D":
        try:
            radius = int(parameters[0])
            a = float(parameters[1])
        except
            raise NameError('PhotoWizard Error: Wrong parameters for gaussian low-pass filter')
       
        F = []
        for elt in range(-radius,radius):
            F.append(math.exp(a*elt**2))
        F1 = numpy.asarray(F,dtype=numpy.float32)
        F2 = F1.reshape((F1.size,1))
        F = numpy.multiply(F2,F1)
        F = F/numpy.sum(F)


    elif filterType == "MEAN-2D":
        try:
            radius = int(parameters[0])
        except
            raise NameError('PhotoWizard Error: Wrong parameters for mean low-pass filter')
        
        F = numpy.array((2*radius+1,2*radius+1),dtype=numpy.float32)
        F = F/numpy.sum(F)
        

    elif filterType == "POISSON-2D":
        try:
            radius = int(parameters[0])
            a = float(parameters[1])
        except
            raise NameError('PhotoWizard Error: Wrong parameters for poisson low-pass filter')

        F = []
        for elt in range(-radius,radius):
            F.append(a*elt*math.exp(-a*elt))
        F1 = numpy.asarray(F,dtype=numpy.float32)
        F2 = F1.reshape((F1.size,1))
        F = numpy.multiply(F2,F1)
        F = F/numpy.sum(F)


    #----------- 1D FILTERS ----------#
               # Horizontal #
    if filterType == "GAUSSIAN-1D-H":
        try:
            radius = int(parameters[0])
            a = float(parameters[1])
        except
            raise NameError('PhotoWizard Error: Wrong parameters for gaussian low-pass filter')
       
        F = []
        for elt in range(-radius,radius):
            F.append(math.exp(a*elt**2))
        F1 = numpy.asarray(F,dtype=numpy.float32)
        F2 = numpy.zeros((2*radius+1,2*radius+1),dtype=numpy.float32)
        F2[radius,:] = F1
        F = F2/numpy.sum(F2)


    elif filterType == "MEAN-1D-H":
        try:
            radius = int(parameters[0])
        except
            raise NameError('PhotoWizard Error: Wrong parameters for mean low-pass filter')
        
        F1 = numpy.ones((1,2*radius),dtype=numpy.float32)
        F2 = numpy.zeros((2*radius+1,2*radius+1),dtype=numpy.float32)
        F2[radius,:] = F1
        F = F2/numpy.sum(F2)
       

    elif filterType == "POISSON-1D-H":
        try:
            radius = int(parameters[0])
            a = float(parameters[1])
        except
            raise NameError('PhotoWizard Error: Wrong parameters for poisson low-pass filter')

        F = []
        for elt in range(-radius,radius):
            F.append(a*elt*math.exp(-a*elt))
        F1 = numpy.asarray(F,dtype=numpy.float32)
        F2 = numpy.zeros((2*radius+1,2*radius+1),dtype=numpy.float32)
        F2[radius,:] = F1
        F = F2/numpy.sum(F2)


    else:
        raise NameError('PhotoWizard Error: Unknown low-pass filter type')
        
        F = numpy.asarray([1])
        

    return F




def highPass(filterType,parameters): # Generates a high-pass filter

    try:
        filterType = str(filterType)
    except
        raise NameError('PhotoWizard Error: Wrong filter type format')
        filterType = "NC"



    #----------- 2D FILTERS ----------#
    
    if filterType == "DIFF-2D":
        try:
            radius = int(parameters[0])
        except
            raise NameError('PhotoWizard Error: Wrong parameters for diff low-pass filter')
        
        F1 = numpy.ones((2*radius+1,1),dtype=numpy.float32)
        F2 = numpy.ones((1,2*radius+1),dtype=numpy.float32)
        F = numpy.zeros((2*radius+1,2*radius+1),dtype=numpy.float32)
        F[0,:] += F1
        F[2*radius,:] += -F1
        F[:,0] += F2
        F[:,2*radius] += -F2
        F = F/numpy.sum(F)
 
    
    #----------- 1D FILTERS ----------#
               # Horizontal #
    if filterType == "DIFF-1D-H":
        try:
            radius = int(parameters[0])
        except
            raise NameError('PhotoWizard Error: Wrong parameters for diff low-pass filter')
        
        #F1 = numpy.ones((2*radius+1,1),dtype=numpy.float32)
        F2 = numpy.ones((1,2*radius+1),dtype=numpy.float32)
        F = numpy.zeros((2*radius+1,2*radius+1),dtype=numpy.float32)
        #F[0,:] += F1
        #F[2*radius,:] += -F1
        F[:,0] += F2
        F[:,2*radius] += -F2
        F = F/numpy.sum(F)


    else:
        raise NameError('PhotoWizard Error: Unknown high-pass filter type')

        F = numpy.asarray([1])


    return F




def rotate(mat,theta): # Rotates a 2D matrix by an angle theta in degrees
    if (type(theta) is int) and (type(mat) is numpy.array):
        
        mat = ndimage.interpolation.rotate(mat,theta)
        
        """
        # PIL Library
        a = numpy.amin(mat)
        b = numpy.amax(mat)
        mat2 = (mat-a)*255/(b-a)
        mat2 = numpy.array(mat2,dtype=numpy.uint8)
        mat2 = Image.fromarray(mat2)
        mat2.rotate(theta)
        mat2 = numpy.asarray(mat2,dtype=mat.dtype)
        mat = mat2*(b-a)/255+a        
        """

    else:
        raise NameError('PhotoWizard Error: Wrong argument type in rotate function')

    return mat


"""
def cubicSpline(oldCoordinates,matrix,newCoordinates): # Interpolation of a 2D matrix using piecewise cubic spline interpolation


    return matrix





def rotate(mat,theta): # Rotates a 2D matrix mat by an angle theta in radians
    if (type(theta) is int) and (type(mat) is numpy.array):
        # First, we calculate the rotation matrix
        rotation = numpy.asarray([[math.cos(theta) -math.sin(theta)],[math.sin(theta) math.cos(theta)]],dtype=numpy.float32)
        a = mat.shape[0]
        b = mat.shape[1]

        # Then we compute the old and new coordinates of the values to interpolate, thanks to the rotation matrix
        coordinates = numpy.zeros((a,b,2),dtype=numpy.float32)
        newCoordinates = numpy.array(coordinates)
        for i in range(1,a):
            y = (i-a/2)
            for j in range(1,b):
                x = (j-b/2)
                coordinates[,i-1,j-1] = [x,y]
                XY = numpy.array([[x],[y]],dtype=numpy.float32)
                XY = numpy.multiply(rotation,XY)
                newCoordinates[,i-1,j-1] = [XY[0],XY[1]]

        # Now we can interpolate the matrix at the new coordinates
        mat = cubicSpline(coordinates,mat,newCoordinates)
        
    else:
        raise NameError('PhotoWizard Error: Wrong argument type in rotate function')

    return mat
"""

