import pygame, sys, datetime
from RTS.main.ScreenManager import ScreenManager
from RTS.main.SoundManager import SoundManager
from RTS.main.EventHandler import EventHandler
from RTS.main.Logger import Logger
'''
RTS - RealTime Isometric pygame-opengl based game.
Copyright (C) 2014 Filip Dobrovolny

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''


class main(object):
    def __init__(self):
        self.logger = Logger(True)
        self.version = "0.0.2"
        self.gameDevelopmentState = "Pre-Alpha"
        self.logger.log(1, "MAIN", "Starting Bellum version "
                        + self.gameDevelopmentState + " " + self.version)
        self.logger.log(1, "MAIN", "Today is " + str(datetime.datetime.today()))

        self.EventHandler = EventHandler(self)
        self.ScreenManager = ScreenManager(self, 1024, 600, 30)
        self.SoundManager = SoundManager(self)
        self.loop = True
        self.start_loop()

    def start_loop(self):
        while self.loop:
            self.ScreenManager.clearScreen()
            self.EventHandler.tick()
            if not self.loop:
                break
            self.ScreenManager.draw()
            self.ScreenManager.UpdateDisplay()

    ''' this func is called when app is closing'''
    def quit(self):
        self.loop = False
        self.logger.log(1, "MAIN", "Quitting...")
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    pass