# -*- coding: utf-8 -*-

#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#


# This module contains tests for the whole software

try:
    import filters,helpm,history,levels,main,tools,mapping
    from picture import Picture
    from history import History, Event
    from loadConfig import *
    import sys,numpy,scipy,math
    from PIL import Image
except Exception as e:
    print(e)
    raise NameError('PhotoWizard Error: unable to load dependencies')



###***--- THE EVENT CLASS ---***###
def eventClass():

    score = 0

    # Init
    try:
        #print('A')
        eventA = Event(1,None,'actionA parameters','eventA')
        eventB = Event(2,1,'actionB parameters','eventB')
        eventC = Event(3,None,'actionC parameters','eventC')
        score+=1
    except Exception as exception:
        print(exception)

    # Class methods
    try:
        #print('B')
        if eventA.getID() == 1:
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('C')
        if eventA.getNext() == {}:
            score+=1
    except Exception as exception:
        print(exception)
 
    try:
        #print('D')
        eventA.setNext(3)
        if 3 in eventA.getNext():
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('E')
        if eventB.getPrevious() == 1:
            score+=1
    except Exception as exception:
        print(exception)
 
    try:
        #print('F')
        eventC.setPrevious(1)
        if eventC.getPrevious() == 1:
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('G')
        if eventB.getContent() == 'actionB parameters':
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('H')
        eventB.setContent('action2 params2')
        if eventB.getContent() == 'action2 params2':
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('I')
        if eventB.getLabel() == 'eventB':
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('J')
        eventB.setLabel('EVENTB')
        if eventB.getLabel() == 'EVENTB':
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
        hist.add('action parameters','eventA')
        hist.add('action parameters','eventB')
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('C')
        if hist.getCurrentState() == 2:
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('D')
        hist.setCurrentState(1)
        if hist.getCurrentState() == 1:
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('E')
        a = hist.getEvent(1)
        if a.getLabel() == 'eventA':
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('F')
        hist.undo()
        if hist.getCurrentState() == 0:
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('G')
        hist.redo()
        if hist.getCurrentState() == 1:
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('H')
        hist.rebase(2)
        if hist.getCurrentState() == 2:
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
        h = hist.getFullHistory()
        if h == '--- 0 - InitialState --- 1 - eventA --- 2 - eventB \n\nCurrent State: 2 - eventB\n':
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('K')
        hist.clearHistory()
        if hist.getEvents() == {}:
            score+=1
    except Exception as exception:
        print(exception)


    return round(1000*score/11)/10




###***--- THE PICTURE CLASS ---***###
def pictureClass():

    score = 0

    # Init
    try:
        #print('A',score)
        image = Picture(int(1),"pic/test1.jpg")
        score+=1
    except Exception as exception:
        print(exception)

    # Class methods
    try:
        #print('B',score)
        if (isinstance(image.getImage(),Image.Image)):
            score+=1
    except Exception as exception:
        print(exception)
   
    try:
        #print('C',score)
        if (isinstance(image.getSmallImage(),Image.Image)):
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('D',score)
        S1 = image.getSmallImage().size
        image.resizeSmall((2,3))
        S2 = image.getSmallImage().size
        if (round(S1[0]*2) == S2[0]) and (round(S1[1]*3) == S2[1]):
            score+=1
    except Exception as exception:
        print(exception)
    
    try:
        #print('E',score)
        h = image.getHistory()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('F',score)
        h.add('normHist R','NewEvent')
        image.setHistory(h)
        if image.getHistory() == h:
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('G',score)
        image.reCompute()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('H',score)
        image.export('pic/test1-2.jpg')
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('I',score)
        image.close()
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('J',score)
        image.histogram('ALL')
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('K',score)
        s = image.getScaling()
        if round(s[0]*1000)/1000 == 0.897 and round(s[1]*1000)/1000 == 1.347:
            score+=1
    except Exception as exception:
        print(exception)

    return round(1000*score/11)/10





###***--- THE FILTERS FILE ---***###
def filtersTest():
    
    score = 0

    # Initialization
    try:
        img = Image.open('pic/test3.jpg')
        img.resize((100,100)) # This will speed up the process
    except Exception as e:
        print(e)    


    # Filters generation
    try:
        #print('A')
        f = filters.lowPass('GAUSSIAN-2D',[1,0.5],(1,1))
        f2 = numpy.asarray([[ 0.07507324, 0.1237793, 0.07507324], [ 0.1237793, 0.20410156, 0.1237793 ], [ 0.07507324, 0.1237793, 0.07507324]])
        if numpy.allclose(f,f2):
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('B')
        f = filters.lowPass('GAUSSIAN-1D',[1,.2,0.],(1,1))
        f2 = numpy.asarray([[ 0., 0., 0.], [ 0.31054688, 0.37915039, 0.31054688], [ 0., 0., 0.]])

        if numpy.allclose(f,f2):
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('C')
        f = filters.lowPass('MEAN-2D',[1,.5],(1,1))
        f2 = numpy.asarray([[ 0.09997559, 0.09997559, 0.09997559], [ 0.09997559, 0.19995117, 0.09997559], [ 0.09997559, 0.09997559, 0.09997559]])
        if numpy.allclose(f,f2):
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('D')
        f = filters.lowPass('MEAN-1D',[1,1.,0.],(1,1))
        f2 = numpy.asarray([[ 0., 0., 0.], [ 0.33325195, 0.33325195, 0.33325195], [ 0., 0., 0. ]])
        if numpy.allclose(f,f2):
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('E')
        f = filters.lowPass('POISSON-2D',[1,1.],(1,1))
        f2 = numpy.asarray([[ 0.25, 0., 0.25], [ 0., 0., 0.], [ 0.25, 0., 0.25]])
        if numpy.allclose(f,f2):
            score+=1
    except Exception as exception:
        print(exception)
 
    try:
        #print('F')
        f = filters.lowPass('POISSON-1D',[1,0.7,15.3],(1,1))
        f2 = numpy.asarray([[ 0., 0., 0., 0.,], [ 0., 0.04679966, 0.23986255,  0.], [ 0., 0.23986255, 0.04679966, 0.], [ 0., 0., 0., 0.]])
        if numpy.allclose(f,f2):
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('G')
        f = filters.highPass('DIFF-2D',[1,1],(1,1))
        f2 = numpy.asarray([[ 0.35355338+0.35355338j, 0.35355338+0.j, 0.35355338-0.35355338j], [ 0.00000000+0.35355338j, 0.00000000+0.j, 0.00000000-0.35355338j], [-0.35355338+0.35355338j, -0.35355338+0.j, -0.35355338-0.35355338j]])
        if numpy.allclose(f,f2):
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('H')
        f = filters.highPass('DIFF-1D',[1,1,0.],(1,1))
        f2 = numpy.asarray([[ 0.5+0.j, 0.0+0.j, -0.5+0.j], [ 0.5+0.j, 0.0+0.j, -0.5+0.j], [ 0.5+0.j, 0.0+0.j, -0.5+0.j]])
        if numpy.allclose(f,f2):
            score+=1
    except Exception as exception:
        print(exception)


    try:
        #print('I')
        f = filters.highPass('SCHARR-2D',[1],(1,1))
        f2 = numpy.asarray([[ 0.16317847+0.16317847j, 0.54392827+0.j, 0.16317847-0.16317847j], [ 0.00000000+0.54392827j, 0.00000000+0.j, 0.00000000-0.54392827j], [-0.16317847-0.16317847j, -0.54392827+0.j, -0.16317847+0.16317847j]])
        if numpy.allclose(f,f2):
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('J')
        f = filters.highPass('SCHARR-1D',[1,0.],(1,1))
        f2 = numpy.asarray([[ 0.23076925+0.j, 0.00000000+0.j, -0.23076925+0.j], [ 0.76923078+0.j,  0.00000000+0.j, -0.76923078+0.j], [ 0.23076925+0.j,  0.00000000+0.j, -0.23076925+0.j]])
        if numpy.allclose(f,f2):
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('K')
        f = filters.highPass('CROSS-2D',[1],(1,1))
        f2 = numpy.asarray([[ 0.70710677+0.j, 0.00000000+0.70710677j], [ 0.00000000-0.70710677j, -0.70710677+0.j]])
        if numpy.allclose(f,f2):
            score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('L')
        f = filters.highPass('CROSS-1D',[1,0.],(1,1))
        f2 = numpy.asarray([[ 1.+0.j, 0.+1.j], [ 0.-1.j, -1.+0.j]])
        if numpy.allclose(f,f2):
            score+=1
    except Exception as exception:
        print(exception)



    # Filters application
    try:
        #print('M')
        Id = numpy.diag([0,0,1,0,0])
        f = filters.filterz(img,'ALL',Id)
        if numpy.allclose(numpy.asarray(f,dtype=numpy.uint8), numpy.asarray(img,dtype=numpy.uint8),1,1):
            score+=1
    except Exception as exception:
        print(exception)


    # Others
    try:
        #print('N')
        f = filters.edgeDetection(img,'R','DIFF-2D',[1,1],100,(1,1))
        score+=1
    except Exception as exception:
        print(exception)
    
    try:
        #print('O')
        f = filters.edgeEnhancement(img,'R','DIFF-2D',[1,1],100,.5,(1,1))
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('P')
        f = filters.sharpen(img,'R','DIFF-2D',[1,.5],.1,(1,1))
        score+=1
    except Exception as exception:
        print(exception)

    return round(1000*score/16)/10




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
        tmp = numpy.asarray(img)
        if numpy.amin(tmp) == 0 and numpy.amax(tmp) == 255:
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

    # Others
    try:
        #print('G')
        levels.contrast(img,'ALL',50)
        score+=1
    except Exception as exception:
        print(exception)
    
    try:
        #print('H')
        levels.exposure(img,'ALL',1)
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('I')
        levels.blackAndWhite(img,'ALL')
        score+=1
    except Exception as exception:
        print(exception)


    return round(1000*score/9)/10




###***--- THE TOOLS FILE ---***###
def toolsTest():

    score = 0

    # Initialization
    try:
        picture = Picture(1,'pic/test2.jpg')
        img = Image.open('pic/test2.jpg')
    except Exception as e:
        print(e)
        

    # every tools
    try:
        #print('A')
        tools.resize(img,[50,50])
        score+=1
    except Exception as exception:
        print(exception)
    
    try:
        #print('B')
        CR = tools.getChannel(img,'R')
        tools.recompose(img,'R',CR)
        CG = tools.getChannel(img,'G')
        tools.recompose(img,'G',CG)
        CB = tools.getChannel(img,'B')
        tools.recompose(img,'B',CB)
        CH = tools.getChannel(img,'H')
        tools.recompose(img,'H',CH)
        CS = tools.getChannel(img,'S')
        CSr = tools.recompose(img,'S',CS)
        CV = tools.getChannel(img,'V')
        tools.recompose(img,'V',CV)
        C = tools.getChannel(img,'ALL')
        Cr = tools.recompose(img,'ALL',C)
        
        #print(numpy.mean(CR),numpy.mean(CG),numpy.mean(CB),round(numpy.mean(CH)*360/255),round(numpy.mean(CS)*100/255),round(numpy.mean(CV)*100/255))
        #print(numpy.sum(numpy.abs(numpy.asarray(Cr,dtype=numpy.uint8)-numpy.asarray(img,dtype=numpy.uint8))))
        #print(numpy.sum(numpy.abs(numpy.asarray(CSr,dtype=numpy.uint8)-numpy.asarray(img.convert('HSV'),dtype=numpy.uint8))))

        #print(numpy.asarray(CSr),numpy.asarray(img.convert('HSV')))
        #print(numpy.abs(numpy.asarray(CSr,dtype=numpy.uint8)-numpy.asarray(img.convert('HSV'),dtype=numpy.uint8)))

        if ((numpy.mean(CR) == 235) and (numpy.mean(CG) == 144) and (numpy.mean(CB) == 63) and (round(numpy.mean(CH)*360/255) == 28) and (round(numpy.mean(CS)*100/255) == 73) and (round(numpy.mean(CV)*100/255) == 92)):
            score+=1
            #print('getChannel ok')
    
        if (numpy.sum(numpy.abs(numpy.asarray(Cr,dtype=numpy.uint8)-numpy.asarray(img,dtype=numpy.uint8))) == 0) and (numpy.sum(numpy.abs(numpy.asarray(CSr,dtype=numpy.uint8)-numpy.asarray(img.convert('HSV'),dtype=numpy.uint8))) == 0):
            score+=1
            #print('getChannel & recompose ok')
        
    except Exception as exception:
        print(exception)


    try:
        #print('C')
        tools.crop(img,(10,10,30,40))
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('D')
        mapping.everyFunction(img,['resize','resize [50,50]'],(1,1))
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
        hist = History(1)
        tools.loadXMD('pic/test5.xmd',hist)
        score+=1
    except Exception as exception:
        print(exception)
    
    try:
        #print('I')
        hist = History(1)
        tools.saveXMD('pic/test0.xmd',hist)
        score+=1
    except Exception as exception:
        print(exception)

    try:
        #print('J')
        a = tools.parseInput('a 1 [2,3,4] 3.14',[str,int,list,float])
        if a == ['a',1,[2.,3.,4.], 3.14]:
            score+=1
    except Exception as exception:
        print(exception)

    # Filters rotation
    try:
        #print('K')
        f = tools.rotate(img,15.)
        f = tools.rotate(numpy.ones((5,7),dtype=numpy.uint8),-15.)
        score+=1
    except Exception as exception:
        print(exception)

    return round(1000*score/12)/10




###***--- A FEW USERCASES ---***###

## UserCase1
def userCase1():

    score = 0

    actions = ['h','open pic/test6.jpg','histogram ALL','eqHist ALL','histogram ALL','export pic/test6-2.jpg','q']
    try:
       main.main(actions,True)
       score+=1
    except Exception as exception:
       print(exception)

    return round(1000*score/1)/10


## UserCase2
def userCase2():
 
    score = 0

    actions = ['open pic/test5.jpg', 'lowPass GAUSSIAN-2D [10,1] ALL', 'eqHist ALL','undo','normHist ALL','save pic/test5.xmd','q']
    try:
       main.main(actions,True)
       score+=1
    except Exception as exception:
       print(exception)

    return round(1000*score/1)/10

   
## UserCase3
def userCase3():

    score = 0

    actions = ['open pic/test1.jpg','load pic/test1.xmd','history','rebase 2','curves ALL [5,10,20,50,128,205,235,245,250] [0,2,10,40,128,215,245,253,255]','export pic/test1-3.jpg','save pic/test1-3.xmd','quitttt','q']
    try:
       main.main(actions,True)
       score+=1
    except Exception as exception:
       print(exception)

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

    
