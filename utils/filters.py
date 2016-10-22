#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This module contains different filters related functionalities

import numpy



def filterz(mat,matFir): # convolves the 2D-matrix mat by the 2D-filter matFir


    return mat




def lowPass(filterType,parameters): # Generates a low-pass filter

    try:
        filterType = str(filterType)
    except
        raise NameError('PhotoWizard Error: Wrong filter type format')
        filterType = "NC"


    if filterType == "GAUSSIAN":
        try:
            radius = int(parameters[0])
            a = float(parameters[1])
        except
            raise NameError('PhotoWizard Error: Wrong parameters for gaussian low-pass filter')
        
        mat = 0


    elif filterType == "MEAN":
        try:
            radius = int(parameters[0])
        except
            raise NameError('PhotoWizard Error: Wrong parameters for mean low-pass filter')

        mat = 0

    elif filterType == "POISSON":
        try:
            radius = int(parameters[0])
            a = float(parameters[1])
        except
            raise NameError('PhotoWizard Error: Wrong parameters for poisson low-pass filter')

        mat = 0

    else:
        raise NameError('PhotoWizard Error: Unknown low-pass filter type')
        
        mat = 0
        

    return mat




def highPass(filterType,parameters): # Generates a high-pass filter

    try:
        filterType = str(filterType)
    except
        raise NameError('PhotoWizard Error: Wrong filter type format')
        filterType = "NC"



    if filterType == "DIFF":
        try:
            radius = int(parameters[0])
        except
            raise NameError('PhotoWizard Error: Wrong parameters for diff low-pass filter')
        
        mat = 0


    else:
        raise NameError('PhotoWizard Error: Unknown high-pass filter type')

        mat = 0


    return mat



