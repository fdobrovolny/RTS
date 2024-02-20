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
import logging
from typing import Any, Callable

import pygame

from RTS.gui.GLTexture import Texture
from RTS.utils.typing import ColorValue, Coordinate

logger = logging.getLogger(__name__)


class Button:
    """

    The Button class represents a clickable button in a graphical user interface.

    Attributes:
        rect (pygame.Rect): The rectangle that defines the button's position and size.
        inside_rect (pygame.Rect): The rectangle that defines the button's inner area.
        surface (pygame.Surface): The surface of the button.
        texture (Texture): The texture of the button.
        hover_surface (pygame.Surface): The surface of the button when hovered.
        hover_texture (Texture): The texture of the button when hovered.
        inside_color (ColorValue): The color of the button's inner area.
        border_color (ColorValue): The color of the button's border.
        hover_color (ColorValue): The color of the button border when hovered.
        text (str): The text displayed on the button.
        text_size (int): The size of the text displayed on the button.
        text_font (pygame.font.Font): The font used for the button's text.
        text_surface (pygame.Surface): The surface of the button's text.
        text_rect (pygame.Rect): The rectangle that defines the position of the button's text.
        text_color (ColorValue): The color of the button's text.
        pos (Coordinate): The position of the button.
        x (float): The x coordinate of the button's position.
        y (float): The y coordinate of the button's position.
        size (Coordinate): The size of the button.
        size_x (float): The width of the button.
        size_y (float): The height of the button.
        on_click_callback (Callable): The callback function to be called when the button is clicked.
        on_click_identifier (Any | None): An optional identifier to be passed to the on_click_callback.

    Methods:
        __init__(self, main, inside_color, border_color, hover_color, text_color, x, y, size_x, size_y,
                 text, text_size, on_click_callback, border_width=5, on_click_identifier=None):
            Initializes a Button instance with the given parameters.

        init_rect(self):
            Initializes the rect and inside_rect attributes of the button.

        gen_textures(self):
            Generates the surface and hover_surface attributes of the button.

        init_text(self):
            Initializes the text_font, text_surface, and text_rect attributes of the button.

        draw(self):
            Draws the button on the screen.

        is_hovered(self):
            Checks if the mouse is hovering over the button.

        on_click(self):
            Execute the on_click_callback if the button is clicked.

        register_click_event(self):
            Registers the on_click method to be called when the button is clicked.

        stop(self):
            Stops the button and releases its resources.

        __del__(self):
            Destructor method that stops the button when it is deleted.

    """

    rect: pygame.Rect
    inside_rect: pygame.Rect
    surface: pygame.Surface
    texture: Texture
    hover_surface: pygame.Surface
    hover_texture: Texture

    inside_color: ColorValue
    border_color: ColorValue
    hover_color: ColorValue

    text: str
    text_size: int
    text_font: pygame.font.Font
    text_surface: pygame.Surface
    text_rect: pygame.Rect
    text_color: ColorValue

    pos: Coordinate
    x: float
    y: float
    size: Coordinate
    size_x: float
    size_y: float

    on_click_callback: Callable[[Any | None], None] | Callable[[], None] | None = None
    on_click_identifier: Any | None = None

    def __init__(
        self,
        main,
        inside_color: ColorValue,
        border_color: ColorValue,
        hover_color: ColorValue,
        text_color: ColorValue,
        x: float,
        y: float,
        size_x: float,
        size_y: float,
        text: str,
        text_size: int,
        on_click_callback: Callable[[Any], None] | Callable[[], None] | None = None,
        border_width=5,
        on_click_identifier: Any | None = None,
    ):
        self.main = main
        self.inside_color = inside_color
        self.border_color = border_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.pos = self.x, self.y = x, y
        self.size = self.size_x, self.size_y = size_x, size_y
        self.border_width = border_width
        self.text = text
        self.text_size = text_size
        self.on_click_callback = on_click_callback
        self.on_click_ident = on_click_identifier

        self.init_rect()
        self.init_text()
        self.gen_textures()
        self.register_click_event()

        logger.info(f'Button "{self.text}" Initialized.')
        logger.debug(
            f'Button "{self.text}" Initialized with the following parameters: '
            f"inside_color={self.inside_color} "
            f"border_color={self.border_color} "
            f"hover_color={self.hover_color} "
            f"text_color={self.text_color} "
            f"pos={self.pos} "
            f"size={self.size} "
            f"border_width={self.border_width} "
            f"text_size={self.text_size}"
        )

    def init_rect(self):
        self.rect = pygame.Rect(0, 0, self.size_x, self.size_y)
        self.inside_rect = pygame.Rect(
            self.border_width,
            self.border_width,
            self.size_x - self.border_width * 2,
            self.size_y - self.border_width * 2,
        )

    def gen_textures(self):
        self.surface = pygame.Surface(self.size)
        self.hover_surface = pygame.Surface(self.size)

        pygame.draw.rect(self.surface, self.border_color, self.rect, self.border_width)
        pygame.draw.rect(self.surface, self.inside_color, self.inside_rect, 0)
        self.surface.blit(self.text_surface, self.text_rect)

        pygame.draw.rect(
            self.hover_surface, self.hover_color, self.rect, self.border_width
        )
        pygame.draw.rect(self.hover_surface, self.inside_color, self.inside_rect, 0)
        self.hover_surface.blit(self.text_surface, self.text_rect)

        self.hover_texture = Texture(None, self.hover_surface, self.rect)
        self.texture = Texture(None, self.surface, self.rect)

        logger.debug(f'Button "{self.text}" Textures generated.')

    def init_text(self):
        self.text_font = pygame.font.Font(None, self.text_size)
        self.text_surface = self.text_font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = self.inside_rect.center

    def draw(self):
        if self.is_hovered():
            self.hover_texture.draw(self.x, self.y)
        else:
            self.texture.draw(self.x, self.y)

    def is_hovered(self):
        pos = pygame.mouse.get_pos()
        return (
            self.x < pos[0] < self.size_x + self.x
            and self.y < pos[1] < self.size_y + self.y
        )

    def on_click(self):
        if self.is_hovered():
            if self.on_click_ident is None:
                self.on_click_callback()
            else:
                self.on_click_callback(self.on_click_ident)

    def register_click_event(self):
        self.main.EventHandler.registerMOUSEBUTTONDOWNevent(1, self.on_click)

    def stop(self):
        try:
            del self.hover_texture
        except:
            pass
        try:
            del self.texture
        except:
            pass
        self.main.EventHandler.unregisterMOUSEBUTTONDOWNevent(1, self.on_click)
        logger.debug(f'Button "{self.text}" has been destroyed.')

    def __del__(self):
        self.stop()
