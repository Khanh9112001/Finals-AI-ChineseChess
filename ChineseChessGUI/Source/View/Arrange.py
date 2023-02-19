from Const.GuiConst import *
from Const.GuiConst import INIT_STATE_ARRANGE
from Model.BoardModel import *
from Utils.FenUtils import *
from View.BoardView import *
from View.EBoardView import *
from Model.GameInfo import *
from Sprite.RecommendPiece import *
class Arrange:
    @staticmethod
    def board_arrangement():
        BoardModel.get_instance().previousStep.empty()
        BoardModel.get_instance().images = IMAGES_PERSON_FIRST[0]
        BoardModel.get_instance().state = copy.deepcopy(INIT_STATE_ARRANGE)
        BoardView.get_instance().draw_pieces()
        GameInfo.get_instance().state = STATE_PROGRAM[0]
        BoardView.get_instance().draw_recommend(RECOMMEND_STATE)
        screen = pygame.display.set_mode((int(BOARD_WIDTH +ELECTRONIC_BOARD_WIDTH * 3), WINDOW_HEIGHT))

    @staticmethod
    def board_init():
        BoardModel.get_instance().state = copy.deepcopy(INIT_STATE)
        BoardView.get_instance().draw_pieces()
        BoardModel.get_instance().recommend_pieces.empty()
        BoardModel.get_instance().previousStep.empty()
        GameInfo.get_instance().state = STATE_PROGRAM[1]
        EBoardView.get_instance().eboard_width = ELECTRONIC_BOARD_WIDTH
        screen = pygame.display.set_mode((int(BOARD_WIDTH + ELECTRONIC_BOARD_WIDTH), WINDOW_HEIGHT))
