from random import choice
import pygame
'''
Created on 30. 11. 2014
@todo: FIX background music and test normal music
@author: fdobrovolny
Background Music copyright:
Gangi_-_22_-_Proton_Beat.mp3 - http://freemusicarchive.org/music/Gangi/Bonus_Beat_Blast_2011/22_gangi-proton_beat
'''

class SoundManager(object):
    '''
    classdocs
    '''

    def __init__(self, main, startBackground=True):
        '''
        Constructor
        '''
        self.BackgroundMusic = ["../res/music/background/Gangi_-_22_-_Proton_Beat.wav"]
        self.musicID = 0
        self.musicList = []
        self.IDnFilenameList = {}
        pygame.mixer.init()
        self.main = main
        self.logger = self.main.logger 
        
        self.SONG_END_event = self.main.EventHandler.registerUserEvent(self.PlayBackgroundMusic)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.set_endevent(self.SONG_END_event)
        self.logger.log(1, "SoundManager", "Initialized.")
        self.logger.log(0, "SoundManager", "Start Background: " + str(startBackground))
        if startBackground:
            self.PlayBackgroundMusic()
    
    def PlayBackgroundMusic(self, event=None):
        music = choice(self.BackgroundMusic)
        self.logger.log(1, "SoundManager", "Playing " + music)
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(0, 0.0)
    
    def RegisterSound(self, filename):
        try:
            return self.IDnFilenameList[filename]
        except:
            self.musicList.append(pygame.mixer.Sound(filename))
            self.IDnFilenameList[filename] = self.musicID
            self.musicID += 1
            self.logger.log(1, "SoundManager", "Registered and loaded new sound. " + str(filename) + " ID: " + str(self.musicID - 1))
            return self.musicID - 1
    
    def PlaySound(self, id):
        self.logger.log(0, "SoundManager", "Playing Sound ID: " + str(id))
        self.musicList[id].play()
        