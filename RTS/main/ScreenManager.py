"""
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
"""

import pygame
from OpenGL.GL import *
from pygame.locals import *

from RTS.gui.Game import Game
from RTS.gui.MainMenu import MainMenu
from RTS.gui.SelectMap import SelectMap


class ScreenManager(object):
    """
    classdocs
    """

    def __init__(self, main, width, height, maxFPS):
        self.main = main
        self.logger = self.main.logger
        self.size = self.width, self.height = width, height
        self.flags = OPENGL | DOUBLEBUF  # | FULLSCREEN
        self.maxFPS = maxFPS

        self.display_surf = None
        self._PygameInit()
        self._OpenGLInit()
        self.FPSClock = pygame.time.Clock()
        self.colors = {}
        self.SetupColors()
        self.backgroundColorR = 0.0
        self.backgroundColorG = 0.0
        self.backgroundColorB = 0.0
        self.backgroundColorA = 1.0

        self.logger.log(1, "ScreenManager", "Initialized.")
        self.logger.log(0, "ScreenManager", "Size: " + str(self.size))
        self.logger.log(0, "ScreenManager", "MaxFPS: " + str(self.maxFPS))

        self.screen = None
        self.OpenMainMenu()

    def _PygameInit(self):
        pygame.init()
        self.display_surf = pygame.display.set_mode(self.size, self.flags)
        pygame.display.set_caption(
            "Bellum " + self.main.gameDevelopmentState + " " + self.main.version
        )
        self.logger.log(1, "ScreenManager", "Pygame initialized.")

    def _OpenGLInit(self):
        # init gl
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, self.width, self.height, 0, 0, 1)
        glMatrixMode(GL_MODELVIEW)

        # set textures
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.logger.log(1, "ScreenManager", "OpenGL initialized.")

    def SetupColors(self):
        self.colors["Aqua"] = (0, 255, 255)
        self.colors["Black"] = (0, 0, 0)
        self.colors["Blue"] = (0, 0, 255)
        self.colors["Fuchsia"] = (255, 0, 255)
        self.colors["Gray"] = (128, 128, 128)
        self.colors["Green"] = (0, 128, 0)
        self.colors["Lime"] = (0, 255, 0)
        self.colors["Maroon"] = (128, 0, 0)
        self.colors["Navy Blue"] = (0, 0, 128)
        self.colors["Olive"] = (128, 128, 0)
        self.colors["Purple"] = (128, 0, 128)
        self.colors["Red"] = (255, 0, 0)
        self.colors["Silver"] = (192, 192, 192)
        self.colors["Teal"] = (0, 128, 128)
        self.colors["White"] = (255, 255, 255)
        self.colors["Yellow"] = (255, 255, 0)

    def clearScreen(self):
        glClearColor(
            self.backgroundColorR,
            self.backgroundColorG,
            self.backgroundColorB,
            self.backgroundColorA,
        )
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    def UpdateDisplay(self):
        self.FPSClock.tick(self.maxFPS)
        pygame.display.flip()

    def setBackgrounColor(self, color, alpha=0.0):
        self.backgroundColorR, self.backgroundColorG, self.backgroundColorB = color
        self.backgroundColorA = alpha
        self.logger.log(0, "ScreenManager", "Setting background color to " + str(color))

    def OpenMainMenu(self):
        self.logger.log(1, "ScreenManager", "Opening MainMenu")
        if self.screen is not None:
            self.screen.stop()
        del self.screen
        self.screen = MainMenu(self.main, self)

    def OpenGame(self, map="base"):
        self.logger.log(1, "ScreenManager", "Opening Game")
        if self.screen is not None:
            self.screen.stop()
        del self.screen
        self.screen = Game(self.main, self, 64, 128, map)
        self.logger.log(1, "ScreenManager", "Game Opened")

    def OpenSelectMap(self, nextScreen=None):
        if nextScreen is None:
            nextScreen = self.OpenGame
        if self.screen is not None:
            self.screen.stop()
        del self.screen
        self.screen = SelectMap(self.main, self, nextScreen)

    def draw(self):
        try:
            self.screen.draw()
        except:
            pass
