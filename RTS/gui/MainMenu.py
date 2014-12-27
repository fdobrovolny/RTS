'''
Created on 26. 12. 2014

@author: fdobrovolny
'''
from OpenGL.GL import *
from OpenGL.GLUT import *

from RTS.main.ScreenManager import ScreenManager
from RTS.gui.GLTexture import Texture
from RTS.gui.Button import Button

class MainMenu(object):
    '''
    classdocs
    '''


    def __init__(self, main):
        '''
        Constructor
        '''
        
        self.main = main
        self.screenManager = self.main.ScreenManager
        self.display_surf = self.main.ScreenManager.display_surf
        self.colors = self.screenManager.colors
        self.logo = Texture("../res/UI/Logo.png")
        self.middle = self.screenManager.size[0]/2
        
        self._setupMainMenu()
        self.screenManager.setBackgrounColor(self.colors["Red"])
        
    
        
    def draw(self):
        self.logo.draw(self.middle-324/2, self.screenManager.size[1]/10)
        self.SinglePlayerButton.draw()
        self.OptionsButton.draw()
        self.QuitButton.draw()
    
    
    def _setupMainMenu(self):
        self.SinglePlayerButton = Button(self.main, self.display_surf, 
                                         self.colors["Gray"], self.colors["Blue"], self.colors["Yellow"], self.colors["White"],
                                         self.middle-200, (self.screenManager.size[1]/10)*2+39, 400, 80,
                                         "Single Player", 60, self.SiglePlayer)
        self.OptionsButton = Button(self.main, self.display_surf, 
                                         self.colors["Gray"], self.colors["Blue"], self.colors["Yellow"], self.colors["White"],
                                         self.middle-200, (self.screenManager.size[1]/10)*2+140, 400, 80,
                                         "Options", 60, self.Options)
        self.QuitButton = Button(self.main, self.display_surf, 
                                         self.colors["Gray"], self.colors["Blue"], self.colors["Yellow"], self.colors["White"],
                                         self.middle-200, (self.screenManager.size[1]/10)*2+240, 400, 80,
                                         "Quit", 60, self.main.quit)
    
    def SiglePlayer(self):
        print("Single Player")
    
    def Options(self):
        print("Options")
        
        
        
        