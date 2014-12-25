import os, sys
import pygame
from pygame.locals import *
from pygame.image import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from RTS.main.isoMath import IsoMathHelper
from RTS.main.GLTexture import Texture

'''
Created on 30. 11. 2014

@author: fdobrovolny
'''

class ScreenManager(object):
    '''
    classdocs
    '''


    def __init__(self, main, width, height, tileSizeH, tileSizeW, maxFPS):
        self.main = main
        self.size = self.width, self.height = width, height
        self.tileSizeH = tileSizeH
        self.tileSizeW = tileSizeW
        self.flags = OPENGL | DOUBLEBUF
        self.maxFPS = maxFPS
        self.MapPosX, self.MapPosY =  0.0, 0.0
        self.MapMovConst = 10
        self.MapSize = (20, 20)
        
        self._display_surf = None
        self.IsoMathHelper = None
        self._IsoMathHelperInit()
        self._PygameInit()
        self._OpenGLInit()
        self.FPSClock = pygame.time.Clock()
        self.colors = {}
        self.SetupColors()
        self.RegisterMapMovement()
        
        self.GroundMap = [[1 for i in range(10)] for i in range(10)]
        self.tiles = [Texture("../res/map/grass.png")]
        self.MouseSelectedTexture = Texture("../res/map/select_tile.png")
        self.MouseActive = True # False when user is in GUI
    
    def _IsoMathHelperInit(self):
        self.IsoMathHelper = IsoMathHelper(self.tileSizeW/2, self.tileSizeH/2, self.width/2)
    
    def _PygameInit(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, self.flags)
    
    def _OpenGLInit(self):
        #init gl
        glClearColor(0.0,0.0,0.0,1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
 
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0,self.width ,self.height ,0,0,1)
        glMatrixMode(GL_MODELVIEW)
 
        #set textures
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
    
    def SetupColors(self):
        self.colors["Aqua"] = (  0, 255, 255)
        self.colors["Black"] = (  0,   0,   0)
        self.colors["Blue"] = (  0,  0, 255)
        self.colors["Fuchsia"] = (255,   0, 255)
        self.colors["Gray"] = (128, 128, 128)
        self.colors["Green"] = (  0, 128,   0)
        self.colors["Lime"] = (  0, 255,   0)
        self.colors["Maroon"] = (128,  0,   0)
        self.colors["Navy Blue"] = (  0,  0, 128)
        self.colors["Olive"] = (128, 128,   0)
        self.colors["Purple"] = (128,  0, 128)
        self.colors["Red"] = (255,   0,   0)
        self.colors["Silver"] = (192, 192, 192)
        self.colors["Teal"] = (  0, 128, 128)
        self.colors["White"] = (255, 255, 255)
        self.colors["Yellow"] = (255, 255,   0)
    
    def clearScreen(self):
        glClearColor(0.0,0.0,0.0,1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    def Draw(self):
        self.clearScreen()
        for x in range(self.MapSize[0]):
          for y in range(self.MapSize[1]):
            #tile = self.GroundMap[y][x] - 1
            tile = 0
            tile_x, tile_y = self.IsoMathHelper.Map2ScreenFIN((x,y), (self.MapPosX, self.MapPosY))
            self.tiles[tile].draw(tile_x, tile_y)
        
        mouseCoord = self.IsoMathHelper.Screen2MapFIN(pygame.mouse.get_pos(), (self.MapPosX, self.MapPosY))
        
        if  -1 < mouseCoord[0] <= self.MapSize[0] and -1 < mouseCoord[1] <= self.MapSize[1] and self.MouseActive:
            select_x, select_y = self.IsoMathHelper.Map2ScreenFIN((int(mouseCoord[0]), int(mouseCoord[1])), (self.MapPosX, self.MapPosY))
            self.MouseSelected.draw(select_x, select_y)


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
            
    def UpdateDisplay(self):
        self.FPSClock.tick(self.maxFPS)
        pygame.display.flip()
    