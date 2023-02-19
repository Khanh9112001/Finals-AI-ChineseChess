# import class
from Const.GuiConst import *
from Model.BoardModel import BoardModel


class Piece(pygame.sprite.Sprite):

    def __init__(self, piece_name, position_in_state: Point):
        super(Piece, self).__init__()

        # name attribute
        self.name = piece_name

        # position in state
        self.position_in_state = position_in_state

        # image of sprite
        # self.image = IMAGES_PIECE_TYPE[PIECE_NAME_LIST.index(piece_name)]
        self.image = BoardModel.get_instance().images[PIECE_NAME_LIST.index(piece_name)]
        # rect of  sprite, it's position of sprite in screen
        self.rect = None

        # set position in screen
        self.set_position_in_screen(position_in_state)

    # set position of sprite in screen
    def set_position_in_screen(self, position_in_state: Point):
        # get x,y coordinate in screen
        (i, j) = (position_in_state.x, position_in_state.y)
        (x_in_screen, y_in_screen) = (BOARD_POSITION[i][j].x, BOARD_POSITION[i][j].y)

        # (x_in_screen, y_in_screen) = (x_in_screen - GuiConst.PIECE_SIZE[0] / 2 - GuiConst.BOARD_LINE_WIDTH / 2,
        #                               y_in_screen - GuiConst.PIECE_SIZE[1] / 2 - GuiConst.BOARD_LINE_WIDTH / 2)

        # get image size to set rect of sprite
        image_size = self.image.get_rect().size

        # set position of sprite
        self.rect = pygame.Rect(x_in_screen, y_in_screen, image_size[0],
                                image_size[1])

        self.rect.center = (x_in_screen, y_in_screen)

    # function to call each frame
    def update(self):
        pass
