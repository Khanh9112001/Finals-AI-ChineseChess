from Const.GuiConst import *


class GameInfo:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if GameInfo.__instance is None:
            GameInfo()
        return GameInfo.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if GameInfo.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GameInfo.__instance = self

        self.LowerSideMoveFirst = True
        # this variable = True, this is turn of upper side
        self.isUpperTurn = self.LowerSideMoveFirst

        # if one side win, this variable have value = True
        self.gameIsNotOver = True

        # this variable store mode of game, default is PvsP mode
        self.mode = MODE[0]

        # # button is clicked
        self.button_arrange = None

        # state of program
        self.state = STATE_PROGRAM[1]

    """ this function will reset all attribute to default value"""
    def reset_attributes_to_new_game(self):
        self.isUpperTurn = self.LowerSideMoveFirst
        self.gameIsNotOver = True
        # self.mode = MODE[1]

    def toggle_player(self):
        self.isUpperTurn = not self.isUpperTurn
