from random import choice
import pygame
'''
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

@todo: FIX background music and test normal music
Background Music copyright:
Gangi_-_22_-_Proton_Beat.mp3 -
http://freemusicarchive.org/music/Gangi/Bonus_Beat_Blast_2011/22_gangi-proton_beat
'''


class SoundManager(object):
    '''
    classdocs
    '''

    def __init__(self, main, startBackground=True):
        '''
        Constructor
        '''
        self.BackgroundMusic = ["RTS/res/music/background/Gangi_-_22_-_Proton_Beat.wav"]
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
        self.logger.log(0, "SoundManager", "Start Background: "
                        + str(startBackground))
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
            self.logger.log(1, "SoundManager", "Registered and loaded new sound. "
                            + str(filename) + " ID: " + str(self.musicID - 1))
            return self.musicID - 1

    def PlaySound(self, musicID):
        self.logger.log(0, "SoundManager", "Playing Sound ID: " + str(musicID))
        self.musicList[musicID].play()
