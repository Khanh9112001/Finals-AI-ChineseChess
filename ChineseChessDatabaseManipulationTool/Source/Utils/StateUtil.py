import copy

from Const.GuiConst import *


class StateUtil:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if StateUtil.__instance is None:
            StateUtil()
        return StateUtil.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if StateUtil.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            StateUtil.__instance = self

    """
        RECOMMENDATION OF PIECE
        @:param
            state:matrix
            i,j:position of piece
        @:return: a matrix with recommendation correspond Piece
    """

    def generate_recommend_piece(self, state, position_in_state: Point):

        (i, j) = (position_in_state.x, position_in_state.y)

        if state[i][j] == 'p':
            return self.pawn_go_recommend(state, i, j, True)
        elif state[i][j] == 'P':
            return self.pawn_go_recommend(state, i, j, False)
        elif state[i][j] == 'a':
            return self.advisorGo_Recommends(state, i, j, True)
        elif state[i][j] == 'A':
            return self.advisorGo_Recommends(state, i, j, False)
        elif state[i][j] == 'k':
            return self.kingGo_Recommends(state, i, j, True)
        elif state[i][j] == 'K':
            return self.kingGo_Recommends(state, i, j, False)
        elif state[i][j] == 'r':
            return self.rookGo_Recommends(state, i, j, True)
        elif state[i][j] == 'R':
            return self.rookGo_Recommends(state, i, j, False)
        elif state[i][j] == 'c':
            return self.cannonGo_Recommeds(state, i, j, True)
        elif state[i][j] == 'C':
            return self.cannonGo_Recommeds(state, i, j, False)
        elif state[i][j] == 'e':
            return self.elephantGo_Recommends(state, i, j, True)
        elif state[i][j] == 'E':
            return self.elephantGo_Recommends(state, i, j, False)
        elif state[i][j] == 'h':
            return self.horseGo_Recommends(state, i, j, True)
        elif state[i][j] == 'H':
            return self.horseGo_Recommends(state, i, j, False)

    def generate_recommend_pieces_in_empty_square(self, state):
        """
        this method replace empty square in state by recommend piece
        :param state:
        :return:
        """
        state = copy.deepcopy(state)
        for i in range(len(state)):
            for j in range(len(state[0])):
                if state[i][j] == EMPTY:
                    state[i][j] = RECOMMEND

        return state

    # PAWN RECOMMENDATION---------------------------------------
    """
    pawnGo_Recommend: Recommends of go pawn in chessboard
    @param:
        state: matrix
        i,j: position of pawn
        lowercaseMove: true: lowercase pawn move, uppercase pawn move
    @return: a matrix with Recommendations of paw
    """

    @staticmethod
    def pawn_go_recommend(state, i, j, lowercase_move=True):
        sts = copy.deepcopy(state)

        # black
        if lowercase_move:
            if state[i][j] == 'p':
                if (i < 9) and (state[i + 1][j].islower() == False):  # black pawn go ahead
                    sts[i + 1][j] = 'o'
                if i >= 5:  # if black pawn pass river
                    if j > 0:
                        if state[i][j - 1].islower() == False:  # black pawn can go left
                            sts[i][j - 1] = 'o'
                    if j < 8:
                        if state[i][j + 1].islower() == False:  # black pawn can go right
                            sts[i][j + 1] = 'o'
        # red
        else:
            # red side
            if (state[i][j] == 'P'):
                if ((i > 0) and (state[i - 1][j].isupper() == False)):  # black pawn go ahead
                    sts[i - 1][j] = 'o'
                if (i <= 4):  # if red pawn pass river
                    if (j > 0):
                        if (state[i][j - 1].isupper() == False):  # red pawn can go left
                            sts[i][j - 1] = 'o'
                    if (j < 8):
                        if (state[i][j + 1].isupper() == False):  # red pawn can go right
                            sts[i][j + 1] = 'o'
        return sts

    # ADVISOR RECOMENDATION---------------------------------
    """
    advisorGo_Recommends func: Recommends of go advisor in chessboard
    @param:
        state: matrix
        i,j: position of Avisor
        lowercaseMove: true: lowercase pawn move, uppercase pawn move
    @return: a matrix with Recommendations of Advisor
    """

    @staticmethod
    def advisorGo_Recommends(state, i, j, lowercaseMove=True):
        sts = copy.deepcopy(state)
        # back
        if lowercaseMove:
            # blackside
            if state[i][j] == "a":
                if ((i == 0 or i == 2) and state[1][4].islower() == False):
                    sts[1][4] = 'o'
                if (i == 1):
                    if state[0][3].islower() == False:
                        sts[0][3] = 'o'
                    if state[0][5].islower() == False:
                        sts[0][5] = 'o'
                    if state[2][3].islower() == False:
                        sts[2][3] = 'o'
                    if state[2][5].islower() == False:
                        sts[2][5] = 'o'
        else:
            # redside
            if state[i][j] == "A":
                if ((i == 9 or i == 7) and state[8][4].isupper() == False):
                    sts[8][4] = 'o'
                if (i == 8):
                    if state[9][3].isupper() == False:
                        sts[9][3] = 'o'
                    if state[9][5].isupper() == False:
                        sts[9][5] = 'o'
                    if state[7][3].isupper() == False:
                        sts[7][3] = 'o'
                    if state[7][5].isupper() == False:
                        sts[7][5] = 'o'
        return sts

    # KING RECOMMENDATION-----------------------------------------------------
    """
    kingGo_Recommends: Recommends of go king in chessboard
    @param:
        state: matrix
        i,j: position of king
        lowercaseMove: true: lowercase king move, uppercase king move
    @return: a matrix with recommendations of King
    """

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
                if state[k][j] == 'k':
                    return True
                elif state[k][j] != '.' or k == 0:
                    return False

    @staticmethod
    def kingGo_Recommends(state, i, j, lowercaseMove=True):
        sts = copy.deepcopy(state)
        # back
        if lowercaseMove:
            # blackside
            if (state[i][j] == "k"):
                if (i == 0 and state[i + 1][j].islower() == False and StateUtil.checkKingOpposite(state, i + 1, j,
                                                                                                  True) == False):
                    sts[i + 1][j] = 'o'
                elif (i == 1):
                    if state[i - 1][j].islower() == False:
                        sts[i - 1][j] = 'o'
                    if state[i + 1][j].islower() == False and StateUtil.checkKingOpposite(state, i + 1, j,
                                                                                          True) == False:
                        sts[i + 1][j] = 'o'
                elif (i == 2 and state[i - 1][j].islower() == False):
                    sts[i - 1][j] = 'o'
                if (j == 3 and state[i][j + 1].islower() == False and StateUtil.checkKingOpposite(state, i, j + 1,
                                                                                                  True) == False):
                    sts[i][j + 1] = 'o'
                elif (j == 4):
                    if state[i][j - 1].islower() == False and StateUtil.checkKingOpposite(state, i, j - 1,
                                                                                          True) == False:
                        sts[i][j - 1] = 'o'
                    if state[i][j + 1].islower() == False and StateUtil.checkKingOpposite(state, i, j + 1,
                                                                                          True) == False:
                        sts[i][j + 1] = 'o'
                elif (j == 5 and state[i][j - 1].islower() == False and StateUtil.checkKingOpposite(state, i, j - 1,
                                                                                                    True) == False):
                    sts[i][j - 1] = 'o'
        # red
        else:
            # redside
            if (state[i][j] == "K"):
                if (i == 7 and state[i + 1][j].isupper() == False):
                    sts[i + 1][j] = 'o'
                elif (i == 8):
                    if state[i - 1][j].isupper() == False and StateUtil.checkKingOpposite(state, i - 1, j,
                                                                                          False) == False:
                        sts[i - 1][j] = 'o'
                    if state[i + 1][j].isupper() == False:
                        sts[i + 1][j] = 'o'
                elif (i == 9 and state[i - 1][j].isupper() == False and StateUtil.checkKingOpposite(state, i - 1, j,
                                                                                                    False) == False):
                    sts[i - 1][j] = 'o'
                if (j == 3 and state[i][j + 1].isupper() == False and StateUtil.checkKingOpposite(state, i, j + 1,
                                                                                                  False) == False):
                    sts[i][j + 1] = 'o'
                elif (j == 4):
                    if state[i][j - 1].isupper() == False and StateUtil.checkKingOpposite(state, i, j - 1,
                                                                                          False) == False:
                        sts[i][j - 1] = 'o'
                    if state[i][j + 1].isupper() == False and StateUtil.checkKingOpposite(state, i, j + 1,
                                                                                          False) == False:
                        sts[i][j + 1] = 'o'
                elif (j == 5 and state[i][j - 1].isupper() == False and StateUtil.checkKingOpposite(state, i, j - 1,
                                                                                                    False) == False):
                    sts[i][j - 1] = 'o'

        return sts

    # CANNON RECOMMENDATION--------------------------------
    """
    cannonGo_Recommends func: recommends of go canon in chessboard
    @param:
        state: matrix
        i,j: position of cannon
        lowercaseMove: true: lowercase cannon move, uppercase cannon move
    @return: a matrix with recommendations of cannon
    """

    @staticmethod
    def cannonGo_Recommeds(state, i, j, lowercaseMove=True):
        sts = copy.deepcopy(state)
        # back
        if lowercaseMove:
            # blackside
            if state[i][j] == 'c':
                m = i
                while (m - 1 >= 0):
                    if state[m - 1][j] == '.':
                        sts[m - 1][j] = 'o'
                    else:
                        k = m - 2
                        while (k > 0 and state[k][j] == '.'):
                            k = k - 1
                        if k >= 0 and state[k][j].isupper() == True:
                            sts[k][j] = 'o'
                        break
                    m = m - 1
                m = j
                while (m - 1 >= 0):
                    if state[i][m - 1] == '.':
                        sts[i][m - 1] = 'o'
                    else:
                        k = m - 2
                        while (k > 0 and state[i][k] == '.'):
                            k = k - 1
                        if k >= 0 and state[i][k].isupper() == True:
                            sts[i][k] = 'o'
                        break
                    m = m - 1
                m = j
                while (m + 1 <= 8):
                    if state[i][m + 1] == '.':
                        sts[i][m + 1] = 'o'
                    else:
                        k = m + 2
                        while (k < 8 and state[i][k] == "."):
                            k = k + 1
                        if k <= 8 and state[i][k].isupper() == True:
                            sts[i][k] = 'o'
                        break
                    m = m + 1
                m = i
                while (m + 1 <= 9):
                    if state[m + 1][j] == '.':
                        sts[m + 1][j] = 'o'
                    else:
                        k = m + 2
                        while (k < 9 and state[k][j] == "."):
                            k = k + 1
                        if k <= 9 and state[k][j].isupper() == True:
                            sts[k][j] = 'o'
                        break
                    m = m + 1
        # red cannon
        else:
            # redside
            if state[i][j] == 'C':
                m = i
                while (m - 1 >= 0):
                    if state[m - 1][j] == '.':
                        sts[m - 1][j] = 'o'
                    else:
                        k = m - 2
                        while (k > 0 and state[k][j] == '.'):
                            k = k - 1
                        if k >= 0 and state[k][j].islower() == True:
                            sts[k][j] = 'o'
                        break
                    m = m - 1
                m = j
                while (m - 1 >= 0):
                    if state[i][m - 1] == '.':
                        sts[i][m - 1] = 'o'
                    else:
                        k = m - 2
                        while (k > 0 and state[i][k] == '.'):
                            k = k - 1
                        if k >= 0 and state[i][k].islower() == True:
                            sts[i][k] = 'o'
                        break
                    m = m - 1
                m = j
                while (m + 1 <= 8):
                    if state[i][m + 1] == '.':
                        sts[i][m + 1] = 'o'
                    else:
                        k = m + 2
                        while (k < 8 and state[i][k] == "."):
                            k = k + 1
                        if k <= 8 and state[i][k].islower() == True:
                            sts[i][k] = 'o'
                        break
                    m = m + 1
                m = i
                while (m + 1 <= 9):
                    if state[m + 1][j] == '.':
                        sts[m + 1][j] = 'o'
                    else:
                        k = m + 2
                        while (k < 9 and state[k][j] == "."):
                            k = k + 1
                        if k <= 9 and state[k][j].islower() == True:
                            sts[k][j] = 'o'
                        break
                    m = m + 1
        return sts

    # ELEPHANT RECOMMENDATION-------------------------------------------------
    """
    elephantGo_Recommends: Recommends of go elephant in chessboard
    @param:
        state: matrix
        i,j: position of elephant
        lowercaseMove: true: lowercase elephant move, uppercase elephant move
    @return: a matrix with recommendations of elephant
    """

    @staticmethod
    def elephantGo_Recommends(state, i, j, lowercaseMove=True):
        sts = copy.deepcopy(state)
        # back
        if lowercaseMove:
            # blackside
            if state[i][j] == 'e':
                if i == 0:
                    if state[i + 1][j + 1] == '.' and state[i + 2][j + 2].islower() == False:
                        sts[i + 2][j + 2] = 'o'
                    if state[i + 1][j - 1] == '.' and state[i + 2][j - 2].islower() == False:
                        sts[i + 2][j - 2] = 'o'
                if i == 4:
                    if state[i - 1][j - 1] == '.' and state[i - 2][j - 2].islower() == False:
                        sts[i - 2][j - 2] = 'o'
                    if state[i - 1][j + 1] == '.' and state[i - 2][j + 2].islower() == False:
                        sts[i - 2][j + 2] = 'o'
                if i == 2:
                    if j == 0:
                        if state[i - 1][j + 1] == '.' and state[i - 2][j + 2].islower() == False:
                            sts[i - 2][j + 2] = 'o'
                        if state[i + 1][j + 1] == '.' and state[i + 2][j + 2].islower() == False:
                            sts[i + 2][j + 2] = 'o'
                    if j == 8:
                        if state[i - 1][j - 1] == '.' and state[i - 2][j - 2].islower() == False:
                            sts[i - 2][j - 2] = 'o'
                        if state[i + 1][j - 1] == '.' and state[i + 2][j - 2].islower() == False:
                            sts[i + 2][j - 2] = 'o'
                    if j == 4:
                        if state[i - 1][j - 1] == '.' and state[i - 2][j - 2].islower() == False:
                            sts[i - 2][j - 2] = 'o'
                        if state[i + 1][j - 1] == '.' and state[i + 2][j - 2].islower() == False:
                            sts[i + 2][j - 2] = 'o'
                        if state[i + 1][j + 1] == '.' and state[i + 2][j + 2].islower() == False:
                            sts[i + 2][j + 2] = 'o'
                        if state[i - 1][j + 1] == '.' and state[i - 2][j + 2].islower() == False:
                            sts[i - 2][j + 2] = 'o'
        # Red elephant
        else:
            # redside
            if state[i][j] == "E":
                if i == 9:
                    if state[i - 1][j - 1] == '.' and state[i - 2][j - 2].isupper() == False:
                        sts[i - 2][j - 2] = 'o'
                    if state[i - 1][j + 1] == '.' and state[i - 2][j + 2].isupper() == False:
                        sts[i - 2][j + 2] = 'o'
                if i == 5:
                    if state[i + 1][j + 1] == '.' and state[i + 2][j + 2].isupper() == False:
                        sts[i + 2][j + 2] = 'o'
                    if state[i + 1][j - 1] == '.' and state[i + 2][j - 2].isupper() == False:
                        sts[i + 2][j - 2] = 'o'
                if i == 7:
                    if j == 0:
                        if state[i + 1][j + 1] == '.' and state[i + 2][j + 2].isupper() == False:
                            sts[i + 2][j + 2] = 'o'
                        if state[i - 1][j + 1] == '.' and state[i - 2][j + 2].isupper() == False:
                            sts[i - 2][j + 2] = 'o'
                    if j == 8:
                        if state[i - 1][j - 1] == '.' and state[i - 2][j - 2].isupper() == False:
                            sts[i - 2][j - 2] = 'o'
                        if state[i + 1][j - 1] == '.' and state[i + 2][j - 2].isupper() == False:
                            sts[i + 2][j - 2] = 'o'
                    if j == 4:
                        if state[i - 1][j - 1] == '.' and state[i - 2][j - 2].isupper() == False:
                            sts[i - 2][j - 2] = 'o'
                        if state[i + 1][j - 1] == '.' and state[i + 2][j - 2].isupper() == False:
                            sts[i + 2][j - 2] = 'o'
                        if state[i + 1][j + 1] == '.' and state[i + 2][j + 2].isupper() == False:
                            sts[i + 2][j + 2] = 'o'
                        if state[i - 1][j + 1] == '.' and state[i - 2][j + 2].isupper() == False:
                            sts[i - 2][j + 2] = 'o'

        return sts

    # ROOK RECOMMENDATION-------------------------------
    """
    rookGo_Recommends func: Recommends of go rook in chessboard
    @param:
        state: matrix
        i,j: position of rook
        lowercaseMove: true: lowercase rook move, uppercase rook move
    @return: a matrix with recommends of rook
    """

    @staticmethod
    def rookGo_Recommends(state, i, j, lowercaseMove=True):
        sts = copy.deepcopy(state)
        # black
        if lowercaseMove:
            # blackside
            if (state[i][j] == 'r'):
                m = i
                while (m - 1 >= 0 and state[m - 1][j].islower() == False):
                    sts[m - 1][j] = 'o'
                    if state[m - 1][j].isupper() == True:
                        break
                    m = m - 1
                m = j
                while (m - 1 >= 0 and state[i][m - 1].islower() == False):
                    sts[i][m - 1] = 'o'
                    if state[i][m - 1].isupper() == True:
                        break
                    m = m - 1
                m = j
                while (m + 1 <= 8 and state[i][m + 1].islower() == False):
                    sts[i][m + 1] = 'o'
                    if state[i][m + 1].isupper() == True:
                        break
                    m = m + 1
                m = i
                while (m + 1 <= 9 and state[m + 1][j].islower() == False):
                    sts[m + 1][j] = 'o'
                    if state[m + 1][j].isupper() == True:
                        break
                    m = m + 1
        # red rook
        else:
            # redside
            if (state[i][j] == 'R'):
                m = i
                while (m - 1 >= 0 and state[m - 1][j].isupper() == False):
                    sts[m - 1][j] = 'o'
                    if state[m - 1][j].islower() == True:
                        break
                    m = m - 1
                m = j
                while (m - 1 >= 0 and state[i][m - 1].isupper() == False):
                    sts[i][m - 1] = 'o'
                    if state[i][m - 1].islower() == True:
                        break
                    m = m - 1
                m = j
                while (m + 1 <= 8 and state[i][m + 1].isupper() == False):
                    sts[i][m + 1] = 'o'
                    if state[i][m + 1].islower() == True:
                        break
                    m = m + 1
                m = i
                while (m + 1 <= 9 and state[m + 1][j].isupper() == False):
                    sts[m + 1][j] = 'o'
                    if state[m + 1][j].islower() == True:
                        break
                    m = m + 1
        return sts

    # HORSE RECOMMENDATION---------------------------
    """
    horseGo_Recommends func: Recommends of go horse in chessboard
    @param:
        state: matrix
        i,j: position of horse
        lowercaseMove: true: lowercase horse move, uppercase horse move
    @return: a matrix with recommends of horse
    """

    @staticmethod
    def horseGo_Recommends(state, i, j, lowercaseMove=True):
        sts = copy.deepcopy(state)
        # back
        if lowercaseMove:
            # blackside
            if state[i][j] == "h":
                if i - 1 > 0 and state[i - 1][j] == ".":
                    if j - 1 >= 0 and state[i - 2][j - 1].islower() == False:
                        sts[i - 2][j - 1] = 'o'
                    if j + 1 <= 8 and state[i - 2][j + 1].islower() == False:
                        sts[i - 2][j + 1] = 'o'
                if j - 1 > 0 and state[i][j - 1] == ".":
                    if i - 1 >= 0 and state[i - 1][j - 2].islower() == False:
                        sts[i - 1][j - 2] = 'o'
                    if i + 1 <= 9 and state[i + 1][j - 2].islower() == False:
                        sts[i + 1][j - 2] = 'o'
                if j + 1 < 8 and state[i][j + 1] == ".":
                    if i - 1 >= 0 and state[i - 1][j + 2].islower() == False:
                        sts[i - 1][j + 2] = 'o'
                    if i + 1 <= 9 and state[i + 1][j + 2].islower() == False:
                        sts[i + 1][j + 2] = 'o'
                if i + 1 < 9 and state[i + 1][j] == '.':
                    if j - 1 >= 0 and state[i + 2][j - 1].islower() == False:
                        sts[i + 2][j - 1] = 'o'
                    if j + 1 <= 8 and state[i + 2][j + 1].islower() == False:
                        sts[i + 2][j + 1] = 'o'
        # Red Horse
        else:
            # redside
            if state[i][j] == "H":
                if i - 1 > 0 and state[i - 1][j] == ".":
                    if j - 1 >= 0 and state[i - 2][j - 1].isupper() == False:
                        sts[i - 2][j - 1] = 'o'
                    if j + 1 <= 8 and state[i - 2][j + 1].isupper() == False:
                        sts[i - 2][j + 1] = 'o'
                if j - 1 > 0 and state[i][j - 1] == ".":
                    if i - 1 >= 0 and state[i - 1][j - 2].isupper() == False:
                        sts[i - 1][j - 2] = 'o'
                    if i + 1 <= 9 and state[i + 1][j - 2].isupper() == False:
                        sts[i + 1][j - 2] = 'o'
                if j + 1 < 8 and state[i][j + 1] == ".":
                    if i - 1 >= 0 and state[i - 1][j + 2].isupper() == False:
                        sts[i - 1][j + 2] = 'o'
                    if i + 1 <= 9 and state[i + 1][j + 2].isupper() == False:
                        sts[i + 1][j + 2] = 'o'
                if i + 1 < 9 and state[i + 1][j] == '.':
                    if j - 1 >= 0 and state[i + 2][j - 1].isupper() == False:
                        sts[i + 2][j - 1] = 'o'
                    if j + 1 <= 8 and state[i + 2][j + 1].isupper() == False:
                        sts[i + 2][j + 1] = 'o'
        return sts
