# this file contain function to use everywhere

from Const.const import *


class FenUtils:

    @staticmethod
    def fen2matrix(fen):
        """
        fen2matrix: translate fen string to matrix 2 dimension
        @param: a fen string
        @return: 2d matrix correspond with fen string
        """
        state = np.array(
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.'])
        i = 0
        for e in fen:
            if e in NUMSTRING:
                i += int(e)
            elif e in CHESSMAN:
                state[i] = e
                i += 1
        # print(id(state))
        return state.reshape(10, 9)

    @staticmethod
    def matrix2fen(matrix):
        """
        matrix2fen: translate 2d matrix to fen string
        @param: a fen string
        @return: 2d matrix correspond with fen string
        """
        fen = ""
        count_row = 0
        for row in matrix:
            i = 0
            count_row += 1
            for e in row:
                if e == '.':
                    i += 1
                elif i != 0:
                    fen += str(i)
                    fen += e
                    i = 0
                else:
                    fen += e
            if i != 0:
                fen += str(i)
            if count_row != 10:
                fen += '/'

        return fen

    @staticmethod
    def valueofPiece(piece):
        if piece == 'k':
            return 16
        elif piece == 'a':
            return 17
        elif piece == 'e':
            return 18
        elif piece == 'h':
            return 19
        elif piece == 'r':
            return 20
        elif piece == 'c':
            return 21
        elif piece == 'p':
            return 22
        elif piece == 'K':
            return 8
        elif piece == 'A':
            return 9
        elif piece == 'E':
            return 10
        elif piece == 'H':
            return 11
        elif piece == 'R':
            return 12
        elif piece == 'C':
            return 13
        elif piece == 'P':
            return 14
        else:
            return 0

    @staticmethod
    def convert2dto1darray(state):
        CHESSMAN = {'k', 'a', 'e', 'h', 'r', 'c', 'p', 'K', 'A', 'E', 'H', 'R', 'C', 'P'}
        MAPPING = {16, 17, 18, 19, 20, 21, 22, 8, 9, 10, 11, 12, 13, 14}
        squares = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]
        for i in range(0, 10):
            for j in range(0, 9):
                if state[i][j] in CHESSMAN:
                    index = 16 * 3 + 16 * i + 3 + j
                    squares[index] = FenUtils.valueofPiece(state[i][j])
        return squares
    @staticmethod
    def change_uper_lower_fen(fen):
        s = ''
        for i in fen:
            if i.islower():
                s += fen[fen.index(i)].upper()
            elif i.isupper():
                s += fen[fen.index(i)].lower()
            else:
                s += fen[fen.index(i)]
        return s