from RTS.main.ScreenManager import ScreenManager
from RTS.main.SoundManager import SoundManager
from RTS.main.EventHandler import EventHandler
from RTS.main.InGameScreenManager import InGameScreenManager
import pygame
'''
Created on 30. 11. 2014

@author: fdobrovolny
'''
class main(object):
    def __init__(self):
        
        self.version = "0.0.1"
        self.gameDevelopmentState = "Pre-Alpha"
        
        self.EventHandler = EventHandler(self)
        self.ScreenManager = ScreenManager(self, 1024, 680, 30)
        self.SoundManager = SoundManager(self)
        self.InGameScreenManager = InGameScreenManager(self, 64, 128,)
        self.start_loop()
    
    def start_loop(self):
        while True:
            self.ScreenManager.clearScreen()
            self.EventHandler.tick()
            self.InGameScreenManager.Draw()
            self.ScreenManager.UpdateDisplay()

if __name__ == '__main__':
    pass