'''
Created on 6. 2. 2015

@author: fdobrovolny
'''
import os

from RTS.main.MapLoader import Map
from RTS.gui.GLTexture import Text
from RTS.gui.Button import Button


class SelectMap(object):
    '''
    classdocs
    '''

    def __init__(self, main, screenManager, nextScreen):
        '''
        Constructor
        '''
        self.main = main
        self.logger = self.main.logger
        self.screenManager = screenManager
        self.display_surf = screenManager.display_surf
        self.colors = screenManager.colors
        self.middle = screenManager.size[0]/2
        self.nextScreen = nextScreen
        self.screenManager.setBackgrounColor(self.colors["Navy Blue"])
        self.MAPS_PATH = "../res/maps"
        self.MapList = []

        self._loadMaps()

        self.pages = len(self.MapList)/5
        self.arePages = True if self.pages > 1 else False
        self.page = 0

        self.buttons = []

        self.text = Text("Select Map", 50,
                         self.colors["Black"],
                         self.middle-200,
                         self.screenManager.size[1]/20)

        self.logger.log(1, "SelectMap", "Initialized.")

    def draw(self):
        self.text.draw()

    def stop(self):
        pass

    def _genTextures(self):
        for MapEntry in self.MapList:
            self.buttons.append(Button(self.main,
                                       self.display_surf,
                                       self.colors["Gray"],
                                       self.colors["Blue"],
                                       self.colors["Yellow"],
                                       self.colors["White"],
                                       self.middle-200,
                                       (self.screenManager.size[1]/10)*2+39,
                                       400, 80,
                                       MapEntry.name, 60,
                                       self.onClick,
                                       MapEntry))

    def _loadMaps(self):
        self.logger.log(1, "SelectMap", "Loading maps.")
        files = os.listdir(self.MAPS_PATH)
        for i in files:
            if i[-4:] == ".map":
                self.logger.log(0, "SelectMap", "Loading info for map \""
                                + self.MAPS_PATH+"/"+i+"\"")
                self.MapList.append(Map(i[:-4], self.logger).loadMapInfo())
                self.logger.log(1, "SelectMap", "Loaded info for map \""
                                + self.MAPS_PATH+"/"+i+"\"")

    def _onClick(self, ident):
        self.nextScreen(ident)