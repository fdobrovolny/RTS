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
from pygame.locals import *


class EventHandler(object):
    """
    classdocs
    """

    def __init__(self, main):
        """
        Constructor
        """
        self.main = main
        self.logger = self.main.logger
        self.userEvents = {}
        self.userEventsNum = 0
        # SONG_END = pygame.USEREVENT + 1
        self.KEYDOWN_event = {}
        self.KEYUP_event = {}
        self.KEYPRESSED_event = {}
        self.MOUSEBUTTONDOWN_event = {}
        self.MOUSEBUTTONUP_event = {}
        self.KEYDOWN_listener = []

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
            self.checkForEvent(
                event, MOUSEBUTTONDOWN, self.MOUSEBUTTONDOWN_event, False
            )
            self.checkForEvent(event, MOUSEBUTTONUP, self.MOUSEBUTTONUP_event, False)

            if event.type == KEYDOWN:
                for i in self.KEYDOWN_listener:
                    i(event.key)

        if self.main.loop:
            keys_presed = pygame.key.get_pressed()

            for i in self.KEYPRESSED_event:
                if keys_presed[i]:
                    for func in self.KEYPRESSED_event[i]:
                        func()

    """
    @author: Filip Dobrovolny
    @param event:  event from pygame.event.get() list
    @param checkEvent: for which event are we looking? MOUSEBUTTONUP, ...
    @param functions: dictationary in format {key : [func1, func2 ...]}
    @param key: True = event.key; False=event.button (index in functions)
    """

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

    """
    ** Register user - Event section
    UserEvent - Register UserEvent at EventHandler to call function when occur
    ####################################################################################
    """

    def registerUserEvent(self, function):
        self.userEventsNum += 1
        event = pygame.USEREVENT + self.userEventsNum
        self.userEvents[event] = function
        return event

    def unregisterUserEvent(self, event):
        del self.userEvents[event]

    def unregisterUserEventsAll(self):
        self.userEvents = {}

    """
    ** Register KEYDOWN - Event section
    KEYDOWN - event which occur when user press a key
    ####################################################################################
    """

    def registerKEYDOWNevent(self, key, function):
        try:
            temp = self.KEYDOWN_event[key]
            temp.append(function)
            self.KEYDOWN_event[key] = temp
            self.logger.log(
                0,
                "EventHandler",
                "Added new binding to KEYDOWN for key "
                + str(key)
                + " function"
                + str(function),
            )
        except:
            self.KEYDOWN_event[key] = [function]
            self.logger.log(
                0,
                "EventHandler",
                "Added new binding to KEYDOWN for key "
                + str(key)
                + " function"
                + str(function),
            )

    def unregisterKEYDOWNeventAll(self, key):
        del self.KEYDOWN_event[key]

    def unregisterKEYDOWNevent(self, key, function):
        try:
            self.KEYDOWN_event[key].remove(function)
        except:
            pass

    def unregisterKEYDOWNeventAllKeys(self):
        self.KEYDOWN_event = {}

    """
    ** Register KEYUP - Event section
    KEYUP - event which occur when user release a key
    ####################################################################################
    """

    def registerKEYUPevent(self, key, function):
        try:
            temp = self.KEYUP_event[key]
            temp.append(function)
            self.KEYUP_event[key] = temp
        except:
            self.KEYUP_event[key] = [function]

    def unregisterKEYUPeventAll(self, key):
        del self.KEYUP_event[key]

    def unregisterKEYUPevent(self, key, function):
        try:
            self.KEYUP_event[key].remove(function)
        except:
            pass

    def unregisterKEYUPeventAllKeys(self):
        self.KEYUP_event = {}

    """
    ** Register KEYPRESSED - section
    KEYPRESSED - this section takes care of buttons which were pressed before.
    ####################################################################################
    """

    def registerKEYPRESSEDevent(self, key, function):
        try:
            temp = self.KEYPRESSED_event[key]
            temp.append(function)
            self.KEYPRESSED_event[key] = temp
        except:
            self.KEYPRESSED_event[key] = [function]

    def unregisterKEYPRESSEDeventAll(self, key):
        del self.KEYPRESSED_event[key]

    def unregisterKEYPRESSEDevent(self, key, function):
        try:
            self.KEYPRESSED_event[key].remove(function)
        except:
            pass

    def unregisterKEYPRESSEDeventAllKeys(self):
        self.KEYPRESSED_event = {}

    """
    ** Register MOUSEBUTTONDOWN - event section
    MOUSEBUTTONDOWN - event which occur when user press one of the mouse buttons
    ####################################################################################
    """

    def registerMOUSEBUTTONDOWNevent(self, button, function):
        try:
            temp = self.MOUSEBUTTONDOWN_event[button]
            temp.append(function)
            self.MOUSEBUTTONDOWN_event[button] = temp
            self.logger.log(
                0,
                "EventHandler",
                "Added new binding to MOUSEBUTTONDOWN for button"
                + str(button)
                + " function"
                + str(function),
            )
        except KeyError:
            self.MOUSEBUTTONDOWN_event[button] = [function]
            self.logger.log(
                0,
                "EventHandler",
                "Creating new binding to MOUSEBUTTONDOWN for button"
                + str(button)
                + " function"
                + str(function),
            )

    def unregisterMOUSEBUTTONDOWNeventAll(self, button):
        del self.MOUSEBUTTONDOWN_event[button]
        self.logger.log(
            0,
            "EventHandler",
            "Removed all bindings to MOUSEBUTTONDOWN for button" + str(button),
        )

    def unregisterMOUSEBUTTONDOWNevent(self, button, function):
        try:
            self.MOUSEBUTTONDOWN_event[button].remove(function)
            self.logger.log(
                0,
                "EventHandler",
                "Removed binding to MOUSEBUTTONDOWN for button"
                + str(button)
                + " function"
                + str(function),
            )
        except:
            pass

    def unregisterMOUSEBUTTONDOWNeventAllKEys(self):
        self.MOUSEBUTTONDOWN_event = {}

    """
    ** Register MOUSEBUTTOUP - event section
    MOUSEBUTTONUP - event which occur when user release one of the mouse buttons
    ####################################################################################
    """

    def registerMOUSEBUTTONUPevent(self, button, function):
        try:
            temp = self.MOUSEBUTTONUP_event[button]
            temp.append(function)
            self.MOUSEBUTTONUP_event[button] = temp
        except KeyError:
            self.MOUSEBUTTONUP_event[button] = [function]

    def unregisterMOUSEBUTTONUPeventAll(self, button):
        del self.MOUSEBUTTONUP_event[button]

    def unregisterMOUSEBUTTONUPevent(self, button, function):
        try:
            self.MOUSEBUTTONUP_event[button].remove(function)
        except:
            pass

    def unregisterMOUSEBUTTONUPeventAllKEys(self):
        self.MOUSEBUTTONUP_event = {}

    """
    ** Register keydown listener - listener section
    keydown listener - Listener function which is called when user press a key
    ####################################################################################
    """

    def registerKEYDOWNlistener(self, function):
        self.KEYDOWN_listener.append(function)

    def unregisterKEYDOWNlistener(self, function):
        del self.KEYDOWN_listener[self.KEYDOWN_listener.index(function)]

    def unregisterAllKEYDOWNlisteners(self):
        self.KEYDOWN_listener = []
