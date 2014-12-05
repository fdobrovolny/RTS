from RTS.main.ScreenManager import ScreenManager
from RTS.main.SoundManager import SoundManager
from RTS.main.EventHandler import EventHandler
import pygame
'''
Created on 30. 11. 2014

@author: fdobrovolny
'''
class main(object):
    def __init__(self):
        self.EventHandler = EventHandler(self)
        self.ScreenManager = ScreenManager(self, 1024, 680, 64, 128, 30)
        self.SoundManager = SoundManager(self)
        self.start_loop()
    
    def start_loop(self):
        while True:
            self.EventHandler.tick()
            self.ScreenManager.Draw()
            self.ScreenManager.UpdateDisplay()

if __name__ == '__main__':
    pass