'''
Created on 5. 12. 2014

@author: Filip Dobrovolny
'''
import os
import numpy


class Map(object):
    '''
    @author: Filip Dobrovolny
    @param src: Location of .map file
    @note: Load/Save/Edit Map
    @note: there can be only 256 textures (0-255)
    @todo: move map size info before textures
    bin map file definition
        <> - string
        [] - int
        <version> = ISO_Game_1.0
        <name> - name of map
        <desc> - descryption
        <texture> - name of texture without .PNG
        {} - loop
        \1 - start of heading
        \2 - start of text
        \3 - end of text
        \25 - end of medium
        \30 - End of Record Seperator
        ----- FILE -----
        \1<version>\3<name>\3<author>\3<desc>\3\30{\2<texture>\3}\30 # header
        [len-x-1][len-x-2]\3[len-y-1][len-y-2]\3\30 # size
        \1{\2{[index]}\3}\30\25 # matrix
    '''

    def __init__(self, src, logger):
        '''
        Constructor
        '''
        self.Header = "ISO_Game_1.0"
        if src[-4:] == ".map":
            self.src = src[:-4]
        else:
            self.src = src
        self.MAP_FOLDER = "RTS/res/maps/"
        self.name = None
        self.author = None
        self.desc = None
        self.textures = None
        self.sizeX = None
        self.sizeY = None
        self.matrix = None
        self.logger = logger
        self.loggerName = "Map \"" + self.src + ".map\""

        self.logger.log(1, self.loggerName, "Map initialized.")

    def _readTextTillByte(self, f, end):
        text = ""
        temp = f.read(1)
        while temp != bytes([end]):
            text = text + chr(ord(temp))
            temp = f.read(1)
        return text

    def createMap(self, name, author, desc, textures, sizeX, sizeY):
        self.name = name
        self.author = author
        self.desc = desc
        self.textures = textures
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.matrix = numpy.array([[0 for _y in range(sizeY)] for _x in range(sizeX)],
                                  dtype=numpy.int8)
        self.logger.log(1, self.loggerName, "New map created.")
        self._logMapInfo()

    def writeMap(self):
        f = open(self.MAP_FOLDER + self.src + ".map", "wb")

        f.write(bytes([1]))  # start of heading
        for i in self.Header:
            f.write(bytes([ord(i)]))
        f.write(bytes([3]))  # end of text

        for i in self.name:
            f.write(bytes([ord(i)]))
        f.write(bytes([3]))  # end of text

        for i in self.author:
            f.write(bytes([ord(i)]))
        f.write(bytes([3]))  # end of text

        for i in self.desc:
            f.write(bytes([ord(i)]))
        f.write(bytes([3]))  # end of text

        f.write(bytes([30]))  # EndOfRecordSeperator

        for texture in self.textures:
            f.write(bytes([2]))  # start of text
            for i in texture:
                f.write(bytes([ord(i)]))
            f.write(bytes([3]))  # end of text

        f.write(bytes([30]))  # EndOfRecordSeperator

        size_x_bin = '{0:016b}'.format(self.sizeX)
        f.write(bytes([int(size_x_bin[:8], 2)]))
        f.write(bytes([int(size_x_bin[8:], 2)]))
        f.write(bytes([3]))  # end of text

        size_y_bin = '{0:016b}'.format(self.sizeY)
        f.write(bytes([int(size_y_bin[:8], 2)]))
        f.write(bytes([int(size_y_bin[8:], 2)]))
        f.write(bytes([3]))  # end of text

        f.write(bytes([30]))  # end of text

        # The Matrix
        f.write(bytes([1]))  # start of heading
        for x in self.matrix:
            f.write(bytes([2]))
            for y in x:
                f.write(bytes([y]))
            f.write(bytes([3]))
        f.write(bytes([30]))  # End of record separator
        f.write(bytes([25]))  # end of medium
        f.close()
        self.logger.log(1, self.loggerName, "Map saved.")

    def loadMap(self):
        path = self.MAP_FOLDER + self.src + ".map"
        if not os.path.exists(path):
            self.logger.log(3, self.loggerName, "File \"" + path + "\" was not found.")
            return False, "Not found"

        f = open(path, "rb")
        header = [1]
        for i in "ISO_Game_1.0":
            header.append(ord(i))
        header.append(3)
        if not f.read(14) == bytes(header):
            return False, "Header"
        self.name = self._readTextTillByte(f, 3)
        self.author = self._readTextTillByte(f, 3)
        self.desc = self._readTextTillByte(f, 3)
        if not f.read(1) == bytes([30]):
            return False, "End of Header"

        self.textures = []
        temp = f.read(1)
        if temp == bytes([30]):
            return False, "No textures!"
        elif temp == bytes([2]):
            while temp != bytes([30]):
                self.textures.append(self._readTextTillByte(f, 3))
                temp = f.read(1)
        else:
            return False, "No end header"
        self.sizeX = int(bin(ord(f.read(1)))[2:] + bin(ord(f.read(1)))[2:], 2)
        if not f.read(1) == bytes([3]):
            return False, "No size seperator"
        self.sizeY = int(bin(ord(f.read(1)))[2:] + bin(ord(f.read(1)))[2:], 2)
        if not f.read(3) == bytes([3, 30, 1]):
            return False, "No size end"

        self.matrix = []
        for _x in range(self.sizeX):
            if not f.read(1) == bytes([2]):
                return False, "can't find begining of row"
            temp_list = []
            for _y in range(self.sizeY):
                temp_list.append(ord(f.read(1)))
            if not f.read(1) == bytes([3]):
                return False, "can't find end of row"
            self.matrix.append(temp_list)
        if not f.read(2) == bytes([30, 25]):
            return False, "can't find end of file"

        f.close()
        self.logger.log(1, self.loggerName, "Map loaded.")
        self._logMapInfo()

    def loadMapInfo(self):
        f = open("RTS/res/maps/" + self.src + ".map", "rb")
        header = [1]
        for i in "ISO_Game_1.0":
            header.append(ord(i))
        header.append(3)
        if not f.read(14) == bytes(header):
            return False, "Header"
        self.name = self._readTextTillByte(f, 3)
        self.author = self._readTextTillByte(f, 3)
        self.desc = self._readTextTillByte(f, 3)
        if not f.read(1) == bytes([30]):
            return False, "End of Header"

        self.textures = []
        temp = f.read(1)
        if temp == bytes([30]):
            return False, "No textures!"
        elif temp == bytes([2]):
            temp = self._readTextTillByte(f, 30)  # skip map textures
        else:
            return False, "No end header"

        self.sizeX = int(bin(ord(f.read(1)))[2:] + bin(ord(f.read(1)))[2:], 2)
        if not f.read(1) == bytes([3]):
            return False, "No size seperator"
        self.sizeY = int(bin(ord(f.read(1)))[2:] + bin(ord(f.read(1)))[2:], 2)
        if not f.read(3) == bytes([3, 30, 1]):
            return False, "No size end"
        f.close()

        self.logger.log(1, self.loggerName, "Map info loaded.")
        self._logMapInfo()

    def _logMapInfo(self):
        self.logger.log(0, self.loggerName, "name: " + self.name)
        self.logger.log(0, self.loggerName, "author: " + self.author)
        self.logger.log(0, self.loggerName, "desc: " + self.desc)
        self.logger.log(0, self.loggerName, "sizeX: " + str(self.sizeX))
        self.logger.log(0, self.loggerName, "sizeY: " + str(self.sizeY))
