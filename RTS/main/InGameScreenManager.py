import pygame
from pygame.locals import *
from pygame.image import *
from  RTS.main.isoMath import IsoMathHelper
from RTS.main.GLTexture import Texture
'''
Created on 25. 12. 2014

@author: fdobrovolny
'''

class InGameScreenManager(object):
    '''
    This class takes care of drawing map units buldings etc.
    '''


    def __init__(self, main, tileSizeH, tileSizeW):
        '''
        Constructor
        '''
        self.main = main
        self.screenManager = self.main.ScreenManager
        self.tileSizeH = tileSizeH
        self.tileSizeW = tileSizeW
        
        self.IsoMathHelper = None
        self._IsoMathHelperInit()
        
        self.RegisterMapMovement()
        self.MapPosX, self.MapPosY =  0.0, 0.0
        self.MapMovConst = 10  
        
        #this stuff should be in future load by MapLoader
        self.MapSize = (20, 20)
        self.GroundMap = [[1 for i in range(self.MapSize[0])] for i in range(self.MapSize[1])]
        self.tiles = [Texture("../res/map/grass.png")]
        
        self.MouseSelectedTexture = Texture("../res/map/select_tile.png")
        self.MouseActive = True # False when user is in GUI
        
    
    def _IsoMathHelperInit(self):
        self.IsoMathHelper = IsoMathHelper(self.tileSizeW/2, self.tileSizeH/2, self.screenManager.width/2)
    
    def Draw(self):
        for x in range(self.MapSize[0]):
            for y in range(self.MapSize[1]):
                #tile = self.GroundMap[y][x] - 1
                tile = 0
                tile_x, tile_y = self.IsoMathHelper.Map2ScreenFIN((x,y), (self.MapPosX, self.MapPosY))
                self.tiles[tile].draw(tile_x, tile_y)
        
        mouseCoord = self.IsoMathHelper.Screen2MapFIN(pygame.mouse.get_pos(), (self.MapPosX, self.MapPosY))
        
        if  -1 < mouseCoord[0] <= self.MapSize[0] and -1 < mouseCoord[1] <= self.MapSize[1] and self.MouseActive:
            select_x, select_y = self.IsoMathHelper.Map2ScreenFIN((int(mouseCoord[0]), int(mouseCoord[1])), (self.MapPosX, self.MapPosY))
            self.MouseSelectedTexture.draw(select_x, select_y)
    
    
    def moveMap(self, dir1, dir2):
        if dir1:
            self.MapPosY += self.MapMovConst
        elif not dir1:
            self.MapPosY -= self.MapMovConst
        if dir2:
            self.MapPosX += self.MapMovConst
        elif not dir2:
            self.MapPosX -= self.MapMovConst
    
    def moveMapUp(self):
        self.MapPosY += self.MapMovConst
        self.MapPos = self.MapPosX, self.MapPosY
    
    def moveMapDown(self):
        self.MapPosY -= self.MapMovConst
        self.MapPos = self.MapPosX, self.MapPosY
    
    def moveMapRight(self):
        self.MapPosX -= self.MapMovConst
        self.MapPos = self.MapPosX, self.MapPosY
    
    def moveMapLeft(self):
        self.MapPosX += self.MapMovConst
        self.MapPos = self.MapPosX, self.MapPosY
    
    def RegisterMapMovement(self):
        self.main.EventHandler.registerKEYPRESSEDevent(K_UP, self.moveMapUp)
        self.main.EventHandler.registerKEYPRESSEDevent(K_DOWN, self.moveMapDown)
        self.main.EventHandler.registerKEYPRESSEDevent(K_LEFT, self.moveMapLeft)
        self.main.EventHandler.registerKEYPRESSEDevent(K_RIGHT, self.moveMapRight)
    
