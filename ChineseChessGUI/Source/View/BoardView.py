# library
from builtins import *

# class
from Const import GuiConst
from Model.BoardModel import BoardModel
from Sprite.Piece import Piece
from Sprite.RecommendPiece import RecommendPiece
from Utils.StateUtil import *
from Sprite.IsCheck import *
from Sprite.IsMate import *
from Model.GameInfo import GameInfo
class BoardView(pygame.Surface):
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if BoardView.__instance is None:
            BoardView()
        return BoardView.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if BoardView.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            BoardView.__instance = self

        super(BoardView, self).__init__((GuiConst.BOARD_WIDTH, GuiConst.BOARD_HEIGHT))

        # draw color background
        self.BOARD_BACKGROUND = pygame.transform.smoothscale(
            pygame.image.load(RESOURCE_PATH + "/pieces/background.png"), (WINDOW_HEIGHT, WINDOW_HEIGHT))

        # draw board background
        self.draw_board_background()

        # init pieces
        self.draw_pieces()

    # Draw background of chinese chess board
    def draw_board_background(self):
        # draw vertical lines
        for i in range(GuiConst.BOARD_DIMENSION[0]):
            if i == 0 or i == 8:
                start_point = (
                    GuiConst.COLUMN_WIDTH / 2 + GuiConst.COLUMN_WIDTH * i - math.floor(GuiConst.BOARD_LINE_WIDTH / 2),
                    GuiConst.ROW_WIDTH / 2)
                end_point = (
                    GuiConst.COLUMN_WIDTH / 2 + GuiConst.COLUMN_WIDTH * i - math.floor(GuiConst.BOARD_LINE_WIDTH / 2),
                    GuiConst.BOARD_HEIGHT - GuiConst.ROW_WIDTH / 2)
                pygame.draw.line(self, GuiConst.BLACK, start_point, end_point, GuiConst.BOARD_LINE_WIDTH)
                continue

            start_point = (
                GuiConst.COLUMN_WIDTH / 2 + GuiConst.COLUMN_WIDTH * i - math.floor(GuiConst.BOARD_LINE_WIDTH / 2),
                GuiConst.ROW_WIDTH / 2)
            end_point = (
                GuiConst.COLUMN_WIDTH / 2 + GuiConst.COLUMN_WIDTH * i - math.floor(GuiConst.BOARD_LINE_WIDTH / 2),
                GuiConst.ROW_WIDTH / 2 + GuiConst.ROW_WIDTH * 4)
            pygame.draw.line(self, GuiConst.BLACK, start_point, end_point, GuiConst.BOARD_LINE_WIDTH)

            start_point = (
                GuiConst.COLUMN_WIDTH / 2 + GuiConst.COLUMN_WIDTH * i - math.floor(GuiConst.BOARD_LINE_WIDTH / 2),
                GuiConst.ROW_WIDTH / 2 + GuiConst.ROW_WIDTH * 5)
            end_point = (
                GuiConst.COLUMN_WIDTH / 2 + GuiConst.COLUMN_WIDTH * i - math.floor(GuiConst.BOARD_LINE_WIDTH / 2),
                GuiConst.BOARD_HEIGHT - GuiConst.ROW_WIDTH / 2)
            pygame.draw.line(self, GuiConst.BLACK, start_point, end_point, GuiConst.BOARD_LINE_WIDTH)

        # draw horizontal lines
        for i in range(GuiConst.BOARD_DIMENSION[1]):
            start_point = (
                GuiConst.COLUMN_WIDTH / 2,
                GuiConst.ROW_WIDTH / 2 + GuiConst.ROW_WIDTH * i - math.floor(GuiConst.BOARD_LINE_WIDTH / 2))
            end_point = (GuiConst.BOARD_WIDTH - GuiConst.COLUMN_WIDTH / 2,
                         GuiConst.ROW_WIDTH / 2 + GuiConst.ROW_WIDTH * i - math.floor(GuiConst.BOARD_LINE_WIDTH / 2))
            pygame.draw.line(self, GuiConst.BLACK, start_point, end_point, GuiConst.BOARD_LINE_WIDTH)

        # draw diagonal line
        start_point = (GuiConst.BOARD_WIDTH / 2 - GuiConst.COLUMN_WIDTH - math.floor(GuiConst.BOARD_LINE_WIDTH / 2),
                       GuiConst.ROW_WIDTH / 2 - math.floor(GuiConst.BOARD_LINE_WIDTH / 2))
        end_point = (GuiConst.BOARD_WIDTH / 2 + GuiConst.COLUMN_WIDTH - math.floor(GuiConst.BOARD_LINE_WIDTH / 2),
                     GuiConst.ROW_WIDTH / 2 + GuiConst.ROW_WIDTH * 2 - math.floor(GuiConst.BOARD_LINE_WIDTH / 2))
        pygame.draw.line(self, GuiConst.BLACK, start_point, end_point, GuiConst.BOARD_LINE_WIDTH)

        start_point = (
            GuiConst.BOARD_WIDTH / 2 - GuiConst.COLUMN_WIDTH - math.floor(GuiConst.BOARD_LINE_WIDTH / 2),
            GuiConst.ROW_WIDTH / 2 + GuiConst.ROW_WIDTH * 2 - math.floor(GuiConst.BOARD_LINE_WIDTH / 2))
        end_point = (GuiConst.BOARD_WIDTH / 2 + GuiConst.COLUMN_WIDTH - math.floor(GuiConst.BOARD_LINE_WIDTH / 2),
                     GuiConst.ROW_WIDTH / 2 - math.floor(GuiConst.BOARD_LINE_WIDTH / 2))
        pygame.draw.line(self, GuiConst.BLACK, start_point, end_point, GuiConst.BOARD_LINE_WIDTH)

        end_point = (
            GuiConst.BOARD_WIDTH / 2 - GuiConst.COLUMN_WIDTH - math.floor(GuiConst.BOARD_LINE_WIDTH / 2),
            GuiConst.BOARD_HEIGHT - GuiConst.ROW_WIDTH / 2 - math.floor(GuiConst.BOARD_LINE_WIDTH / 2))
        start_point = (GuiConst.BOARD_WIDTH / 2 + GuiConst.COLUMN_WIDTH - math.floor(GuiConst.BOARD_LINE_WIDTH / 2),
                       GuiConst.BOARD_HEIGHT - GuiConst.ROW_WIDTH * 2.5 - math.floor(GuiConst.BOARD_LINE_WIDTH / 2))
        pygame.draw.line(self, GuiConst.BLACK, start_point, end_point, GuiConst.BOARD_LINE_WIDTH)

        start_point = (
            GuiConst.BOARD_WIDTH / 2 - GuiConst.COLUMN_WIDTH - math.floor(GuiConst.BOARD_LINE_WIDTH / 2),
            GuiConst.BOARD_HEIGHT - GuiConst.ROW_WIDTH * 2.5 - math.floor(GuiConst.BOARD_LINE_WIDTH / 2))
        end_point = (GuiConst.BOARD_WIDTH / 2 + GuiConst.COLUMN_WIDTH - math.floor(GuiConst.BOARD_LINE_WIDTH / 2),
                     GuiConst.BOARD_HEIGHT - GuiConst.ROW_WIDTH / 2 - math.floor(GuiConst.BOARD_LINE_WIDTH / 2))
        pygame.draw.line(self, GuiConst.BLACK, start_point, end_point, GuiConst.BOARD_LINE_WIDTH)

    # draw recommend pieces
    def draw_recommend(self, state):
        # make list empty
        BoardModel.get_instance().recommend_pieces.empty()
        for i in range(10):
            for j in range(9):
                if state[i][j] == 'o':
                    piece = RecommendPiece(Point(i, j))
                    BoardModel.get_instance().recommend_pieces.add(piece)

    # draw previous step of piece
    def daw_previous_step(self, position_in_state: Point):
        print(position_in_state.x, position_in_state.y)
        piece = RecommendPiece(position_in_state)
        BoardModel.get_instance().previousStep.add(piece)

    # create piece sprite
    def draw_pieces(self):
        # make piece group empty
        BoardModel.get_instance().piece_sprites.empty()
        state = BoardModel.get_instance().state

        for i in range(10):
            for j in range(9):
                if state[i][j] in GuiConst.PIECE_NAME_LIST:
                    # create piece and add it to group
                    piece = Piece(state[i][j], Point(i, j))
                    BoardModel.get_instance().piece_sprites.add(piece)

                    # declare king
                    if state[i][j] == PIECE_NAME_LIST[0]:
                        BoardModel.get_instance().black_king_sprite = piece
                    elif state[i][j] == PIECE_NAME_LIST[7]:
                        BoardModel.get_instance().red_king_sprite = piece

    def draw_input_fen_text(self, input_fen):
        """
        this method to draw input FEN
        :param input_fen:
        :return:
        """
        font = pygame.font.SysFont("comicsansms", int(TEXT_WIDTH))
        font.render(input_fen, True, (100, 140, 100))
    # draw if is check
    def draw_is_check(self):
        BoardModel.get_instance().is_check.add(IsCheck())

    # draw if is check
    def draw_is_mate(self):
        BoardModel.get_instance().is_mate.add(IsMate())
    # update logic
    def update(self):
        BoardModel.get_instance().piece_sprites.update()
        BoardModel.get_instance().recommend_pieces.update()
        BoardModel.get_instance().previousStep.update()
        BoardModel.get_instance().is_mate.update()
        ischeck = [s for s in BoardModel.get_instance().is_check]
        ismate = [s2 for s2 in BoardModel.get_instance().is_mate]
        if ischeck and ischeck[0].index <= len(IMAGES_CHECK) - 1:
            BoardModel.get_instance().is_check.update()
            print('is check')
        else:
            BoardModel.get_instance().is_check.empty()
        if ismate and ismate[0].index <= len(IMAGES_MATE) - 1:
            BoardModel.get_instance().is_mate.update()
            print('is check')
        else:
            BoardModel.get_instance().is_mate.empty()

    # draw
    def draw(self, screen):
        # draw background
        self.blit(self.BOARD_BACKGROUND, (0, 0))
        # draw board
        self.draw_board_background()
        # draw piece

        BoardModel.get_instance().piece_sprites.draw(screen)
        # draw recommend
        BoardModel.get_instance().recommend_pieces.draw(screen)

        # draw previous step
        BoardModel.get_instance().previousStep.draw(screen)

        # draw King is Checked
        if BoardModel.get_instance().is_check:
            BoardModel.get_instance().is_check.draw(screen)
        if BoardModel.get_instance().is_mate:
            BoardModel.get_instance().is_mate.draw(screen)