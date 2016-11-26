# -*- coding: utf-8 -*-

#/////////////////////////////#
# - P H O T O   W I Z A R D - #
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#


# This file loads the configuration variables in the config.py file



### DEFAULT VALUES ###

LANG = "EN"
MODE = "c"

WIDTH_PREVIEW = 400
HEIGHT_PREVIEW = 400

CURVES_RESOLUTION = 8
EQHIST_RESOLUTION = 4
EXPHIST_RESOLUTION = 8
EXPOSURE_RESOLUTION = 8
LOGHIST_RESOLUTION = 8



def load():

    try:
        import config

        global LANG,MODE,WIDTH_PREVIEW,HEIGHT_PREVIEW,CURVES_RESOLUTION,EQHIST_RESOLUTION,EXPHIST_RESOLUTION,EXPOSURE_RESOLUTION,LOGHIST_RESOLUTION
    

        if config.LANG in ['EN','FR','DE','JA']:
            LANG = config.LANG
        else:
            print('PhotoWizard Error: Unknown language - using default settings')

        if config.MODE in ['c','g']:
            MODE = config.MODE
        else:
            print('PhotoWizard Error: Unknown mode - using default settings')


        if (config.WIDTH_PREVIEW > 0) and (config.WIDTH_PREVIEW < 10000):
            WIDTH_PREVIEW = config.WIDTH_PREVIEW
        else:
            print('PhotoWizard Error: Wrong value for width_preview - using default settings')


        if (config.HEIGHT_PREVIEW > 0) and (config.HEIGHT_PREVIEW < 10000):
            HEIGHT_PREVIEW = config.HEIGHT_PREVIEW
        else:
            print('PhotoWizard Error: Wrong value for height_preview - using default settings')

        if (config.CURVES_RESOLUTION > 0) and (config.CURVES_RESOLUTION < 129):
            CURVES_RESOLUTION = config.CURVES_RESOLUTION
        else:
            print('PhotoWizard Error: Wrong value for curves_resolution - using default settings')
       
        if (config.EQHIST_RESOLUTION > 0) and (config.EQHIST_RESOLUTION < 129):
            EQHIST_RESOLUTION = config.EQHIST_RESOLUTION
        else:
            print('PhotoWizard Error: Wrong value for eqhist_resolution - using default settings')

        if (config.EXPHIST_RESOLUTION > 0) and (config.EXPHIST_RESOLUTION < 129):
            EXPHIST_RESOLUTION = config.EXPHIST_RESOLUTION
        else:
            print('PhotoWizard Error: Wrong value for exphist_resolution - using default settings')
       
        if (config.EXPOSURE_RESOLUTION > 0) and (config.EXPOSURE_RESOLUTION < 129):
            EXPOSURE_RESOLUTION = config.EXPOSURE_RESOLUTION
        else:
            print('PhotoWizard Error: Wrong value for exposure_resolution - using default settings')

        if (config.LOGHIST_RESOLUTION > 0) and (config.LOGHIST_RESOLUTION < 129):
            LOGHIST_RESOLUTION = config.LOGHIST_RESOLUTION
        else:
            print('PhotoWizard Error: Wrong value for loghist_resolution - using default settings')

    except Exception as e:
        print(e)
        raise NameError('PhotoWizard Error: Unable to load configuration file; using default values')


    return

