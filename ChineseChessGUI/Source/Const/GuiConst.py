import os

import math
import pygame

# import class
from Utils.Point import Point

pygame.init()

# color const
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ELECTRONIC_BACKGROUND_COLOR = (237, 225, 185)
FCAF3E = (252, 175, 62)
CE5C00 = (206, 92, 0)

FPS = 60

infoObject = pygame.display.Info()
SCREEN_WIDTH = infoObject.current_w
SCREEN_HEIGHT = infoObject.current_h

# game size
WINDOW_HEIGHT = SCREEN_HEIGHT - 50
WINDOW_WIDTH = WINDOW_HEIGHT + math.floor(2 * WINDOW_HEIGHT / 10)
PLY_DEPTH = 4
# board const
BOARD_HEIGHT = WINDOW_HEIGHT
BOARD_WIDTH = (WINDOW_HEIGHT / 10) * 9

BOARD_DIMENSION = (9, 10)

COLUMN_WIDTH = BOARD_WIDTH / 9
ROW_WIDTH = BOARD_HEIGHT / 10

BOARD_LINE_WIDTH = 2

DEFAULT_PLY_DEPTH = 4

# # piece
# PIECE_SIZE = (math.floor(COLUMN_WIDTH * 0.8), math.floor(ROW_WIDTH * 0.8))

PIECE_SIZE = (math.floor(COLUMN_WIDTH*1), math.floor(COLUMN_WIDTH*1))

#check side
CHECK_SIZE_IMAGE = (math.floor(COLUMN_WIDTH * 4), math.floor(ROW_WIDTH * 4))

# Recommendation Piece
RECOMMEND_PIECE_SIZE = (math.floor(COLUMN_WIDTH*0.8), math.floor(COLUMN_WIDTH*0.8))
# piece name list
PIECE_NAME_LIST = ("k", "a", "e", "h", "r", "c", "p",
                   "K", "A", "E", "H", "R", "C", "P")

DELETE_BUTTON = "DELETE"
RESET_BUTTON = "BACK"
PLAY_BUTTON = "PLAY"
RED_PIECES = ["k", "a", "e", "h", "r", "c", "p", PLAY_BUTTON]
BLACK_PIECES = ["K", "A", "E", "H", "R", "C", "P", DELETE_BUTTON]
# INIT_BOARD
INIT_STATE = [
    ['r', 'h', 'e', 'a', 'k', 'a', 'e', 'h', 'r'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', 'c', '.', '.', '.', '.', '.', 'c', '.'],
    ['p', '.', 'p', '.', 'p', '.', 'p', '.', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],

    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', '.', 'P', '.', 'P', '.', 'P', '.', 'P'],
    ['.', 'C', '.', '.', '.', '.', '.', 'C', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['R', 'H', 'E', 'A', 'K', 'A', 'E', 'H', 'R'],
]

# INIT_STATE = [
#     ['R', 'H', 'E', 'A', 'K', 'A', 'E', 'H', 'R'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', 'C', '.', '.', '.', '.', '.', 'C', '.'],
#     ['P', '.', 'P', '.', 'P', '.', 'P', '.', 'P'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['p', '.', 'p', '.', 'p', '.', 'p', '.', 'p'],
#     ['.', 'c', '.', '.', '.', '.', '.', 'c', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['r', 'h', 'e', 'a', 'k', 'a', 'e', 'h', 'r'],
# ]

# INIT_STATE = [
#   ['.', 'R', '.', 'a', 'k', 'a', 'e', '.', '.'],
#   ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#   ['.', '.', '.', 'P', 'e', '.', '.', '.', '.'],
#   ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#   ['.', '.', '.', '.', '.', '.', 'p', '.', 'p'],
#   ['.', '.', '.', 'p', '.', '.', '.', '.', '.'],
#   ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#   ['.', '.', '.', '.', 'h', 'A', '.', '.', '.'],
#   ['.', '.', '.', 'r', 'A', '.', '.', '.', '.'],
#   ['.', '.', 'E', '.', 'K', '.', '.', '.', '.'],
#   ]
# INIT_STATE = [
#   ['.', '.', '.', '.', 'k', '.', '.', '.', '.'],
#   ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#   ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#   ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#   ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#   ['.', '.', '.', '.', '.', '.', '.', '.', 'P'],
#   ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#   ['.', '.', '.', '.', '.', 'p', '.', 'c', '.'],
#   ['.', '.', '.', '.', 'p', '.', '.', '.', '.'],
#   ['.', '.', '.', '.', '.', 'K', '.', '.', '.'],
#   ]
# POSITION OF PIECE TO DRAW IN SCREEN
BOARD_POSITION = list()
for i in range(10):
    BOARD_POSITION.append(list())
    for j in range(9):
        position = Point(COLUMN_WIDTH / 2 + COLUMN_WIDTH * j,
                         ROW_WIDTH / 2 + ROW_WIDTH * i)
        BOARD_POSITION[i].append(position)

# electronic board
ELECTRONIC_BOARD_WIDTH = (WINDOW_WIDTH - BOARD_WIDTH)/2
ELECTRONIC_BOARD_HEIGHT = WINDOW_HEIGHT

# gap
CONTROL_SECTION_WIDTH = ELECTRONIC_BOARD_WIDTH
CONTROL_SECTION_HEIGHT = 3 * ROW_WIDTH

# information section
INFORMATION_SECTION_WIDTH = ELECTRONIC_BOARD_WIDTH
INFORMATION_SECTION_HEIGHT = (ELECTRONIC_BOARD_HEIGHT - CONTROL_SECTION_HEIGHT) / 2

# progress bar
PROGRESS_BAR_WIDTH = INFORMATION_SECTION_WIDTH / 4
PROGRESS_BAR_HEIGHT = 3 * ROW_WIDTH

# button
BUTTON_SIZE = (int(ELECTRONIC_BOARD_WIDTH / 2), int(ELECTRONIC_BOARD_WIDTH / 2))

# button name list
# button name list
BUTTON_TYPE_LIST = ('undo', 'mode', 'reset', 'setting')

MODE = ['AIvsP', 'PvsP']
COLOR = ['red', 'black']

RESOURCE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Asset'))

ABS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Asset/Button'))

UNDO_BUTTON = pygame.transform.smoothscale(pygame.image.load(ABS_PATH + "/undoBtn.png"), BUTTON_SIZE)

MODE_BUTTON = (pygame.transform.smoothscale(pygame.image.load(ABS_PATH + "/mode1.png"), BUTTON_SIZE),
               pygame.transform.smoothscale(pygame.image.load(ABS_PATH + "/mode2.png"), BUTTON_SIZE))

RESET_BUTTON = pygame.transform.smoothscale(pygame.image.load(ABS_PATH + "/reset.png"), BUTTON_SIZE)

SETTING_BUTTON = pygame.transform.smoothscale(pygame.image.load(ABS_PATH + "/setting.png"), BUTTON_SIZE)


KING_RED_DIED = pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/rkm.png"),PIECE_SIZE)
KING_BLACK_DIED = pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/bkm.png"),PIECE_SIZE)

#text_width
TEXT_WIDTH = ROW_WIDTH/5
RECOMMEND = 'o'
EMPTY = '.'
# INIT_BOARD ARRANGE
RECOMMEND_STATE = [
    [RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND],
    [RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND],
    [RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND],
    [RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND],
    [RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND],

    [RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND],
    [RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND],
    [RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND],
    [RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND],
    [RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND, RECOMMEND],
]
INIT_STATE_ARRANGE = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
]
STATE_PROGRAM = ['init_board', 'play']


# IMAGES_PIECE = IMAGES_PIECE1
IMAGES_PIECE_TYPE = [
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/rk.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/ra.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/rb.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/rn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/rr.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/rc.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/rp.png"), PIECE_SIZE),

    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/bk.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/ba.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/bb.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/bn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/br.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/bc.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/bp.png"), PIECE_SIZE),
]

#person first
IMAGES_PERSON_FIRST = [[
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/rk.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/ra.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/rb.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/rn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/rr.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/rc.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/rp.png"), PIECE_SIZE),

    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/bk.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/ba.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/bb.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/bn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/br.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/bc.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/bp.png"), PIECE_SIZE),


],[
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/rk.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/ra.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/rb.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/rn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/rr.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/rc.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/rp.png"), PIECE_SIZE),

    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/bk.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/ba.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/bb.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/bn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/br.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/bc.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/bp.png"), PIECE_SIZE),
],[
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/rk.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/ra.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/rb.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/rn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/rr.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/rc.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/rp.png"), PIECE_SIZE),

    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/bk.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/ba.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/bb.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/bn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/br.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/bc.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/bp.png"), PIECE_SIZE),


]]
#AI first
IMAGES_AI_FIRST = [[
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/bk.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/ba.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/bb.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/bn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/br.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/bc.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/bp.png"), PIECE_SIZE),

    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/rk.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/ra.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/rb.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/rn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/rr.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/rc.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/rp.png"), PIECE_SIZE),
],[
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/bk.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/ba.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/bb.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/bn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/br.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/bc.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/bp.png"), PIECE_SIZE),

    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/rk.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/ra.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/rb.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/rn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/rr.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/rc.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Eng/rp.png"), PIECE_SIZE),
],[
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/bk.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/ba.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/bb.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/bn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/br.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/bc.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/bp.png"), PIECE_SIZE),

    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/rk.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/ra.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/rb.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/rn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/rr.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/rc.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/pieces/Figure/rp.png"), PIECE_SIZE),

]]

