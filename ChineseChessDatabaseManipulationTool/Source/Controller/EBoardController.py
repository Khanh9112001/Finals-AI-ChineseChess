from Const.GuiConst import *
from Model.BoardModel import BoardModel
from Model.EBoardModel import EBoardModel
from Model.GameInfo import GameInfo
from Utils.FenUtils import FenUtils
from Utils.StateUtil import StateUtil
from Validator.Validator import *
from View.BoardView import BoardView
from XMLHandler.XMLHandler import XMLHandler
from Database.Hash import *

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
        button = [s for s in EBoardModel.get_instance().button_group if
                  s.rect.collidepoint(mouse_position.get_position())]

        # Exit method when user dont click any button in toolbar
        if not button:
            if GameInfo.get_instance().button is not None:
                GameInfo.get_instance().button.setClicked(False)
                GameInfo.get_instance().button = None
            return
        print(BoardModel.get_instance().state)
        button = button[0]
        if button.name == PLAY_BUTTON:
            self.next_button()
        elif button.name == SAVE_BUTTON:
            self.save_button()
        elif button.name == RESET_BUTTON:
            self.back_button()
        else:
            # set animation in clicked button
            if GameInfo.get_instance().button is not None:
                GameInfo.get_instance().button.setClicked(False)
            button.setClicked(True)

            GameInfo.get_instance().button = button

    def save_button(self):
        """
        this method handle behavior of save button
        :return:
        """
        fen_input = BoardModel.get_instance().input_fen
        fen_output = BoardModel.get_instance().output_fen

        if GameInfo.get_instance().isUpperTurn and fen_input != '' and fen_output != '':
            hash = Hashtable()
            hash.fromFen(fen_input+' b')
            mv = self.move_in_square(BoardModel.get_instance().move)
            hash.Insert_Dat(mv)
            print(hash.zobristLock>>1)
            # XMLHandler.insert(fen_input, fen_output)
            print("saving process")

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
                # reset text
                # BoardView.get_instance().draw_input_fen_text(FenUtils.matrix2fen(BoardModel.get_instance().state))
                # delete recommend pieces
                BoardModel.get_instance().recommend_pieces.empty()
                print("Valid",BoardModel.get_instance().state)
                GameInfo.get_instance().state = STATE_PROGRAM[1]


    def back_button(self):
        """
        this method handle behavior of back button
        :return:
        """
        if GameInfo.get_instance().state == STATE_PROGRAM[1]:
            # change state of game info
            GameInfo.get_instance().state = STATE_PROGRAM[0]

            # draw recommend
            state = FenUtils.fen2matrix(BoardModel.get_instance().input_fen)
            BoardView.get_instance().draw_recommend(
                StateUtil.get_instance().generate_recommend_pieces_in_empty_square(state))

            # delete output fen
            BoardView.get_instance().draw_input_fen_text("")

    def move_in_square(self,move):
        previous_move = 3 * 16 + move[0][0] * 16 + move[0][1] + 3
        next_move = 3 * 16 + move[1][0] * 16 + move[1][1] + 3
        mv = previous_move + (next_move << 8)
        return mv