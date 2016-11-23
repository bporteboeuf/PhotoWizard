# PhotoWizard


This project aims at providing a basic image editing software, both in command line and with a graphical interface.


This image editing software is still at an early stage development. More functionalities are to come soon.

To open an image, simply type open [filePath]. You can edit it using the different functionalities implemented, such as filters, levels, and much more.
To switch between two opened images, simply type switch [filePath]. You can save your changes by typing save [filePath], load previous changes by typing load [filePath] or export your final images using the export [fileName] command.

An histogram can be displayed thanks to the histogram command, and a preview pop-up window appears with the preview command.

You can revoke the last action by typing undo or restore it with redo.

You can have more informations on how to use the functionalities by typing [moduleName] -h or [moduleName] --help.


List of modules availables:
    
lowPass,highPass,detectEdges,enhanceEdges,sharpen,levels,curves,contrast,exposure,blackandwhite,histogram,rotate,crop,resize,normHist,eqHist,expHist,logHist,preview,history


Preferences can be set in the utils/config.py file.

