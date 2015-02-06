'''
Created on 6. 2. 2015

@author: fdobrovolny
'''
import os

from RTS.main.MapLoader import Map


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

        self.logger.log(1, "SelectMap", "Initialized.")

    def draw(self):
        pass

    def stop(self):
        pass

    def _genTextures(self):
        pass

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
