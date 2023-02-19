import pygame
from Const.const import *


class Validator:
    __instance = None

    def __init__(self):
        if Validator.__instance is None:
            Validator.__instance = self
        else:
            raise Exception("this class is a singleton class")

    @staticmethod
    def get_instance():
        if Validator.__instance is None:
            Validator()
        return Validator.__instance

    @staticmethod
    def checkKingOpposite(state, i, j, lowercase=True):
        if lowercase:
            for k in range(i + 1, 10):
                if state[k][j] == 'K':
                    return True
                elif state[k][j] != '.' or k == 9:
                    return False
        else:
            for k in range(i - 1, -1, -1):
                if state[k][j] == 'K':
                    return True
                elif state[k][j] != '.' or k == 0:
                    return False

    @staticmethod
    def Valide_state(state):
        blackKing_position = 0  # =0 have not appear King,=1 Black on Top,=2 Black on Bottom
        blackAdvisor_position = 0  # =0 have not appear Avisor,=1 Black on Top,=2 Black on Bottom
        blackElephant_position = 0  # =0 have not appear Elephant,=1 Black on Top,=2 Black on Bottom
        count_King = 0
        count_BlackAdvisor = 0
        count_RedAdvisor = 0
        count_BlackElephant = 0
        count_RedElephant = 0
        count_BlackRook = 0
        count_RedRook = 0
        count_BlackCannon = 0
        count_RedCannon = 0
        count_BlackHorse = 0
        count_RedHorse = 0
        count_BlackPawn = 0
        count_RedPawn = 0
        for i in range(ROW):
            for j in range(COLUMN):
                if state[i][j] == 'r':
                    if count_BlackRook == 2:
                        return False
                    else:
                        count_BlackRook += 1
                elif state[i][j] == 'R':
                    if count_RedRook == 2:
                        return False
                    else:
                        count_RedRook += 1
                elif state[i][j] == 'c':
                    if count_BlackCannon == 2:
                        return False
                    else:
                        count_BlackCannon += 1
                elif state[i][j] == 'C':
                    if count_RedCannon == 2:
                        return False
                    else:
                        count_RedCannon += 1
                elif state[i][j] == 'h':
                    if count_BlackHorse == 2:
                        return False
                    else:
                        count_BlackHorse += 1
                elif state[i][j] == 'H':
                    if count_RedHorse == 2:
                        return False
                    else:
                        count_RedHorse += 1
                elif state[i][j] == 'k':
                    if count_King == 2:
                        return False
                    else:
                        count_King += 1
                    if i < 3:
                        if blackAdvisor_position == 2 or blackElephant_position == 2 \
                                or blackKing_position == 2:
                            return False
                        blackKing_position = 1  # King black on Top Board
                        if j < 3 or j > 5:
                            return False
                        elif Validator.checkKingOpposite(state, i, j, True):
                            return False
                    elif i > 6:
                        if blackAdvisor_position == 1 or blackElephant_position == 1 \
                                or blackKing_position == 1:
                            return False
                        blackKing_position = 2
                        if j < 3 or j > 5:
                            return False
                        elif Validator.checkKingOpposite(state, i, j, False):
                            return False
                    else:
                        return False
                elif state[i][j] == 'K':
                    if count_King == 2:
                        return False
                    else:
                        count_King += 1
                    if i < 3:
                        if blackAdvisor_position == 1 or blackElephant_position == 1 \
                                or blackKing_position == 1:
                            return False
                        blackKing_position = 2
                        if j < 3 or j > 5:
                            return False
                    elif i > 6:
                        if blackAdvisor_position == 2 or blackElephant_position == 2 \
                                or blackKing_position == 2:
                            return False
                        blackKing_position = 1
                        if j < 3 or j > 5:
                            return False
                    else:
                        return False
                elif state[i][j] == 'a':
                    if count_BlackAdvisor == 2:
                        return False
                    else:
                        count_BlackAdvisor += 1
                    if i < 3:
                        if blackKing_position == 2:
                            return False
                        blackAdvisor_position = 1
                        if i > 2 or (i == 1 and j != 4) or (i == 2 and j == 4) or j < 3 or j > 5 \
                                or (i == 0 and j == 4):
                            return False
                    else:
                        if blackKing_position == 1:
                            return False
                        blackAdvisor_position = 2
                        if i < 7 or (i == 8 and j != 4) or (i == 7 and j == 4) or j < 3 or j > 5 \
                                or (i == 9 and j == 4):
                            return False
                elif state[i][j] == 'A':
                    if count_RedAdvisor == 2:
                        return False
                    else:
                        count_RedAdvisor += 1
                    if i < 3:
                        if blackKing_position == 1:
                            return False
                        blackAdvisor_position = 2
                        if i > 2 or (i == 1 and j != 4) or (i == 2 and j == 4) or j < 3 or j > 5 \
                                or (i == 0 and j == 4):
                            return False
                    else:
                        if blackKing_position == 2:
                            return False
                        blackAdvisor_position = 1
                        if i < 7 or (i == 8 and j != 4) or (i == 7 and j == 4) or j < 3 or j > 5 \
                                or (i == 9 and j == 4):
                            return False
                elif state[i][j] == 'e':
                    if count_BlackElephant == 2:
                        return False
                    else:
                        count_BlackElephant += 1
                    if (i < 5):
                        if blackKing_position == 2:
                            return False
                        if i == 1 or i == 3:
                            return False
                        elif (i == 0 or i == 4) and j != 2 and j != 6:
                            return False
                        elif i == 2 and j != 0 and j != 4 and j != 8:
                            return False
                        blackElephant_position = 1
                    elif i > 4:
                        if blackKing_position == 1:
                            return False
                        elif i == 8 or i == 6:
                            return False
                        elif (i == 9 or i == 5) and j != 2 and j != 6:
                            return False
                        elif i == 7 and j != 0 and j != 4 and j != 8:
                            return False
                        blackElephant_position = 2
                elif state[i][j] == 'E':
                    if count_RedElephant == 2:
                        return False
                    else:
                        count_RedElephant += 1
                    if i < 5:
                        if blackKing_position == 1:
                            return False
                        if i == 1 or i == 3:
                            return False
                        elif (i == 0 or i == 4) and j != 2 and j != 6:
                            return False
                        elif i == 2 and j != 0 and j != 4 and j != 8:
                            return False
                        blackElephant_position = 2
                    elif i > 4:
                        if blackKing_position == 2:
                            return False
                        elif i == 8 or i == 6:
                            return False
                        elif (i == 9 or i == 5) and j != 2 and j != 6:
                            print(111)
                            return False
                        elif i == 7 and j != 0 and j != 4 and j != 8:
                            return False
                        blackElephant_position = 1
                elif blackKing_position == 1:  # King Black on top Board
                    if state[i][j] == 'p':
                        count_BlackPawn += 1
                        if i < 3:
                            return False
                        elif 3 <= i < 5 and (j == 1 or j == 3 or j == 5 or j == 7):
                            return False
                    elif state[i][j] == 'P':
                        count_RedPawn += 1
                        if i > 6:
                            return False
                        elif 6 >= i > 4 and (j == 1 or j == 3 or j == 5 or j == 7):
                            return False
                elif blackKing_position == 2:
                    if state[i][j] == 'P':
                        count_RedPawn += 1
                        if i < 3:
                            return False
                        elif 3 <= i < 5 and (j == 1 or j == 3 or j == 5 or j == 7):
                            return False
                    elif state[i][j] == 'p':
                        count_BlackPawn += 1
                        if i > 6:
                            return False
                        elif 6 >= i > 4 and (j == 1 or j == 3 or j == 5 or j == 7):
                            return False
        if count_King < 2:
            print(1111)
            return False
        else:
            return True
