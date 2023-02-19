# import libraries
import pygame

# import class
from Utils import Point


class Button(pygame.sprite.Sprite):

    def __init__(self, button_type, image, position: Point):
        super(Button, self).__init__()

        # name attribute
        self.type = button_type

        # image of sprite
        self.image = image

        # rect of  sprite, it's position of sprite in screen
        self.rect = self.image.get_rect()
        self.rect.center = position.get_position()

    # function to call each frame
    def update(self):
        pass

    def change_image(self, image):
        self.image = image
