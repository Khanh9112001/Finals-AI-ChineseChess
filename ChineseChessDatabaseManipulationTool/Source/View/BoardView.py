# library
from builtins import *

# class
from Const.GuiConst import *
from Model.BoardModel import BoardModel
from Sprite.RecommendPiece import RecommendPiece
from Utils.StateUtil import *
from Sprite.Button import Button

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

        super(BoardView, self).__init__((BOARD_WIDTH, BOARD_HEIGHT))

        # draw color background
        self.BOARD_BACKGROUND = pygame.transform.smoothscale(
            pygame.image.load(RESOURCE_PATH + "/images/background.png"), (WINDOW_HEIGHT, WINDOW_HEIGHT))

        # draw board background
        self.draw_board_background()

        # init images
        self.draw_pieces()

        # init recommend
        self.draw_recommend(RECOMMEND_STATE)

        # draw input FEN
        self.input_fen_obj = None
        self.draw_input_fen_text("")

        # draw out FEN
        self.output_fen_obj = None
        self.draw_output_fen_text("")

    # Draw background of chinese chess board
    def draw_board_background(self):
        # draw vertical lines
        for i in range(BOARD_DIMENSION[0]):
            if i == 0 or i == 8:
                start_point = (
                    COLUMN_WIDTH  + COLUMN_WIDTH * i - math.floor(BOARD_LINE_WIDTH / 2),
                    ROW_WIDTH)
                end_point = (
                    COLUMN_WIDTH + COLUMN_WIDTH * i - math.floor(BOARD_LINE_WIDTH / 2),
                    BOARD_HEIGHT - ROW_WIDTH)
                pygame.draw.line(self, BLACK, start_point, end_point, BOARD_LINE_WIDTH)
                continue

            start_point = (
                COLUMN_WIDTH  + COLUMN_WIDTH * i - math.floor(BOARD_LINE_WIDTH / 2),
                ROW_WIDTH)
            end_point = (
                COLUMN_WIDTH + COLUMN_WIDTH * i - math.floor(BOARD_LINE_WIDTH / 2),
                ROW_WIDTH + ROW_WIDTH * 4)
            pygame.draw.line(self, BLACK, start_point, end_point, BOARD_LINE_WIDTH)

            start_point = (
                COLUMN_WIDTH + COLUMN_WIDTH * i - math.floor(BOARD_LINE_WIDTH / 2),
                ROW_WIDTH + ROW_WIDTH * 5)
            end_point = (
                COLUMN_WIDTH + COLUMN_WIDTH * i - math.floor(BOARD_LINE_WIDTH / 2),
                BOARD_HEIGHT - ROW_WIDTH)
            pygame.draw.line(self, BLACK, start_point, end_point, BOARD_LINE_WIDTH)

        # draw horizontal lines
        for i in range(BOARD_DIMENSION[1]):
            start_point = (
                COLUMN_WIDTH,
                ROW_WIDTH + ROW_WIDTH * i - math.floor(BOARD_LINE_WIDTH / 2))
            end_point = (BOARD_WIDTH - COLUMN_WIDTH,
                         ROW_WIDTH + ROW_WIDTH * i - math.floor(BOARD_LINE_WIDTH / 2))
            pygame.draw.line(self, BLACK, start_point, end_point, BOARD_LINE_WIDTH)

        # draw diagonal line
        start_point = (BOARD_WIDTH / 2 - COLUMN_WIDTH - math.floor(BOARD_LINE_WIDTH / 2),
                       ROW_WIDTH - math.floor(BOARD_LINE_WIDTH / 2))
        end_point = (BOARD_WIDTH / 2 + COLUMN_WIDTH - math.floor(BOARD_LINE_WIDTH / 2),
                     ROW_WIDTH + ROW_WIDTH * 2 - math.floor(BOARD_LINE_WIDTH / 2))
        pygame.draw.line(self, BLACK, start_point, end_point, BOARD_LINE_WIDTH)

        end_point = (BOARD_WIDTH / 2 + COLUMN_WIDTH - math.floor(BOARD_LINE_WIDTH / 2),
                     ROW_WIDTH - math.floor(BOARD_LINE_WIDTH / 2))
        start_point = (
            BOARD_WIDTH / 2 - COLUMN_WIDTH - math.floor(BOARD_LINE_WIDTH / 2),
            ROW_WIDTH + ROW_WIDTH * 2 - math.floor(BOARD_LINE_WIDTH / 2))
        pygame.draw.line(self, BLACK, start_point, end_point, BOARD_LINE_WIDTH)

        start_point = (BOARD_WIDTH / 2 + COLUMN_WIDTH - math.floor(BOARD_LINE_WIDTH / 2),
                       BOARD_HEIGHT - ROW_WIDTH * 3 - math.floor(BOARD_LINE_WIDTH / 2))
        end_point = (
            BOARD_WIDTH / 2 - COLUMN_WIDTH - math.floor(BOARD_LINE_WIDTH / 2),
            BOARD_HEIGHT - ROW_WIDTH - math.floor(BOARD_LINE_WIDTH / 2))
        pygame.draw.line(self, BLACK, start_point, end_point, BOARD_LINE_WIDTH)

        start_point = (
            BOARD_WIDTH / 2 - COLUMN_WIDTH - math.floor(BOARD_LINE_WIDTH / 2),
            BOARD_HEIGHT - ROW_WIDTH * 3 - math.floor(BOARD_LINE_WIDTH / 2))
        end_point = (BOARD_WIDTH / 2 + COLUMN_WIDTH - math.floor(BOARD_LINE_WIDTH / 2),
                     BOARD_HEIGHT - ROW_WIDTH - math.floor(BOARD_LINE_WIDTH / 2))
        pygame.draw.line(self, BLACK, start_point, end_point, BOARD_LINE_WIDTH)

    # draw recommend images
    def draw_recommend(self, state):
        # make list empty
        BoardModel.get_instance().recommend_pieces.empty()
        for i in range(10):
            for j in range(9):
                if state[i][j] == RECOMMEND:
                    piece = RecommendPiece(Point(i, j))
                    BoardModel.get_instance().recommend_pieces.add(piece)

    # create piece sprite
    def draw_pieces(self):
        # make piece group empty
        BoardModel.get_instance().piece_sprites.empty()
        state = BoardModel.get_instance().state

        for i in range(10):
            for j in range(9):
                if state[i][j] in PIECE_NAME_LIST:
                    # create piece and add it to group
                    piece = Button(state[i][j],BOARD_POSITION[i][j] , PIECE_SIZE, state[i][j].islower(), Point(i,j))
                    BoardModel.get_instance().piece_sprites.add(piece)

    # Show Red/Black win
    def draw_game_over(self, win):
        font = pygame.font.SysFont("comicsansms", int(ROW_WIDTH))

        text = font.render(win, True, (0, 140, 0))
        self.blit(text, (BOARD_WIDTH / 4, BOARD_HEIGHT / 2 - text.get_height() / 2))

    def draw_input_fen_text(self, input_fen):
        """
        this method to draw input FEN
        :param input_fen:
        :return:
        """
        BoardModel.get_instance().input_fen = input_fen
        font = pygame.font.SysFont("comicsansms", int(TEXT_WIDTH))

        self.input_fen_obj = font.render("Input FEN: " + input_fen, True, (0, 140, 0))

    def draw_output_fen_text(self, output_fen):
        """
        this method to draw input FEN
        :param output_fen:
        :return:
        """
        BoardModel.get_instance().output_fen = output_fen
        font = pygame.font.SysFont("comicsansms", int(TEXT_WIDTH))

        self.output_fen_obj = font.render("Output FEN: " + output_fen, True, (0, 140, 0))

    # update logic
    def update(self):
        BoardModel.get_instance().piece_sprites.update()
        BoardModel.get_instance().recommend_pieces.update()

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

        # draw input FEN
        self.blit(self.input_fen_obj, (0, 0))

        # draw output FEN
        self.blit(self.output_fen_obj, (0, TEXT_WIDTH))
