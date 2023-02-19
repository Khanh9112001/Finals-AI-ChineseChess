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

        # previousStep
        self.previousStep = pygame.sprite.Group()

        self.black_king_sprite = None
        self.red_king_sprite = None

        self.move = None

        # is check
        self.is_check = pygame.sprite.Group()

        #is mate
        self.is_mate = pygame.sprite.Group()

        #number of Step Red
        self.number_step_red = 0

        # number of Step Red
        self.number_step_black = 0

        #number of ply
        self.plydepth = DEFAULT_PLY_DEPTH

        #type piece
        self.typepiece = 'Chinese Piece'

        #who fist?
        self.whofist = 'Person'

        #images
        self.images = IMAGES_PERSON_FIRST[0]

        #color
        self.top_color = COLOR[0]

    @staticmethod
    def get_instance():
        if BoardModel.__instance is None:
            BoardModel()

        return BoardModel.__instance
