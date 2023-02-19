# import sys
# from builtins import print

from Const.GuiConst import *
from Controller.Controller import Controller
from View.EBoardView import EBoardView

clock = pygame.time.Clock()

# set title
pygame.display.set_caption('Co Tuong Program')

# create surface
screen = pygame.display.set_mode((int(BOARD_WIDTH +ELECTRONIC_BOARD_WIDTH), WINDOW_HEIGHT))

controller = Controller()


def main():

    # block of code in while loop will do FPS times per second
    while True:
        # get event
        controller.handle_event()

        # update logic
        controller.update()

        # render in graphic card
        controller.draw(screen)

        # render in computer screen
        pygame.display.update()

        clock.tick(FPS)

if __name__ == '__main__':
    main()
