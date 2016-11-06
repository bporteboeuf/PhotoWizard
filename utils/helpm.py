#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# -*- coding: utf-8 -*-

# This module generates various help messages in the shell



def help(matter,language): # Matter indicates the matter on which the user needs help, language indicates the language to use


    # ENGLISH VERSION

    if str(language) == "EN" :
        if matter == 'idle':
            hmess = '\nThis image editing software is still at an early stage development. More functionalities are to come soon.'
            hmess += '\n\nTo open an image, simply type open [filePath].'
            hmess += ' You can edit it using the different functionalities implemented, such as filters, levels, and much more.'
            hmess += '\nTo switch between two opened images, simply type switch [filePath]. You can save your changes by typing save [filePath] and load previous changes by typing load [filePath].'
            hmess += ' You can also export your final images using the export [fileName] command.'
            hmess += '\nAn histogram can be displayed thanks to the histogram command, and a preview pop-up window appears with the preview command.'
            hmess += '\nYou can revoke the last action by typing undo or restore it with redo.'
            hmess += '\n\nYou can have more informations on how to use the functionalities by typing [moduleName] -h or [moduleName] --help.'
            hmess += '\n\nList of modules availables:\n\n'
            hmess += ' -*- '.join(["lowPass","highPass","detectEdges","enhanceEdges","levels","curves","contrast","exposure","blackandwhite","histogram","rotate","crop","resize","normHist","eqHist","expHist","logHist","preview","history"])
            hmess += '\n'
        
        elif matter == 'levels':
            hmess = '\nHELP - LEVELS'
            hmess += '\nThis module offers the possibility to change the levels of an image, that is to change the outputs values of specific inputs values.'
            hmess += '\nYou need to first select a channel to apply your levels modifications. You can choose between R,G,B,H,S,V or ALL.'
            hmess += '\nYou then need to enter the values of the desired inputs range as follows: [ia,ib,ic] where (ia,ib,ic) are integers from 0 to 255, ia/ib defines the low tones of the image and ib/ic the light tones of the image.'
            hmess += '\nIn the same way, you need to enter the desired outputs values as follows: [oa,ob,oc] as integers from 0 to 255.'
            hmess += '\n\nNote: you can specify as many inputs or outputs values as you want, as long as your inputs and outputs lengths are equal and comprised between 2 and 257.'
            hmess += '\n\nExample: levels ALL [30,128,220] [0,128,255]'
            hmess += '\n'

        elif matter == 'curves':
            hmess = '\nHELP - CURVES'
            hmess += '\nThis module offers the possibility to change the tone curves of an image, that is to change the outputs values of specific inputs values.'
            hmess += '\nThis module works very similarly to the LEVELS module, except that LEVELS offers a C-0 dynamic response whereas CURVES uses spline interpolation to offer a C-1 dynamic response.'
            hmess += '\nYou need to first select a channel to apply your curves modifications. You can choose between R,G,B,H,S,V or ALL.'
            hmess += '\nYou then need to enter the values of the desired inputs range as follows: [ia,ib,ic] where (ia,ib,ic) are integers from 0 to 255, ia/ib defines the low tones of the image and ib/ic the light tones of the image.'
            hmess += '\nIn the same way, you need to enter the desired outputs values as follows: [oa,ob,oc] as integers from 0 to 255.'
            hmess += '\n\nNote: you can specify as many inputs or outputs values as you want, as long as your inputs and outputs lengths are equal and comprised between 4 and 257.'
            hmess += '\n\nExample: curves ALL [20,30,50,128,200,220,230] [0,5,15,128,240,250,255]'
            hmess += '\n'

        elif matter == 'eqHist':
            hmess = '\nHELP - EQHIST'
            hmess += '\nThis module offers the possibility to equalize the histogram, which is a way to increase the contrast and overall detail of an image.'
            hmess += '\nYou just need to select the channel on which you want to apply the effect. You can choose between R,G,B,H,S,V and ALL'
            hmess += '\n\nExample: eqHist V'
            hmess += '\n'

        elif matter == 'normHist':
            hmess = '\nHELP - NORMHIST'
            hmess += '\nThis module offers the possibility to normalize the histogram using a linear function, which is a way to increase the contrast and overall detail of an image.'
            hmess += '\nYou just need to select the channel on which you want to apply the effect. You can choose between R,G,B,H,S,V and ALL'
            hmess += '\n\nExample: normHist V'
            hmess += '\n'


        elif matter == 'logHist':
            hmess = '\nHELP - LOGHIST'
            hmess += '\nThis module offers the possibility to normalize the histogram using a logarithmic function, which is a way to increase the contrast and overall detail of an underexposed image, recovering a lot of details in the dark areas.'
            hmess += '\nYou just need to select the channel on which you want to apply the effect. You can choose between R,G,B,H,S,V and ALL'
            hmess += '\n\nExample: logHist V'
            hmess += '\n'


        elif matter == '\nexpHist':
            hmess = '\nHELP - EXPHIST'
            hmess += '\nThis module offers the possibility to normalize the histogram using an exponential function, which is a way to increase the contrast and overall detail of an overexposed image, recovering a lot of details in the light areas.'
            hmess += '\nYou just need to select the channel on which you want to apply the effect. You can choose between R,G,B,H,S,V and ALL'
            hmess += '\n'


        elif matter == 'contrast':
            hmess = '\nHELP - CONTRAST'
            hmess += '\nUnfortunately, this function is not implemented yet. Try using levels or curves.'

        elif matter == 'exposure':
            hmess = '\nHELP - EXPOSURE'
            hmess += '\nUnfortunately, this function is not implemented yet. Try using levels or curves.'

        elif matter == 'histogram':
            hmess = '\nHELP - HISTOGRAM'
            hmess += '\nThis module displays a normalized histogram of the working copy of your image.'
            hmess += '\nAn histogram is a graphic that details how much pixels have a given value. The value (range 0 to 255 from left to right) is on the X-axis and the number (or proportion) of concerned pixels is represented on the Y-axis.'
            hmess += '\nIt is a great way to know if your picture is over or underexpoed for instance.'
            hmess += '\nYou just need to select the channel on which you want to apply the effect. You can choose between R,G,B,H,S,V and ALL'
            hmess += '\n\nExample: histogram R'
            hmess += '\n'

        elif matter == 'lowPass':
            hmess = '\nHELP - LOWPASS'
            hmess += '\nThis module offers the possibility to apply a low-pass filter on your image (essentially a blurring effet).'
            hmess += '\nYou first need to specify the filter you want to use. It can currently be: GAUSSIAN-2D, MEAN-2D or POISSON-2D.'
            hmess += '\nThen you also need to provide the correct parameters for those filters, such as a radius (integer) and a coefficient (float) for GAUSSIAN-2D and POISSON-2D.'
            hmess += '\nFinally, you need to precise the channel on which you want to apply your effect. You can choose between R,G,B,H,S,V or ALL.'
            hmess += '\n\nExample: lowPass GAUSSIAN-2D [20,1] ALL'
            hmess += '\n'

        elif matter == 'highPass':
            hmess = '\nHELP - HIGHPASS'
            hmess += '\nThis module offers the possibility to apply a high-pass filter on your image (essentially a sharpening effet).'
            hmess += '\nYou first need to specify the filter you want to use. It can currently be: DIFF-2D.'
            hmess += '\nThen you also need to provide the correct parameters for those filters, such as a radius (integer).'
            hmess += '\nFinally, you need to precise the channel on which you want to apply your effect. You can choose between R,G,B,H,S,V or ALL.'
            hmess += '\n\nExample: highPass DIFF-2D [5]  ALL'
            hmess += '\n'

        elif matter == 'detectEdges':
            hmess = '\nHELP - DETECTEDGES'
            hmess += '\nThis module offers the possibility to detect edges on your image.'
            hmess += '\nThis module works similarly to the HIGHPASS module, except that it has a threshold value.'
            hmess += '\nYou first need to precise the channel on which you want to apply your effect. You can choose between R,G,B,H,S,V or ALL.'
            hmess += '\nYou then need to specify the filter you want to use. It can currently be: DIFF-2D.'
            hmess += '\nThen you also need to provide the correct parameters for those filters, such as a radius (integer).'
            hmess += '\nFinally, you need to specify your threshold value (integer from 0 to 255).'
            hmess += '\n\nExample: detectEdges V DIFF-2D [5] 100'
            hmess += '\n'

        elif matter == 'enhanceEdges':
            hmess = '\nHELP - ENHANCEEGDES'
            hmess += '\nThis module offers the possibility to enhance edges on your image.'
            hmess += '\nThis module works similarly to the HIGHPASS module, except that it has a threshold value and a gain value (or opacity).'
            hmess += '\nYou first need to specify the channel you want to use. You can choose between R,G,B,H,S,V or ALL.'
            hmess += '\nYou then need to specify the filter you want to use. It can currently be: DIFF-2D.'
            hmess += '\nThen you also need to provide the correct parameters for those filters, such as a radius (integer).'
            hmess += '\nFinally, you need to precise the threshold value (integer from 0 to 255) and your gain (float from 0 to 1)'
            hmess += '\n\nExample: enhanceEdges V DIFF-2D [5] 100 .85'
            hmess += '\n'



        elif matter == 'blackandwhite':
            hmess = '\nHELP - BLACKANDWHITE'
            hmess += '\nUnfortunately, this function is not implemented yet. Try using levels on the S channel.'

        elif matter == 'rotate':
            hmess = '\nHELP - ROTATE'
            hmess += '\nThis module offers the possibility to rotate your image by a given angle in degrees (float).'
            hmess += '\n\nExample: rotate 30'
            hmess += '\n'

        elif matter == 'crop':
            hmess = '\nHELP - CROP'
            hmess += '\nThis module offers the possibility to crop your image.'
            hmess += '\nYou simply need to specify the coordinates of your new top left point and your new bottom right point.'
            hmess += '\n\nExample: crop [10,20,150,210]'
            hmess += '\n'

        elif matter == 'resize':
            hmess = '\nHELP - RESIZE'
            hmess += '\nThis module offers the possibility to resize your image.'
            hmess += ' You simply need to specify a given width and height.'
            hmess += '\n\nExample: resize [800,600]'
            hmess += '\n'

        elif matter == 'preview':
            hmess = '\nHELP - PREVIEW'
            hmess += '\nThis module opens a pop-up window to preview the result on your final image.'
            hmess += '\n\nExample: preview'
            hmess += '\n'

        elif matter == 'history':
            hmess = '\nHELP - HISTORY'
            hmess += '\nUnfortunately, this function is not fully supported yet.'

        elif matter == 'undo':
            hmess = '\nHELP - UNDO'
            hmess += '\nThis command undoes or revoked your last action, until you come back to the initial state.'
            hmess += '\n\nExample: undo'
            hmess += '\n'

        elif matter == 'redo':
            hmess = '\nHELP - REDO'
            hmess += '\nThis command redoes or restore your last cancelled action by the UNDO command. If you want to restore more than one action, it will try to go along your history branch as long as it does not find a leaf or a node.'
            hmess += '\n\nNote: If a node is found and the redo action proves to be inefficient, you can always force it to enter a new branch or to directly restore a new state by using the REBASE command.'
            hmess += '\n\nExample: redo'
            hmess += '\n'

        elif matter == 'rebase':
            hmess = '\nHELP - REBASE'
            hmess += '\nThis command restore your system to a given state in the current history.'
            hmess += '\nYou just need to specify which state number you want to restore (0 being the initial state).'
            hmess += '\n\nExample: rebase 0'
            hmes += '\n'

        elif matter == 'open':
            hmess = '\nHELP - OPEN'
            hmess += '\nThis command opens a picture file compatible with PhotoWizard.'
            hmess += '\nYou just need to specify the path (relative or absolute) to your image.'
            hmess += ' This path will serve as an ID to identify your picture among the different files you have opened.'
            hmess += '\n\nExample: open pic/test1.jpg'
            hmess += '\n'

        elif matter == 'close':
            hmess = '\nHELP - CLOSE'
            hmess += '\nThis command closes a given picture and deleted the attached history (if not saved in an XMD file, of course).'
            hmess += '\nYou just need to specify the ID of your picture, which is the path you have entered to open it in the first place.'
            hmess += '\n\nExample: close pic/test1.jpg'
            hmess += '\n'

        elif matter == 'load':
            hmess = '\nHELP - LOAD'
            hmess += '\nThis command loads an XMD file which contains a history of modifications, forks it to your current history and update your current state.'
            hmess += '\nYou just need to specify the path of the XMD file (relative or absolute)'
            hmess += '\n\nExample: load pic/test3.xmd'
            hmess += '\n'

        elif matter == 'save':
            hmess = '\nHELP - SAVE'
            hmess += '\nThis command saves the current history in an XMD file, so that it can be restored for future use.'
            hmess += '\nYou just need to specify the desired path (relative or absolute).'
            hmess += '\n\nExample: save pic/test3-1.xmd'

        elif matter == 'export':
            hmess = '\nHELP - EXPORT'
            hmess += '\nThis command actually exports your final image. All your modifications will then be applied to your original full-sized image.'
            hmess += '\nYou just need to specify the desired path (relative or absolute). The extension of the file will be interpreted as the format for export.'
            hmess += '\n\nExample: export pic/test3.tiff'
            hmess += '\n'

        elif matter == 'switch':
            hmess = '\nHELP - SWITCH'
            hmess += '\nThis function allows you to switch between several opened images so that you can edit them in parallel.'
            hmess += '\nYou just need to specify the ID of your picture, which is the path you have entered to open it in the first place.'
            hmess += '\n\nExample: switch pic/test2.jpg'
            hmess += '\n'

        else:
            hmess = "\nHELP - Unknown matter."


    # FRENCH VERSION
    elif str(language) == "FR" :
        if matter == 'idle':
            hmess = "\nCe logiciel de traitement d'images est encore au stade de développement. Plus de fonctionnalités devraient bientôt arriver."
            hmess += '\n\nPour ouvrir une image, il suffit de taper open [filePath].'
            hmess += 'Vous pouvez alors modifier l\'image à l\'aide des fonctionnalités présentes, comme des filtres, niveaux et bien plus.'
            hmess += '\nPour sélectionner l\'image de travail parmi plusieurs images ouvertes, taper switch [filePath]. Vous pouvez enregistrer les changements effectués en tapant save [filePath] et charger des changements antérieurs avec load [filePath].'
            hmess += ' Vous pouvez aussi exporter vos images en utilisant la commande export [filePath].'
            hmess += '\nUn histogramme peut être affiché en tapant histogram, et une fenêtre de prévisualisation est disponible grâce à la commande preview.'
            hmess += '\nVous pouvez annuler la dernière action en tapan undo ou la restaurer avec redo.'
            hmess += '\n\nPour plus d\'informations sur la façon d\'utiliser les fonctionnalités, taper [moduleName] -h ou [moduleName] --help.'
            hmess += '\n\nListe des modules disponibles:\n\n'
            hmess += ' -*- '.join(['lowPass','highPass','detectEdges','enhanceEdges','levels','curves','contrast','exposure','blackandwhite','histogram','rotate','crop','resize','normHist','eqHist','expHist','logHist','preview','history'])
            hmess += '\n'
    
        elif matter == 'levels':
            hmess = '\nAIDE - LEVELS'

        elif matter == 'curves':
            hmess = '\nAIDE - CURVES'

        elif matter == 'eqHist':
            hmess = '\nAIDE - EQHIST'

        elif matter == 'normHist':
            hmess = '\nAIDE - NORMHIST'

        elif matter == 'logHist':
            hmess = '\nAIDE - LOGHIST'

        elif matter == 'expHist':
            hmess = '\nAIDE - EXPHIST'

        elif matter == 'contrast':
            hmess = '\nAIDE - CONTRAST'

        elif matter == 'exposure':
            hmess = '\nAIDE - EXPOSURE'

        elif matter == 'histogram':
            hmess = '\nAIDE - HISTOGRAM'

        elif matter == 'lowPass':
            hmess = '\nAIDE - LOWPASS'

        elif matter == 'highPass':
            hmess = '\nAIDE - HIGHPASS'

        elif matter == 'detectEdges':
            hmess = '\nAIDE - DETECTEDGES'

        elif matter == 'enhanceEdges':
            hmess = '\nAIDE - ENHANCEEDGES'

        elif matter == 'blackandwhite':
            hmess = '\nAIDE - BLACKANDWHITE'

        elif matter == 'rotate':
            hmess = '\nAIDE - ROTATE'

        elif matter == 'crop':
            hmess = '\nAIDE - CROP'

        elif matter == 'resize':
            hmess = '\nAIDE - RESIZE'

        elif matter == 'preview':
            hmess = '\nAIDE - PREVIEW'

        elif matter == 'history':
            hmess = '\nAIDE - HISTORY'

        elif matter == 'undo':
            hmess = '\nAIDE - UNDO'

        elif matter == 'redo':
            hmess = '\nAIDE - REDO'

        elif matter == 'rebase':
            hmess = '\nAIDE - REBASE'

        elif matter == 'open':
            hmess = '\nAIDE - OPEN'

        elif matter == 'close':
            hmess = '\nAIDE - CLOSE'

        elif matter == 'load':
            hmess = '\nAIDE - LOAD'

        elif matter == 'save':
            hmess = '\nAIDE - SAVE'

        elif matter == 'export':
            hmess = '\nAIDE - EXPORT'

        elif matter == 'switch':
            hmess = '\nAIDE - SWITCH'

        else:
            hmess = '\nAIDE - Sujet inconnu.'
    

    # DEUTSCH VERSION
    elif str(language) == "DE" :
        hmess = 'Hilfe'
        hmess += '\nEntschüldigung, aber Deutsch ist nicht ganz unterstützt.'
        hmess += '\n'

    # JAPANESE VERSION
    elif str(language) == "JA" :
        hmess = 'てつだいましょうか？'
        hmess += '\n住みませんが、日本語は今あまりできません。。。英語で津かいってください。'
        hmess += '\n'

    else :
        raise NameError('PhotoWizard Error: Unsupported language')
    

    return hmess



