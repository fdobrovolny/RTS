'''
Created on 26. 12. 2014

@author: fdobrovolny
'''
from OpenGL.GL import *
from OpenGL.GLUT import *

from RTS.gui.GLTexture import Text
from RTS.gui.Button import Button

class MainMenu(object):
    '''
    classdocs
    '''


    def __init__(self, main, screenManager):
        '''
        Constructor
        '''
        
        self.main = main
        self.logger = self.main.logger
        self.screenManager = screenManager
        self.display_surf = screenManager.display_surf
        self.colors = screenManager.colors
        self.middle = screenManager.size[0]/2
        self.logo = Text("BELLUM", 140, self.colors["Black"], self.middle-200, self.screenManager.size[1]/10)
        
        self._setupMainMenu()
        self.screenManager.setBackgrounColor(self.colors["Red"])
        self.logger.log(1, "MainMenu", "Initialized.")
    
        
    def draw(self):
        self.logo.draw()
        self.SinglePlayerButton.draw()
        self.LevelEditorButton.draw()
        self.OptionsButton.draw()
        self.QuitButton.draw()
    
    
    def _setupMainMenu(self):
        self.SinglePlayerButton = Button(self.main, self.display_surf, 
                                         self.colors["Gray"], self.colors["Blue"], self.colors["Yellow"], self.colors["White"],
                                         self.middle-200, (self.screenManager.size[1]/10)*2+39, 400, 80,
                                         "Single Player", 60, self.SiglePlayer)
        self.LevelEditorButton = Button(self.main, self.display_surf, 
                                         self.colors["Gray"], self.colors["Blue"], self.colors["Yellow"], self.colors["White"],
                                         self.middle-200, (self.screenManager.size[1]/10)*2+140, 400, 80,
                                         "Level Editor", 60, self.LevelEditor)
        self.OptionsButton = Button(self.main, self.display_surf, 
                                         self.colors["Gray"], self.colors["Blue"], self.colors["Yellow"], self.colors["White"],
                                         self.middle-200, (self.screenManager.size[1]/10)*2+240, 400, 80,
                                         "Options", 60, self.Options)
        self.QuitButton = Button(self.main, self.display_surf, 
                                         self.colors["Gray"], self.colors["Blue"], self.colors["Yellow"], self.colors["White"],
                                         self.middle-200, (self.screenManager.size[1]/10)*2+340, 400, 80,
                                         "Quit", 60, self.Quit)
    
    def SiglePlayer(self):
        self.logger.log(0, "MainMenu", "Button Single Player was hit.")
        self.screenManager.OpenGame()
    
    def LevelEditor(self):
        self.logger.log(0, "MainMenu", "Button Level Editor was hit.")
    
    def Options(self):
        self.logger.log(0, "MainMenu", "Button Options was hit.")
    
    def Quit(self):
        self.logger.log(0, "MainMenu", "Button Quit was hit.")
        self.main.quit()
    
    def __del__(self):
        del(self.SinglePlayerButton)
        del(self.OptionsButton)
        del(self.QuitButton)
        self.logger.log(1, "MainMenu", "Deinitialized.")
        
        
        
        