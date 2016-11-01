#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This module contains tests for the whole software

try:
    import filters,helpm,history,levels,main,tools
    from config import *
    import sys,numpy,scipy,math
    from PIL import Image
except:
   raise NameError('PhotoWizard Error: unable to load dependencies')


###***--- THE PICTURE CLASS ---***###
def pictureClass():

    # Init

    # Class methods

    return 0


###***--- THE EVENT CLASS ---***###
def eventClass():

    # Init

    # Class methods

    return 0


###***--- THE HISTORY CLASS ---***###
def historyClass():

    # Init

    # Class methods

    return 0


###***--- THE FILTERS FILE ---***###
def filtersTest():
    
    # Filters generation


    # Filters rotation


    # Filters application


    return 0


###***--- THE HELPM FILE ---***###
def helpmTest():

    # User cases

    return 0


###***--- THE LEVELS FILE ---***###
def levelsTest():

    # levels

    # automatic adjustments

    return 0


###***--- THE MAIN FILE ---***###
def mainTest():


    return 0


###***--- THE TOOLS FILE ---***###
def toolsTest():

    # every tools

    return 0


###***--- A FEW USERCASES ---***###

## UserCase1
def userCase1():

    return 0

## UserCase2
def userCase2():
    
    return 0

## UserCase3
def userCase3():

    return 0



#########################
#########################
#####    M A I N    #####
#########################
#########################


if len(sys.argv) > 1:
    # We run the desired tests
    """
    try:
        options = str(sys.argv[1:])
    except:
        raise NameError('PhotoWizard Error: Wrong format for launching options in test')
        options = ""

    start = False
    for elt in options:
        
        if elt == "-":
            start = True
        
        if start:
            if elt == "v":
                try:
                    print("Current Version of PhotoWizard: "+str(VER))
                except:
                    raise NameError('PhotoWizard Error: Wrong version format in config')
                launched = True
    """
    print('PhotoWizard Error: launching options currenly not supported in test')

else:
    # We run all tests
    print('\n\n   ### PhotoWizard TestBench ###\n\n')
    res = pictureClass()
    print('Picture class - score: '+str(res*100)+"%\n")
    res = eventClass()
    print('Event class - score: '+str(res*100)+"%\n")
    res = historyClass()
    print('History class - score: '+str(res*100)+"%\n")
    res = filtersTest()
    print('Filters module - score: '+str(res*100)+"%\n")
    res = helpmTest()
    print('Help module - score: '+str(res*100)+"%\n")
    res = levelsTest()
    print('Levels module - score: '+str(res*100)+"%\n")
    res = mainTest()
    print('Main module - score: '+str(res*100)+"%\n")
    res = toolsTest()
    print('Tools module - score: '+str(res*100)+"%\n")
    res = userCase1()
    print('User case 1 - score: '+str(res*100)+"%\n")
    res = userCase2()
    print('USer case 2 - score: '+str(res*100)+"%\n")
    res = userCase3()
    print('User case 3 - score: '+str(res*100)+"%\n")
    print('Done.')

    
