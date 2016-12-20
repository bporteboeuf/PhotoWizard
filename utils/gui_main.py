# -*- coding : utf-8 -*-

#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#



# The aim of this module is to bring together the python script and its GUI

import sys,os,time
sys.path.insert(0,'scripts/')

try :
    import PIL,numpy,scipy
except ImportError :
    print("Pillow, Numpy, Scipy and Theano dependancies must be installed. Please try running the setup.py script - Fatal Error.\n")
    sys.exit()


import PIL.Image, PIL.ImageTk
from math import floor
from gui_panels import *


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






# This is the actual Graphical User Interface

from config import FRAME_BACKGROUND,WIDGET_BACKGROUND,WIDGET_FOREGROUND
#FRAME_BACKGROUND = "#2c2929" # "dark gray"
#WIDGET_BACKGROUND = "#565252" # "medium gray"
#WIDGET_FOREGROUND =  "#ffffff" # "white"


class Interface(Frame) : # We define our window

    def __init__(self, window, picture, **kwargs) :
 
    
        self.openedFiles = []


        style = Style()
        style.map('TCombobox', background=[('readonly',WIDGET_BACKGROUND)])


        # Window Background
        Frame.__init__(self, window, width=800, height=600, **kwargs)#,background=FRAME_BACKGROUND)
        self.pack(fill = BOTH, expand = YES)


        # Quit Button
        self.Oquit_button = Button(self, text='Quit', command=quit, background=WIDGET_BACKGROUND, foreground=WIDGET_FOREGROUND)  # command = self.quit defines the callback function
        self.Oquit_button.grid(row=8,column=5,pady=10,padx=5,sticky=N+E+W)
        

        # Export Button
        self.Oexport_button = Button(self, text='Export', command=hello, background=WIDGET_BACKGROUND, foreground=WIDGET_FOREGROUND)
        self.Oexport_button.grid(row=8,column=6,pady=10,padx=5,sticky=N+E+W)
        
        
        # Comparison Button
        self.Ocompare_button = Button(self, text='Compare', command=hello, background=WIDGET_BACKGROUND, foreground=WIDGET_FOREGROUND)
        self.Ocompare_button.grid(row=8,column=1,pady=10,padx=5,sticky=N+E+W)
        
       
        # Tabs
        self.otabs = Tabs(self)
        self.otabs.grid(row=1,column=1,columnspan=5,padx=10,pady=1,sticky=N+W+S)

        # History Widget
        

        # Levels Widget


        # Filters Widget


        # Other Widget

        
        # Image preview
        if os.path.exists(picture) :
            self.imagePath = str(picture)
        else :
            self.imagePath = "pic/default.png"
        self.image_original = PIL.Image.open(self.imagePath)
        self.image_copy = self.image_original.copy()
        self.Oimage = PIL.ImageTk.PhotoImage(self.image_copy) # We use a label to display a picture
        self.Opic = Label(self,image=self.Oimage)
        self.Opic.grid(row=2,column=1,columnspan=3, rowspan=3, padx=10, pady=1, sticky=N+W+S)
        self.Opic.bind('<Configure>',self.resize)
        self.resizeable = False # Security to avoid the resize function to get out of control



        # Histogram preview
        if self.imagePath != 'pic/default.png':
            self.histogram = self.computeHistogram()
            self.histogram = PIL.ImageTk.PhotoImage(PIL.Image.fromarray(self.histogram,'RGB'))
            self.Ohistogram = Label(self,image=self.histogram, background=FRAME_BACKGROUND)
        else:
            self.histogram = ''
            self.Ohistogram = Label(self,background=FRAME_BACKGROUND)
        self.Ohistogram.grid(row=2,column=5,columnspan=3, rowspan=1, padx=10, pady=10, sticky=N+E+S)



        # Resizing column coefficients
        self.columnconfigure(1,weight=1,pad=10)
        self.columnconfigure(2,weight=1,pad=10)
        self.columnconfigure(3,weight=1,pad=10)
        self.columnconfigure(4,weight=3,pad=10)
        self.columnconfigure(5,weight=3,pad=10)
        self.columnconfigure(6,weight=3,pad=10)

        # Resizing row coefficients
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=1)
        self.rowconfigure(3,weight=1)
        self.rowconfigure(4,weight=1)
        self.rowconfigure(5,weight=1)
        self.rowconfigure(6,weight=1)
        self.rowconfigure(7,weight=1)
        self.rowconfigure(8,weight=1)

        return



    def computeHistogram(self):
        precisionH = 1
        precisionV = 2
        img = numpy.asarray(self.image_original.convert('RGB'))
        i = 0
        size = (round(255/precisionV),round(256/precisionH))
        histogram = numpy.zeros((size[0],size[1],3))
        images = [img[:,:,0],img[:,:,1],img[:,:,2],img]
        for elt in images:
            [histogramArr,histogramBins] = numpy.histogram(elt,bins=int(round(256/precisionH)),range=(0,255))
            histogramArr = 255*histogramArr/max(histogramArr)
            a = numpy.reshape(255-numpy.linspace(0,255,round(255/precisionV)),(round(255/precisionV),1))
            propElt = numpy.ones(size)
            a = propElt*a
            array = numpy.ones(size)*histogramArr
            if i<=2:
                histogram[:,:,i] = 255*propElt*(array>=a)
            else:
                for j in range(0,3):
                    histogram[:,:,j] = histogram[:,:,j]*(array<a) + 255*propElt*(array>=a)
            i+=1
        histogram = numpy.asarray(histogram,dtype=numpy.uint8)
        return histogram



    def resize(self,event) : # This functions dynamically resizes the displayed picture
        
        #print(event.width,self.Opic.winfo_width(),self.image_original.size)

        if self.resizeable :
            r = self.image_copy.size
            #print(self.image_original.size)
            r = r[0]/r[1]
            height = int(event.height - 4)
            width = int(floor(height*r) -4) # New widget's dimensions
           
            self.image_original = self.image_copy.resize((width, height),PIL.Image.ANTIALIAS)
            self.Oimage = PIL.ImageTk.PhotoImage(self.image_original)
            self.Opic.configure(image = self.Oimage)
            #self.resizeable = False
        else :
            self.resizeable = True
        #self.update()
        return



    def setImage(self,picture) : # This function updates the displayed image by replacing the old widget
        if os.path.exists(picture) :
            self.imagePath = picture
            self.image_original = PIL.Image.open(self.imagePath)
            self.image_copy = self.image_original.copy()
            self.image_copy = self.image_copy.resize((int(self.Opic.winfo_width()-4), int(self.Opic.winfo_height())-4),PIL.Image.ANTIALIAS)
            self.Oimage = PIL.ImageTk.PhotoImage(self.image_copy) # We use a label to display a picture
            self.Opic.configure(image=self.Oimage)
            #self.Opic.destroy()
            self.resizeable = False # Security to avoid the resize function to get out of control
            #self.Opic = Label(self,image=self.Oimage)
            #self.Opic.grid(row=4,column=1,columnspan=3, padx=10,sticky=N+W+S)
            #self.Opic.bind('<Configure>',self.resize)
            
            # We update the histogram preview
            self.histogram = self.computeHistogram()
            self.histogram = PIL.ImageTk.PhotoImage(PIL.Image.fromarray(self.histogram,'RGB'))
            self.Ohistogram.configure(image=self.histogram)
            #self.update()
        return

    
    def switchTabs(self,ID):
        self.otabs.updateCurrent(ID)
        return



def hello():
    print('Hello')
    return


def openFile(): # Displays the picture - Should also store the associated Picture object and load the XMD file if found
    global interface
    filePath = askopenfilename()
    interface.setImage(filePath)
    interface.otabs.add(interface,filePath)
    interface.openedFiles.append(filePath)
    interface.otabs.updateCurrent(len(interface.openedFiles)-1)
    return




pic = "pic/default.png"

# GUI initialization

window = Tk()

# Generating the Menu bar

menubar = Menu(window, background=FRAME_BACKGROUND, foreground=WIDGET_FOREGROUND)
fileMenu = Menu(menubar, tearoff=0, background=FRAME_BACKGROUND, foreground=WIDGET_FOREGROUND)
fileMenu.add_command(label='Open file         <Ctrl>+O',command=openFile)
fileMenu.add_command(label='Export file       <Ctrl>+E',command=hello)
fileMenu.add_separator()
fileMenu.add_command(label='Load XMD       <Ctrl>+L',command=hello)
fileMenu.add_command(label='Save XMD       <Ctrl>+S',command=hello)
fileMenu.add_separator()
fileMenu.add_command(label='Print               <Ctrl>+P',command=hello)
fileMenu.add_separator()
fileMenu.add_command(label='Quit                <Ctrl>+Q',command=quit)

editMenu = Menu(menubar, tearoff=0, background=FRAME_BACKGROUND, foreground=WIDGET_FOREGROUND)
editMenu.add_command(label='Undo           <Ctrl>+Z',command=hello)
editMenu.add_command(label='Redo           <Ctrl>+R',command=hello)

preferencesMenu = Menu(menubar, tearoff=0, background=FRAME_BACKGROUND, foreground=WIDGET_FOREGROUND)
preferencesMenu.add_command(label='Language',command=hello)
preferencesMenu.add_command(label='Default Settings',command=hello)

aboutMenu = Menu(menubar, tearoff=0, background=FRAME_BACKGROUND, foreground=WIDGET_FOREGROUND)
aboutMenu.add_command(label='Help',command=hello)
aboutMenu.add_separator()
aboutMenu.add_command(label='Check for Updates',command=hello)
aboutMenu.add_separator()
aboutMenu.add_command(label='About',command=hello)

menubar.add_cascade(label='File', menu=fileMenu)
menubar.add_cascade(label='Edit', menu=editMenu)
menubar.add_cascade(label='Preferences', menu=preferencesMenu)
menubar.add_cascade(label='?', menu=aboutMenu)

window.config(menu=menubar)


# Defining style

combostyle = Style() # We create a ttk style for all comboboxes
combostyle.theme_create('combostyle', parent='alt',settings = {'TCombobox':{'configure':{'selectbackground': WIDGET_BACKGROUND,'fieldbackground': WIDGET_BACKGROUND,'background': WIDGET_BACKGROUND, 'selectforeground': WIDGET_FOREGROUND, 'fieldforeground': WIDGET_FOREGROUND,'foreground': WIDGET_FOREGROUND}}})
combostyle.theme_use('combostyle') 

window.title("PhotoWizard")
window.option_add("*background",FRAME_BACKGROUND)
icon = PhotoImage(file='pic/icon.png')
window.tk.call('wm','iconphoto',window._w,icon)


# Initializing the Interface

interface = Interface(window,pic)


# Launching the GUI

interface.mainloop()






