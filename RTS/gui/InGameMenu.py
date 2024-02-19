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

from RTS.gui.Button import Button
from RTS.gui.GLTexture import Texture


class InGameMenu(object):
    """
    classdocs
    """

    def __init__(self, main, screenManager, game, x, y):
        """
        Constructor
        """
        self.main = main
        self.screenManager = screenManager
        self.logger = self.main.logger
        self.game = game

        self.size = self.sizeX, self.sizeY = 200, 430
        self.pos = self.x, self.y = x, y
        self.text_size = 40
        self.text = "Menu"
        self.text_color = self.screenManager.colors["White"]
        self.font = None
        self.textSurf = None
        self.textRect = None

        self.Rect = None

        self.BaseSurface = None
        self.BaseTexture = None
        self.ButtonQuit = None
        self.ButtonMainMenu = None
        self.ButtonBackToGame = None
        self.ButtonOptions = None

        self._initText()
        self._initBaseTexture()
        self._initButtons()

        self.logger.log(1, "InGameMenu", "Initialized.")

    def _initBaseTexture(self):
        self.logger.log(0, "InGameMenu", "Executing _initBaseTexturet")
        self.Rect = pygame.Rect(0, 0, self.sizeX, self.sizeY)
        self.BaseSurface = pygame.Surface(self.size)

        self.textRect.centerx = self.Rect.centerx
        self.textRect.y = 15

        pygame.draw.rect(self.BaseSurface, self.screenManager.colors["Red"], self.Rect)
        pygame.draw.rect(
            self.BaseSurface, self.screenManager.colors["Black"], self.Rect, 10
        )
        self.BaseSurface.blit(self.textSurf, self.textRect)

        self.BaseTexture = Texture(None, self.BaseSurface, self.Rect)

    def _initText(self):
        self.logger.log(0, "InGameMenu", "Executing _initText")
        self.font = pygame.font.Font(None, self.text_size)
        self.textSurf = self.font.render(self.text, True, self.text_color)
        self.textRect = self.textSurf.get_rect()

    def BackToGame(self):
        if self.game.InGameMenuActive:
            self.logger.log(0, "InGameMenu", "Button Back To Game was hit.")
            self.game.closeInGameMenu()

    def Quit(self):
        if self.game.InGameMenuActive:
            self.logger.log(0, "InGameMenu", "Button Quit was hit.")
            self.game.stop()
            self.main.quit()

    def MainMenu(self):
        if self.game.InGameMenuActive:
            self.logger.log(0, "InGameMenu", "Button Main Menu was hit.")
            self.game.stop()
            self.screenManager.OpenMainMenu()

    def Options(self):
        if self.game.InGameMenuActive:
            self.logger.log(0, "InGameMenu", "Button Options was hit.")
            self.game.stop()
            # self.screenManager.OpenOptions()

    def _initButtons(self):
        self.logger.log(0, "InGameMenu", "Executing _initButtons")
        self.BackToGameButton = Button(
            self.main,
            self.screenManager.display_surf,
            self.screenManager.colors["Gray"],
            self.screenManager.colors["Blue"],
            self.screenManager.colors["Yellow"],
            self.screenManager.colors["White"],
            self.x + self.Rect.centerx - 75,
            self.y + 60,
            150,
            80,
            "Back to Game",
            30,
            self.BackToGame,
        )
        self.ButtonMainMenu = Button(
            self.main,
            self.screenManager.display_surf,
            self.screenManager.colors["Gray"],
            self.screenManager.colors["Blue"],
            self.screenManager.colors["Yellow"],
            self.screenManager.colors["White"],
            self.x + self.Rect.centerx - 75,
            self.y + 150,
            150,
            80,
            "Main Menu",
            30,
            self.MainMenu,
        )
        self.ButtonOptions = Button(
            self.main,
            self.screenManager.display_surf,
            self.screenManager.colors["Gray"],
            self.screenManager.colors["Blue"],
            self.screenManager.colors["Yellow"],
            self.screenManager.colors["White"],
            self.x + self.Rect.centerx - 75,
            self.y + 240,
            150,
            80,
            "Options",
            30,
            self.Options,
        )
        self.ButtonQuit = Button(
            self.main,
            self.screenManager.display_surf,
            self.screenManager.colors["Gray"],
            self.screenManager.colors["Blue"],
            self.screenManager.colors["Yellow"],
            self.screenManager.colors["White"],
            self.x + self.Rect.centerx - 75,
            self.y + 330,
            150,
            80,
            "Quit",
            30,
            self.Quit,
        )

    def draw(self):
        self.BaseTexture.draw(self.x, self.y)
        self.BackToGameButton.draw()
        self.ButtonMainMenu.draw()
        self.ButtonOptions.draw()
        self.ButtonQuit.draw()
