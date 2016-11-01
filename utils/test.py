#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This module contains tests for the whole software

try:
    import filters,helpm,history,levels,main,tools
    from tools import Picture
    from history import History, Event
    from config import *
    import sys,numpy,scipy,math
    from PIL import Image
except:
   raise NameError('PhotoWizard Error: unable to load dependencies')



###***--- THE EVENT CLASS ---***###
def eventClass():

    score = 0

    # Init
    try:
        eventA = Event(1,None,('action',['parameters']),'eventA')
        eventB = Event(2,1,('action',['parameters']),'eventB')
        eventC = Event(3,None,('action',['parameters']),'eventC')
        score+=1
    except Exception as exception:
        print(exception)

    # Class methods
    try:
        eventA.getID()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        eventA.getNext()
        score+=1
    except Exception as exception:
        print(exception)
    
    try:
        eventA.setNext(3)
        score+=1
    except Exception as exception:
        print(exception)

    try:
        eventC.getPrevious()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        eventC.setPrevious(1)
        score+=1
    except Exception as exception:
        print(exception)

    try:
        eventB.getContent()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        eventB.setContent(('action2',['params2']))
        score+=1
    except Exception as exception:
        print(exception)

    try:
        eventB.getLabel()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        eventB.setLabel('EVENTB')
        score+=1
    except Exception as exception:
        print(exception)


    return round(1000*score/10)/10




###***--- THE HISTORY CLASS ---***###
def historyClass():

    score = 0

    # Init
    try:
        hist = History(1)
        score+=1
    except Exception as exceptio:
        print(exception)

    # Class methods
    try:
        hist.add(('action',['parameters']),'eventA')
        hist.add(('action',['parameters']),'eventB')
        score+=1
    except Exception as exception:
        print(exception)

    try:
        hist.getCurrentState()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        hist.setCurrentState(2)
        score+=1
    except Exception as exception:
        print(exception)

    try:
        hist.getEvent(1)
        score+=1
    except Exception as exception:
        print(exception)

    try:
        hist.undo()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        hist.redo()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        hist.rebase(1)
        score+=1
    except Exception as exception:
        print(exception)

    try:
        hist.getHistory()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        hist.getFullHistory()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        hist.clearHistory()
        score+=1
    except Exception as exception:
        print(exception)


    return round(1000*score/11)/10




###***--- THE PICTURE CLASS ---***###
def pictureClass():

    score = 0

    # Init
    try:
        image = Picture(1,"pic/test1.jpg")
        score+=1
    except Exception as exception:
        print(exception)

    # Class methods
    try:
        (isinstance(image.asImage(),Image.Image))
        score+=1
    except Exception as exception:
        print(exception)
    
    try:
        image.asArray()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        (isinstance(image.smallAsImage(),Image.Image))
        score+=1
    except Exception as exception:
        print(exception)

    try:
        image.smallAsArray()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        image.resizeSmall((20,30))
        score+=1
    except Exception as exception:
        print(exception)
    
    try:
        image.getHistory()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        image.setHistory(image.getHistory())
        score+=1
    except Exception as exception:
        print(exception)

    try:
        image.reCompute()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        image.export('pic/test1-2.jpg')
        score+=1
    except Exception as exception:
        print(exception)

    try:
        image.close()
        score+=1
    except Exception as exception:
        print(exception)


    return round(1000*score/11)/10





###***--- THE FILTERS FILE ---***###
def filtersTest():
    
    score= 0

    # Filters generation
    try:
        f = filters.lowPass('GAUSSIAN-2D',[5,0.5])
        score+=1
    except Exception as exception:
        print(exception)

    try:
        f = filters.lowPass('GAUSSIAN-1D',[10,2])
        score+=1
    except Exception as exception:
        print(exception)

    try:
        f = filters.lowPass('MEAN-2D',[3])
        score+=1
    except Exception as exception:
        print(exception)

    try:
        f = filters.lowPass('MEAN-1D',[6])
        score+=1
    except Exception as exception:
        print(exception)

    try:
        f = filters.lowPass('POISSON-2D',[5,2])
        score+=1
    except Exception as exception:
        print(exception)
    
    try:
        f = filters.lowPass('POISSON-1D',[10,0.7])
        score+=1
    except Exception as exception:
        print(exception)

    try:
        f = filters.highPass('DIFF-2D',[5])
        score+=1
    except Exception as exception:
        print(exception)

    try:
        f = filters.highPass('DIFF-1D',[10])
        score+=1
    except Exception as exception:
        print(exception)


    # Filters rotation
    try:
        f = filters.rotate(numpy.zeros((5,5)),15)
        score+=1
    except Exception as exception:
        print(exception)


    # Filters application
    try:
        f = filters.filterz(numpy.zeros((3,3)),numpy.zeros((3,3)))
        score+=1
    except Exception as exception:
        print(exception)


    # Others
    try:
        f = filters.edgeDetection(numpy.zeros((3,3)),'filterType',10,100)
        score+=1
    except Exception as exception:
        print(exception)
    
    try:
        f = filters.edgeEnhancement(numpy.zeros((3,3)),'filterType',10,100,5)
        score+=1
    except Exception as exception:
        print(exception)



    return round(1000*score/12)/10




###***--- THE LEVELS FILE ---***###
def levelsTest():

    # levels

    # automatic adjustments

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
    print('Event Class Tests')
    res = eventClass()
    print('   - score: '+str(res)+"%\n")
    print('History Class Tests')
    res = historyClass()
    print('   - score: '+str(res)+"%\n")
    print('Picture Class Tests')
    res = pictureClass()
    print('   - score: '+str(res)+"%\n")
    print('Filters Module Tests')
    res = filtersTest()
    print('   - score: '+str(res)+"%\n")
    print('Levels Module Tests')
    res = levelsTest()
    print('   - score: '+str(res)+"%\n")
    print('Tools Module Tests')
    res = toolsTest()
    print('   - score: '+str(res)+"%\n")
    print('User Case 1')
    res = userCase1()
    print('   - score: '+str(res)+"%\n")
    print('User Case 2')
    res = userCase2()
    print('   - score: '+str(res)+"%\n")
    print('User Case 3')
    res = userCase3()
    print('   - score: '+str(res)+"%\n")
    print('Done.')

    sys.exit(0)

    
