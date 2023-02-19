import pygame
"""this class contain functions which play music for game"""


class Sound:

    """call this method when chess is moved to another location"""
    @staticmethod
    def chessMoveSound():
        effect = pygame.mixer.Sound('Asset/Sounds/move_piece.wav')
        effect.play()


