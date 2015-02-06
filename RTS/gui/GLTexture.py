import pygame
from OpenGL.GL import *
from OpenGL.GLU import *


class Texture(object):
    def __init__(self, src, surf=None, rect=None):
        if src is not None:
            """src -from where shuld be image loaded"""
            image = pygame.image.load(src)
            self.rect = image.get_rect()
            texdata = pygame.image.tostring(image, "RGBA", 0)
        else:
            self.rect = rect
            texdata = pygame.image.tostring(surf, "RGBA", 0)
        # Create texture object
        self.texid = glGenTextures(1)

        # Activate Texture Object
        glBindTexture(GL_TEXTURE_2D, self.texid)

        # Use texture filters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

        # Create Image of Texture
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.rect.w, self.rect.h,
                     0, GL_RGBA, GL_UNSIGNED_BYTE, texdata)

        self.newList = glGenLists(1)
        glNewList(self.newList, GL_COMPILE)
        glBindTexture(GL_TEXTURE_2D, self.texid)
        glBegin(GL_QUADS)

        glTexCoord2f(0, 0)
        glVertex3f(0, 0, 0)

        glTexCoord2f(0, 1)
        glVertex3f(0, self.rect.h, 0)

        glTexCoord2f(1, 1)
        glVertex3f(self.rect.w, self.rect.h, 0)

        glTexCoord2f(1, 0)
        glVertex3f(self.rect.w, 0, 0)

        glEnd()
        glEndList()

    def draw(self, x, y):
        glLoadIdentity()
        glTranslatef(x, y, 0)
        glCallList(self.newList)


class Text(object):
    def __init__(self, text, textSize, text_color, x, y, font=None):
        self.x = x
        self.y = y
        font = pygame.font.Font(None, textSize)
        textSurf = font.render(text, True, text_color)
        textRect = textSurf.get_rect()
        self.rect = textRect
        self.Texture = Texture(None, textSurf, textRect)

    def draw(self, x=None, y=None):
        if x is None and y is None:
            self.Texture.draw(self.x, self.y)
        elif x is None:
            self.Texture.draw(self.x, y)
        elif y is None:
            self.Texture.draw(x, self.y)
        else:
            self.Texture.draw(x, y)