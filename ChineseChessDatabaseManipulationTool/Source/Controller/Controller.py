import sys

from Controller.BoardController import BoardController
from Controller.EBoardController import EBoardController
from Model.GameInfo import *
from Utils.StateUtil import *
from View.BoardView import BoardView
from View.EBoardView import EBoardView


class Controller:
    def __init__(self):
        BoardView()
        EBoardView()
        GameInfo()
        StateUtil.get_instance()

    def handle_event(self):
        """
        this method will be called each frame to handle event from user
        :return:
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            # event mouse click
            elif event.type == pygame.MOUSEBUTTONUP:
                # get mouse position
                mouse_position = Point(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

                # board handle event
                BoardController.get_instance().handle_mouse_click(mouse_position)
                # eboard handle event
                EBoardController.get_instance().handle_mouse_click(mouse_position)

    """"update logic in each frame"""

    def update(self):
        BoardView.get_instance().update()
        EBoardView.get_instance().update()

    """"this method draw into computer graphic card"""

    def draw(self, screen):

        screen.blit(BoardView.get_instance(), (0, 0))
        screen.blit(EBoardView.get_instance(), (BOARD_WIDTH, 0))

        BoardView.get_instance().draw(screen)
        EBoardView.get_instance().draw(screen)
