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
        #print('A')
        eventA = Event(1,None,('action',['parameters']),'eventA')
        eventB = Event(2,1,('action',['parameters']),'eventB')
        eventC = Event(3,None,('action',['parameters']),'eventC')
        score+=1
    except Exception as exception:
        print(exception)

    # Class methods
    try:
        #print('B')
        eventA.getID()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('C')
        eventA.getNext()
        score+=1
    except Exception as exception:
        print(exception)
    
    try:
        #print('D')
        eventA.setNext(3)
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('E')
        eventC.getPrevious()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('F')
        eventC.setPrevious(1)
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('G')
        eventB.getContent()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('H')
        eventB.setContent(('action2',['params2']))
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('I')
        eventB.getLabel()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('J')
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
        #print('A')
        hist = History(1)
        score+=1
    except Exception as exceptio:
        print(exception)

    # Class methods
    try:
        #print('B')
        hist.add(('action',['parameters']),'eventA')
        hist.add(('action',['parameters']),'eventB')
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('C')
        hist.getCurrentState()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('D')
        hist.setCurrentState(2)
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('E')
        hist.getEvent(1)
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('F')
        hist.undo()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('G')
        hist.redo()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('H')
        hist.rebase(1)
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('I')
        hist.getHistory()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('J')
        hist.getFullHistory()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('K')
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
        #print('A')
        image = Picture(1,"pic/test1.jpg")
        score+=1
    except Exception as exception:
        print(exception)

    # Class methods
    try:
        #print('B')
        (isinstance(image.getImage(),Image.Image))
        score+=1
    except Exception as exception:
        print(exception)
   
    try:
        #print('C')
        (isinstance(image.getSmallImage(),Image.Image))
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('D')
        image.resizeSmall((20,30))
        score+=1
    except Exception as exception:
        print(exception)
    
    try:
        #print('E')
        image.getHistory()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('F')
        image.setHistory(image.getHistory())
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('G')
        image.reCompute()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('H')
        image.export('pic/test1-2.jpg')
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('I')
        image.close()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('J')
        image.histogram('ALL')
        score+=1
    except Exception as exception:
        print(exception)


    return round(1000*score/10)/10





###***--- THE FILTERS FILE ---***###
def filtersTest():
    
    score = 0

    # Filters generation
    try:
        #print('A')
        f = filters.lowPass('GAUSSIAN-2D',[5,0.5])
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('B')
        f = filters.lowPass('GAUSSIAN-1D',[10,2])
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('C')
        f = filters.lowPass('MEAN-2D',[3])
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('D')
        f = filters.lowPass('MEAN-1D',[6])
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('E')
        f = filters.lowPass('POISSON-2D',[5,2])
        score+=1
    except Exception as exception:
        print(exception)
    
    try:
        #print('F')
        f = filters.lowPass('POISSON-1D',[10,0.7])
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('G')
        f = filters.highPass('DIFF-2D',[5])
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('H')
        f = filters.highPass('DIFF-1D',[10])
        score+=1
    except Exception as exception:
        print(exception)


    # Filters rotation
    try:
        #print('I')
        img = Image.open('pic/test1.jpg')
        img = img.resize((50,50),Image.ANTIALIAS) # This will speed up the process
        f = filters.rotate(img,15)
        score+=1
    except Exception as exception:
        print(exception)


    # Filters application
    try:
        #print('J')
        f = filters.filterz(img,'R',numpy.zeros((3,3)))
        score+=1
    except Exception as exception:
        print(exception)


    # Others
    try:
        #print('K')
        f = filters.edgeDetection(img,'R','DIFF-2D',[10],100)
        score+=1
    except Exception as exception:
        print(exception)
    
    try:
        #print('L')
        f = filters.edgeEnhancement(img,'R','DIFF-2D',[10],100,.5)
        score+=1
    except Exception as exception:
        print(exception)



    return round(1000*score/12)/10




###***--- THE LEVELS FILE ---***###
def levelsTest():
    
    score = 0

    # levels
    try:
        #print('A')
        img = Image.open('pic/test1.jpg')
        img = img.resize((50,50),Image.ANTIALIAS) # This will speed up the process
        levels.levels(img,'ALL',[10,100,240],[0,128,255])
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('B')
        levels.curves(img,'ALL',[10,30,60,120,200],[0,20,55,128,230])
        score+=1
    except Exception as exception:
        print(exception)

    # automatic adjustments
    try:
        #print('C')
        levels.equalizeHistogram(img,'ALL')
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('D')
        levels.normalizeHistogram(img,'ALL')
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('E')
        levels.expHistogram(img,'ALL')
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('F')
        levels.logHistogram(img,'ALL')
        score+=1
    except Exception as exception:
        print(exception)
    
    return round(1000*score/6)/10




###***--- THE TOOLS FILE ---***###
def toolsTest():

    score = 0

    # every tools
    try:
        #print('A')
        img = Image.open('pic/test1.jpg')
        tools.resize(img,(50,50))
        score+=1
    except Exception as exception:
        print(exception)
    
    try:
        #print('B')
        C = tools.getChannel(img,'R')
        tools.recompose(img,'R',C)
        C = tools.getChannel(img,'G')
        tools.recompose(img,'G',C)
        C = tools.getChannel(img,'B')
        tools.recompose(img,'B',C)
        C = tools.getChannel(img,'H')
        tools.recompose(img,'H',C)
        C = tools.getChannel(img,'S')
        tools.recompose(img,'S',C)
        C = tools.getChannel(img,'V')
        tools.recompose(img,'V',C)
        C = tools.getChannel(img,'ALL')
        tools.recompose(img,'ALL',C)
        score+=2
    except Exception as exception:
        print(exception)


    try:
        #print('C')
        tools.crop(img,(10, 10, 50, 70))
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('D')
        tools.everyFunction(img,['resize',['resize [50,50]']])
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('E')
        tools.explore('','')
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('F')
        tools.unzip('')
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('G')
        tools.zip('')
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('H')
        tools.loadXMP('')
        score+=1
    except Exception as exception:
        print(exception)
    
    try:
        #print('I')
        tools.saveXMP('')
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('J')
        tools.parseInput('a 1 [2,3,4] 3.14',[str,int,list,float])
        score+=1
    except Exception as exception:
        print(exception)


    return round(1000*score/11)/10


###***--- A FEW USERCASES ---***###

## UserCase1
def userCase1():

    score = 0

    #actions = ['h','open pic/test1.jpg','histogram','equalizeHistogram','histogram','save pic/test1-1.jpg','q']
    #try:
    #   main.main(actions,'TEST')
    #   score+=1
    #except Exception as exception:
    #   print(exception)

    return round(1000*score/1)/10


## UserCase2
def userCase2():
 
    score = 0

    #actions = ['open pic/test1.jpg', 'blur gaussian-2d 10 1 ALL', 'equalizeHistogram','undo','normalizeHistogram','saveXMP pic/test1-2.xmp','q']
    #try:
    #   main.main(actions,'TEST')
    #   score+=1
    #except Exception as exception:
    #   print(exception)

    return round(1000*score/1)/10

   
## UserCase3
def userCase3():

    score = 0

    #actions = ['open pic/test1.jpg','loadXMP pic/test1.xmp','history','rebase 2','curves [5, 10, 20, 50, 128, 205, 235, 245, 250] [0, 2, 10, 128, 245, 253, 255]','save pic/test1-3.jpg','saveXMP pic/test1-3.jpg','quitttt','q']
    #try:
    #   main.main(actions,'TEST')
    #   score+=1
    #except Exception as exception:
    #   print(exception)

    return round(1000*score/1)/10





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

    
