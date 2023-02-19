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

        # this variable = True, this is turn of upper side
        self.isUpperTurn = True

        # if one side win, this variable have value = True
        self.gameIsNotOver = True

        # this variable store mode of game, default is PvsP mode
        self.mode = MODE[0]

        # button is clicked
        self.button = None

        # state of program
        self.state = STATE_PROGRAM[0]

    """ this function will reset all attribute to default value"""
    def reset_attributes_to_new_game(self):
        self.isUpperTurn = True
        self.gameIsNotOver = True
        # self.mode = MODE[1]

    def toggle_player(self):
        self.isUpperTurn = not self.isUpperTurn
