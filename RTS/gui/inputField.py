'''
Created on 23. 1. 2015

@author: fdobrovolny
'''


class InputField(object):
    '''
    classdocs
    @todo: Complete
    '''

    def __init__(self, main, surface, in_color, bord_color, text_color, x, y,
                 sizeX, sizeY, defaultText, textSize, border=5, maxLen=100,
                 restrictedKeys=None):
        '''
        Constructor
        '''
        self.main = main
        self.logger = self.main.logger
        self.surface = surface
        self.in_color = in_color
        self.bord_color = bord_color
        self.text_color = text_color
        self.pos = self.x, self.y = x, y
        self.size = self.sizeX, self.sizeY, sizeX, sizeY
        self.text = defaultText
        self.restrictedKeys = restrictedKeys

    def getText(self):
        return self.text