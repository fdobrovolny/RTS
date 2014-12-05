'''
Created on 30. 11. 2014

@author: fdobrovolny
'''

class IsoMathHelper(object):
    '''
    Class to convert between Screen XY coord and Map XY coord 
    '''


    def __init__(self, TILE_WIDTH_HALF, TILE_HEIGHT_HALF, SCREEN_WIDTH_HALF):
        self.TILE_WIDTH_HALF = TILE_WIDTH_HALF
        self.TILE_HEIGHT_HALF = TILE_HEIGHT_HALF
        self.SCREEN_WIDTH_HALF = SCREEN_WIDTH_HALF
    
    def Map2Iso(self, tupple):
        x = tupple[0]
        y = tupple[1]
        screen_x = (x - y) * self.TILE_WIDTH_HALF;
        screen_y = (x + y) * self.TILE_HEIGHT_HALF;
        return (screen_x, screen_y)
    
    def Screen2Map(self, tupple):
        screen_x = tupple[0]
        screen_y = tupple[1]
        map_x = (screen_x / self.TILE_WIDTH_HALF + screen_y / self.TILE_HEIGHT_HALF) /2;
        map_y = (screen_y / self.TILE_HEIGHT_HALF - (screen_x / self.TILE_WIDTH_HALF)) /2;
        return (map_x, map_y)
    
    def Map2Screen(self, tupple):
        tupple = self.Map2Iso(tupple)
        screen_x = tupple[0]
        screen_y = tupple[1]
        screen_x -= self.TILE_WIDTH_HALF
        screen_x += self.SCREEN_WIDTH_HALF
        return (screen_x, screen_y)
    
    def MapPosCorrect(self, tupple, pos, SCREENHEIGHT, SCREENWIDTH):
        screen_x, screen_y = self.tuppleHelper(tupple)
        pos_x, pos_y = self.tuppleHelper(pos)
        screen_x += pos_x * self.TILE_WIDTH_HALF
        screen_y += pos_y * self.TILE_HEIGHT_HALF
        if screen_x < -self.TILE_WIDTH_HALF*2 or screen_x > SCREENWIDTH + self.TILE_WIDTH_HALF*3:
            return None
        elif screen_y < -self.TILE_HEIGHT_HALF*2 or screen_y > SCREENHEIGHT + self.TILE_HEIGHT_HALF*3:
            return None
        return (screen_x, screen_y)
    
    def Map2ScreenCorrect(self, tupple, pos, SCREENHEIGHT, SCREENWIDTH):
        tupple = self.Map2Screen(tupple)
        return self.MapPosCorrect(tupple, pos, SCREENHEIGHT, SCREENWIDTH)
    
    def tuppleHelper(self, tupple):
        return tupple[0], tupple[1]
        