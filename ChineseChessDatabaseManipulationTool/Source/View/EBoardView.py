# library
from Model.EBoardModel import EBoardModel
from Sprite.Button import Button
# class
from Utils.TextUtils import *


class EBoardView(pygame.Surface):
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if EBoardView.__instance is None:
            EBoardView()
        return EBoardView.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if EBoardView.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            EBoardView.__instance = self

        super(EBoardView, self).__init__((math.ceil(ELECTRONIC_BOARD_WIDTH), math.ceil(ELECTRONIC_BOARD_HEIGHT)))

        # draw color background
        self.fill(ELECTRONIC_BACKGROUND_COLOR)

        # button
        # self.create_buttons()

        # draw images
        self.draw_buttons()

    def draw_buttons(self):
        """
        this method to buttons
        :return: nothing
        """
        EBoardModel.get_instance().pieces.empty()
        i = 0
        for chess_piece_type in BLACK_PIECES:
            position_in_screen = Point(int(BOARD_WIDTH + ELECTRONIC_BOARD_WIDTH / 4),
                                       ROW_WIDTH / 2 + (BOARD_HEIGHT - ROW_WIDTH) / 8 * i)
            piece = Button(chess_piece_type, position_in_screen, BUTTON_SIZE, True)
            EBoardModel.get_instance().button_group.add(piece)
            i += 1

        i = 0
        for chess_piece_type in RED_PIECES:
            position_in_screen = Point(int(BOARD_WIDTH + ELECTRONIC_BOARD_WIDTH * 3 / 4),
                                       ROW_WIDTH / 2 + (BOARD_HEIGHT - ROW_WIDTH) / 8 * i)
            piece = Button(chess_piece_type, position_in_screen, BUTTON_SIZE, False)
            EBoardModel.get_instance().button_group.add(piece)
            i += 1

    # update logic
    def update(self):
        # EBoardModel.get_instance().button_group.update()
        pass

    # draw in  computer screen
    def draw(self, screen):
        EBoardModel.get_instance().pieces.draw(screen)
        EBoardModel.get_instance().button_group.draw(screen)
