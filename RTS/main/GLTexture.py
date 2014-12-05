import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
 
class Texture(object):
 
    def __init__(self, src):
        """src - sciezka/nazwa_obrazka.png"""
        image = pygame.image.load(src)
 
        self.rect = image.get_rect()
        texdata = pygame.image.tostring(image,"RGBA",0)
        print(self.rect)
        # tworzymy obiekt tekstury
        self.texid = glGenTextures(1)
 
        # aktywujemy obiekt tekstury
        glBindTexture(GL_TEXTURE_2D, self.texid)
 
        # ustawiamy filtry tekstury
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
 
        # tworzymy obraz tekstury
        glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,self.rect.w,self.rect.h,0,GL_RGBA,GL_UNSIGNED_BYTE,texdata)
 
        self.newList = glGenLists(1)
        glNewList(self.newList, GL_COMPILE)
        glBindTexture(GL_TEXTURE_2D, self.texid)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(0, 0 ,0)
        glTexCoord2f(0, 1); glVertex3f(0, self.rect.h, 0)
        glTexCoord2f(1, 1); glVertex3f(self.rect.w, self.rect.h, 0)
        glTexCoord2f(1, 0); glVertex3f(self.rect.w, 0, 0)
        glEnd()
        glEndList()
 
    def draw(self,x,y):
        glLoadIdentity()
        glTranslatef(x, y, 0)
        glCallList(self.newList)
    