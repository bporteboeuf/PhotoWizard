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
            hmess += '\nYou just need to select the channel on which you want to apply the effect. You can choose between R,G,B,H,S,V and ALL.'
            hmess += '\n\nExample: eqHist V'
            hmess += '\n'

        elif matter == 'normHist':
            hmess = '\nHELP - NORMHIST'
            hmess += '\nThis module offers the possibility to normalize the histogram using a linear function, which is a way to increase the contrast and overall detail of an image.'
            hmess += '\nYou just need to select the channel on which you want to apply the effect. You can choose between R,G,B,H,S,V and ALL.'
            hmess += '\n\nExample: normHist V'
            hmess += '\n'


        elif matter == 'logHist':
            hmess = '\nHELP - LOGHIST'
            hmess += '\nThis module offers the possibility to normalize the histogram using a logarithmic function, which is a way to increase the contrast and overall detail of an underexposed image, recovering a lot of details in the dark areas.'
            hmess += '\nYou just need to select the channel on which you want to apply the effect. You can choose between R,G,B,H,S,V and ALL.'
            hmess += '\n\nExample: logHist V'
            hmess += '\n'


        elif matter == '\nexpHist':
            hmess = '\nHELP - EXPHIST'
            hmess += '\nThis module offers the possibility to normalize the histogram using an exponential function, which is a way to increase the contrast and overall detail of an overexposed image, recovering a lot of details in the light areas.'
            hmess += '\nYou just need to select the channel on which you want to apply the effect. You can choose between R,G,B,H,S,V and ALL.'
            hmess += '\n'


        elif matter == 'contrast':
            hmess = '\nHELP - CONTRAST'
            hmess += '\nThis module offers the possibility to modify the contrast of an image.'
            hmess += '\nYou first need to specify the channel on which you want to apply the effect. You can choose between R,G,B,H,S,V or ALL.'
            hmess += '\nYou then simply need to specify the percentage by which you want to modify your contrast: +100 to double it or -50 to divide it by 2 for isntance.'
            hmess += '\n\nExample: contrast ALL 25'
            hmess += '\n'

        elif matter == 'exposure':
            hmess = '\nHELP - EXPOSURE'
            hmess += '\nUnfortunately, this function is not implemented yet. Try using LEVELS or CURVES.'

        elif matter == 'histogram':
            hmess = '\nHELP - HISTOGRAM'
            hmess += '\nThis module displays a normalized histogram of the working copy of your image.'
            hmess += '\nAn histogram is a graphic that details how much pixels have a given value. The value (range 0 to 255 from left to right) is on the X-axis and the number (or proportion) of concerned pixels is represented on the Y-axis.'
            hmess += '\nIt is a great way to know if your picture is over or underexpoed for instance.'
            hmess += '\nYou just need to select the channel on which you want to apply the effect. You can choose between R,G,B,H,S,V and ALL.'
            hmess += '\n\nExample: histogram R'
            hmess += '\n'

        elif matter == 'lowPass':
            hmess = '\nHELP - LOWPASS'
            hmess += '\nThis module offers the possibility to apply a low-pass filter on your image (essentially a blurring effet).'
            hmess += '\nYou first need to specify the filter you want to use. It can currently be: GAUSSIAN-2D, MEAN-2D, POISSON-2D,GAUSSIAN-1D, MEAN-1D, POISSON-1D.'
            hmess += '\nThen you also need to provide the correct parameters for those filters, such as a radius (integer), a coefficient (float) for GAUSSIAN-2D and POISSON-2D, an opacity coefficient (float bewteen O and 1) for MEAN-2D and MEAN-1D  and an angle in degrees (float) for GAUSSIAN-1D, MEAN-1D, POISSON-1D.'
            hmess += '\nFinally, you need to precise the channel on which you want to apply your effect. You can choose between R,G,B,H,S,V or ALL.'
            hmess += '\n\nExamples: lowPass GAUSSIAN-2D [20,1] ALL'
            hmess += '          lowPass MEAN-1D [20,45] ALL'
            hmess += '\n'

        elif matter == 'highPass':
            hmess = '\nHELP - HIGHPASS'
            hmess += '\nThis module offers the possibility to apply a high-pass filter on your image (essentially a sharpening effet).'
            hmess += '\nYou first need to specify the filter you want to use. It can currently be: DIFF-2D, DIFF-1D.'
            hmess += '\nThen you also need to provide the correct parameters for those filters, such as a radius (integer), an opacity coefficient (float bewteen 0 and 1) for DIFF-1D and an angle in degrees (float) for DIFF-1D.'
            hmess += '\nFinally, you need to precise the channel on which you want to apply your effect. You can choose between R,G,B,H,S,V or ALL.'
            hmess += '\n\nExamples: highPass DIFF-2D [5]  ALL'
            hmess += '          highPass DIFF-1D [5,45] ALL'
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
            hmess += '\nUnfortunately, this function is not implemented yet. Try using LEVELS on the S channel.'

        elif matter == 'rotate':
            hmess = '\nHELP - ROTATE'
            hmess += '\nThis module offers the possibility to rotate your image counter clockwise by a given angle in degrees (float).'
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
            hmess += '\n\nNote: If a node is found and the REDO action proves to be inefficient, you can always force it to enter a new branch or to directly restore a new state by using the REBASE command.'
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
            hmess += '\nYou just need to specify the path of the XMD file (relative or absolute).'
            hmess += '\n\nExample: load pic/test3.xmd'
            hmess += '\n'

        elif matter == 'save':
            hmess = '\nHELP - SAVE'
            hmess += '\nThis command saves the current history in an XMD file, so that it can be restored for future use.'
            hmess += '\nYou just need to specify the desired path (relative or absolute).'
            hmess += '\n\nExample: save pic/test3-1.xmd'

        elif matter == 'export':
            hmess = '\nHELP - EXPORT'
            hmess += '\nThis command actually exports your final image. All your modifications will then be applied to your full-sized image.'
            hmess += '\nYou just need to specify the desired path (relative or absolute). The extension of the file will be interpreted as the format for export.'
            hmess += '\n\nExample: export pic/test3.tiff'
            hmess += '\n'

        elif matter == 'switch':
            hmess = '\nHELP - SWITCH'
            hmess += '\nThis function allows you to switch between several opened images so that you can edit different pictures in parallel.'
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
            hmess += '\nCe module offre la possibilité de modifier les niveaux d\'une image, c\'est-à-dire de modifier les valeurs de sorties sur des intervalles d\'entrée donnés.'
            hmess += '\nIl faut tout d\'abord sélectionner un canal sur lequel appliquer l\'effet, au choix parmi R,G,B,H,S,V ou ALL.'
            hmess += '\nIl faut ensuite donner les bornes des intervalles d\'entrée comme suit : [ia,ib,ic] où (ia,ib,ic) sont des entiers de 0 à 255, ia/ib définissant les tons sombres de l\'image et ib/ic les tons clairs.'
            hmess += '\nDe la même manière, il faut renseigner les bornes des intervalles de sortie [oa,ob,oc] comme des entiers de 0 à 255.'
            hmess += '\n\nRemarque : il est possible de renseigner autant de bornes en entrée et en sortie, du moment que les longueurs des listes d\'entrées et de sorties sont égales et comprises entre 2 et 257.'
            hmess += '\n\nExemple : levels ALL [30,128,220] [0,128,255]'
            hmess += '\n'
        
        elif matter == 'curves':
            hmess = '\nAIDE - CURVES'
            hmess += '\nCe module offre la possibilité de changer la courbe de dynamique de l\'image, c\'est-à-dire de changer les valeurs de sortie en fonction d\'intervalles de valeurs d\'entrée précisés.'
            hmess += '\nCe module fonctionne de manière très similaire au module LEVELS, sauf que LEVELS propose une réponse dynamique C-0 alors que CURVES propose une réponse dynamique C1 en utilisant une interpolation par spline.'
            hmess += '\nIl faut tout d\'abord sélectionner un cannal sur lequel appliquer l\'effet, au choix parmi R,G,B,H,S,V ou ALL.'
            hmess += '\nIl faut ensuite donner les bornes des intervalles d\'entrée comme suit : [ia,ib,ic] où (ia,ib,ic) sont des entiers de 0 à 255, ia/ib définissant les tons sombres de l\'image et ib/ic les tons clairs.'
            hmess += '\nDe la même manière, il faut renseigner les bornes des intervalles de sortie [oa,ob,oc] comme des entiers de 0 à 255.'
            hmess += '\n\nRemarque : il est possible de renseigner autant de bornes en entrée et en sortie, du moment que les longueurs des listes d\'entrées et de sorties sont égales et comprises entre 4 et 257.'
            hmess += '\n\nExemple : curves ALL [20,30,50,128,200,220,230] [0,5,15,128,240,250,255]'
            hmess += '\n'

        elif matter == 'eqHist':
            hmess = '\nAIDE - EQHIST'
            hmess += '\nCe module offre la possibilité d\'égaliser l\'histogramme, ce qui est une moyen d\'augmenter le contrast et le détail global d\'une image.'
            hmess += '\nIl suffit de sélectionner un cannal sur lequel appliquer l\'effet, au choix parmi R,G,B,H,S,V ou ALL.'
            hmess += '\n\nExemple : eqHist V'
            hmess += '\n'

        elif matter == 'normHist':
            hmess = '\nAIDE - NORMHIST'
            hmess += '\nCe module offre la possibilité de normaliser l\'histogramme en utilisant une fonction linéaire, ce qui est un moyen d\'augmenter le contraste et le détail global d\'une image.'
            hmess += '\nIl suffit de sélectionner un cannal sur lequel appliquer l\'effet, au choix parmi R,G,B,H,S,V ou ALL.'
            hmess += '\n\nExemple : normHist V'
            hmess += '\n'

        elif matter == 'logHist':
            hmess = '\nAIDE - LOGHIST'
            hmess += '\nCe module offre la possibilité de normaliser l\'histogramme en utilisant une fonction logarithmique, ce qui est un moyen d\'augmenter le contraste et le détail global d\'une image sous-exposée, en restaurant beaucoup de détails dans les zones sombres.'
            hmess += '\nIl suffit de sélectionner un cannal sur lequel appliquer l\'effet, au choix parmi R,G,B,H,S,V ou ALL.'
            hmess += '\n\nExemple : logHist V'
            hmess += '\n'

        elif matter == '\nexpHist':
            hmess = '\nAIDE - EXPHIST'
            hmess += '\nCe module offre la possibilité de normaliser l\'histogramme en utilisant une fonction exponentielle, ce qui est un moyen d\'augmenter le contraste et le détail global d\'une image sur-exposée, en restaurant beaucoup de détails dans les zones claires.'
            hmess += '\nIl suffit de sélectionner un cannal sur lequel appliquer l\'effet, au choix parmi R,G,B,H,S,V ou ALL.'
            hmess += '\n\nExemple : expHist V'
            hmess += '\n'

        elif matter == 'contrast':
            hmess = '\nAIDE - CONTRAST'
            hmess += '\nCe module offre la possibilité de modifier le contraste d\'une image.'
            hmess += '\nIl faut d\'abord sélectionner le canal sur lequel appliquer l\'effet, au choix parmi R,G,B,H,S,V ou ALL.'
            hmess += '\nIl suffit ensuite de préciser le pourcentage par lequel vous voulez modifier le contraste: +100 pour le doubler ou -50 pour le diviser par 2 par exemple.'
            hmess += '\n\nExemple : contrast ALL 25'
            hmess ++ '\n'

        elif matter == 'exposure':
            hmess = '\nAIDE - EXPOSURE'
            hmess += '\nMalheureusement, cette fonction n\'est pas encore implémentée. Essayez d\'utiliser le module LEVELS ou CURVES.'

        elif matter == 'histogram':
            hmess = '\nAIDE - HISTOGRAM'
            hmess += '\nCe module affiche un histogramme normalisé de la copie de travail de votre image.'
            hmess += '\nUn histogramme est un diagramme qui explique quel nombre de pixels ont une valeur donnée. Les valeurs (entiers de 0 à 255 de gauche à droite) sont sur l\'axe des abscisses et le nombre (ou la proportion) de pixels correspondants représenté sur l\'axe des ordonnées.'
            hmess += '\nC\'est par exemple un très bon outil pour savoir si une image est sous-exposée ou sur-exposée.'
            hmess += '\nIl suffit de sélectionner un cannal sur lequel appliquer l\'effet, au choix parmi R,G,B,H,S,V ou ALL.'
            hmess += '\n\nExemple : histogram R'
            hmess += '\n'

        elif matter == 'lowPass':
            hmess = '\nAIDE - LOWPASS'
            hmess += '\nCe module offre la possibilité d\'appliquer un filtre passe-bas sur une image (soit essentiellement un effet de flou).'
            hmess += '\nIl faut d\'abord sélectionner le type de filtre à utiliser. Pour l\'instant, vous pouvez choisir parmi : GAUSSIAN-2D, MEAN-2D, POISSON-2D, GAUSSIAN-1D, MEAN-1D, POISSON-1D.'
            hmess += '\nIl faut ensuite fournir les paramètres nécessaires au filtre, comme le rayon (entier), éventuellement un coefficient (flottant) pour GAUSSIAN-2D et POISSON-2D, un coefficient d\'opacité (flottant entre 0 et 1) pour MEAN-2D et MEAN-1D et un angle en degrés (flottant) pour GAUSSIAN-1D, MEAN-1D et POISSON-1D.'
            hmess += '\nEnfin, il faut préciser le canal sur lequel appliquer l\'effet, au choix parmi R,G,B,H,S,V ou ALL.'
            hmess += '\n\nExemples : lowPass GAUSSIAN-2D [20,1] ALL'
            hmess += '           lowPass MEAN-1D [20,45] ALL'
            hmess += '\n'

        elif matter == 'highPass':
            hmess = '\nAIDE- HIGHPASS'
            hmess += '\nCe module offre la possibilité d\'appliquer un filtre passe-haut sur une image (soit essentiellement un effet d\'accentuation).'
            hmess += '\nIl faut d\'abord sélectionner le type de filtre à utiliser. Pour l\'instant, vous pouvez choisir parmi : DIFF-2D.'
            hmess += '\nIl faut ensuite fournir les paramètres nécessaires au filtre, comme le rayon (entier), un coefficient d\'opacité (float entre 0 et 1) pour DIFF-1D et un angle en degrés (flottant) pour DIFF-1D.'
            hmess += '\nEnfin, il faut préciser le canal sur lequel appliquer l\'effet, au choix parmi R,G,B,H,S,V ou ALL.'
            hmess += '\n\nExemples : highPass DIFF-2D [5]  ALL'
            hmess += '           highPass DIFF-1D [5,45] ALL'
            hmess += '\n'

        elif matter == 'detectEdges':
            hmess = '\nAIDE - DETECTEDGES'
            hmess += '\nCe module offre la possibilité de détecter les contours sur une image.'
            hmess += '\nCe module fonctionne de manière similaire au module HIGHPASS sauf qu\'il nécessite également une valeur de seuil.'
            hmess += '\nIl faut d\'abord sélectionner le canal sur lequel appliquer l\'effet, au choix parmi R,G,B,H,S,V ou ALL.'
            hmess += '\nIl faut ensuite préciser le type de filtre à utiliser. Pour l\'instant, vous pouvez choisir parmi : DIFF-2D.'
            hmess += '\nIl faut ensuite fournir les paramètres nécessaires au filtre, comme le rayon (entier).'
            hmess += '\nEnfin, il faut renseigner la valeur de seuil (entier de 0 à 255).'
            hmess += '\n\nExemple : detectEdges V DIFF-2D [5] 100'
            hmess += '\n'

        elif matter == 'enhanceEdges':
            hmess = 'AIDE - ENHANCEEDGES'
            hmess += '\nCe module offre la possibilité d\'accetuer les contours sur une image.'
            hmess += '\nCe module fonctionne de manière similaire au module HIGHPASS sauf qu\'il nécessite également une valeur de seuil et de gain (opacité).'
            hmess += '\nIl faut d\'abord sélectionner le canal sur lequel appliquer l\'effet, au choix parmi R,G,B,H,S,V ou ALL.'
            hmess += '\nIl faut ensuite préciser le type de filtre à utiliser. Pour l\'instant, vous pouvez choisir parmi : DIFF-2D.'
            hmess += '\nIl faut ensuite fournir les paramètres nécessaires au filtre, comme le rayon (entier).'
            hmess += '\nEnfin, il faut renseigner la valeur de seuil (entier de 0 à 255), ainsi que le gain (flottant de 0 à 1).'
            hmess += '\n\nExemple : enhanceEdges V DIFF-2D [5] 100 .85'
            hmess += '\n'



        elif matter == 'blackandwhite':
            hmess = '\nAIDE - BLACKANDWHITE'
            hmess += '\nMalheureusement, cette fonction n\'est pas encore implémentée. Essayer d\'utiliser le module LEVELS sur le canal S.'


        elif matter == 'rotate':
            hmess = '\nAIDE - ROTATE'
            hmess += '\nCe module offre la possibilité d\'appliquer une rotation d\'un angle (en degrés, flottant) donné sur une image.'
            hmess += '\n\nExemple : rotate 30'
            hmess += '\n'

        elif matter == 'crop':
            hmess = '\nAIDE - CROP'
            hmess += '\nCe module offre la possibilité de recadrer une image.'
            hmess += '\nIl suffit de préciser les coordonnées du nouveau point supérieur gauche et du nouveau point inférieur droit.'
            hmess += '\n\nExemple : crop [10,20,150,210]'
            hmess += '\n'

        elif matter == 'resize':
            hmess = '\nAIDE - RESIZE'
            hmess += '\nCe module offre la possibilité de mettre à l\'échelle une image.'
            hmess += ' Il suffit de préciser la largeur et la hauteur de la nouvelle image.'
            hmess += '\n\nExemple : resize [800,600]'
            hmess += '\n'

        elif matter == 'preview':
            hmess = '\nAIDE - PREVIEW'
            hmess += '\nCe module ouvre une fenêtre pop-up afin de prévisualiser l\'image finale.'
            hmess += '\n\nExemple : preview'
            hmess += '\n'

        elif matter == 'history':
            hmess = '\nAIDE - HISTORY'
            hmess += '\nMalheureusement, cette fonction n\'est pas encore totalement supportée.'

        elif matter == 'undo':
            hmess = '\nAIDE - UNDO'
            hmess += '\nCette commande annule la dernière modification, jusqu\'à retourner à l\'état initial.'
            hmess += '\n\nExemple : undo'
            hmess += '\n'

        elif matter == 'redo':
            hmess = '\nAIDE - REDO'
            hmess += '\nCette commande restaure la dernière action annulée par la commande UNDO. Si vous voulez restaurer plus d\'une action, la fonction essaiera de remonter le long de la branche de l\'historique jusqu\'à atteindre une feuille ou un noeud.'
            hmess += '\n\nRemarque : Si un noeud est trouvé et que la commande REDO s\'avère inefficace, il est toujours possible de la forcer à entrer dans une branche ou à restaurer un état précis de l\'historique à l\'aide de la commande REBASE.'
            hmess += '\n\nExemple : redo'
            hmess += '\n'

        elif matter == 'rebase':
            hmess = '\nAIDE - REBASE'
            hmess += '\nCette commande restaure le système à l\'état donné dans l\'historique courant.'
            hmess += '\nIl suffit de préciser le numéro de l\'état à restaurer (0 pour l\'état initial).'
            hmess += '\n\nExemple : rebase 0'
            hmes += '\n'

        elif matter == 'open':
            hmess = '\nAIDE - OPEN'
            hmess += '\nCette commande ouvre un fichier image compatible avec PhotoWizard.'
            hmess += '\nIl suffit de préciser le chemin (relatif ou absolu) de l\'image.'
            hmess += ' Ce chemin servira d\'identifiant pour sélectionner cette image parmi les différents fichiers ouverts.'
            hmess += '\n\nExemple : open pic/test1.jpg'
            hmess += '\n'

        elif matter == 'close':
            hmess = '\nAIDE - CLOSE'
            hmess += '\nCette commande ferme une image donnée et supprime l\'historique correspondant (sauf s\'il a été sauvegardé dans un fichier XMD, bien sûr).'
            hmess += '\nIl suffit de préciser l\'identifiant de votre image, qui est le chemin que vous avez entré pour l\'ouvrir.'
            hmess += '\n\nExemple : close pic/test1.jpg'
            hmess += '\n'

        elif matter == 'load':
            hmess = '\nAIDE - LOAD'
            hmess += '\nCette commande charge un fichier XMD qui contient un historique de modifications, le greffe à l\'historique courant comme une nouvelle branche, et met à jour l\'état courant.'
            hmess += '\nIl suffit de préciser le chemin vers le fichier XMD (relatif ou absolu).'
            hmess += '\n\nExemple : load pic/test3.xmd'
            hmess += '\n'

        elif matter == 'save':
            hmess = '\nAIDE - SAVE'
            hmess += '\nCette commande sauvegarde l\'historique courant dans un fichier XMD, afin de permettre une restauration de celui-ci pour un usage futur.'
            hmess += '\nIl suffit de préciser le chemin désiré (relatif ou absolu).'
            hmess += '\n\nExemple : save pic/test3-1.xmd'

        elif matter == 'export':
            hmess = '\nAIDE - EXPORT'
            hmess += '\nCette commande exporte l\'image finale. Toutes les modifications seront alors appliquées à votre image en pleine résolution.'
            hmess += '\nIl suffit de préciser le chemin désiré (relatif ou absolu). L\'extension du fichier sera interprétée comme le format pour l\'export.'
            hmess += '\n\nExemple : export pic/test3.tiff'
            hmess += '\n'

        elif matter == 'switch':
            hmess = '\nAIDE - SWITCH'
            hmess += '\nCette commande permet de changer entre plusieurs images ouvertes et de sélectionner l\'image courante de travail, permettant ainsi d\'éditer différentes images en parallèle.'
            hmess += '\nIl suffit de préciser l\'identifiant de l\'image, qui est le chemin que vous avez entré pour l\'ouvrir.'
            hmess += '\n\nExemple : switch pic/test2.jpg'
            hmess += '\n'

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



