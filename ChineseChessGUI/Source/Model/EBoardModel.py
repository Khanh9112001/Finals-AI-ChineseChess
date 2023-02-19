import pygame

class EBoardModel:
    __instance = None

    def __init__(self):
        if EBoardModel.__instance is None:
            EBoardModel.__instance = self
        else:
            raise Exception("this class is a singleton class")

        # # progress bar
        # self.progress_bar1 = None
        # self.progress_bar2 = None

        # # clock timer
        # self.timer1 = None
        # self.timer2 = None

        # button
        self.button_group = pygame.sprite.Group()

        # chinese chess images
        self.pieces = pygame.sprite.Group()

        # button
        self.button_arrange = pygame.sprite.Group()

    @staticmethod
    def get_instance():
        if EBoardModel.__instance is None:
            EBoardModel()

        return EBoardModel.__instance


