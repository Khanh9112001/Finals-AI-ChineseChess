import pygame


class EBoardModel:
    __instance = None

    def __init__(self):
        if EBoardModel.__instance is None:
            EBoardModel.__instance = self
        else:
            raise Exception("this class is a singleton class")

        # chinese chess images
        self.pieces = pygame.sprite.Group()

        # button
        self.button_group = pygame.sprite.Group()

    @staticmethod
    def get_instance():
        if EBoardModel.__instance is None:
            EBoardModel()

        return EBoardModel.__instance
