import os

# import class
from Const.GuiConst import *
from Utils.Point import Point

ABS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Asset/fonts'))
FONT30 = ABS_PATH + "/Muli-Regular.ttf"
FONT30B = ABS_PATH + '/Muli-Bold.ttf'
FONT60B = ABS_PATH + '/Muli-Bold.ttf'
green = (0, 255, 0)
blue = (0, 0, 128)


class Text:
    """"
        text : text to display
        size :  size of text
        position :  position of text in computer screen
    """

    def __init__(self, font_path, text, size, position: Point):
        # create font object
        self.FONT30B = pygame.font.Font(font_path, size)
        self.text = self.FONT30B.render(text, True, green, blue)
        self.rect = self.text.get_rect()

        # set position
        self.rect.center = position.get_position()

    """"
        call this function each frame to display text in computer screen
        screen :  surface
    """

    def draw(self, screen):
        screen.blit(self.text, self.rect)
