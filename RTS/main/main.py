import pygame, sys, datetime
from RTS.main.ScreenManager import ScreenManager
from RTS.main.SoundManager import SoundManager
from RTS.main.EventHandler import EventHandler
from RTS.main.InGameScreenManager import InGameScreenManager
from RTS.main.Logger import Logger
from RTS.gui.MainMenu import MainMenu
'''
Created on 30. 11. 2014

@author: fdobrovolny
'''
class main(object):
    def __init__(self):
        
        self.logger = Logger(True)
        self.version = "0.0.1"
        self.gameDevelopmentState = "Pre-Alpha"
        self.logger.log(1, "MAIN", "Starting Bellum version " + self.gameDevelopmentState + " " + self.version)
        self.logger.log(1, "MAIN", "Today is " + str(datetime.datetime.today()))
        
        self.EventHandler = EventHandler(self)
        self.ScreenManager = ScreenManager(self, 1024, 600, 30)
        self.SoundManager = SoundManager(self)
        self.mainMenu = MainMenu(self)
        #self.InGameScreenManager = InGameScreenManager(self, 64, 128,)
        self.start_loop()
    
    def start_loop(self):
        while True:
            self.ScreenManager.clearScreen()
            self.EventHandler.tick()
            self.mainMenu.draw()
            #self.InGameScreenManager.Draw()
            self.ScreenManager.UpdateDisplay()
    
    
    ''' this func is called when app is closing'''
    def quit(self):
        self.logger.log(1, "MAIN", "Quitting...")
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    main()