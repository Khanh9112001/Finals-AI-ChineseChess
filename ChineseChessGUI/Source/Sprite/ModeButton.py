# import libraries

from Const.GuiConst import MODE_BUTTON
from Sprite.Button import Button
# import class
from Utils import Point


class ModeButton(Button):
    def __init__(self, position: Point):
        super(Button, self).__init__()

        # name attribute
        self.type = 'mode'

        self.index = 0
        # image of sprite
        self.image = MODE_BUTTON[self.index]

        # rect of  sprite, it's position of sprite in screen
        self.rect = self.image.get_rect()
        self.rect.center = position.get_position()

    # function to call each frame
    def update(self):
        pass

    def change_image(self):
        self.index = 1 - self.index
        self.image = MODE_BUTTON[self.index]
