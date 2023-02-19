import copy

from Const.GuiConst import *


class BoardModel:
    __instance = None

    def __init__(self):
        if BoardModel.__instance is None:
            BoardModel.__instance = self
        else:
            raise Exception("this class is a singleton class")

        # init piece group
        self.piece_sprites = pygame.sprite.Group()

        # init recommend piece
        self.recommend_pieces = pygame.sprite.Group()

        # previous click piece
        self.clicked_piece = None

        # this variable: list of state
        # purpose: to store  history of state
        self.previousStates = []

        # this variable to store current state
        self.state = copy.deepcopy(INIT_STATE)

        # input fen
        self.input_fen = None

        # output fen
        self.output_fen = None

        self.move = None

    @staticmethod
    def get_instance():
        if BoardModel.__instance is None:
            BoardModel()

        return BoardModel.__instance
