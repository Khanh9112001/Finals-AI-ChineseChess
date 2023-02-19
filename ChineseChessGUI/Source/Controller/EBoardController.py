import copy

from Const.GuiConst import *
from Model.BoardModel import BoardModel
from Model.EBoardModel import EBoardModel
from Model.GameInfo import GameInfo
from View.BoardView import BoardView
from Model.GameInfo import GameInfo
from Sound.Sound import Sound
from View.Setting import *
from Validator.Validator import Validator
from Utils.StateUtil import StateUtil
class EBoardController:
    __instance = None

    def __init__(self):
        if self.__instance is None:
            EBoardController.__instance = self
        else:
            raise Exception("this class is a singleton class")

    @staticmethod
    def get_instance():
        if EBoardController.__instance is None:
            EBoardController()

        return EBoardController.__instance

    def handle_mouse_click(self, mouse_position: Point):

        # get object which is selected by mouse
        clicked_piece = [s for s in EBoardModel.get_instance().button_group if
                         s.rect.collidepoint(mouse_position.get_position())]
        clicked_piece_arrange = [s for s in EBoardModel.get_instance().button_arrange if
                         s.rect.collidepoint(mouse_position.get_position())]

        # if button is undo type
        if clicked_piece and clicked_piece[0].type == BUTTON_TYPE_LIST[0]:  # undo button
            self.back_previous_state()
        elif clicked_piece and clicked_piece[0].type == BUTTON_TYPE_LIST[1]:  # mode toggle button
            clicked_piece[0].change_image()
            self.change_mode()
        elif clicked_piece and clicked_piece[0].type == BUTTON_TYPE_LIST[2]:  # reset button
            self.reset_chess_board()
        elif clicked_piece and clicked_piece[0].type == BUTTON_TYPE_LIST[3]:  # setting button
            self.setting_board()

        print(clicked_piece_arrange)
        # Exit method when user dont click any button in toolbar
        if not clicked_piece_arrange:
            if GameInfo.get_instance().button_arrange is not None:
                GameInfo.get_instance().button_arrange.setClicked(False)
                GameInfo.get_instance().button_arrange = None
            return
        button = clicked_piece_arrange[0]
        if button.name == PLAY_BUTTON:
            self.next_button()
        else:
            # set animation in clicked button
            if GameInfo.get_instance().button_arrange is not None:
                GameInfo.get_instance().button_arrange.setClicked(False)
            button.setClicked(True)
            GameInfo.get_instance().button_arrange = button

    """ this function will change mode of game"""

    def change_mode(self):
        # reset board
        self.reset_chess_board()
        # if change mode then intital back_previous
        BoardModel.get_instance().previousStates = []
        # change mode in game info
        if GameInfo.get_instance().mode == MODE[0]:
            GameInfo.get_instance().mode = MODE[1]
        else:
            GameInfo.get_instance().mode = MODE[0]

    """this functions will be call when user click into undo button"""

    def back_previous_state(self):
        boardModel = BoardModel.get_instance()
        boardModel.previousStep.empty()
        boardModel.is_mate.empty()

        # Statistic
        if GameInfo.get_instance().mode == MODE[1]:
            print('P vs P')
            if GameInfo.get_instance().isUpperTurn and boardModel.number_step_red > 0:
                boardModel.number_step_red -= 1
            elif boardModel.number_step_black > 0:
                boardModel.number_step_black -= 1
        elif boardModel.number_step_red > 0 and boardModel.number_step_black > 0:
            boardModel.number_step_red -= 1
            boardModel.number_step_black -= 1

        if boardModel.previousStates:
            boardModel.state = boardModel.previousStates.pop()
            BoardView.get_instance().draw_pieces()
            if GameInfo.get_instance().mode == MODE[1]:  # undo of 2 player
                GameInfo.get_instance().toggle_player()
            GameInfo.get_instance().gameIsNotOver = True

    """this function will be call when user click into reset button"""

    def reset_chess_board(self):
        Sound.reset_board()
        BoardModel.get_instance().is_mate.empty()

        #Statistic
        BoardModel.get_instance().number_step_red = 0
        BoardModel.get_instance().number_step_black = 0

        BoardModel.get_instance().state = copy.deepcopy(INIT_STATE)
        BoardModel.get_instance().previousStep.empty()
        # BoardModel.get_instance().previousStep.empty()
        BoardView.get_instance().draw_pieces()
        GameInfo.get_instance().reset_attributes_to_new_game()

    def setting_board(self):
        root = Root()

        # root.geometry("550x300+300+150")
        # root.resizable(width=True, height=True)
        # root.mainloop()

    def next_button(self):
        """
        this method handle behavior of next button
        :return:
        """
        if GameInfo.get_instance().state == STATE_PROGRAM[0]:
            print("return value:", Validator.Valide_state(BoardModel.get_instance().state))
            if not Validator.get_instance().Valide_state(BoardModel.get_instance().state):
                BoardView.get_instance().draw_input_fen_text("invalid board")
            else:
                # delete recommend pieces
                BoardModel.get_instance().recommend_pieces.empty()
                if not StateUtil.get_instance().check_side_lower(BoardModel.get_instance().state):
                    GameInfo.get_instance().isUpperTurn = False
                    BoardModel.get_instance().state = StateUtil.get_instance().change_upper_to_lower(BoardModel.get_instance().state)
                    BoardModel.get_instance().images = IMAGES_AI_FIRST[0]
                print('Valid', BoardModel.get_instance().state)
                GameInfo.get_instance().state = STATE_PROGRAM[1]
                screen = pygame.display.set_mode((int(BOARD_WIDTH +ELECTRONIC_BOARD_WIDTH), WINDOW_HEIGHT))