# library

from Const.GuiConst import *
from Model.EBoardModel import EBoardModel
from Sprite.Button import *
from Sprite.Button_arrange import *
# class
from Utils.ProgressBar import ProgressBar
from Utils.TextUtils import *
from Sprite.ModeButton import ModeButton

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

        self.eboard_width = ELECTRONIC_BOARD_WIDTH
        self.eboard_height = ELECTRONIC_BOARD_HEIGHT
        super(EBoardView, self).__init__((math.ceil(self.eboard_width*3), math.ceil(self.eboard_height)))

        # super(EBoardView, self).__init__((math.ceil(ELECTRONIC_BOARD_WIDTH), math.ceil(ELECTRONIC_BOARD_HEIGHT)))
        # # draw color background
        # self.fill(ELECTRONIC_BACKGROUND_COLOR)

        # draw color background
        self.EBOARD_BACKGROUND = pygame.transform.smoothscale(
            pygame.image.load(RESOURCE_PATH + "/pieces/ebackground.png"),(math.ceil(self.eboard_width*4),
                                                                          math.ceil(self.eboard_height))
        )
        # progress bar
        # self.create_progress_bar()

        # clock timer
        # self.create_timer()

        # button
        self.create_buttons()


        self.draw_buttons_arrange()

    """"
        this function init progress bar in electronic board
    """

    def create_progress_bar(self):
        position = (BOARD_WIDTH + ELECTRONIC_BOARD_WIDTH * 3 / 4 - PROGRESS_BAR_WIDTH / 2, ROW_WIDTH / 2)
        EBoardModel.get_instance().progress_bar1 = ProgressBar(300, position, PROGRESS_BAR_WIDTH, PROGRESS_BAR_HEIGHT,
                                                               RED, BLACK)

        position = (BOARD_WIDTH + ELECTRONIC_BOARD_WIDTH * 3 / 4 - PROGRESS_BAR_WIDTH / 2,
                    BOARD_HEIGHT - INFORMATION_SECTION_HEIGHT)
        EBoardModel.get_instance().progress_bar2 = ProgressBar(300, position, PROGRESS_BAR_WIDTH, PROGRESS_BAR_HEIGHT,
                                                               RED, BLACK)

    """"
        this function to init timer for e-board
    """

    def create_timer(self):
        position = Point(BOARD_WIDTH + ELECTRONIC_BOARD_WIDTH / 4, INFORMATION_SECTION_HEIGHT / 2)
        EBoardModel.get_instance().timer1 = Text(FONT30, "15:00", 30, position)

        position = Point(BOARD_WIDTH + ELECTRONIC_BOARD_WIDTH / 4,
                         ELECTRONIC_BOARD_HEIGHT - INFORMATION_SECTION_HEIGHT / 2)
        EBoardModel.get_instance().timer2 = Text(FONT30, "15:00", 30, position)

    """
        this function to init button in e-board
    """

    def create_buttons(self):
        # create undo button
        position = Point(BOARD_WIDTH + ELECTRONIC_BOARD_WIDTH / 2,
                         INFORMATION_SECTION_HEIGHT + CONTROL_SECTION_HEIGHT / 3)
        undo_btn = Button("undo", UNDO_BUTTON, position)
        EBoardModel.get_instance().button_group.add(undo_btn)

        # create mode button
        position = Point(BOARD_WIDTH + ELECTRONIC_BOARD_WIDTH / 2,
                         INFORMATION_SECTION_HEIGHT )
        undo_btn = ModeButton(position)
        EBoardModel.get_instance().button_group.add(undo_btn)

        # create reset button
        position = Point(BOARD_WIDTH + ELECTRONIC_BOARD_WIDTH / 2,
                         INFORMATION_SECTION_HEIGHT + CONTROL_SECTION_HEIGHT * 2 / 3)
        undo_btn = Button("reset", RESET_BUTTON, position)
        EBoardModel.get_instance().button_group.add(undo_btn)

        # create setting button
        position = Point(BOARD_WIDTH + ELECTRONIC_BOARD_WIDTH / 2,
                         INFORMATION_SECTION_HEIGHT + CONTROL_SECTION_HEIGHT * 3 / 3)
        undo_btn = Button("setting", SETTING_BUTTON, position)
        EBoardModel.get_instance().button_group.add(undo_btn)

    def draw_buttons_arrange(self):
        """
        this method to buttons
        :return: nothing
        """
        EBoardModel.get_instance().pieces.empty()
        i = 0
        for chess_piece_type in BLACK_PIECES:
            position_in_screen = Point(int(BOARD_WIDTH + ELECTRONIC_BOARD_WIDTH / 4+ELECTRONIC_BOARD_WIDTH*1.25),
                                       ROW_WIDTH / 2 + (BOARD_HEIGHT - ROW_WIDTH) / 8 * i)
            piece = Button_arrange(chess_piece_type, position_in_screen, BUTTON_SIZE, False)
            EBoardModel.get_instance().button_arrange.add(piece)
            i += 1

        i = 0
        for chess_piece_type in RED_PIECES:
            position_in_screen = Point(int(BOARD_WIDTH + ELECTRONIC_BOARD_WIDTH * 3 / 4+ ELECTRONIC_BOARD_WIDTH*1.75),
                                       ROW_WIDTH / 2 + (BOARD_HEIGHT - ROW_WIDTH) / 8 * i)
            piece = Button_arrange(chess_piece_type, position_in_screen, BUTTON_SIZE, True)
            EBoardModel.get_instance().button_arrange.add(piece)
            i += 1
    # update logic
    def update(self):
        # EBoardModel.get_instance().progress_bar1.update(1)
        # EBoardModel.get_instance().progress_bar2.update(1)
        # EBoardModel.get_instance().button_group.update()
        pass

    # draw in  computer screen
    def draw(self, screen):
        # draw background
        self.blit(self.EBOARD_BACKGROUND, (0, 0))
        # EBoardModel.get_instance().progress_bar1.draw(screen)
        # EBoardModel.get_instance().progress_bar2.draw(screen)
        # EBoardModel.get_instance().timer1.draw(screen)
        #
        # EBoardModel.get_instance().timer2.draw(screen)
        EBoardModel.get_instance().button_group.draw(screen)
        EBoardModel.get_instance().button_arrange.draw(screen)

