import pygame, sys
from pygame.locals import *
'''
Created on 30. 11. 2014

@author: fdobrovolny
'''
from _csv import Error

class EventHandler(object):
    '''
    classdocs
    '''


    def __init__(self, main):
        '''
        Constructor
        '''
        self.main = main
        self.logger = self.main.logger
        self.userEvents = {}
        self.userEventsNum = 0
        #SONG_END = pygame.USEREVENT + 1
        self.KEYDOWN_event = {}
        self.KEYUP_event = {}
        self.KEYPRESSED_event = {}
        self.MOUSEBUTTONDOWN_event = {}
        self.MOUSEBUTTONUP_event = {}
        
        self.logger.log(1, "EventHandler", "Initialized.")
    
    def tick(self):
        for event in pygame.event.get():
            
            if event.type == QUIT:
                self.main.quit()
            
            for i in self.userEvents:
                if event.type == i:
                    self.userEvents[i](event)
            
            self.checkForEvent(event, KEYDOWN, self.KEYDOWN_event, True) 
            self.checkForEvent(event, KEYUP, self.KEYUP_event, True)   
            self.checkForEvent(event, MOUSEBUTTONDOWN, self.MOUSEBUTTONDOWN_event, False)
            self.checkForEvent(event, MOUSEBUTTONUP, self.MOUSEBUTTONUP_event, False) 
        
        if self.main.loop:
            keys_presed = pygame.key.get_pressed()
            
            for i in self.KEYPRESSED_event:
                if keys_presed[i]:
                    for func in self.KEYPRESSED_event[i]:
                        func()
    
    
    ''' 
    @author: Filip Dobrovolny
    @param event:  event from pygame.event.get() list
    @param checkEvent: for which event are we looking? (MOUSEBUTTONUP, KEYUP, ...)
    @param functions: dictationary in format {key : [func1, func2 ...]} 
    @param key: True = event.key; False=event.button (index in functions)
    '''
    def checkForEvent(self, event, checkEvent, functions, key):
        if event.type == checkEvent:
            try:
                if key:
                    functionsFIN = functions[event.key]
                else:
                    functionsFIN = functions[event.button]
                for i in functionsFIN:
                        i()
            except:
                pass
    
        
    def registerUserEvent(self, function):
        self.userEventsNum += 1
        event = pygame.USEREVENT + self.userEventsNum
        self.userEvents[event] = function
        return event
    
    
    def unregisterUserEvent(self, event):
        del(self.userEvents[event])
    
    
    def unregisterUserEventsAll(self):
        self.userEvents = {}
    
    
    def registerKEYDOWNevent(self, key, function):
        try:
            temp = self.KEYDOWN_event[key]
            temp.append(function)
            self.KEYDOWN_event[key] = temp
        except:
            self.KEYDOWN_event[key] = [function]
    
    
    def unregisterKEYDOWNeventAll(self, key):
        del(self.KEYDOWN_event[key])
     
    
    def unregisterKEYDOWNevent(self, key, function):
        try:
            self.KEYDOWN_event[key].remove(function)
        except:
            pass
    
    
    def unregisterKEYDOWNeventAllKeys(self):
        self.KEYDOWN_event = {}
    
    
    def registerKEYUPevent(self, key, function):
        try:
            temp = self.KEYUP_event[key]
            temp.append(function)
            self.KEYUP_event[key] = temp
        except:
            self.KEYUP_event[key] = [function]
    
    
    def unregisterKEYUPeventAll(self, key):
        del(self.KEYUP_event[key])
    
    
    def unregisterKEYUPevent(self, key,function):
        try:
            self.KEYUP_event[key].remove(function)
        except:
            pass
    
    
    def unregisterKEYUPeventAllKeys(self):
        self.KEYUP_event = {}
    
    
    def registerKEYPRESSEDevent(self, key, function):
        try:
            temp = self.KEYPRESSED_event[key]
            temp.append(function)
            self.KEYPRESSED_event[key] = temp
        except:
            self.KEYPRESSED_event[key] = [function]
    
    
    def unregisterKEYPRESSEDeventAll(self, key):
        del(self.KEYPRESSED_event[key])
    
    
    def unregisterKEYPRESSEDevent(self, key, function):
        try:
            self.KEYPRESSED_event[key].remove(function)
        except:
            pass
    
    
    def unregisterKEYPRESSEDeventAllKeys(self):
        self.KEYPRESSED_event = {}
    
    
    def registerMOUSEBUTTONDOWNevent(self, button, function):
        try:
            temp = self.MOUSEBUTTONDOWN_event[button]
            temp.append(function)
            self.MOUSEBUTTONDOWN_event[button] = temp
            self.logger.log(0, "EventHandler", "Added new binding to MOUSEBUTTONDOWN for button " + str(button) + " function" + str(function))
        except KeyError:
            self.MOUSEBUTTONDOWN_event[button] = [function]
            self.logger.log(0, "EventHandler", "Creating new binding to MOUSEBUTTONDOWN for button " + str(button) + " function" + str(function))
    
    
    def unregisterMOUSEBUTTONDOWNeventAll(self, button):
        del(self.MOUSEBUTTONDOWN_event[button])
        self.logger.log(0, "EventHandler", "Removed all bindings to MOUSEBUTTONDOWN for button " + str(button))
    
    
    def unregisterMOUSEBUTTONDOWNevent(self, button, function):
        try:
            self.MOUSEBUTTONDOWN_event[button].remove(function)
            self.logger.log(0, "EventHandler", "Removed binding to MOUSEBUTTONDOWN for button " + str(button) + " function" + str(function))
        except:
            pass
    
    
    def unregisterMOUSEBUTTONDOWNeventAllKEys(self):
        self.MOUSEBUTTONDOWN_event = {}
    
    
    def registerMOUSEBUTTONUPevent(self, button, function):
        self.MOUSEBUTTOUP_event[button] = function
    
       
    def unregisterMOUSEBUTTONUPeventAll(self, button):
        del(self.MOUSEBUTTONUP_event[button])
    
    
    def unregisterMOUSEBUTTONUPevent(self, button, function):
        try:
            self.MOUSEBUTTONUP_event[button].remove(function)
        except:
            pass
    
    
    def unregisterMOUSEBUTTONUPeventAllKEys(self):
        self.MOUSEBUTTONUP_event = {}
    