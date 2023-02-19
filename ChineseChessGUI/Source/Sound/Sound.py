import pygame

"""this class contain functions which play music for game"""


class Sound:
    __instance = None
    def __init__(self):
        if self.__instance is None:
            Sound.__instance = self
        self.is_turn_on_move = True
    """call this method when chess is moved to another location"""

    @staticmethod
    def get_instance():
        if Sound.__instance is None:
            Sound()
        return Sound.__instance

    def chessMoveSound(self):
        if self.is_turn_on_move:
            effect = pygame.mixer.Sound('Asset/Sounds/move_piece.wav')
            effect.play()
        else:
            pass
    @staticmethod
    def reset_board():
        effect = pygame.mixer.Sound('Asset/Sounds/reset_board.wav')
        effect.play()
