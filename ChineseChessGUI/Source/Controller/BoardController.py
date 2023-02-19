import copy

from Const.GuiConst import *
from Model.BoardModel import BoardModel
from Model.GameInfo import GameInfo
from Sound.Sound import Sound
from Sprite.Piece import Piece
from Sprite.RecommendPiece import RecommendPiece
from Sprite.Button_arrange import Button_arrange
from Utils.Checked import Checked
from Utils.FenUtils import FenUtils
from Utils.StateUtil import StateUtil
from View.BoardView import BoardView
from Const.const import AI_SIDE
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

    """ this function handle event when game in person vs person mode"""

    def person_mode(self, mouse_position: Point):
        global event_piece

        state = BoardModel.get_instance().state
        board_model = BoardModel.get_instance()
        board_view = BoardView.get_instance()

        clicked_piece = [s for s in board_model.piece_sprites if s.rect.collidepoint(mouse_position.get_position())]
        clicked_recommend_piece = [s for s in board_model.recommend_pieces if
                                   s.rect.collidepoint(mouse_position.get_position())]

        # move piece to a location which is occupied by another piece

        if clicked_piece and clicked_recommend_piece:
            print('1')

            # play sound
            Sound.get_instance().chessMoveSound()

            # toggle turn
            GameInfo.get_instance().toggle_player()

            # delete recommend sprite list
            board_model.recommend_pieces.empty()

            # delete previousStep
            board_model.previousStep.empty()

            # self.recommend_pieces.kill()
            clicked_piece[0].kill()
            # previous step
            board_view.daw_previous_step(event_piece[len(event_piece) - 1].position_in_state)

            # present step
            board_view.daw_previous_step(clicked_recommend_piece[0].position_in_state)

            # move piece
            self.move_piece(event_piece[len(event_piece) - 1], clicked_recommend_piece[0])

            # number of Step
            if event_piece[len(event_piece) - 1].name.islower():
                BoardModel.get_instance().number_step_black += 1
            else:
                BoardModel.get_instance().number_step_red += 1

            # check Mate:
            if self.isMate(BoardModel.get_instance().state, 0):
                board_view.draw_is_mate()
                # BoardModel.get_instance().red_king_sprite.image = KING_RED_DIED
                GameInfo.get_instance().gameIsNotOver = False
            elif self.isMate(BoardModel.get_instance().state, 1):
                board_view.draw_is_mate()
                # BoardModel.get_instance().black_king_sprite.image = KING_BLACK_DIED
                GameInfo.get_instance().gameIsNotOver = False

            #is Check
            elif clicked_piece[0].name.islower():
                if self.is_check(state,1):
                    board_view.draw_is_check()
                    print('chieu tuong')
            elif self.is_check(state,0):
                board_view.draw_is_check()
                print('chieu tuong')
        # move piece into empty position
        elif clicked_recommend_piece:
            print('2')

            # Sound
            Sound.get_instance().chessMoveSound()

            # toggle turn
            GameInfo.get_instance().toggle_player()

            # delete recommend sprite list
            board_model.recommend_pieces.empty()

            board_model.previousStep.empty()

            # previous step
            board_view.daw_previous_step(event_piece[len(event_piece) - 1].position_in_state)

            # present step
            board_view.daw_previous_step(clicked_recommend_piece[0].position_in_state)

            # move piece
            self.move_piece(event_piece[len(event_piece) - 1], clicked_recommend_piece[0])

            # number of Step
            if event_piece[len(event_piece) - 1].name.islower():
                BoardModel.get_instance().number_step_black += 1
            else:
                BoardModel.get_instance().number_step_red += 1

            # check Mate:
            if self.isMate(BoardModel.get_instance().state, 0):
                board_view.draw_is_mate()
                # BoardModel.get_instance().red_king_sprite.image = KING_RED_DIED
                GameInfo.get_instance().gameIsNotOver = False
            elif self.isMate(BoardModel.get_instance().state, 1):
                board_view.draw_is_mate()
                # BoardModel.get_instance().black_king_sprite.image = KING_BLACK_DIED
                GameInfo.get_instance().gameIsNotOver = False

            # is Check
            elif self.is_check(state, 0):
                board_view.draw_is_check()
                print('chieu tuong')
            elif self.is_check(state, 1):
                board_view.draw_is_check()
                print('chieu tuong')
        # if click upper piece
        elif clicked_piece and clicked_piece[
            0].name.islower() and GameInfo.get_instance().isUpperTurn and GameInfo.get_instance().gameIsNotOver:
            print("3")
            event_piece += clicked_piece
            # delete recommend oppside sprite list
            board_model.previousStep.empty()
            board_view.draw_recommend(
                self.check_recomend(state, event_piece[len(event_piece) - 1].position_in_state, 1)[0])
            # check Mate:
            if self.isMate(BoardModel.get_instance().state, 0):
                board_view.draw_is_mate()
                GameInfo.get_instance().gameIsNotOver = False

        # if click lower piece
        elif clicked_piece and clicked_piece[0].name.isupper() and (
                not GameInfo.get_instance().isUpperTurn) and GameInfo.get_instance().gameIsNotOver:
            print("4")
            # delete recommend oppside sprite list
            board_model.previousStep.empty()
            event_piece += clicked_piece
            board_view.draw_recommend(
                self.check_recomend(state, event_piece[len(event_piece) - 1].position_in_state, 0)[0])
            # board_view.draw_recommend(
            #     StateUtil.get_instance().generate_recommend_piece(state, clicked_piece[0].position_in_state))
            # check Mate
            if self.isMate(BoardModel.get_instance().state, 1):
                board_view.draw_is_mate()
                # BoardModel.get_instance().black_king_sprite.image = KING_BLACK_DIED
                GameInfo.get_instance().gameIsNotOver = False
        # if click into a empty position
        else:
            print("5")
            # delete recommend sprite list
            board_model.recommend_pieces.empty()

    def ai_mode(self, mouse_position: Point):
        """
        this function handle event when game mode is AI vs person mode
        :param mouse_position: hjh
        :return: kjhj
        """
        global event_piece
        state = BoardModel.get_instance().state
        board_model = BoardModel.get_instance()
        board_view = BoardView.get_instance()

        clicked_piece = [s for s in board_model.piece_sprites if s.rect.collidepoint(mouse_position.get_position())]
        clicked_recommend_piece = [s for s in board_model.recommend_pieces if
                                   s.rect.collidepoint(mouse_position.get_position())]

        # if self.isMate(BoardModel.get_instance().state, 0):
        #     # BoardModel.get_instance().red_king_sprite.image = KING_RED_DIED
        #     BoardView.get_instance().draw_is_mate()
        #     GameInfo.get_instance().gameIsNotOver = False

        # move piece to a location which is occupied by another piece
        if clicked_piece and clicked_recommend_piece:
            print('1')

            # play sound
            Sound.get_instance().chessMoveSound()

            # toggle turn
            GameInfo.get_instance().toggle_player()

            # delete recommend sprite list
            board_model.recommend_pieces.empty()

            board_model.previousStep.empty()

            # self.recommend_pieces.kill()
            clicked_piece[0].kill()

            # previous step
            board_view.daw_previous_step(event_piece[len(event_piece) - 1].position_in_state)

            # present step
            board_view.daw_previous_step(clicked_recommend_piece[0].position_in_state)

            # move piece
            self.move_piece(event_piece[len(event_piece) - 1], clicked_recommend_piece[0])

            BoardModel.get_instance().number_step_red += 1

            # check Mate
            if self.isMate(BoardModel.get_instance().state, 0):
                # BoardModel.get_instance().black_king_sprite.image = KING_BLACK_DIED
                BoardView.get_instance().draw_is_mate()
                GameInfo.get_instance().gameIsNotOver = False

            # is Check
            elif self.is_check(state, 0):
                board_view.draw_is_check()
                print('chieu tuong')
            elif self.is_check(state, 1):
                board_view.draw_is_check()
                print('chieu tuong')
        # move piece into empty position
        elif clicked_recommend_piece:
            print('2')

            # Sound
            Sound.get_instance().chessMoveSound()

            # toggle turn
            GameInfo.get_instance().toggle_player()

            # delete recommend sprite list
            board_model.recommend_pieces.empty()

            board_model.previousStep.empty()

            # previous step
            board_view.daw_previous_step(event_piece[len(event_piece) - 1].position_in_state)

            # present step
            board_view.daw_previous_step(clicked_recommend_piece[0].position_in_state)

            # move piece
            self.move_piece(event_piece[len(event_piece) - 1], clicked_recommend_piece[0])

            BoardModel.get_instance().number_step_red += 1

            # check Mate
            # print(self.isMate(BoardModel.get_instance().state, 1))
            if self.isMate(BoardModel.get_instance().state, 0):
                # BoardModel.get_instance().black_king_sprite.image = KING_BLACK_DIED
                BoardView.get_instance().draw_is_mate()
                GameInfo.get_instance().gameIsNotOver = False
            # is Check
            elif self.is_check(state, 0):
                board_view.draw_is_check()
                print('chieu tuong')
            elif self.is_check(state, 1):
                board_view.draw_is_check()
                print('chieu tuong')
        # if click upper piece
        elif clicked_piece and clicked_piece[
            0].name.islower() and GameInfo.get_instance().isUpperTurn and GameInfo.get_instance().gameIsNotOver:
            print("3")
            # delete recommend oppside sprite list
            board_model.previousStep.empty()
            event_piece += clicked_piece
            board_view.draw_recommend(
                self.check_recomend(state, event_piece[len(event_piece) - 1].position_in_state, AI_SIDE)[0])
            # board_view.draw_recommend(
            #     StateUtil.get_instance().generate_recommend_piece(state, clicked_piece[0].position_in_state))
        # # if click lower piece
        # elif clicked_piece and clicked_piece[0].name.islower() and (
        #         not GameInfo.get_instance().isUpperTurn) and GameInfo.get_instance().gameIsNotOver:
        #     print("4")
        #     event_piece += clicked_piece
        #     board_view.draw_recommend(
        #         StateUtil.get_instance().generate_recommend_piece(state, clicked_piece[0].position_in_state))
        # if click into a empty position
        else:
            print("5")
            # delete recommend sprite list
            board_model.recommend_pieces.empty()

    """ this function handle event"""

    def handle_mouse_click(self, mouse_position: Point):
        if GameInfo.get_instance().state == STATE_PROGRAM[0]:
            self.draw_recommend_piece(mouse_position)
            self.draw_piece(mouse_position)
        elif GameInfo.get_instance().state == STATE_PROGRAM[1]:
            if GameInfo.get_instance().mode == MODE[1]:
                self.person_mode(mouse_position)
            else:
                self.ai_mode(mouse_position)

    """
        move piece from this position to new position

        piece :param
        des_recommend_piece :param

    """

    def move_piece(self, piece: Piece, des_recommend_piece: RecommendPiece):
        # posotion of move
        BoardModel.get_instance().move = [(piece.position_in_state.x, piece.position_in_state.y),
                                          (des_recommend_piece.position_in_state.x,
                                           des_recommend_piece.position_in_state.y)]
        # move piece in board
        piece.set_position_in_screen(des_recommend_piece.position_in_state)

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

    # def move_piece(self, piece: Button_arrange, des_recommend_piece: RecommendPiece):
    #     """
    #         move piece from this position to new position
    #
    #         piece :param
    #         des_recommend_piece :param
    #
    #     """
    #     # posotion of move
    #     BoardModel.get_instance().move = [(piece.position_in_state.x, piece.position_in_state.y),
    #                                       (des_recommend_piece.position_in_state.x,
    #                                        des_recommend_piece.position_in_state.y)]
    #     # move piece in board
    #     point = Point(des_recommend_piece.rect.centerx, des_recommend_piece.rect.centery)
    #
    #     piece.set_position_in_screen(point, PIECE_SIZE)
    #     # piece.position_in_state = des_recommend_piece.position_in_state
    #
    #     # move piece in state
    #     state = BoardModel.get_instance().state
    #
    #     # add state to history
    #     BoardModel.get_instance().previousStates.append(copy.deepcopy(state))
    #
    #     # change state
    #     state[des_recommend_piece.position_in_state.x][des_recommend_piece.position_in_state.y] = \
    #         state[piece.position_in_state.x][piece.position_in_state.y]
    #     state[piece.position_in_state.x][piece.position_in_state.y] = '.'
    #
    #     # move sprite location in computer screen
    #     piece.position_in_state.x = des_recommend_piece.position_in_state.x
    #     piece.position_in_state.y = des_recommend_piece.position_in_state.y
    def is_game_over(self, piece: Piece):
        if piece.name == PIECE_NAME_LIST[0] or piece.name == PIECE_NAME_LIST[7]:
            return True

        return False

    def check_recomend(self, state, point_in_state: Point, sdPlayer):
        """
         filter generate recommend
        :param state: state in Board model
        :param point_in_state: Point of piece generate
        :param sdPlayer: 0 or 1 to define Side move
        :return state filtered
        """
        state_generate = StateUtil.get_instance().generate_recommend_piece(state, point_in_state)
        result = copy.deepcopy(state)
        piece = state[point_in_state.x][point_in_state.y]
        isGenerate = False
        for i in range(0, 10):
            for j in range(0, 9):
                if state_generate[i][j] == 'o':
                    sts = copy.deepcopy(state)
                    sts[point_in_state.x][point_in_state.y] = '.'
                    sts[i][j] = piece
                    if not self.is_check(sts, sdPlayer):
                        result[i][j] = 'o'
                        isGenerate = True
        return result, isGenerate

    def isMate(self, state, sdPlayer):
        """
        :param state: state in Board model
        :param sdPlayer: 0 or 1 to define side move
        :return: True if is mate , else False
        """
        point_in_state = Point()
        sts = copy.deepcopy(state)
        for i in range(0, 10):
            for j in range(0, 9):
                if sdPlayer == 0:
                    if state[i][j].isupper():
                        point_in_state.x = i
                        point_in_state.y = j
                        if self.check_recomend(sts, point_in_state, sdPlayer)[1]:
                            return False
                else:
                    if state[i][j].islower():
                        point_in_state.x = i
                        point_in_state.y = j
                        if self.check_recomend(sts, point_in_state, sdPlayer)[1]:
                            return False
        return True

    def is_check(self, state, sdPlayer):
        """
        :param state: state in Board model
        :param sdPlayer: 0 or 1 to define side move
        :return: True if King being checked
        """
        check = Checked()
        sts = copy.deepcopy(state)
        check.sdPlayer = sdPlayer
        check.squares = FenUtils.convert2dto1darray(sts)
        if check.checked():
            return True

    def create_recommend_piece(self, piece: Button_arrange):
        # create new piece in position of recommend piece
        new_recommend_piece = RecommendPiece(piece.position_in_state)
        BoardModel.get_instance().recommend_pieces.add(new_recommend_piece)

        (i, j) = piece.position_in_state.get_position()
        BoardModel.get_instance().state[i][j] = EMPTY

        # delete recommend piece
        GameInfo.get_instance().button_arrange.setClicked(False)
        GameInfo.get_instance().button_arrange = None
        piece.kill()
    def create_piece(self, piece: Button_arrange, recommend_piece: RecommendPiece):
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
        # new_piece = Button_arrange(piece.name, recommend_piece.get_position(), PIECE_SIZE, piece.name.islower(),
        #                    recommend_piece.position_in_state)
        new_piece = Piece(piece.name,recommend_piece.position_in_state)
        BoardModel.get_instance().piece_sprites.add(new_piece)

        # delete recommend piece
        recommend_piece.kill()

    def draw_piece(self, mouse_position):
        """
        this method draw piece in board if user choose a piece in toolbar and click into recommend piece
        :param mouse_position:
        :return:
        """
        # get object which is selected by mouse
        recommend_pieces = [s for s in BoardModel.get_instance().recommend_pieces if
                            s.rect.collidepoint(mouse_position.get_position())]

        if (not recommend_pieces) or (GameInfo.get_instance().button_arrange is None) or (
                GameInfo.get_instance().button_arrange.name == DELETE_BUTTON):
            return

        recommend_piece = recommend_pieces[0]
        self.create_piece(GameInfo.get_instance().button_arrange, recommend_piece)

    def draw_recommend_piece(self, mouse_position):
        """
        this method delete piece when user choose delete button in toolbar and click into piece in board
        :param mouse_position: position of mouse
        :return:
        """
        pieces = [s for s in BoardModel.get_instance().piece_sprites if
                  s.rect.collidepoint(mouse_position.get_position())]

        if (not pieces) or (GameInfo.get_instance().button_arrange is None):
            return

        piece = pieces[0]
        if GameInfo.get_instance().button_arrange.name == DELETE_BUTTON:
            self.create_recommend_piece(piece)