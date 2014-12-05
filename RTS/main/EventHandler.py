import pygame, sys
from pygame.locals import *
'''
Created on 30. 11. 2014

@author: fdobrovolny
'''

class EventHandler(object):
    '''
    classdocs
    '''


    def __init__(self, main):
        '''
        Constructor
        '''
        self.main = main
        self.userEvents = {}
        self.userEventsNum = 0
        #SONG_END = pygame.USEREVENT + 1
        self.KEYDOWN_event = {}
        self.KEYPRESSED_event = {}
    
    def tick(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            for i in self.userEvents:
                if event.type == i:
                    self.userEvents[i](event)
            if event.type == KEYDOWN:
                for i in self.KEYDOWN_event:
                    if event.key == i:
                        self.KEYDOWN_event[i]()
        
        keys_presed = pygame.key.get_pressed()
        
        for i in self.KEYPRESSED_event:
            if keys_presed[i]:
                self.KEYPRESSED_event[i]()
    
    def registerUserEvent(self, function):
        self.userEventsNum += 1
        event = pygame.USEREVENT + self.userEventsNum
        self.userEvents[event] = function
        return event
    
    def registerKEYDOWNevent(self, key, function):
        self.KEYDOWN_event[key] = function
    
    def registerKEYPRESSEDevent(self, key, function):
        self.KEYPRESSED_event[key] = function