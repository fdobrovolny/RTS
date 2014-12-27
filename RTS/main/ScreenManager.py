import os, sys
import pygame
from pygame.locals import *
from pygame.image import *
from OpenGL.GL import *
from OpenGL.GLUT import *

'''
Created on 30. 11. 2014

@author: fdobrovolny
'''

class ScreenManager(object):
    '''
    classdocs
    '''

    def __init__(self, main, width, height, maxFPS):
        self.main = main
        self.size = self.width, self.height = width, height
        self.flags = OPENGL | DOUBLEBUF #| FULLSCREEN
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
    
    def _PygameInit(self):
        pygame.init()
        self.display_surf = pygame.display.set_mode(self.size, self.flags)
        pygame.display.set_caption('Bellum ' + self.main.gameDevelopmentState + " " + self.main.version)
    
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
        glClearColor(self.backgroundColorR, self.backgroundColorG, self.backgroundColorB, self.backgroundColorA)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    def UpdateDisplay(self):
        self.FPSClock.tick(self.maxFPS)
        pygame.display.flip()
    
    def setBackgrounColor(self, color, alpha=0.0):
        self.backgroundColorR, self.backgroundColorG, self.backgroundColorB = color
        self.backgroundColorA = alpha