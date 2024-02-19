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


class IsoMathHelper(object):
    """
    Class to convert between Screen XY coord and Map XY coord
    """

    """
    @author: Filip Dobrovolny
    @param TILE_WIDTH_HALF: width of tile / 2
    @param TILE_HEIGHT_HALF: height of tile / 2
    @param SCREEN_WIDTH_HALF: width of screen / 2
    @return: IsoMathHelper object
    """

    def __init__(self, TILE_WIDTH_HALF, TILE_HEIGHT_HALF, SCREEN_WIDTH_HALF):
        self.TILE_WIDTH_HALF = TILE_WIDTH_HALF
        self.TILE_HEIGHT_HALF = TILE_HEIGHT_HALF
        self.SCREEN_WIDTH_HALF = SCREEN_WIDTH_HALF

    """
    @author: Filip Dobrovony
    @param tupple: Map XY coord
    @return: XY coord of title with top corner of map as 0,0
    """

    def Map2Iso(self, tupple):
        x, y = self.tuppleHelper(tupple)
        screen_x = (x - y) * self.TILE_WIDTH_HALF
        screen_y = (x + y) * self.TILE_HEIGHT_HALF
        return (screen_x, screen_y)

    """
    @author: Filip Dobrovolny
    @param tupple: XY coord on screen
    @return: XY map coord
    @note: Usage for example to define on which tile is mouse
    """

    def Screen2Map(self, tupple):
        x, y = self.tuppleHelper(tupple)
        # x += self.TILE_WIDTH_HALF
        x -= self.SCREEN_WIDTH_HALF
        map_x = (x / self.TILE_WIDTH_HALF + y / self.TILE_HEIGHT_HALF) / 2
        map_y = (y / self.TILE_HEIGHT_HALF - (x / self.TILE_WIDTH_HALF)) / 2
        return (map_x, map_y)

    """
    @author: Filip Dobrovolny
    @param tupple: Map XY coord
    @return: Screen XY coord corrected that the top corner is in the middle
             and we want the top right corner
    """

    def Map2Screen(self, tupple):
        screen_x, screen_y = self.tuppleHelper(self.Map2Iso(tupple))
        screen_x -= self.TILE_WIDTH_HALF
        screen_x += self.SCREEN_WIDTH_HALF
        return (screen_x, screen_y)

    """
    @author: Filip Dobrovolny
    @param tupple: Screen XY coord
    @param pos: position of map (position of the map e.g. when we move the map)
    @return: correct Screen XY coord
    """

    def MapMovePos(self, tupple, pos):
        screen_x, screen_y = self.tuppleHelper(tupple)
        pos_x, pos_y = self.tuppleHelper(pos)
        screen_x += pos_x
        screen_y += pos_y
        return (screen_x, screen_y)

    """
    @author: Filip Dobrovolny
    @param tupple: Screen XY coord
    @param pos: position of map (position of the map e.g. when we move the map)
    @note: reverse of MapMovePos()
    @return: uncorrect Screen XY coord
    """

    def MapUnmovePos(self, tupple, pos):
        screen_x, screen_y = self.tuppleHelper(tupple)
        pos_x, pos_y = self.tuppleHelper(pos)
        screen_x -= pos_x
        screen_y -= pos_y
        return (screen_x, screen_y)

    """
    @author: Filip Dobrovolny
    @param tupple: Map XY coord
    @param pos: position of map (position of the map e.g. when we move the map)
    @return: correct Screen XY coord
    """

    def Map2ScreenFIN(self, tupple, pos):
        tupple = self.Map2Screen(tupple)
        return self.MapMovePos(tupple, pos)

    """
    @author: Filip Dobrovolny
    @param tupple: Screen XY coord
    @param pos: position of map (position of the map e.g. when we move the map)
    @return: correct Map XY coord
    """

    def Screen2MapFIN(self, tupple, pos):
        tupple = self.MapUnmovePos(tupple, pos)
        return self.Screen2Map(tupple)

    """
    @author: Filip Dobrovolny
    @param tupple: tupple of coord e.g. (5, 10)
    @return: disassembled coords e.g. 5, 10
    """

    def tuppleHelper(self, tupple):
        return tupple[0], tupple[1]
