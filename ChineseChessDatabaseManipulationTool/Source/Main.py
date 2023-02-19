# import sys
# from builtins import print

from Const.GuiConst import *
from Controller.Controller import Controller

clock = pygame.time.Clock()

# set title
pygame.display.set_caption('Chinese Chess Database Manipulation Tool')

# create surface
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

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


main()
