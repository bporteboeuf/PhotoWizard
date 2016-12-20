# -*- coding: utf-8 -*-

#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#


import sys
import PIL,numpy

# Python Version Compatibility Modes

if int(sys.version[0]) == 2 :
    print("Using Python2 compatibility mode - For a better experience, please try running Python3")
    from Tkinter import *
    from ttk import *
    from Tkinter import Button,Frame # We import those items from the tkinter module because they easily allow to change their style 
    from tkFileDialog import askopenfilename

elif int(sys.version[0]) == 3 :
    from tkinter import *
    from tkinter.ttk import *
    from tkinter import Button,Frame # We import those items from the tkinter module because they easily allow to change their style 
    from tkinter.filedialog import askopenfilename


else :
    print("Unsupported Python version: please try running Python2 or greater - Fatal Error")
    sys.exit()


from config import FRAME_BACKGROUND,WIDGET_BACKGROUND,WIDGET_FOREGROUND



class Tabs(Frame): # Tabs Widget for managing multiple files

    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.labels =  []
        return

    def add(self,parent,text):
        lbl = Label(self,text=text,background=FRAME_BACKGROUND, foreground=WIDGET_FOREGROUND)
        lbl.grid(row=1,column=len(self.labels)+1,columnspan=1, rowspan=1, padx=2, pady=5, sticky=N+E+S)
        ID = len(self.labels)
        lbl.bind('<Button-1>', lambda e: parent.switchTabs(ID))
        self.labels.append(lbl)
        return

    def updateCurrent(self,ID):
        for i in range(0,len(self.labels)):
            self.labels[i].configure(background=FRAME_BACKGROUND)            
        self.labels[ID].configure(background=WIDGET_BACKGROUND)
        return

    def remove(self,parent,ID):
        self.labels[ID].destroy()
        del self.labels[ID]
        return
        
    def insert(self,parent,text,index):
        lbl = Label(self,text=text,background=FRAME_BACKGROUND, foreground=WIDGET_FOREGROUND)
        lbl.grid(row=1,column=len(self.labels)+1,columnspan=1, rowspan=1, padx=2, pady=5, sticky=N+E+S)
        ID = len(self.labels)
        lbl.bind('<Button-1>', lambda e: parent.switchTabs(ID))
        self.labels = self.labels[:index]+list(lbl)+self.labels[index:]
        return



class HistoryWidget(Frame):
    
    def __init__(self, parent, frame_background, widget_background, widget_foreground):
        #Frame.__init__(self, parent)
        try:
            # We want to get the RGB representation of the colours
            i = 0
            for colour in [frame_background,widget_background,widget_foreground]:
                colour = colour.lstrip('#')
                l = len(colour)
                rgb = tuple(int(colour[i:i + l // 3], 16) for i in range(0, l, l // 3))
                if i == 0:
                    frame_background = rgb
                elif i == 1:
                    widget_background = rgb
                else:
                    widget_foreground = rgb
                       
            # We then load the shapes            
            self.start = numpy.asarray(PIL.Image.open('pic/start.png','RGB'))
            self.endDs = numpy.asarray(PIL.Image.open('pic/end.png','RGB'))
            self.endEn = numpy.asarray(PIL.Image.open('pic/end.png','RGB'))
            self.line = numpy.asarray(PIL.Image.open('pic/lineA.png','RGB'))
            self.lineDs = numpy.asarray(PIL.Image.open('pic/lineB.png','RGB'))
            self.lineEn = numpy.asarray(PIL.Image.open('pic/lineB.png','RGB'))
            self.slopeA = numpy.asarray(PIL.Image.open('pic/slopeA.png','RGB'))
            self.slopeB = numpy.asarray(PIL.Image.open('pic/slopeB.png','RGB'))
            self.slopeC = numpy.asarray(PIL.Image.open('pic/slopeC.png','RGB'))
            self.slopeD = numpy.asarray(PIL.Image.open('pic/slopeD.png','RGB'))


            # And we colour them accordingly
            self.start = PIL.Image.fromarray((self.start==255)*frame_background+(self.start==0)*widget_background+(self.start==128)*widget_foreground,'RGB')

        except Exception as e:
            print(e)
            raise NameError('PhotoWizard Error: Unable to load HistoryWidget')

        return



class ExpositionWidget(Frame):
    def __init__(self):
        self.foo = ''
        return


class LevelsWidget(Frame):
    def __init__(self):
        self.foo = ''
        return


class FiltersWidget(Frame):
    def __init__(self):
        self.foo = ''
        return


class TransformWidget(Frame):
    def __init__(self):
        self.foo = ''
        return


class ColoursWidget(Frame):
    def __init__(self):
        self.foo = ''
        return


class HistogramTransformWidget(Frame):
    def __init__(self):
        self.foo = ''
        return


class OtherWidget(Frame):
    def __init__(self):
        self.foo = ''
        return




#a = Tk()
#b = HistoryWidget(a,"#2c2929" ,"#565252", "#ffffff")

#b.start.show()

