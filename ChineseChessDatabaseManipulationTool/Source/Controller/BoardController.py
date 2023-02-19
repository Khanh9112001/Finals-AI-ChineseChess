import copy

from Const.GuiConst import *
from Model.BoardModel import BoardModel
from Model.GameInfo import GameInfo
from Sound.Sound import Sound
from Sprite.Button import Button
from Sprite.RecommendPiece import RecommendPiece
from Utils.FenUtils import FenUtils
from Utils.StateUtil import StateUtil
from View.BoardView import BoardView

"""
this class is controller of board
"""

event_piece = []  # save piece when click


class BoardController:
    __instance = None

    def __init__(self):
        if BoardController.__instance is None:
            BoardController.__instance = self
        else:
            raise Exception("this class is a singleton class")

    @staticmethod
    def get_instance():
        if BoardController.__instance is None:
            BoardController()

        return BoardController.__instance

    """ this function handle event"""

    def handle_mouse_click(self, mouse_position: Point):
        if GameInfo.get_instance().state == STATE_PROGRAM[0]:
            self.draw_recommend_piece(mouse_position)
            self.draw_piece(mouse_position)
        elif GameInfo.get_instance().state == STATE_PROGRAM[1]:
            self.p_vs_p_mode(mouse_position)

    def p_vs_p_mode(self, mouse_position: Point):
        """
        this method allow user choose next state for AI
        :param mouse_position:
        :return:
        """
        global event_piece

        state = BoardModel.get_instance().state
        board_model = BoardModel.get_instance()
        board_view = BoardView.get_instance()

        clicked_piece = [s for s in board_model.piece_sprites if s.rect.collidepoint(mouse_position.get_position())]
        clicked_recommend_piece = [s for s in board_model.recommend_pieces if
                                   s.rect.collidepoint(mouse_position.get_position())]

        # move piece to a location which is occupied by another piece
        if clicked_piece and clicked_recommend_piece:
            # play sound
            Sound.chessMoveSound()

            # delete recommend sprite list
            board_model.recommend_pieces.empty()
            # self.recommend_pieces.kill()
            clicked_piece[0].kill()

            # move piece
            self.move_piece(event_piece[len(event_piece) - 1], clicked_recommend_piece[0])

            # get Fen
            if GameInfo.get_instance().isUpperTurn:
                BoardView.get_instance().draw_input_fen_text(FenUtils.matrix2fen(BoardModel.get_instance().state))
            else:
                BoardView.get_instance().draw_output_fen_text(FenUtils.matrix2fen(BoardModel.get_instance().state))

            # toggle play turn
            GameInfo.get_instance().toggle_player()


        # move piece into empty position
        elif clicked_recommend_piece:
            # Sound
            Sound.chessMoveSound()

            # delete recommend sprite list
            board_model.recommend_pieces.empty()

            # move piece
            self.move_piece(event_piece[len(event_piece) - 1], clicked_recommend_piece[0])

            # get Fen
            if GameInfo.get_instance().isUpperTurn:
                BoardView.get_instance().draw_input_fen_text(FenUtils.matrix2fen(BoardModel.get_instance().state))
            else:
                BoardView.get_instance().draw_output_fen_text(FenUtils.matrix2fen(BoardModel.get_instance().state))

            # toggle play turn
            GameInfo.get_instance().toggle_player()

        # if click upper piece
        elif clicked_piece and clicked_piece[
            0].name.islower() and (not GameInfo.get_instance().isUpperTurn):
            event_piece += clicked_piece
            board_view.draw_recommend(
                StateUtil.get_instance().generate_recommend_piece(state, clicked_piece[0].position_in_state))
        elif clicked_piece and clicked_piece[0].name.isupper() and GameInfo.get_instance().isUpperTurn:
            event_piece += clicked_piece
            board_view.draw_recommend(
                StateUtil.get_instance().generate_recommend_piece(state, clicked_piece[0].position_in_state))
        else:
            # delete recommend sprite list
            board_model.recommend_pieces.empty()

    def draw_piece(self, mouse_position):
        """
        this method draw piece in board if user choose a piece in toolbar and click into recommend piece
        :param mouse_position:
        :return:
        """
        # get object which is selected by mouse
        recommend_pieces = [s for s in BoardModel.get_instance().recommend_pieces if
                            s.rect.collidepoint(mouse_position.get_position())]

        if (not recommend_pieces) or (GameInfo.get_instance().button is None) or (
                GameInfo.get_instance().button.name == DELETE_BUTTON):
            return

        recommend_piece = recommend_pieces[0]
        self.create_piece(GameInfo.get_instance().button, recommend_piece)

    def draw_recommend_piece(self, mouse_position):
        """
        this method delete piece when user choose delete button in toolbar and click into piece in board
        :param mouse_position: position of mouse
        :return:
        """
        pieces = [s for s in BoardModel.get_instance().piece_sprites if
                  s.rect.collidepoint(mouse_position.get_position())]

        if (not pieces) or (GameInfo.get_instance().button is None):
            return

        piece = pieces[0]
        if GameInfo.get_instance().button.name == DELETE_BUTTON:
            self.create_recommend_piece(piece)

    def create_recommend_piece(self, piece: Button):
        # create new piece in position of recommend piece
        new_recommend_piece = RecommendPiece(piece.position_in_state)
        BoardModel.get_instance().recommend_pieces.add(new_recommend_piece)

        (i, j) = piece.position_in_state.get_position()
        BoardModel.get_instance().state[i][j] = EMPTY

        # delete recommend piece
        GameInfo.get_instance().button.setClicked(False)
        GameInfo.get_instance().button = None
        piece.kill()

    def create_piece(self, piece: Button, recommend_piece: RecommendPiece):
        """
        this method create a piece in board using position of recommend piece
        :param piece:
        :param recommend_piece:
        :return:
        """
        # change state of board
        (i, j) = recommend_piece.position_in_state.get_position()
        BoardModel.get_instance().state[i][j] = piece.name

        # create new piece in position of recommend piece
        new_piece = Button(piece.name, recommend_piece.get_position(), PIECE_SIZE, piece.name.islower(),
                           recommend_piece.position_in_state)

        BoardModel.get_instance().piece_sprites.add(new_piece)

        # delete recommend piece
        recommend_piece.kill()

    def move_piece(self, piece: Button, des_recommend_piece: RecommendPiece):
        """
            move piece from this position to new position

            piece :param
            des_recommend_piece :param

        """
        # posotion of move
        BoardModel.get_instance().move = [(piece.position_in_state.x, piece.position_in_state.y),
                                          (des_recommend_piece.position_in_state.x, des_recommend_piece.position_in_state.y)]
        # move piece in board
        point = Point(des_recommend_piece.rect.centerx, des_recommend_piece.rect.centery)

        piece.set_position_in_screen(point, PIECE_SIZE)
        # piece.position_in_state = des_recommend_piece.position_in_state


        # move piece in state
        state = BoardModel.get_instance().state

        # add state to history
        BoardModel.get_instance().previousStates.append(copy.deepcopy(state))

        # change state
        state[des_recommend_piece.position_in_state.x][des_recommend_piece.position_in_state.y] = \
            state[piece.position_in_state.x][piece.position_in_state.y]
        state[piece.position_in_state.x][piece.position_in_state.y] = '.'

        # move sprite location in computer screen
        piece.position_in_state.x = des_recommend_piece.position_in_state.x
        piece.position_in_state.y = des_recommend_piece.position_in_state.y

