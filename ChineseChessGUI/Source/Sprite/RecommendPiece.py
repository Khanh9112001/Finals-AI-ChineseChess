# import libraries
import pygame
import os
# import class
from Utils import Point
from Utils.Point import Point
from Const import GuiConst
from Model.GameInfo import GameInfo
from Const.GuiConst import STATE_PROGRAM
# ABS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Asset'))
ABS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Asset/pieces'))

IMAGES = (
    # pygame.transform.smoothscale(pygame.image.load(ABS_PATH + "/RecommendPiece.png"), GuiConst.RECOMMEND_PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(ABS_PATH + "/mask.png"), GuiConst.RECOMMEND_PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(ABS_PATH + "/mask1.png"), GuiConst.PIECE_SIZE),
)


class RecommendPiece(pygame.sprite.Sprite):

    def __init__(self, position_in_state: Point):
        super(RecommendPiece, self).__init__()

        # image of sprite
        if GameInfo.get_instance().state == STATE_PROGRAM[1]:
            self.image = IMAGES[0]
        else:
            self.image = IMAGES[1]

        # position in state
        self.position_in_state = position_in_state

        # name of piece
        self.name = "0"

        # rect of  sprite, it's position of sprite in screen
        self.rect = None

        # set position of sprite in screen
        self.set_position_in_screen(position_in_state)

    # set position of sprite in screen
    def set_position_in_screen(self, position_in_state: Point):

        # get x,y coordinate in screen
        (i, j) = (position_in_state.x, position_in_state.y)
        (x_in_screen, y_in_screen) = (GuiConst.BOARD_POSITION[i][j].x, GuiConst.BOARD_POSITION[i][j].y)
        # (x_in_screen, y_in_screen) = (x_in_screen - GuiConst.PIECE_SIZE[0] / 2 - GuiConst.BOARD_LINE_WIDTH / 2,
        #                               y_in_screen - GuiConst.PIECE_SIZE[1] / 2 - GuiConst.BOARD_LINE_WIDTH / 2)

        # get image size to set rect of sprite
        image_size = self.image.get_rect().size

        # set position of sprite
        self.rect = pygame.Rect(x_in_screen, y_in_screen, image_size[0],
                                image_size[1])
        self.rect.center = (x_in_screen, y_in_screen)

    def update(self):
        pass

    def get_position(self):
        point = Point()
        point.set_position(self.rect.center)
        return point