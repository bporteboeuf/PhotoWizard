#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This module contains mapping tools

import levels,filters
from tools import *


def everyFunction(image,action): # Maps the action in the main or history to the real image editing functions
    if (isinstance(image,Image.Image)) and (type(action) is list):
        try:
            f = action[0]
            params = action[1]
            #params = params[0]
        except:
            raise NameError('PhotoWizard Error: Wrong argument format in everyFunction')
            f = ""
            params = []

        if f == 'InitState': # This is the initialization state for the history
            image = image # We keep the image intact

        elif f == "levels":
            #print(f)
            try:
                params = parseInput(params,[str,str,list,list])
                params = params[1:]
                image = levels.levels(image,params[0],params[1],params[2])
            except Exception as e:
                print(e)
                raise NameError('PhotoWizard Error: Unable to call levels() in everyFunction')
        elif f == "curves":
            #print(f)
            try:
                params = parseInput(params,[str,str,list,list])
                params = params[1:]
                image = levels.curves(image,params[0],params[1],params[2])
            except Exception as e:
                print(e)
                raise NameError('PhotoWizard Error: Unable to call curves() in everyFunction')
        elif f == "normHist":
            #print(f)
            try:
                params = parseInput(params,[str,str])
                params = params[1:]
                image = levels.normalizeHistogram(image,params[0])
            except Exception as e:
                print(e)
                raise NameError('PhotoWizard Error: Unable to call normalizeHistogram() in everyFunction')
        elif f == "eqHist":
            #print(f)
            try:
                params = parseInput(params,[str,str])
                params = params[1:]
                image = levels.equalizeHistogram(image,params[0])
            except Exception as e:
                print(e)
                raise NameError('PhotoWizard Error: Unable to call equalizeHistogram() in everyFunction')
        elif f == "expHist":
            #print(f)
            try:
                params = parseInput(params,[str,str])
                params = params[1:]
                image = levels.expHistogram(image,params[0])
            except Exception as e:
                print(e)
                raise NameError('PhotoWizard Error: Unable to call expHistogram() in everyFunction')
        elif f == "logHist":
            #print(f)
            try:
                params = parseInput(params,[str,str])
                params = params[1:]
                image = levels.logHistogram(image,params[0])
            except Exception as e:
                print(e)
                raise NameError('PhotoWizard Error: Unable to call logHistogram() in everyFunction')
        elif f == "lowPass":    
            #print(f)
            try:
                params = parseInput(params,[str,str,int,float,str])
                params = params[1:]
                image = filters.filterz(image,params[3],filters.lowPass(params[0],[params[1],params[2]]))
            except Exception as e:
                print(e)
                raise NameError('PhotoWizard Error: Unable to call filterz() and/or lowPass() in everyFunction')
        elif f == "highPass":
            #print(f)
            try:
                params = parseInput(params,[str,str,int,str])
                params = params[1:]
                image = filters.filterz(image,params[2],filters.highPass(params[0],[params[1]]))
            except Exception as e:
                print(e)
                raise NameError('PhotoWizard Error: Unable to call filterz() and/or highPass() in everyFunction')
        elif f == "detectEdges":
            #print(f)
            try:
                params = parseInput(params,[str,str,str,int,float])
                params = params[1:]
                image = filters.edgeDetection(image,params[0],params[1],params[2],params[3])
            except Exception as e:
                print(e)
                raise NameError('PhotoWizard Error: Unable to call edgeDetection() in everyFunction')
        elif f == "enhanceEdges":
            #print(f)
            try:
                params = parseInput(params,[str,str,str,int,int,float])
                params = params[1:]
                image = filters.edgeEnhancement(image,params[0],params[1],params[2],params[3],params[4])
            except Exception as e:
                print(e)
                raise NameError('PhotoWizard Error: Unable to call edgeEnhancement() in everyFunction')
        elif f == "rotate":
            #print(f)
            try:
                params = parseInput(params,[str,float])
                params = params[1:]
                image = rotate(image,params[0])
            except Exception as e:
                print(e)
                raise NameError('PhotoWizard Error: Unable to call rotate() in everyFunction')
        elif f == "crop":
            #print(f)
            try:
                params = parseInput(params,[str,list])
                params = params[1:]
                image = crop(image,params[0])
            except Exception as e:
                print(e)
                raise NameError('PhotoWizard Error: Unable to call crop() in everyFunction')
        elif f == "resize":
            #print(f)
            try:
                params = parseInput(params,[str,list])
                params = params[1:]
                image = resize(image,params[0])
            except Exception as e:
                print(e)
                raise NameError('PhotoWizard Error: Unable to call resize() in everyFunction')
        else:
            raise NameError('PhotoWizard Error: Unknown function in everyFunction')

    else:
        raise NameError('PhotoWizard Error: Wrong argument type in everyFunction')

    return image,params




